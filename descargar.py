from pytube import YouTube

def descargar_video(url, respuesta):
    yt = YouTube(url)
    video = yt.streams.filter(file_extension='mp4').first()
    video.download()  
    return video.default_filename

