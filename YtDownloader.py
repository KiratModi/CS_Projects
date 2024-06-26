from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(yt, save_path):
    try:
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print(f"Video '{yt.title}' downloaded successfully")
    except Exception as e:
        print(e)

def download_audio(yt, save_path):
    try:
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=save_path)
        print(f"Audio '{yt.title}' downloaded successfully")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Please select a folder...")
    else:
        choice = input("Do you want to download video or audio? (Enter 'video' or 'audio'): ").strip().lower()
        yt = YouTube(video_url)

        if choice == 'video':
            print("Download Started: Video")
            download_video(yt, save_dir)
        elif choice == 'audio':
            print("Download Started: Audio")
            download_audio(yt, save_dir)
        else:
            print("Invalid choice. Please enter 'video' or 'audio'.")
