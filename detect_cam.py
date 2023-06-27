from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

class FaceDetection():
    def __init__(self) -> None:
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("converted_keras/keras_model.h5", compile=False)

        # Load the labels
        self.class_names = open("converted_keras/labels.txt", "r", encoding="utf-8").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture("test_video.MOV")

    def image_detector(self):        
        # Grab the webcamera's image.
        ret, image = self.camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        return class_name[2:], str(np.round(confidence_score * 100))[:-2]


