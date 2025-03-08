import sys
import os
from urllib.parse import urlparse, parse_qs

def clear_screen():
    """ Clears the screen for better UI experience. """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """ Displays a structured and visually improved menu. """
    clear_screen()
    print("=" * 50)
    print("   🎬 YouTube Transcript Downloader   ")
    print("=" * 50)
    print("  1. Enter YouTube URL")
    print("  2. Exit")
    print("=" * 50)

def get_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    Handles standard, short, and embed URL formats.
    """
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname or ''
    if hostname.endswith('youtu.be'):
        return parsed_url.path[1:]
    elif 'youtube' in hostname:
        if parsed_url.path == '/watch':
            query_params = parse_qs(parsed_url.query)
            return query_params.get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
    return None

def save_transcript(video_id):
    """
    Retrieves and saves the YouTube transcript silently.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript_text = " ".join(entry["text"] for entry in transcript_list)

        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(transcript_text)
        
        print("\n✅ Transcript successfully exported to 'output.txt'.")
    
    except Exception as e:
        print("\n❌ An error occurred while retrieving the transcript:", e)
        sys.exit(1)

def main():
    while True:
        display_menu()
        choice = input("➡ Enter either 1 or 2, then press Enter: ").strip()
        
        if choice == "1":
            url = input("\n➡ Enter YouTube URL, then press Enter: ").strip()
            video_id = get_video_id(url)
            
            if not video_id:
                print("\n⚠ Error: Could not extract video ID from the provided URL.")
                input("Press Enter to continue...")
                continue

            save_transcript(video_id)
            input("\nPress Enter to return to the main menu...")

        elif choice == "2":
            print("\n👋 Exiting... Have a great day!")
            sys.exit(0)

        else:
            print("\n⚠ Invalid option. Please enter 1 or 2 and press Enter.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()

