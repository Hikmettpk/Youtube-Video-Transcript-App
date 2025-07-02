# YouTube Video Transcript Extractor

A Python application that automatically extracts transcripts (subtitles) from YouTube videos and saves them to a text file.

## Features

- Automatically extracts transcripts from YouTube videos
- Enhances readability by adding proper punctuation at the end of each sentence
- Saves output as a text file
- Supports automatically generated subtitles
- Handles multiple languages (defaults to English)

## Installation

### Method 1: Direct Installation

First, install the required library:

If you using MacOS or Linux:
```bash
pip3 install youtube-transcript-api 
```

If you using Windows:
```bash
pip install youtube-transcript-api
```

### Method 2: Using Requirements File

1. Clone the repository:
```bash
git clone [your-repo-url]
cd youtube-transcript-script
```

2. Create a virtual environment:

If you using MacOS or Linux:
```bash
python3 -m venv env
source env/bin/activate
```

If you using Windows:
```bash
python -m venv env
env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Identify the Video ID (e.g., from YouTube URL `https://www.youtube.com/watch?v=T8mKo3Aa7z1` -> `T8mKo3Aa7z1`)

2. Run the script:

If you using MacOS or Linux:
```bash
python3 app.py 
```

If you using Windows:
```bash
python app.py
```

The script will generate a file named `transcript_[VIDEO_ID].txt` containing the formatted transcript.

## How It Works

1. Fetches the transcript using the YouTube Transcript API
2. Processes each text snippet to ensure proper punctuation
3. Combines all snippets into a single coherent text
4. Saves the formatted text to a file


## Acknowledgments

This project uses the [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) library. Special thanks to [@jdepoix](https://github.com/jdepoix) and all contributors for developing this amazing library that makes transcript extraction simple and efficient. 

## Contributing

Feel free to:
1. Fork the repository
2. Create a new branch
3. Submit a pull request