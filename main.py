from goprocam import GoProCamera, constants
import time

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


##Setup Boot Order
thisBootOrder = 'BootOrder00001'



##Instantiate Go Pro - Note, must be connected to gopro via Wifi - might be useful to have a seperate script
gpCam = GoProCamera.GoPro()
CameraName = gpCam.infoCamera()

##Set Video Settings
gpCam.video_settings("1080p","60")






videos_duration=[10,20]
gpCam.video_settings("1080p","60")
gpCam.gpControlSet(constants.Video.PROTUNE_VIDEO, constants.Video.ProTune.ON)
for i in videos_duration:
	print("Recording " + str(i) + " seconds video")
	gpCam.downloadLastMedia(gpCam.shoot_video(i), custom_filename="VIDEO_"+str(i)+".MP4")
	time.sleep(2)



