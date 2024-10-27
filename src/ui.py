import tkinter as tk
from tkinter import ttk, filedialog
from downloader import download_audio
from config import save_directory
from styles import COLORS 

def create_ui(root, download_directory):
    global status_label, entry 

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    main_frame = tk.Frame(notebook, bg=COLORS["frame_background"]) 
    notebook.add(main_frame, text="Downloader")

    title_label = tk.Label(main_frame, text="Downloader de Áudio", bg=COLORS["frame_background"], font=("Segoe UI", 18, "bold"), fg=COLORS["text"])
    title_label.pack(pady=10)

    label = tk.Label(main_frame, text="Insira o link do vídeo do YouTube:", bg=COLORS["frame_background"], font=("Segoe UI", 12), fg=COLORS["text"])
    label.pack(pady=10)

    entry = tk.Entry(main_frame, width=60, font=("Segoe UI", 10), bd=1, fg="black", bg="#f0f0f0", relief="solid")  # Estilo da entrada
    entry.pack(pady=15, padx=50)

    status_label = tk.Label(main_frame, text="", bg=COLORS["frame_background"], font=("Segoe UI", 10), fg=COLORS["text"])
    status_label.pack(pady=5)

    style = ttk.Style()
    style.configure("RoundedButton.TButton",
                    relief="flat", 
                    borderwidth=0, 
                    padding=10,
                    background=COLORS["button_background"], 
                    foreground=COLORS["button_foreground"], 
                    font=("Segoe UI", 10, "bold")) 
    style.map("RoundedButton.TButton",
              background=[('active', COLORS["button_active_background"])])

    download_button = ttk.Button(main_frame, text="Baixar Áudio", command=lambda: download_audio(entry.get(), download_directory, status_label),
                                  style="RoundedButton.TButton")
    download_button.pack(pady=0)

    settings_frame = tk.Frame(notebook, bg=COLORS["frame_background"]) 
    notebook.add(settings_frame, text="Configurações")

    settings_label = tk.Label(settings_frame, text="Configurações", bg=COLORS["frame_background"], font=("Segoe UI", 18, "bold"), fg=COLORS["text"])
    settings_label.pack(pady=10)
    
    directory_button_settings = ttk.Button(settings_frame, text="Selecionar Diretório", command=select_directory,
                                           style="RoundedButton.TButton")
    
    directory_button_settings.pack(pady=10)

    info_frame = tk.Frame(settings_frame, bg=COLORS["frame_background"])  
    info_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    center_frame = tk.Frame(info_frame, bg=COLORS["frame_background"])
    center_frame.pack(expand=True)

    author_label = tk.Label(center_frame, text="Autor: Pedro Bassani", bg=COLORS["frame_background"], font=("Segoe UI", 10), fg=COLORS["text"])
    author_label.pack(side=tk.LEFT, padx=(0, 10))

    version_label = tk.Label(center_frame, text="Versão: 1.0.0", bg=COLORS["frame_background"], font=("Segoe UI", 10), fg=COLORS["text"])
    version_label.pack(side=tk.LEFT)

def select_directory():
    global download_directory
    download_directory = filedialog.askdirectory()
    if download_directory:
        save_directory(download_directory)
