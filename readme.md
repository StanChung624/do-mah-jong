# How to launch a game
## Step 1. Download source code
Clone/Download this repository to your computer.
## Step 2. Download requirements
run $ `pip3 install -r requirements.txt` in terminal
## Step 3. Play
run $ `py Run.py` then enjoy!


# UI setting using pyqt designer

## install pyqt6
in terminal, type:
`$ pip3 install pyqt6`

## launch ui designer
in terminal, type:
`$ pyqt6-tools designer`
then establish your design

## create .py from .ui
in terminal, type:
`$ pyuic6 -x ${ui_filename} -o ${out_py_filename}`
    `${ui_filename}` : created .ui from designer
    `${out_py_filename}` : output python script

the python script will bw generated for usage.
