"""
Big idea: take Google Cloud's Text-to-Speech API and build something cool!
- This trivial example outputs audio files for common fruits
- remember! set GOOGLE_APPLICATION_CREDENTIALS=C:\yourpath\yourcredentials.json
- to supress warnings: python -W ignore fruits.py
"""

import speech2text as st

if __name__ == '__main__':
    # output one
    text = "Welcome to Appcology! I can't wait to see what you all create."
    fileName = "hi.mp3"
    st.outputSpeech(text, fileName)

    # output multiple
    fruitList = ["apple", "banana", "cherry", "watermelon", "tomato"]
    # NB: don't include the .mp3
    fileName2 = "fruit"
    st.outputMultiple(fruitList, fileName2)
