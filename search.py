from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/busca', methods=['GET'])
def search_results():
    searched_term = request.args.get('q')
    html_response = """<html><body>
        Pesquisou por -- %s --
        </body></html>""" % searched_term

    response = requests.get('http://g1.globo.com/busca/?q={term}'.format(
        term=searched_term))

    return response.text

if __name__ == "__main__":
    app.run(debug=True)
