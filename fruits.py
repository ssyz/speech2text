"""
Big idea: take Google Cloud's Text-to-Speech API and build something cool!
- This trivial example outputs audio files for common fruits
- remmber! set GOOGLE_APPLICATION_CREDENTIALS=C:\yourpath\yourcredentials.json
- to supress warnings: python -W ignore fruits.py
"""

import speech2text as st

if __name__ == '__main__':
    # list of values to translate to speech
    fruits = ["apple", "banana", "cherry", "watermelon", "tomato"]
    # use loops to output multiple files! https://www.w3schools.com/python/python_for_loops.asp
    for f in fruits:
        st.outputSpeech("This is how I say " + f, f + ".mp3")
