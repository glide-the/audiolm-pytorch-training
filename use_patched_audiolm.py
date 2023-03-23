# use the personal_hacks branch of my fork of the repo to get print statements, etc etc.

import urllib.request
import os
import zipfile
import subprocess
import shutil

raise AssertionError("don't forget to revert the encodec supoprt commit when the encodec_support PR is merged")
zip_file_path = "audiolm-pytorch-encodec-support.zip"
input("type anything to confirm that you have pushed the latest version of the encodec_support branch to Github as well!!")

if os.path.isfile(zip_file_path):
    replace = input("personal hacks zip already exists. replacing (as well as audiolm_pytorch library...)")
    os.remove(zip_file_path)
    shutil.rmtree("audiolm_pytorch")
urllib.request.urlretrieve("https://github.com/LWProgramming/audiolm-pytorch/archive/refs/heads/encodec_support.zip", zip_file_path)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall("audiolm-pytorch")


# install requirements from the patched audiolm-pytorch directory
subprocess.run(['pip', 'install', 'audiolm-pytorch/audiolm-pytorch-encodec_support'])

# move library itself to current directory
subprocess.run(['mv', 'audiolm-pytorch/audiolm-pytorch-encodec_support/audiolm_pytorch', '.'])

# # move setup.py to current directory for requirements
# subprocess.run(['mv', 'audiolm-pytorch/audiolm-pytorch-encodec_support/setup.py', '.'])

# remove the rest of the audiolm-pytorch directory
subprocess.run(['rm', '-rf', 'audiolm-pytorch'])
