import subprocess

def make_folder(y):
    result=subprocess.run(["mkdir",y])
    return result

def delete_folder(y):
    subprocess.run(["rmdir",y])
    return

def file_count():
    
