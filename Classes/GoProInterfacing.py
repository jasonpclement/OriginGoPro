from goprocam import GoProCamera, constants
import time
import shutil

#Let me preface this by saying go pros are freaking weird, 
#and at this point I more or less hate them, despite it being my recommendation to try.

#How this POS works
#	YOu need to turn the thing on, and go to connections in the go pro to set it in pairing more
#	Then you need to use your phone... yeah your phone... and the go pro app to connect to the thing
#	This will use bluetooth between phone and go pro, to make the go pro emit a wifi network
#	Your phone will then automatically connect to the wifi network, but that does not matter at all.
#	At this point, because the go pro is emitting the wifi network, you can connect your PC to the gopro's wifi
#	Now your home free, except your PC can't use the internet anymore because its connected to the gopro... 
#	So unless you have multiple wifi adapters your SOL if you want to do anything outside talk to the go pro.

#note:  I found a setting that made it so it won't go to sleep... i think...

class ClipCreator:
    def __init__(self):
        self.gpCam = GoProCamera.GoPro()    
        self.gpCam.video_settings("1080p","60")
        self.CameraInfo = self.gpCam.infoCamera()
        self.CameraName = self.CameraInfo['serial_number']
        self.BarCodeScan = None
        self.Clip = None

    def AssignBarCode(self, pBarCodeScan):
        self.BarCodeScan = pBarCodeScan

    def StartClip(self):
        print(self.gpCam.IsRecording())
        if self.BarCodeScan == None:
            raise Exception("BarcodeScan is not assigned")
        elif self.gpCam.IsRecording() != 0:
            raise Exception("Go Pro appears to already be recording...")
        
        else:
            print(f"Recording Started for BarcodeID: {self.BarCodeScan} using Camera:{self.CameraName}")
            self.Clip = self.gpCam.shoot_video()

    def StopClip(self):
        if self.gpCam.IsRecording() != 1:
            raise Exception("GoPro is not recording, and thus cannot be stopped")
        else:
            print(f"Recording Stopped for BarcodeID: {self.BarCodeScan} using Camera:{self.CameraName}")
            self.gpCam.shutter(constants.stop)
            #go pro takes a few seconds to finish up
        time.sleep(5)

    def SaveClip(self, pCopyFilePath, pTargetFilePath):
        filename = f"{self.BarCodeScan}_{self.CameraName}.mp4"
        sourcePath = pCopyFilePath + filename
        targetPath = pTargetFilePath + filename
        self.gpCam.downloadLastMedia(custom_filename=filename)  #This can take in a path, but it seems sorta broken... just save it locally and move manually with another line of code
        shutil.move(sourcePath, targetPath)
    


