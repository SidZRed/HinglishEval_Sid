import json
import os

from openai import OpenAI


def mistral7b(docstr):
    # Create an OpenAI client with your deepinfra token and endpoint
    openai = OpenAI(
        api_key="api-key",
        base_url="https://api.deepinfra.com/v1/openai",
    )

    chat_completion = openai.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",  ## MODEL NAME
        messages=[
            {
                "role": "system",
                "content": "You are an experienced Python programmer. Complete the Python functions from the given docstrings. Do NOT write anything except the function definition. Avoid print and input statements.\n",
            },
            {
                "role": "user",
                "content": f"Can you complete the following Python function? Retain the function header and docstring.\n\n```python\n{docstr}```",
            },
        ],
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    path_humaneval_hinglish = os.path.join(base_dir, "HinglishEval.json")
    unsanitized_hinglish_dir = os.path.join(base_dir, "Hinglish", "unsanitized",  "mistral7b")
    os.makedirs(unsanitized_hinglish_dir, exist_ok=True)

    with open(path_humaneval_hinglish) as f:
        data = json.load(f)
        for pid in range(164):
            prompt = data[pid]["prompt"]
            with open(os.path.join(unsanitized_hinglish_dir, f"{str(pid).zfill(3)}.py"), "w") as file:
                file.write(mistral7b(prompt))
                print(f"done for {pid}")

    path_humaneval_english = os.path.join(base_dir, "HumanEval.json")
    unsanitized_english_dir = os.path.join(base_dir, "English", "unsanitized",  "mistral7b")
    os.makedirs(unsanitized_english_dir, exist_ok=True)

    with open(path_humaneval_english) as f:
        data = json.load(f)
        for pid in range(164):
            prompt = data[pid]["prompt"]
            with open(os.path.join(unsanitized_english_dir, f"{str(pid).zfill(3)}.py"), "w") as file:
                file.write(mistral7b(prompt))
                print(f"done for {pid}")