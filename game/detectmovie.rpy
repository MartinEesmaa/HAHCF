# Detect movie format based appropriate on platforms on Ren'Py
# Programmed by Martin Eesmaa (2025)
# License: MIT License
# Use of Ren'Py 6.13 and earlier/later support of this file.
# Source code: https://github.com/MartinEesmaa/HAHCF

init -100 python:
    recodeMovie = False  # Default value to play original files.
    if renpy.windows or renpy.macintosh or renpy.linux:
        recodeMovie = False
    elif renpy.android:
        recodeMovie = True
    elif renpy.ios:
        recodeMovie = True
    elif renpy.emscripten:
        recodeMovie = True # Modern website supports their codecs.
    else:
        recodeMovie = False # Fallback to default behavior.