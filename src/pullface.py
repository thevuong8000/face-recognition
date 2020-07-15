from PIL import Image
import face_recognition as fr 

image = fr.load_image_file('../images/group/team2.jpg')
face_locations = fr.face_locations(image)

for face_location in face_locations:
	top, right, bottom, left = face_location

	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()
	#pil_image.save() # save image