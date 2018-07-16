#! python3
# Program that deletes the old GBA savefile after using the multiplayer feature
# in VBA-M, and removes the numbers added to the end of the new savefile so
# that it matches the name of the ROM again.

# Put the .exe file in the same folder as your GBA roms and savefiles.

# By Anderson Adon andersonaadon@gmail.com

import os
import re
import send2trash
import shutil

# Get list of files in directory
file_list = os.listdir('.')

# Regular expression used for finding GBA rom files
extension = re.compile('\.gba$')
rom_files = list(filter(extension.search, file_list))

# Gets the name of the games themselves without the ".gba"
rom_names = [file[:file.index('.gba')] for file in rom_files]

# For each game, look for its savefiles, delete the old one and rename the new one
# There should be no more than two savefiles, the old one and the new one with
# a number at the end
for name in rom_names:
    savefiles = [file for file in file_list if file.startswith(name) &
                 file.endswith('.sav')]
    if len(savefiles) == 2:
        index = [i for i, file in enumerate(savefiles) if
                 re.search('-\d\.sav$', file)]
        if index[0] == 0:
            save_name = savefiles[1]
            send2trash.send2trash(savefiles[1])
            shutil.move(savefiles[0], save_name)
        elif index[0] == 1:
            save_name = savefiles[0]
            send2trash.send2trash(savefiles[0])
            shutil.move(savefiles[1], save_name)
