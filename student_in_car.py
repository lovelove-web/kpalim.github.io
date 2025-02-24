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
