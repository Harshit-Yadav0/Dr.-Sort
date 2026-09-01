# Section of lib i use in this project
import function as fun #The functions that i made
import subprocess
import os
import shutil
from pathlib import path
import getpass


#Main code
username=getpass.getuser()
subprocess.run(["mkdir",username])
subprocess.run(["cd",username]) #Not working till now
subprocess.run(["mkdir","big"])
subprocess.run(["cd","big"])
subprocess.run(["mkdir","Document"])
subprocess.run(["mkdir","Images"])
subprocess.run(["mkdir","Audio"])
subprocess.run(["mkdir","Vedio"])
subprocess.run(["mkdir","Undefined"])
device_path=Path.home()

#/main/file extension table
text=["txt", "doc", "docx", "pdf", "rtf", "odt", "md", "tex", "log"]
