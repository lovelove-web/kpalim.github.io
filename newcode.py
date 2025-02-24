from openai import OpenAI

def generate_image(prompt):
    """
    Generates an image based on the given prompt using OpenAI's DALL-E mini model.

    Parameters:
    prompt (str): The text prompt for generating the image.

    Returns:
    None. Prints the generated image.
    """
    client = OpenAI()

    response = client.images.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )

    print(response.data[0].url)

generate_image("dog playing with a child under a tree")