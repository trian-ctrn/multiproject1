from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import glob

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("converted_keras/keras_model.h5", compile=False)

# Load the labels
class_names = open("converted_keras/labels.txt", "r", encoding="utf-8").read().splitlines()

# Create an empty list to store the predictions
predictions = []

# Replace this with the path to your image folder
image_folder = "data"

# Retrieve a list of image paths from the folder
image_paths = glob.glob(image_folder + "/*.jpg")

# Iterate over the image paths
for image_path in image_paths:
    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Load the image
    image = Image.open(image_path).convert("RGB")
# Replace this with the path to your image
image = Image.open(IMAGEPATH).convert("RGB")

# Resize and crop the image
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# Convert the image to a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Make a prediction
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Store the prediction
predictions.append((class_name, confidence_score))

# Print the predictions
for i, (class_name, confidence_score) in enumerate(predictions):
    print(f"Image {i+1}:")
    print("Class:", class_name)
    print("Confidence Score:", confidence_score)
    print()
