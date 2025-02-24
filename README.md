Here’s a detailed **README.md** file for your GitHub repository:  

---

# **ytaudio – YouTube Audio Downloader Script** 🎵  

**ytaudio** is a simple command-line tool that allows users to download audio from YouTube videos easily. It uses `pytubefix`, a modified version of `pytube`, to handle YouTube's latest streaming changes. The script supports both **Windows PowerShell** and **Linux Terminal**, making it a versatile tool for audio extraction.  

---

## **Features** 🚀  
✅ Download high-quality audio from YouTube videos  
✅ Simple command-line interface for quick execution  
✅ Supports Windows (PowerShell) & Linux (Terminal)  
✅ Handles YouTube URL validation  
✅ Uses `pytubefix` for reliable downloading  

---

## **Installation** 🛠️  

### **1. Install Python**  
Ensure **Python 3.x** is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).  

### **2. Install Required Dependencies**  
Run the following command to install `pytubefix`:  
```sh
pip install pytubefix
```
Run the following command to install `colorama`:  
```sh
pip install colorama
```
---

## **Default Download Path** 📁  

By default, the script saves downloaded audio files in:  
```python
# Windows
DOWNLOAD_PATH = 'C:\Users\USER\Music'

# Linux
DOWNLOAD_PATH = '/home/USER/Music'
```
---
## **Changing the Download Path** 📁  

If you want to change the download location:  

1. Open **`ytaudio.py`** in a text editor.  
2. Modify the `DOWNLOAD_PATH` variable to your desired folder. Example:

```python
DOWNLOAD_PATH = "D:\\Music"
```
3. Save the file, and the audio will be downloaded to the new location.

---

## **Usage** 🎧  

### **Run the Script Directly**
To download audio from a YouTube link, use:  
```sh
python ytaudio.py "https://youtu.be/your_video_id"
```

If no URL is provided, the script will prompt you to enter one manually.

---

## **PowerShell Integration (Windows)** 💻  

To simplify usage, add a **PowerShell function**:  

1. Open PowerShell and edit your profile:  
   ```powershell
   notepad $PROFILE
   ```  
2. Add the following function at the end:  
   ```powershell
   function ytaudio { python "C:\path\to\ytaudio.py" $args }
   ```  
3. Save the file and refresh your profile:  
   ```powershell
   . $PROFILE
   ```
4. Now, you can run:  
   ```powershell
   ytaudio "https://youtu.be/your_video_id"
   ```

---

## **Linux Terminal Integration** 🐧  

To make `ytaudio` a terminal command:  

1. Open your terminal and edit your `.bashrc` or `.zshrc` file:  
   ```sh
   nano ~/.bashrc   # For Bash users
   nano ~/.zshrc    # For Zsh users
   ```  
2. Add the following alias at the end:  
   ```sh
   alias ytaudio='python3 /path/to/ytaudio.py'
   ```  
3. Save and reload the profile:  
   ```sh
   source ~/.bashrc   # or source ~/.zshrc
   ```
4. Now, you can run:  
   ```sh
   ytaudio "https://youtu.be/your_video_id"
   ```

---

## **Example Output** 📜  
```sh
Processing...
Song Title - Artist
Downloading...
Download Complete: D:\Music
```

---

## **Contributing** 🤝  
Pull requests and improvements are welcome! Feel free to fork the project and contribute.

---

## **License** 📜  
This project is licensed under the **MIT License**.

---

Let me know if you need any modifications! 🚀