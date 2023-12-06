import tkinter as tk
import subprocess

def launch_program():
    program_path = "C:\\Users\\Kishan Sharma\\Desktop\\bbracing.lnk"  
    subprocess.Popen(program_path, shell=True)



launch_program()

