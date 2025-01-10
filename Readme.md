# YouTube Content Downloader

A simple and easy-to-use desktop application that allows users to download YouTube videos and audio in MP3 or MP4 formats. The app uses `yt-dlp` for content downloading and provides a GUI built with `Tkinter`.

## Features

- **Download YouTube Videos** in MP4 format.
- **Download Audio** in MP3 format.
- **Customizable Download Path**: Choose where to save the downloaded content.
- **Supports MP3 and MP4 formats**.

## Requirements

- Python 3.x
- FFmpeg (bundled with the project)
- `yt-dlp` library (included in `requirements.txt`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AneeshNagdev/YouTube-Content-Downloader.git
    cd YouTube-Content-Downloader
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    python main.py
    ```

## Usage

1. Launch the application.
2. Enter the YouTube video URL you want to download.
3. Choose the desired format (MP3 or MP4).
4. Select the download folder.
5. Click **Start Download** to begin the download process.

The downloaded content will be saved in the chosen folder or the default `DownloadedVideos` folder.

## Contributing

Contributions are welcome! To contribute, fork the repository, make your changes, and submit a pull request.

## Troubleshooting

- **FFmpeg not found**: Ensure the `ffmpeg1` folder is present and contains `ffmpeg.exe`.
- **Download errors**: Ensure your internet connection is working and that the URL is correct.
- **Missing dependencies**: Run `pip install -r requirements.txt` to install all necessary libraries.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube downloading.
- [FFmpeg](https://ffmpeg.org/) for media conversion.
