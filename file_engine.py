# Section of lib i use in this project
import function as fun #The functions that i made
import subprocess
import os
import shutil
from pathlib import path
import getpass


#Main code
username = getpass.getuser()

# Define base path at the user's home directory
base_path = Path.home() / username / "big"

# Create directories including parents if they do not exist
for folder in ["Document", "Images", "Audio", "Video", "Undefined"]:
    dir_path = base_path / folder
    dir_path.mkdir(parents=True, exist_ok=True)

#/main/file extension table
text=["txt", "doc", "docx", "pdf", "rtf", "odt", "md", "tex", "log"]
