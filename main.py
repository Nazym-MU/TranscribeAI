import os
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

os.environ['IMAGEIO_FFMPEG_EXE'] = '/usr/local/bin/ffmpeg'
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def extract_audio(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def split_audio(audio_path, chunk_length_ms=60000):
    audio = AudioSegment.from_wav(audio_path)
    chunks = make_chunks(audio, chunk_length_ms)
    return chunks

def transcribe_audio(audio_chunk):
    with open("temp_chunk.wav", "wb") as f:
        audio_chunk.export(f, format="wav")
    
    with open("temp_chunk.wav", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    
    os.remove("temp_chunk.wav")
    return transcript.text

def transcribe_video(video_path):
    # Extract audio from video
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)

    # Split audio into chunks
    audio_chunks = split_audio(audio_path)

    # Transcribe each chunk
    full_transcript = ""
    for i, chunk in enumerate(audio_chunks):
        print(f"Transcribing chunk {i+1}/{len(audio_chunks)}...")
        chunk_transcript = transcribe_audio(chunk)
        full_transcript += chunk_transcript + " "

    # Clean up temporary files
    os.remove(audio_path)

    return full_transcript.strip()

def save_transcript(transcript, video_name):
    # Get the Downloads folder path
    downloads_folder = os.path.expanduser("~/Downloads")
    
    # Create a file name based on the video name
    file_name = f"{os.path.splitext(video_name)[0]}_transcript.txt"
    file_path = os.path.join(downloads_folder, file_name)
    
    # Save the transcript to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(transcript)
    
    print(f"Transcript saved to: {file_path}")

# Usage 
video_path = os.path.expanduser("~/Downloads/{name_of_your_video}.mp4") # Replace with the path to your video
video_name = os.path.basename(video_path)
transcript = transcribe_video(video_path)
save_transcript(transcript, video_name)
print("Transcription complete and saved to Downloads folder.")