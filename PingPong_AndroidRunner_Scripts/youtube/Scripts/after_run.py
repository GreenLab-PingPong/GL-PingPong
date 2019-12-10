import time
def main(device, *args, **kwargs):
    print "Clearing YouTube cache"
    device.shell("pm clear com.google.android.youtube")
