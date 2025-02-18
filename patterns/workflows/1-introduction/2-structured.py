from pydantic import BaseModel
# from openai import OpenAI
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from pprint import pprint, PrettyPrinter

load_dotenv()


# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

gemini_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_key)

# --------------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# --------------------------------------------------------------


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


# --------------------------------------------------------------
# Step 2: Call the model
# --------------------------------------------------------------

# completion = client.beta.chat.completions.parse(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": "Extract the event information."},
#         {
#             "role": "user",
#             "content": "Alice and Bob are going to a science fair on Friday.",
#         },
#     ],
#     response_format=CalendarEvent,
# )


response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='Alice and Bob are going to a science fair on Friday.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[CalendarEvent],
    },
)
# Use the response as a JSON string.
PrettyPrinter().pprint(response.parsed)

# Use instantiated objects.
my_recipes: CalendarEvent = response.parsed

# --------------------------------------------------------------
# Step 3: Parse the response
# --------------------------------------------------------------

event = response
# print(event.name)
# event.date
# event.participants
