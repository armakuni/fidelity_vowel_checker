from flask import Flask, request
from vowel_checker import check

application = Flask(__name__)

@application.route("/")
def index():
    letter = request.args.get("letter")
    if letter == None:
        return '<form><input name="letter" /><button>Submit</button></form>'
    if check(letter):
        return 'Vowel'
    return 'Not a vowel'

if __name__ == '__main__':
    application.run('0.0.0.0', 8123) # this is only used for local development
