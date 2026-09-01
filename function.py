import subprocess
import os


def make_folder(y):
    subprocess.run(["mkdir",y])
    result=401
    
    return result

def delete_folder(y):
    subprocess.run(["rmdir",y])
    return

def file_count():
    result=subprocess.run

def file_type(x):
    i=0
    with open ("file_dir.txt") as file:
        for line in file:
            i=i+1
            file_def=line.split(',')
            if x in file_def:
                return i
                break
            else:
                code=401
                return code

def find_folder(name):
    result=subprocess.run(["find",".","-name", name], capture_output=True)
    return result.stdout

def file_name():
    
    
