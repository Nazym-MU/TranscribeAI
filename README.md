# TranscribeAI

This project provides a Python script for automatically transcribing video files. It extracts audio from a video, splits it into manageable chunks, and uses OpenAI's Whisper model to generate a text transcript.

## Features

- Extract audio from video files
- Split audio into chunks for processing
- Transcribe audio using OpenAI's Whisper model
- Save transcripts to text files in the Downloads folder

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- FFmpeg installed on your system and accessible in the PATH
- An OpenAI API key

## Installation

1. Clone this repository or download the script.

2. Install the required Python packages:

   ```
   pip install moviepy pydub python-dotenv openai
   ```

3. Create a `.env` file in the same directory as the script and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your video file in the Downloads folder.

2. Modify the `video_path` variable in the script to point to your video file:

   ```python
   video_path = os.path.expanduser("~/Downloads/your_video_file.mp4")
   ```

3. Run the script:

   ```
   python main.py
   ```

4. The script will process the video and save the transcript as a text file in the Downloads folder.

## Configuration

- You can adjust the `chunk_length_ms` parameter in the `split_audio` function to change the size of audio chunks processed at once.
- The script is set to use the "whisper-1" model. You can change this by modifying the `model` parameter in the `transcribe_audio` function.

## Troubleshooting

- If you encounter issues with FFmpeg, ensure it's correctly installed and the path is set in the script:

  ```python
  os.environ['IMAGEIO_FFMPEG_EXE'] = '/path/to/your/ffmpeg'
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.