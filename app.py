from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript_to_file(video_id, transcript_data, output_file):
    # Merge all transcript texts
    full_text = ""
    for snippet in transcript_data:
        # Add a period and space to the end of each text snippet
        text = snippet.get('text', '').strip()
        # If the text doesn't end with a period, add a period
        if not text.endswith(('.', '!', '?')):
            text += '.'
        full_text += text + " "
    
    # Write the text to the file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Transcript saved to {output_file}") # Print the output file name

def main():
    # Video ID
    video_id = "" #ADD VIDEO ID HERE
    
    # Start the YouTube Transcript API
    ytt_api = YouTubeTranscriptApi()

    try:
        # Get the transcript directly
        transcript_data = ytt_api.get_transcript(video_id)
        
        # Create the output file name with the video ID
        output_file = f"transcript_{video_id}.txt"
        
        # Save the transcript to the file
        save_transcript_to_file(video_id, transcript_data, output_file)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}") # Print the error message

if __name__ == "__main__":
    main()
