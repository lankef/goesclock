import requests
import re
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import datetime

# Setting #################################################################

# Setting 1: Sector. Choose the sector that corresponds to your location 
sector_name = 'ne'

# Setting 2: Kindle resolution
res_x = 800
res_y = 600

# Setting 3: Center location. Choose a location that you like. You can 
# find the location of a feature by downloading the image and looking at 
# the lower left corner in ms paint. The number should be between 
# x_resolution/2, 2400-x_resolution/2, 
# and 
# y_resolution/2, 2400-x_resolution/2,
center_x = 1400
center_y = 1170

# Setting 4: Clock location
clockx = 550
clocky = 420

# Setting ##############################################################

if center_x > 2400 - res_x//2:
    raise ValueError('x cropping point > 2400-res/2')
if center_x < res_x//2:
    raise ValueError('x cropping point < res/2')
if center_y > 2400 - res_y//2:
    raise ValueError('y cropping point > 2400-res/2')
if center_y < res_y//2:
    raise ValueError('y cropping point < res/2')

# Fetching satellite image ---------------------

url = 'https://cdn.star.nesdis.noaa.gov/GOES19/ABI/SECTOR/' + sector_name + '/GEOCOLOR/'
response = requests.get(url)

# Extract filenames using regex
filenames = re.findall(r'(\d{11}_GOES19-ABI-' + sector_name + r'-GEOCOLOR-2400x2400\.jpg)', response.text)

if filenames:
    filenames.sort(reverse=True)  # Sort descending, latest first
    latest_file = filenames[0]
    latest_url = url + latest_file

# Downloading image
response = requests.get(latest_url)
image = Image.open(BytesIO(response.content))

# Cropping image
cropped = image.crop((
    center_x-res_x//2,
    center_y-res_y//2,
    center_x+res_x//2,
    center_y+res_y//2,
))

# Drawing clock face --------------------------

draw = ImageDraw.Draw(cropped)
rgb_white = (255,255,255)
# Loading font 
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("futura medium bt.ttf", 16)
font_large = ImageFont.truetype("futura medium bt.ttf", 80)

datetime.datetime.now()

# Generating clock overlay -------------------------

# Converting dates
timestamp_str = latest_url[63:74]
# Parse parts
year = int(timestamp_str[0:4])
doy = int(timestamp_str[4:7])
hour = int(timestamp_str[7:9])
minute = int(timestamp_str[9:11])
# Convert to datetime
dt = datetime.datetime(year, 1, 1, hour, minute) + datetime.timedelta(days=doy - 1)
# Format output: year-month-day and 12hr format
formatted = dt.strftime("%Y-%m-%d %I:%M %p")
# Drawing satellite image info
info_str = 'Image taken by GOES19-GLM'
info_str2 = 'at ' + formatted + ' GMT.'

# Generating texts
current_time = datetime.datetime.now()
clock_str = str(current_time)[11:16]
date_str = current_time.strftime("%Y %b. %d")

draw.text((clockx, clocky), clock_str, fill=rgb_white, font=font_large)
draw.text((clockx+56, clocky+92), date_str, fill=rgb_white, font=font)
draw.text((clockx, clocky+115+5), info_str, fill=rgb_white, font=font)
draw.text((clockx-4, clocky+135+5), info_str2, fill=rgb_white, font=font)

# Saving image
cropped = cropped.transpose(Image.ROTATE_270)
cropped.convert("L").save('goes_latest.png', format='PNG')