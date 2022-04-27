from flask import Flask
from threading import Thread
from json import load
import random

app = Flask(__name__)

# list of jokes
with open('jokes.txt') as file:
  jokes = file.read().split("\n")

@app.route('/')

def home():
  return  {"joke":jokes[random.choice(jokes)]}

def run():
  app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()