import os
import sys
from pathlib import Path
from cairosvg import svg2png

import tkinter as tk
from tkinter import filedialog, messagebox

def svg_string2png(svg_path):
    with open(svg_path) as fp:
        svg_code = fp.read()
        png_path = f'{Path(svg_path).stem}.png'
        svg2png(bytestring=svg_code, write_to=png_path)
        return png_path

def get_bundle_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.abspath(__file__))

def process_file():
    initial_dir = get_bundle_dir()
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    try:
        png_path = svg_string2png(file_path)
        messagebox.showinfo('Success',
                            f'SVG file converted to PNG successfully at {png_path} !')
        os.startfile(png_path)
    except FileNotFoundError:
        messagebox.showinfo('Error', f'File {file_path} not found. Please check the file path.')

if len(sys.argv) != 2:
    root = tk.Tk()
    root.withdraw()
    process_file()
else:
    file_path = sys.argv[1]
    try:
        svg_string2png(file_path)
    except FileNotFoundError:
        print(f'Error: File {file_path} not found. Please check the file path.')

