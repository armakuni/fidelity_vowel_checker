from flask import Flask, request

from vowelchecker import vowel_checker

application = Flask(__name__)

@application.route("/")
def index():
    letter = request.args.get("letter")
    if vowel_checker(letter):
        return "Vowel"
    else:
        return "Not a vowel"

if __name__ == '__main__':
    application.run('0.0.0.0', 8123) # this is only used for local development
