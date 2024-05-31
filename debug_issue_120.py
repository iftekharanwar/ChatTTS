import ChatTTS
import numpy as np
import soundfile as sf
import wave

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
print("Generating audio...")
audio_array_en = chat.infer(inputs_en, params_refine_text=params_refine_text, use_decoder=False)
print("Audio generation complete.")

# Check the shape and type of the audio array
print(f"Audio array shape: {np.shape(audio_array_en)}")
print(f"Audio array type: {type(audio_array_en)}")

# Concatenate the audio array and check its shape and type
concatenated_audio = np.concatenate(audio_array_en)
print(f"Concatenated audio shape: {np.shape(concatenated_audio)}")
print(f"Concatenated audio type: {type(concatenated_audio)}")

# Ensure the concatenated audio is a 2D array with shape (frames, channels)
if concatenated_audio.ndim == 1:
    concatenated_audio = np.expand_dims(concatenated_audio, axis=1)

# Ensure the audio data is in the correct range [-1, 1]
concatenated_audio = np.clip(concatenated_audio, -1, 1)

# Print the type and content of the audio array
print(f"Concatenated audio content: {concatenated_audio[:10]}")  # Print the first 10 elements for inspection

# Save the generated audio to a file using the wave module
with wave.open('output_en.wav', 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes((concatenated_audio * 32767).astype(np.int16).tobytes())
print("Audio saved to output_en.wav.")

# Simulate audio generation with a small dummy audio array
dummy_audio = np.random.rand(1000, 1)  # Create a small dummy audio array
sf.write('dummy_output.wav', dummy_audio, 24000, format='WAV')  # Save the dummy audio to a file
print("Dummy audio saved to dummy_output.wav.")
