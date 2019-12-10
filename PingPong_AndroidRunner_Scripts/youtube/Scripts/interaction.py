import time
def main(device, *args, **kwargs):
    while(not "youtube" in device.shell("dumpsys window windows | grep mCurrentFocus")):
      time.sleep(1)
    
    #put fullsize
    time.sleep(2)
    device.tap(1356, 808)
    time.sleep(2)
    
    device.tap(1356, 808)
    #time.sleep(.30)
    device.tap(1356, 808)
    #time.sleep(.30)
    
    #now set quality:
    
    #show overlay
    device.tap(2500,100)
    #time.sleep(.30)
    
    #click on wheel
    device.tap(2500,100)
    #time.sleep(.30)
    
    #quality
    device.tap(320,830)
    #time.sleep(.30)
    
    #360
    #device.tap(320, 830)
    
    #1080pui
    device.tap(320,1330)
