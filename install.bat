@echo off 
Title downloading the nitro gen...
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python -m pip install -r requirements.txt
cls
Title Downloading the nitro gen
echo python nitro.py >> start.bat
start start.bat
