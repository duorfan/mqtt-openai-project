import paho.mqtt.client as mqtt  # type: ignore # Import MQTT client library
from openai import OpenAI  # type: ignore # Import OpenAI client
from dotenv import load_dotenv  # type: ignore # Import dotenv to load environment variables
import os  # Library for accessing environment variables

# Load .env file
load_dotenv()  # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")  # Get OpenAI API key

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Function to handle connection to MQTT broker
def on_connect(client, userdata, flags, rc):
    print(f"✅ Connected to MQTT broker with result code {rc}")

# Function to handle incoming MQTT messages
def on_message(client_mqtt, userdata, message):
    payload = message.payload.decode("utf-8")  # Decode the received message
    print(f"✅ Received: {payload}")  # Log the received message

    # Create a prompt for OpenAI
    prompt = f"Write a short poem about {payload}"

    # Query OpenAI for a creative response
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use chat model
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and print the AI-generated poem
        poem = completion.choices[0].message.content
        print("\n🌦️ AI-Generated Poem:\n", poem)

    except Exception as e:
        # Log any errors from the OpenAI API
        print(f"❌ Error with OpenAI API: {str(e)}")

# Define MQTT broker and topic
broker = "mqtt.eclipseprojects.io"  # Public MQTT broker
topic = "sensor/weather"  # Topic to subscribe to

# Connect to MQTT broker and set up callbacks
client_mqtt = mqtt.Client()  # Initialize MQTT client
client_mqtt.on_connect = on_connect  # Define connection callback
client_mqtt.on_message = on_message  # Define message callback
client_mqtt.connect(broker, 1883)  # Connect to broker on port 1883
client_mqtt.subscribe(topic)  # Subscribe to the topic

# Start listening for messages
print("✅ Waiting for messages...")
client_mqtt.loop_forever()  # Keep the script running to process messages
