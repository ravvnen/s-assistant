from flask import Flask, render_template
from queries import query_best_buildings

app = Flask(__name__)

@app.route("/")
def index():
    # query_best_buildings returns a list of tuples (building_id, {building_name, best_ranking})
    results = query_best_buildings()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)