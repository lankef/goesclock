# Kindle satellite clock

This is a clock that fetches real-time images from the [GOES-19](https://en.wikipedia.org/wiki/GOES-19)
weather satellites. It runs entirely on the kindle, and doesn't need a 
web server! By default, the clock works with a 800x600 
resolution, fetches GeoColor images (real color in daytime, IR 
at night) in the NE sector (centered at New York), and displays
the clock face at the lower right corner. To change the
resolution, sector, satellite [image type](https://www.star.nesdis.noaa.gov/goes/sector.php?sat=G19&sector=ne) 
or clock location, please edit the opening lines of `bin/clock.py`.

## Installing

To use this you must first jailbreak your kindle and install
KUAL and MRPI. See [here](https://kindlemodding.org/) for a 
guide.

It also requires disabling kindle deep sleep. To do this, 
simply enter `~ds` in the search bar. *You have to do this again* 
*every time you reboot!*

This extension requires python3, Pillow, and requests. First install [python3](https://www.mobileread.com/forums/showthread.php?t=225030). 

Then, run in kterm:
```
python3 -m ensurepip --upgrade
```
And then 
```
python3 -m install requests
python3 -m install pillow
```

Then, copy the `goes-clock` folder into the `extensions`, and run it from KUAL!

Be patient after clicking launch. Don't click anything else - It 
takes a while to launch! The Kindle has to think very hard (for about 20s)
just to download and refresh every frame. This is also a simple extension that runs 
over the default UI, but does not disable it. For about 30 seconds nothing will happen,
then the image will kick in.

Don't launch multiple instances - there's no multi-launch detection and the workload
can make your kindle unresponsive.

Enjoy!

## Special thanks
[4dcu.be](https://blog.4dcu.be/diy/2020/09/27/PythonKindleDashboard_1.html)
for the tutorial!
