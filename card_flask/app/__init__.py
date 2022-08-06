from flask import Flask,render_template
from .xls.read_xls import get_card

app = Flask(__name__)
@app.route("/")
def top_page():
    return "Top Page"

@app.route("/card/<num>")
def card(num):
    card_num = int(num)
    card_num = abs(card_num)
    card = get_card(card_num)
    return render_template("card.html",card=card)

@app.route("/cards")
def cards():
    cards = [get_card(i+1) for i in range(100)]
    return render_template("cards.html",cards=cards)