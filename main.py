import descargar
import convertir
import sys

while True:
    print("Introduce la URL del video")
    url = input("URL: ")

    respuesta = input("""
    1. Descargar video
    2. Descargar audio
    3. Salir
    """)

    if respuesta == "1":
        print("Descargando...")
        descargar.descargar_video(url, respuesta)
        print("¡Video descargado!")
    if respuesta == "2":
        print("Descargando...")
        video = descargar.descargar_video(url, respuesta)
        convertir.convertir_mp3(video)
        print("¡Video descargado!")
    else:
        sys.exit(0)        