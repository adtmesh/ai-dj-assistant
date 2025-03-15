import analyzer
import playlist_generator
import pandas as pd
from paths import FOLDER_PATH  # Import path for MP3 files

# Step 1: Analyze all MP3 files
tracks = analyzer.analyze_folder()

# Step 2: Ask for Custom Weight Preferences
print("\n🔧 Customize Track Sequencing Weights:")
bpm_weight = float(input("➡️  Enter BPM Weight (Recommended: 1-3): ") or 1)
key_weight = float(input("➡️  Enter Key Weight (Recommended: 1-3): ") or 1)
energy_weight = float(input("➡️  Enter Energy Weight (Recommended: 1-3): ") or 1)

# Step 3: Sort tracks with custom weights
ordered_filenames = playlist_generator.create_transition_graph(tracks, bpm_weight, key_weight, energy_weight)

# Step 4: Display Final Setlist
df_ordered = pd.DataFrame([t for t in tracks if t["filename"] in ordered_filenames])
print("\n🎶 Final DJ Setlist:")
print(df_ordered)

# Save to CSV for reference
df_ordered.to_csv("dj_setlist.csv", index=False)
