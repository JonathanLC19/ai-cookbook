from google.genai import types
from google import genai
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os
from dotenv import load_dotenv
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
# from openai import OpenAI


"###############################################################################################"

# region OPENAI

"###############################################################################################"


# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": "You're a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a limerick about the Python programming language.",
#         },
#     ],
# )

# response = completion.choices[0].message.content
# print(response)


"###############################################################################################"

# region HUGGINGFACE

"###############################################################################################"


# llm = HuggingFaceEndpoint(
#     repo_id="microsoft/Phi-3-mini-4k-instruct",
#     task="text-generation",
#     max_new_tokens=1000,
#     do_sample=False,
#     # repetition_penalty=1.03,
#     temperature=0.2,
#     model_kwargs={
#         'stream': True
#     }
# )

# chat = ChatHuggingFace(llm=llm, verbose=True)

# messages = [
#     ("system", "You are a helpful translator. Translate the user sentence to French."),
#     ("human", "I love programming."),
# ]

# print(chat.invoke(messages))


"###############################################################################################"

# region GEMINI

"###############################################################################################"

client = genai.Client(api_key=gemini_key)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
)

for chunk in response:
    print(chunk.text, end="")
