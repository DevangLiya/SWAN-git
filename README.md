# SWAN
[![forthebadge](https://forthebadge.com/images/badges/built-with-science.svg)](https://forthebadge.com)	[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)	[![forthebadge](https://forthebadge.com/images/badges/contains-technical-debt.svg)](https://forthebadge.com)

Personal programs for SWAN Imaging Challenge 2019

## Description of programs
*Important: Please try to maintain the given directory structure. Don't forget to modify the programs accordingly if you want to work with a different directory structure.*

* __read_data.py__: Primarily used as a module in other programs to read the data from .mbr file and convert it into lists. Can be run on its own to print the number of packets in the .mbr file.

* __read_save_data.py__: Creates a new file for each tile and saves the polarization data for respective tile in the form of X, Y columns separated by single space. Takes .mbr file as input.

* __spectrums<span>.py</span>__: Generates dynamic spectrum starting from a file where X and Y polarizations are arranged in columns separated by a single space. The program also contains code to plot and compare power spectrum (commented out). However, it is up to the user to modify the program suitable to their needs. This program can be used directly after executing read_save_data.py.

* __generate_PS2.0.py__: Generates dynamic spectrum starting from an .mbr file. This is a legacy code and it is uploaded here just for the sake of completeness. THIS PROGRAM SHOULD NOT BE USED ANYMORE.

## Developer's note
I have taken every step in my control to make these programs as readable as I can. All the programs contain comments wherever they're needed. All the functions have docstrings (madlad stuff, right‽) which can be accessed by using `print(function.__doc__)` on python prompt or `function?` in ipython prompt.

Feel free to ask questions (or raise an issue) about these programs if it's not clear even after reading the documentation. If you come to me without reading the documentation then I might tell you to go [RTFM](https://www.urbandictionary.com/define.php?term=RTFM).

Oh, and here's a playful Golden Retriever puppy wanting to hug you and wish you a great day!

<div align="center">
<img src="good_day.jpg" alt="https://www.flickr.com/photos/138248475@N03/23930735040" width="50%" />
</div>


[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
