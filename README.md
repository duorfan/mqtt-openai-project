# MQTT + OpenAI Weather Poetry Generator

## Features

- Fetches real-time weather data from WeatherAPI
- Publishes weather updates via MQTT
- Generates poetry based on received weather data using OpenAI

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd mqtt-openai-project
```

### 2. Create & Activate a Virtual Environment

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

Create a `.env` file and add:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Project

### Start the MQTT Publisher (Fetch & Publish Weather)

```bash
python pub.py
```

### Start the MQTT Subscriber (Receive & Generate Poems)

```bash
python sub.py
```

### Test OpenAI API

```bash
python llm_test.py
```

## Troubleshooting

### Virtual Environment Issues

```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### Missing Packages

```bash
pip install openai python-dotenv paho-mqtt requests
```

### MQTT Messages Not Received

```bash
mosquitto_pub -h mqtt.eclipseprojects.io -t "sensor/weather" -m "Test message: Hello MQTT!"
```

## Example Output

### Publisher (`pub.py`)

```
Published: Weather: Cloudy, Temperature: 12°C, AQI: 8.5
```

### Subscriber (`sub.py`)

```
✅ Received: Weather: Cloudy, Temperature: 12°C, AQI: 8.5

🌦️ AI-Generated Poem:
The sky is gray, a quiet song,
A whispered breeze that floats along.
Soft clouds drift in a silver hue,
A peaceful day, serene and new.
```

## Technologies Used

- Python
- MQTT (paho-mqtt)
- WeatherAPI
- OpenAI API
- dotenv

## License

Open-source project. Feel free to modify and contribute!

## Author

**Duorfan** – [duorfan.com](https://duorfan.com)
Formatting with ChatGPT 4.0

