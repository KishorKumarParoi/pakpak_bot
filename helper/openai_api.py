import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Use your API key
# openai.api_key = os.getenv('OPENAI_API_KEY')

# print(openai.api_key)


# Set your API key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a poem about recursion in programming in 100 words .",
#         },
#     ],
# )

# print(completion.choices[0].message.content)


def text_completion(prompt: str) -> dict:
    """
    Call OpenAI API for text completion.

    Parameters:
        prompt (str): The user query.

    Returns:
        dict: The response from the OpenAI API containing the completion.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        print("response: ", response.choices[0].message.content)
        return {"status": 1, "response": response.choices[0].message.content}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"status": 0, "response": "", "error": str(e)}


def generate_image(prompt: str) -> dict:
    """
    Call OpenAI API to generate an image.

    Parameters:
        prompt (str): The user query.

    Returns:
        dict: The response from the OpenAI API containing the image URL.
    """
    try:
        response = client.images.generate(prompt=prompt, n=1, size="1024x1024")
        return {"status": 1, "url": response.data[0].url}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"status": 0, "url": "No Photo Found", "error": str(e)}


print(text_completion("What is the capital of Bangladesh?"))
# print(generate_image("A cute baby boy"))
