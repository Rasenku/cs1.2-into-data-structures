from flask import Flask
from histogram import histogram


app = Flask(__name__)


@app.route('/')
def generate_words():
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)


if __name__ == '__main__':
    app.run()
