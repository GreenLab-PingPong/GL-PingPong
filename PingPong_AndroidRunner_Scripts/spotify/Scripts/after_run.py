import time
def main(device, *args, **kwargs):
    

    while(not "spotify" in device.shell("dumpsys window windows | grep mCurrentFocus")):
      device.shell("am start -n com.spotify.music/.MainActivity")
      time.sleep(1)

    time.sleep(5)
    
    #gear
    device.tap(1380,180)
    time.sleep(1)
    #clear cache
    #device.shell("input roll 0 25")
    device.shell("input swipe 730 1970 730 0")
    time.sleep(1)
    device.shell("input swipe 730 1970 730 500")
    
    time.sleep(1)
    device.tap(730,1920)
    time.sleep(0.2)
    
    device.tap(730,1380)
    time.sleep(0.5)
    
    
    #set to low quality
    device.shell("input roll 0 -5")
    time.sleep(1)
    device.tap(1170, 365)
    time.sleep(0.05)
    #device.tap(1170, 750)
    
    #high quality
    device.tap(1170,1240)
