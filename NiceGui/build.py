import os
import subprocess
from pathlib import Path
import nicegui

static_dir = Path(nicegui.__file__).parent
parameters = '--onefile main.py --name "myapp" --add-binary "D:/Python/NiceGui/SimConnect.dll;." ' + \
    f'--add-data="{static_dir}{os.pathsep}nicegui"'

subprocess.call('pyinstaller ' + parameters, shell=True)