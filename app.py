import os
from tkinter import Tk, ttk, filedialog, StringVar, messagebox, Radiobutton
from yt_dlp import YoutubeDL

# Download from YouTube
def download_from_youtube(search_query, download_path, format_choice):
    try:
        ffmpeg_path = './ffmpeg1/ffmpeg.exe'
        if not os.path.exists(ffmpeg_path):
            raise FileNotFoundError("FFmpeg executable not found")
        

        ydl_opts = {}
        if format_choice == "MP3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': True,
                'ffmpeg_location': ffmpeg_path
            }
        elif format_choice == "MP4":
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'merge_output_format': 'mp4',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'ffmpeg_location': ffmpeg_path
            }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")



# Download YouTube video
def download_youtube_video(url, download_path, format_choice):
    download_from_youtube(url, download_path, format_choice)
    messagebox.showinfo("Success", "YouTube video downloaded successfully!, Check selected folder or DownloadedVideos folder")

# Start download based on user selection
def start_download():
    url = url_entry.get().strip()
    download_path = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return
    if download_path == "Select Download Path:":
        try:
            download_path = './DownloadedVideos'
        except:
            messagebox.showinfo("Success", "Choose Download Path")
            return

    format_choice = format_var.get()
    download_youtube_video(url, download_path, format_choice)

# Select download path
def select_path():
    path = filedialog.askdirectory()
    if path:
        path_var.set(path)

# GUI setup
app = Tk()
app.title("YouTube Content Downloader")
app.geometry("700x500")

# File path selection
path_var = StringVar()
path_var.set("Select Download Path:")
path_label = ttk.Label(app, textvariable=path_var)
path_label.pack(pady=10)
path_button = ttk.Button(app, text="Browse", command=select_path)
path_button.pack(pady=5)

# URL entry
url_label = ttk.Label(app, text="Enter URL:")
url_label.pack(pady=10)
url_entry = ttk.Entry(app, width=50)
url_entry.pack(pady=5)


# Format selection (for YouTube only)
format_var = StringVar(value="MP3")
format_label = ttk.Label(app, text="Select Format (YouTube Only):")
format_label.pack(pady=10)
mp3_radio = Radiobutton(app, text="MP3", variable=format_var, value="MP3")
mp3_radio.pack()
mp4_radio = Radiobutton(app, text="MP4", variable=format_var, value="MP4")
mp4_radio.pack()

# Download button
download_button = ttk.Button(app, text="Start Download", command=start_download)
download_button.pack(pady=20)

# Exit button
exit_button = ttk.Button(app, text="Exit", command=app.destroy)
exit_button.pack(pady=10)

# Run the GUI
app.mainloop()
