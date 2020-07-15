import face_recognition as fr

Gates_image = fr.load_image_file('../images/known/Bill Gates.jpg')
# fr.face_encodings return an array of people in the image
Gates_encoding = fr.face_encodings(Gates_image)

test_image = fr.load_image_file('../images/unknown/Gates-test.jpg')
test_encoding = fr.face_encodings(Gates_image)[0]

result = fr.compare_faces(Gates_encoding, test_encoding)

print(result[0])
