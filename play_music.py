"""Now the most fun part, its time to listen to the generated music!!"""

import subprocess
import os

# --- File paths ---
abc_file = "generated.abc"
midi_file = "generated.mid"
wav_file = "generated.wav"
soundfont_path = "/Users/s.sevinc/musicgen-nottingham/FluidR3_GM.sf2"  # Download and adjust the path to this file


#First, convert the ABC file to a MIDI file.

try:
    subprocess.run(["abc2midi", abc_file, "-o", midi_file], check=True)
    print(f"MIDI created: {midi_file}")
except subprocess.CalledProcessError as e:
    print("Failed to convert ABC to MIDI:", e)
    exit()


#Second, covnert the MIDI file to a wav file with fluidsynth.

try:
    subprocess.run([
        "fluidsynth",
        soundfont_path,
        midi_file,
        "-F",
        wav_file,
        "-r", "44100"
    ], check=True)
    print(f"WAV created: {wav_file}")
except subprocess.CalledProcessError as e:
    print("Failed to convert MIDI to WAV: ", e)
    exit()


#Autoplay the generated file (on macOS).

try:
    subprocess.run(["open", wav_file])
except Exception:
    print(f"Done. You can open {wav_file} manually.")






