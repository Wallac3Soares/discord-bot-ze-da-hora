from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot do Discord Rodando!"

def run():
    app.run(host='0.0.0.0', port=10000)

def start():
    t = Thread(target=run)
    t.start()
