"""Now the most fun part, its time to listen to the generated music!!"""
from music21 import converter, stream
import subprocess
import os
import copy 

abc_file = "generated.abc"
midi_file = "generated.mid"
wav_file = "generated.wav"

soundfont_path = "/Users/s.sevinc/musicgen-nottingham/FluidR3_GM.sf2" #replace this with the path to the .sf2 file

#first convert the abc file to a midi file
try:
    print(f"Reading {abc_file} ...")
    score = converter.parse(abc_file, format='abc')
    print(f"MIDI created: {midi_file}")
except Exception as e:
    print("Failed to convert ABC to a MIDI file: ", e)
    exit()

#second, covnert the MIDI file to a wav file with fluidsynth

try:
    print(f"Converting {midi_file} to {wav_file }")
    subprocess.run([
        "fluidsynth",
        "-ni",
        soundfont_path,
        midi_file,
        "-F",
        wav_file,
        "-r", "44100"
    ], check=True)
    print(f" Wav file created: {wav_file}")
except subprocess.CalledProcessError as e:
    print("Failed to convert MIDI:", e)
    exit()

#Autoplay the generated file (on macOS)

try:
    subprocess.run(["open", wav_file])
except Exception:
    print(f"Done. You can open {wav_file} manually.")






