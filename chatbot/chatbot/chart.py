from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key="AIzaSyAR9wLsB_KFR96MidEVjSx-YAYm35ZVeSg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What color is orange?answer in one word",
)

print(response.text)