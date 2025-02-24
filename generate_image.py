from transformers import pipeline
from PIL import Image
import requests

# Load the text-to-image pipeline
pipe = pipeline("text-to-image", model="CompVis/stable-diffusion-v1-4")

# Define the prompt
prompt = "a child playing with a dog in a park"

# Generate the image
image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5)["sample"][0]

# Save the image
image.save("child_playing_with_dog.png")

# Display the image
image.show()

import cv2
import numpy as np

# Load image
img = cv2.imread("golden_retriever_sitting_on_grass.jpg")

# Resize image to reduce file size
img = cv2.resize(img, (400, 600))

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary mask
lower_red = np.array([150, 150, 150])
upper_red = np.array([170, 170, 170])
thresh = cv2.inRange(gray, lower_red, upper_red)

# Add a mask to the image for the dog's fur
dog_mask = np.zeros_like(thresh)
dog_mask[thresh == 140] = 255
merged = cv2.addWeighted(img, 1, dog_mask, 0.5, 0.5)

# Add a mask for the child's arm reaching out to the dog
arm_mask = np.zeros_like(thresh)
arm_mask[thresh == 170] = 255
merged = cv2.addWeighted(merged, 0.6, arm_mask, 0.8, 0.8)

# Display the final image
cv2.imshow("Merged Image", merged)
cv2.waitKey()

