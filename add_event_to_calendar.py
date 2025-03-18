import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


# NOTE(shunxian): we need a GCP project
# application(serviceaccount) to act on people's calendar
def CallGoogleCalendar():
    pass


def CallOpenAI():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": "Write a one-sentence bedtime story about a unicorn.",
            }
        ],
    )

    print(completion.choices[0].message.content)
