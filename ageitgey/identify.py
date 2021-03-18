import face_recognition
from PIL import Image, ImageDraw

image_of_bill_gates = face_recognition.load_image_file(
    './faces/bill gates/1.jpg')
bill_gates_face_encoding = face_recognition.face_encodings(image_of_bill_gates)[
    0]

image_of_warren_buffet = face_recognition.load_image_file(
    './faces/warren buffet/1.jpeg')
warren_buffet_face_encoding = face_recognition.face_encodings(image_of_warren_buffet)[
    0]

#  Create arrays of encodings and names
known_face_encodings = [
    bill_gates_face_encoding,
    warren_buffet_face_encoding
]

known_face_names = ['bill gates', 'warren buffet']

# Find faces in test image
unknown_image = face_recognition.load_image_file('./images/bill warren.jpeg')
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(
    unknown_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(unknown_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# loop faces
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    results = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = 'unknown'

    # if match
    if True in results:
        first_match_index = results.index(True)
        name = known_face_names[first_match_index]

        # Draw box
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))

        # Draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right,
                       bottom)), fill=(255, 255, 0), outline=(255, 255, 0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))

del draw

# Display image
pil_image.show()

# Save image
# pil_image.save('identify.jpg')
