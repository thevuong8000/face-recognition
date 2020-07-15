import face_recognition

image = face_recognition.load_image_file('../images/group/team2.jpg')
face_locations = face_recognition.face_locations(image)

# Array of coords of each face
print(face_locations)

# Count how many people
human = "people"
if len(face_locations) <= 1:
	human = "person"
print(f'There are {len(face_locations)} {human} in this image')
