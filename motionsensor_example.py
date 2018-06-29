from gpiozero import MotionSensor
from signal import pause

count = 0
def motion_detected_cb():
	global count
	count += 1
	print("motion detected "+str(count))

#Assumed that the IO pin used is 4. Change the below code if you use different pin	
pir = MotionSensor(4)
	
pir.when_motion= motion_detected_cb
print("ready for events")
pause()


