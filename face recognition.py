# Remove all commant then it working

import cv2
import dlib
#from DB_process as dp " remove the commant "


detection= dlib.get_frontal_face_detector()

cap=cv2.VideoCapture(0)
while cap.isOpened():
    _, frame= cap.read()
    faces =detection(frame)
    for face in faces:
        crop_face= frame[face.top(): face.bottom(), face.left(): face.right()]
    face_img = cv2.resize(crop_face, (70, 70))

    #persone_name = pd.classfy(face_img) " remove the commant "

    print(persone_name)
    cv2.imshow('real', frame)
    cv2.imshow('face', face_img)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cap.release()

# Remove all commant then it working