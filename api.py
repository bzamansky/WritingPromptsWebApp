import openai
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPEN_AI_API_KEY")


def initialPrompt():
  data= openai.Completion.create(
    model="text-davinci-003",
    prompt="Create a writing prompt",
    max_tokens=30,
    temperature=0
  )
  return data.choices[0].text