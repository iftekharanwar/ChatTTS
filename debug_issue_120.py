import ChatTTS
from IPython.display import Audio

# Create an instance of the Chat class
chat = ChatTTS.Chat()

# Load the pre-trained models
chat.load_models()

# Define the English input text
inputs_en = """
chat T T S is a text to speech model designed for dialogue applications.
it supports mixed language input and offers multi speaker
capabilities with precise control over prosodic elements like
laughter, pauses, and intonation.
it delivers natural and expressive speech, so please
use the project responsibly at your own risk.
""".replace('\n', '') # English is still experimental.

# Set the parameters for refining the text
params_refine_text = {
  'prompt': '[oral_2][laugh_0][break_4]'
}

# Generate the audio from the English input text
audio_array_en = chat.infer(inputs_en, params_refine_text=params_refine_text, use_decoder=False)

# Play the generated audio
Audio(audio_array_en[0], rate=24_000, autoplay=True)
