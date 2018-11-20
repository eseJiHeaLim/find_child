import face_recognition
import os

picture_of_me = face_recognition.load_image_file("me.jpg")
print("It's a picture of me!")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

for root, dirs, files in os.walk('/home/odroid/Desktop/test_facerecognition/inforamtion'):
    for fname in files:
        full_fname = os.path.join(root,fname)
        unknown_picture = face_recognition.load_image_file(full_fname)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        if results[0] == True:
            print("It's a picture of me!")
            print (full_fname)
        else:
            print("It's not a picture of me!")
        
        