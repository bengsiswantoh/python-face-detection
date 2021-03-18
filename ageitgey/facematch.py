import face_recognition

image_of_taylor = face_recognition.load_image_file('./faces/warren-buffet/1.jpeg')
taylor_face_encoding = face_recognition.face_encodings(image_of_taylor)[0]

unknown_image = face_recognition.load_image_file('./images/bill-warren.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[1]

results = face_recognition.compare_faces(
    [taylor_face_encoding], unknown_face_encoding)

print(results)
