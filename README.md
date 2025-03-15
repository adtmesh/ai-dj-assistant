# 🎵 AI DJ Assistant - Smart Track Sequencing for DJ Sets 🎧  

This project helps DJs **automatically organize MP3 tracks** for a **smooth and professional DJ set**.  
The system analyzes **BPM, Key, and Energy** from your tracks and orders them for the best **mixing flow**.

## **🚀 Features**
✅ Extracts **BPM, Key, and Energy** from MP3 files  
✅ **Smartly orders tracks** for smooth transitions  
✅ **Customizable weight settings** for different types of sets  
✅ Saves **final DJ setlist** as CSV  

---

## **🛠 Setup Instructions**
### **1️⃣ Install Dependencies**
Run the following in your terminal:
```bash
pip install librosa pydub numpy scipy networkx pandas
```

### **2️⃣ Add MP3 Files**
Place your MP3 files inside the `data/` folder (or update `paths.py` to point to your track folder):
```python
# paths.py
FOLDER_PATH = "/your/path/to/mp3/files"
```

### **3️⃣ Run the Program**
To generate a DJ setlist, run:
```bash
python app.py
```
You'll be prompted to enter **weights** for BPM, Key, and Energy.

---

## **🎛️ Customizing Track Sorting**
The system allows you to **prioritize** different aspects of your DJ set by adjusting weights:

| **Parameter** | **Effect When Weight is High** |
|--------------|--------------------------------|
| **BPM Weight** | Keeps tempo stable, avoiding drastic BPM jumps. |
| **Key Weight** | Ensures smooth **harmonic mixing** between tracks. |
| **Energy Weight** | Prevents sudden drops in energy, ensuring smooth intensity progression. |

You’ll be asked to enter these values when running the script.

---

## **🎵 Recommended Weight Settings for Different DJ Sets**
| **Set Type**          | **BPM Weight** | **Key Weight** | **Energy Weight** | **Description** |
|----------------------|--------------|-------------|--------------|----------------|
| **Chill Lounge Set** ☕ | `1` | `3` | `1` | Focuses on smooth key transitions and low-energy changes. Ideal for relaxed settings like cafes or early-night warm-ups. |
| **Deep House / Minimal Techno** 🎶 | `2` | `2` | `2` | Balanced across BPM, key, and energy to ensure steady progression without sudden shifts. |
| **High-Energy Festival Set** 🎆 | `2` | `1` | `3` | Prioritizes **energy build-up** over perfect key transitions. Great for mainstage EDM, techno, or hardstyle. |
| **Smooth Club Set** 🍸 | `1` | `2` | `2` | Keeps transitions natural and prevents sudden jumps in energy or BPM. Ideal for clubs with an evolving dancefloor. |
| **Harmonic Mixing Focus** 🎼 | `1` | `3` | `1` | Prioritizes **key transitions** for a seamless harmonic set, perfect for deep/progressive house and melodic techno. |
| **Techno / Hard Dance** 🚀 | `3` | `1` | `2` | Prioritizes **BPM consistency** for relentless energy while keeping energy somewhat controlled. |
| **Afrobeats / Reggaeton / Latin** 🔥 | `2` | `2` | `2` | Keeps rhythm steady while allowing key shifts for groove variety. |
| **Trap / Hip-Hop / RnB** 🎤 | `3` | `1` | `2` | Keeps **BPM in sync** to avoid drastic tempo changes while allowing flexible key transitions. |
| **Peak-Hour Club Set** 🔊 | `2` | `2` | `3` | High-energy, crowd-moving music with **controlled BPM flow** and **gradual energy rise**. |
| **Ambient / Downtempo** 🌌 | `1` | `3` | `1` | Ensures relaxed transitions with smooth harmonic flow. |

---

## **📜 How It Works**
1. **Analyzes** all MP3 files inside the specified folder (`paths.py`).
2. **Sorts tracks** using a **graph-based optimization algorithm**.
3. **Creates a final setlist** optimized for smooth transitions.
4. **Saves the setlist** as `dj_setlist.csv`.

---

## **📂 Project Folder Structure**
```
ai-dj-assistant/
│── data/                 # Store MP3 files here
│── app.py                # Main script (runs the DJ assistant)
│── analyzer.py           # Extract BPM, Key, Energy from MP3s
│── playlist_generator.py # Smart sequencing algorithm
│── paths.py              # Stores the track folder path
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## **🛠 Future Improvements**
🔹 **Graph visualization of the setlist (Energy vs. BPM vs. Time)**  
🔹 **Automated cue point detection (Intro & Outro markers)**  
🔹 **Export to DJ software (Serato, Rekordbox)**  
🔹 **User interface with drag-and-drop track adjustments**  

🚀 **Have feedback or feature ideas? Let me know!** 🎧

---

## **📩 Contact**
If you have any questions or want to contribute, feel free to reach out!  
Enjoy your seamless DJ sets! 🎶🔥
