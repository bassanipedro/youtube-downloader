import threading
from tkinter import messagebox
from pytubefix import YouTube

def download_audio(url, download_directory, status_label):
    if not url:
        messagebox.showerror("Erro", "Por favor, insira um link de vídeo do YouTube.")
        return

    status_label.config(text="Baixando...")

    threading.Thread(target=download_thread, args=(url, download_directory, status_label)).start()

def download_thread(url, download_directory, status_label):
    try:
        yt = YouTube(url)
        yt_title = yt.title
        ys = yt.streams.get_audio_only()
        ys.download(output_path=download_directory, mp3=True)

        status_label.config(text=f"Áudio de '{yt_title}' baixado com sucesso!")
    except Exception as e:
        status_label.config(text="Erro ao baixar.")
        messagebox.showerror("Erro", str(e))
    finally:
        status_label.config(text="Pronto")
