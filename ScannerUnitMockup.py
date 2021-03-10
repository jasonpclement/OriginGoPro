import time


#Import the small wrapper class I wrote
from Classes import GoProInterfacing

# Some info about go pro... (And I did not know these details prior to requesting we try it.. my apologies for this.. Like I said, I don't know anything about this stuff)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Go pro's are super annoying it seems, in that you can't do the following
#   Plug it in via USB and run over USB
#   Connect Via bluetooth and run over bluetooth
#
#  Instead, what you must do is
#  -Plug go pro into an outlet (unless you like changing batteries every 5 minutes)
#  -use the gopro app from your phone to connect to the go pro
#       - This will use a bluetooth connection from phone to go pro, which will then tell the go pro to emit it's own wifi signal
#       - The phone will then connect to the wifi signal (but we don't care about the phone anymore at this point...)
#       - Now that the goPro is emitting a wifi signal, you can connect to it with your PC or any device that connects to wifi (the password can be found in the gopro)

#Instantiate a ClipCreator class I created
clipCreator = GoProInterfacing.ClipCreator()

#This needs to be set to the location of the executing script - I don't love this, but the goprocam package seems broken for the filepath functionality
thisLocation = "C:\\Users\\jason\\OneDrive\\Documents\\repos\\OriginGoPro\\"

#Where you want it to go...
TargetLocation = "C:\\Users\\jason\\OneDrive\\Documents\\repos\\OriginGoPro\\myClips\\"

#Let's simulate a barcode scan

##I just scanned a barcode, and I'm saving it into a variable
myBarCode = 'BarCode12345'
print(f"BarCodeScan: {myBarCode}")


#We got our barcode - kick off the go pro, passing in the barcode
clipCreator.AssignBarCode(myBarCode)    #this will give our current barCode to the clipcreator
clipCreator.StartClip()                 #start filming


#simulate some time passing while people do things.
print('')
print(f"Worker doing some work")
for i in range(1, 10):
    if i%3 == 0:
        print(f"Worker continuing to do some work")
    else:
        print(f"......")
    time.sleep(2)

print(f"Worker finishing up...")
print(f"Worker Hits the Stop Button...")
clipCreator.StopClip()                 #Stop filming
clipCreator.SaveClip(thisLocation, TargetLocation)  #a little hacky because of a shortcoming w/ the goprolibrary (i think anyway...)





