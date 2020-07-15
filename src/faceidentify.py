from PIL import Image, ImageDraw
import face_recognition as fr

# knowledge
Gates_image = fr.load_image_file('../images/known/Bill Gates.jpg')
Gates_face_encoding = fr.face_encodings(Gates_image)[0]

Jobs_image = fr.load_image_file('../images/known/SteveJobs.jpg')
Jobs_face_encoding = fr.face_encodings(Jobs_image)[0]

known_face_encodings = [Gates_face_encoding, Jobs_face_encoding]
known_face_labels = ["Bill Gates", "Steve Jobs"]

# test image
test_image = fr.load_image_file('../images/group/Gates Jobs.jpg')
face_locations = fr.face_locations(test_image)
face_encodings = fr.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create draw instance for drawing inside the image
draw = ImageDraw.Draw(pil_image)

# Draw the rectangle
for face_location in face_locations:
	top, right, bottom, left = face_location
	draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0), width=5)

# Identify faces in the image
for face_location, face_encoding in zip(face_locations, face_encodings):
	top, right, bottom, left = face_location

	matches = fr.compare_faces(known_face_encodings, face_encoding)

	label = "Unknown Person"

	# If match
	if True in matches:
		first_true_idx = matches.index(True)
		label = known_face_labels[first_true_idx]

	# Draw label
	text_width, text_height = draw.textsize(label)
	draw.rectangle(((left, bottom + text_height + 10), (left + text_width + 10, bottom)), fill=(255,0,0))

	draw.text((left + 3, bottom + text_height - 5), label, fill=(0,0,0))

del draw

pil_image.show()