import tkinter as tk
from ui import create_ui
from config import load_directory

if __name__ == "__main__":
    download_directory = load_directory()
    root = tk.Tk()
    root.title("Downloader de Áudio do YouTube")
    root.geometry("500x300")
    root.configure(bg="#f9f9f9")
    root.resizable(False, False)
    
    create_ui(root, download_directory)
    
    root.mainloop()

