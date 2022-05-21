#Biblioteca utilizada
from pytube import YouTube

#Função da barra de progresso do download do vídeo
def progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percent = 100 * (int(bytes_download) / total_size)
    bar = '-' * int(percent) + ' ' * (100 - int(percent))
    print(f"\r |{bar}| {percent:.2f}%", end="\r")

#Função que retorna o nome do vídeo, link da thumbnail e efetua o download
def youtube_downloader(url):
    try:
        yt = YouTube(url)
        yt.register_on_progress_callback(progress_bar)
        print("Iniciando download...")
        print("Nome do vídeo: " + str(yt.title))
        print("Link da Thumbnail: " + str(yt.thumbnail_url))
        yt.streams.filter(file_extension='mp4', res="720p").first().download()
    except Exception:
        print("Não foi possível realizar o download do conteúdo.")


#Chamando a função para realizar o download do vídeo
youtube_downloader('https://www.youtube.com/watch?v=xcJtL7QggTI')