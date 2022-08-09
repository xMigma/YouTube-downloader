from flask import Flask, render_template, request, send_file, url_for, redirect, session
from pytube import YouTube
from hurry.filesize import size
from time import strftime, gmtime

app = Flask(__name__)
app.secret_key = 'migma'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        session['url'] = request.form["url"]
        if session['url'] != "":
            url = YouTube(session['url'])
            filesize = round(url.streams.first().filesize / 10**6, 2)
            duracion = strftime("%M:%S", gmtime(round(url.length)))
            return render_template('descargar.html', url=url, filesize=filesize, duracion=duracion)
    return render_template('main.html')

@app.route('/descargar', methods=['GET', 'POST'])
def descargar_video():
    if request.method == 'POST':
        url = YouTube(session['url'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)
        archivo = video.download()
        return send_file(archivo, as_attachment=True)
    return redirect(url_for('main'))   

     
if __name__ == '__main__':
    app.run(port=5000, debug=False)
