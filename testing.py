import subprocess
import os

abc_file = "generated.abc"
midi_file = "generated.mid"
wav_file = "generated.wav"
soundfont_path = "/Users/s.sevinc/Downloads/FluidR3_GM.sf2"  # ✅ change to yours

# ✅ Step 1: Convert ABC to MIDI using abc2midi
try:
    print(f"📖 Converting {abc_file} to {midi_file} using abc2midi...")
    subprocess.run(["abc2midi", abc_file, "-o", midi_file], check=True)
    print(f"✅ MIDI file created: {midi_file}")
except subprocess.CalledProcessError as e:
    print("❌ abc2midi failed. Is it installed?")
    exit()

# ✅ Step 2: Convert MIDI to WAV using fluidsynth
try:
    print(f"🎧 Converting {midi_file} to {wav_file} using fluidsynth...")
    subprocess.run([
        "fluidsynth",
        "-ni", soundfont_path,
        midi_file,
        "-F", wav_file,
        "-r", "44100"
    ], check=True)
    print(f"✅ WAV file created: {wav_file}")
except subprocess.CalledProcessError as e:
    print("❌ fluidsynth failed. Check your soundfont path.")
    exit()

# ✅ Step 3: Auto-play the WAV (macOS)
try:
    subprocess.run(["open", wav_file])
except Exception:
    print(f"📂 Done. You can open {wav_file} manually.")
