from flask import       \
    Flask,              \
    request,            \
    render_template
from os import path

app = Flask(
    import_name=__name__, 
    static_folder='./static',
    template_folder='./templates',
    root_path=path.dirname(__file__)
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.json)
    else:
        pass

    print(request)

    return render_template("login.html")

@app.route("/search")
def search():
    return "Sei nella pagina search!"

@app.route("/weather")
def weather():
    return "Sei nella pagina weather!"


if __name__ == '__main__':
    app.run("127.0.0.1", 8080, debug=True)