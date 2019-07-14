#! python3
""" Script that will delete all save files for a .gba rom except for the most
recently modified one.
"""

from pathlib import Path
__author__ = 'Anderson Adon'
__email__ = 'andersonaadon@gmail.com'

# Get list of all gba roms in directory
rom_list = list(Path('.').glob('*.gba'))

# Convert Paths to names
rom_list = [rom.name for rom in rom_list]

# Gets the name of the games themselves without the ".gba"
rom_names = [rom[:rom.index('.gba')] for rom in rom_list]

for name in rom_names:
    saves = list(Path('.').glob(name + '*.sav'))
    try:
        most_recent = max(saves, key=lambda file:file.stat().st_mtime)
    except ValueError:
        continue
    saves.remove(most_recent)
    for save in saves:
        save.unlink()
    most_recent.rename(name + '.sav')
