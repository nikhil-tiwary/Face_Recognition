import cv2

cap = cv2.VideoCapture(0) # 0 indicates the default webcam of the system
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
	ret,frame = cap.read()
	

	if ret==False:
		continue

	faces = face_cascade.detectMultiScale(frame,1.3,5)

		

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow("Video Frame",frame)



	#wait for user input -1, then you will stop the loop
	# only close the window when "q" button is pressed

	key_pressed=cv2.waitKey(1) & 0xFF  # here we are trying to covert 32-bit number into 8-bit number
	if key_pressed == ord('q'):  # ord is used to get ASCII value of the character
		break

cap.release()  # to release the webcam
cv2.destroyAllWindows()



# scaleFactor : Parameter specifying how much the image size is reduced at each image scale.

# minNeighbours : Parameter specifying how many neigbours each candidate rectangle should have to retain it.