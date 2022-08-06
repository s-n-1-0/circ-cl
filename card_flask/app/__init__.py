from flask import Flask,render_template
from .xls.read_xls import get_card

app = Flask(__name__)
@app.route("/")
def hello():
    return "Top Page"

@app.route("/card/<num>")
def index(num):
    card_num = int(num)
    card_num = abs(card_num)
    card = get_card(card_num)
    return render_template("index.html",card=card)