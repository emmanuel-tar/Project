from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_item_by_barcode(barcode):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT name, price, stock FROM items WHERE barcode = ?", (barcode,))
    item = cur.fetchone()
    conn.close()
    return item


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/lookup", methods=["POST"])
def lookup():
    barcode = request.form["barcode"]
    item = get_item_by_barcode(barcode)
    return render_template("result.html", item=item, barcode=barcode)


if __name__ == "__main__":
    app.run(debug=True)
