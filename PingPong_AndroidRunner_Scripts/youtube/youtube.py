#! /usr/bin/env monkeyrunner

import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

YOUTUBE = 'com.google.android.youtube-2.1.6.apk'
prog = os.path.basename(sys.argv[0])

def usage():
        print >>sys.stderr, "usage: %s" % prog
        sys.exit(1)

def main():
        if len(sys.argv) != 1:
                usage()

        print "waiting for connection..."
        device = MonkeyRunner.waitForConnection()

        print "installing youtube"
        device.installPackage(YOUTUBE)

        device.startActivity(component="com.google.android.youtube/.HomeActivity")
        MonkeyRunner.sleep(3)
        # search
        device.touch(450, 80, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(5)
        device.type('android')
        # done
        device.touch(450, 740, MonkeyDevice.DOWN_AND_UP)




