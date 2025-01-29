from openai import OpenAI  # type: ignore # Import OpenAI client
from dotenv import load_dotenv  # type: ignore # Import dotenv to load environment variables
import os  # Library for accessing environment variables

# Load .env file
load_dotenv()  # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")  # Get OpenAI API key

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Define a test prompt
prompt = "Explain MQTT in simple terms."

# Query OpenAI for a response
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use chat model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Print the AI-generated response
print("\n🤖 OpenAI Response:\n", completion.choices[0].message.content)
