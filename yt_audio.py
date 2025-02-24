import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Get the path to the user's home directory
user_home = os.path.expanduser("~")

# Define the path : Change it like You want
# DOWNLOAD_PATH = "D:\\Music" # EXAMPLE path
DOWNLOAD_PATH = os.path.join(user_home, "Music") # DEFAULT path

# Argument parser setup
parser = argparse.ArgumentParser(description="Download YouTube audio with a URL.")
parser.add_argument("video_URL", type=str, help="URL of the video to download.")
args = parser.parse_args()

def check_url(url):
    if url.startswith("https://youtu.be/"):
        return True
    else:
        print(Fore.RED + Style.BRIGHT + "Error: Invalid URL! Please use a valid YouTube URL starting with 'https://youtu.be/'.")
        return False 

def download_audio(url):
    print(Fore.YELLOW + Style.BRIGHT + "Processing... Please wait.")
    yt = YouTube(url, on_progress_callback=on_progress)
    print(Fore.GREEN + Style.BRIGHT + f"Title: {yt.title}")
    print(Fore.YELLOW + Style.BRIGHT + "Downloading audio...")
    ys = yt.streams.get_audio_only()
    ys.download(DOWNLOAD_PATH)
    print(Fore.GREEN + Style.BRIGHT + "Download complete! File saved to: " + DOWNLOAD_PATH + " ")

if args.video_URL:
    if check_url(args.video_URL):
        download_audio(args.video_URL)    
else:
    url = input(Fore.CYAN + Style.BRIGHT + "Enter the YouTube URL: ")
    if check_url(url):
        download_audio(url)
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid URL. Please try again.")
