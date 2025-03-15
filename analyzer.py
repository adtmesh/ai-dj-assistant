import librosa
import numpy as np
import os
from paths import FOLDER_PATH  # Import the path for MP3 files

def analyze_track(file_path):
    """Extract BPM, key, and energy from an MP3 file"""
    
    try:
        # Load audio file
        y, sr = librosa.load(file_path, sr=None)

        # Extract BPM
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        # Extract spectral energy (RMS energy)
        energy = librosa.feature.rms(y=y).mean()

        # Extract key (chroma features)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        key = int(np.argmax(np.sum(chroma, axis=1)))

        return {
            "filename": os.path.basename(file_path),
            "bpm": round(float(tempo)),
            "key": key,
            "energy": round(float(energy), 4)
        }

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def analyze_folder():
    """Analyze all MP3 files in the specified folder"""
    tracks = []
    
    for file in os.listdir(FOLDER_PATH):
        if file.endswith(".mp3"):
            file_path = os.path.join(FOLDER_PATH, file)
            track_info = analyze_track(file_path)
            if track_info:
                tracks.append(track_info)
    
    return tracks

# Example usage
if __name__ == "__main__":
    tracks = analyze_folder()
    for track in tracks:
        print(track)
