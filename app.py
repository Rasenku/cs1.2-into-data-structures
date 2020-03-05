from flask import Flask
# from histogram import histogram
from markov_chain import render_sentence, get_following_words, get_clean_text


app = Flask(__name__)


@app.route('/')
def generate_words():
    # my_file = open("./words.txt", "r")
    # lines = my_file.readlines()
    # my_histogram = histogram(lines)
    # return my_histogram
    text = get_clean_text("corpus.txt")
    return return_sentence(get_following_words(text), 10)


if __name__ == '__main__':
    app.run()
