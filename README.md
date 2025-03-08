# 🎬 YouTube Transcript Downloader

## **About**

The YouTube Transcript Downloader is a simple yet powerful tool that extracts transcripts from YouTube videos and saves them as a single, clean text file (`output.txt`). It eliminates the need for manual transcription, making it an efficient and time-saving solution for content creators, researchers, and students.

---

## **🚀 Functions**
✔ **Extracts** YouTube transcripts with ease.  

✔ **Saves** the Transcript to `output.txt` without displaying it in the terminal.  

✔ **Overwrites existing data** in `output.txt` for a fresh output every time.  

✔ **Simple UI/UX** with a structured main menu for better navigation.  

✔ **Supports multiple YouTube URL formats** (`watch,` `embed,` `short links`).  

✔ **Handles errors gracefully** if the video has no transcript.  

---
## **📦 Startup sequence**

**1.** Use the git CLI command to clone this GitHub repository:

```bash
git clone https://github.com/LinuxSystemsEngineer/youtube_transcript_downloader.git
```
---

**2.** Change directories to your newly cloned GitHub repository:

```bash
cd youtube_transcript_downloader
```
---

**3.** Create a segmented python virtual environment:

```bash
python3 -m venv .segment
```
---

**4.** Activate your segmented python virtual environment

---

Linux/macOS:

```bash
source .segment/bin/activate
```

---

Windows:

```
.segment\Scripts\activate
```

----------

## **📦 Install the requirements**
This program requires **Python 3.12 or newer** and one external library:

- `youtube-transcript-api` (for retrieving YouTube video transcripts)

### **Installing Required Packages**
Before running the program, install the required package:
```bash
pip3 install -r requirements.txt
``` 

----------


## **📜 How it works**

1️⃣ **Run the script**

```bash
python3 main.py
``` 

2️⃣ **Choose an option**

-   **1** → Enter a YouTube URL to extract the Transcript.
-   **2** → Exit the program.

3️⃣ **Enter the YouTube URL**

-   The program extracts the Transcript and **saves it to `output.txt`** in the current directory.
-   It does **not** display the Transcript in the terminal for a cleaner experience.

4️⃣ **Confirmation Message**

-   If successful:
       
    `✅ Transcript successfully exported to 'output.txt.'` 
    
-   If an error occurs (e.g., no transcript available):
    
    `❌ An error occurred while retrieving the transcript.` 
    
----------

## **🛠 Example Usage**


```bash
==================================================
   🎬 YouTube Transcript Downloader   
==================================================
  1. Enter YouTube URL
  2. Exit
==================================================
➡ Enter either 1 or 2, then press Enter: 1

➡ Enter YouTube URL, then press Enter: https://www.youtube.com/watch?v=EXAMPLE_VIDEO_ID

✅ Transcript successfully exported to 'output.txt.'
``` 

----------

## **✅ Why Use This Tool?**

✔ **Save time** – No need to transcribe videos manually.
  
✔ **Improves productivity** – Useful for research, education, and accessibility. 
 
✔ **Simple and fast** – Runs in the command line with **lightweight efficiency**. 
 
✔ **Lightweight** – Only requires one external Python library.

----------

## **📄 License**

This project license is the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---
