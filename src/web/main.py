from flask import       \
    Flask,              \
    request,            \
    Response,           \
    redirect,           \
    make_response,      \
    render_template
from os.path import dirname, join
import hashlib
import sqlite3
import requests

WEB_DIR = dirname(__file__)
DB_PATH = join(WEB_DIR, "data/database.db")
DB_SCRIPT_PATH = join(WEB_DIR, "config/database.sql")

with open(DB_SCRIPT_PATH, "r") as f:
    connection = sqlite3.connect(DB_PATH)
    connection.executescript(f.read())

app = Flask(
    import_name=__name__, 
    static_folder='./static',
    template_folder='./templates',
    root_path=WEB_DIR
)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", data={})

@app.route("/grafico", methods=["GET", "POST"])
def grafico():
    if request.method == "POST":
        citta = request.form.get("citta")

        print(citta)

        data = requests.get(f"https://wttr.in/{citta}?format=j1").json()

        return render_template("grafico.html", data=data)

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        hashed = hashlib.sha256(password.encode()).hexdigest()

        connection = sqlite3.connect(DB_PATH)
        
        try:
            cursor = connection.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hashed))
            row = cursor.fetchone()
            if not row: raise sqlite3.DataError()
        except sqlite3.DataError as e:
            return Response(render_template("login.html", messages=[("error", "No user found for this email and password")]))

        response = redirect('/user')

        # Questo codice fa pena ma per questo progetto va piu' che bene
        # nella realta' bisognerebbe utilizzare un algoritmo con chiave pubblica e privata
        # per generare un token da salvare nei cookie che lo rende decifrabile solo dal server
        response.headers.set('Set-Cookie', f'user_access_token={hashed};')
        return response
    else:
        return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form)

        username = request.form.get('username')
        email = request.form.get("email")
        password = request.form.get("password")

        hashed = hashlib.sha256(password.encode()).hexdigest()

        try:
            connection = sqlite3.connect(DB_PATH)
            connection.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed))
        except sqlite3.IntegrityError as e:
            connection.rollback()
            return Response(render_template("register.html", messages=[("error", "This email is already registered.")]))
        else:
            connection.commit()

            # Questa response dovrebbe reindirizzare a /user, per ora solo a /
            response = redirect('/')

            # Questo codice fa pena ma per questo progetto va piu' che bene
            # nella realta' bisognerebbe utilizzare un algoritmo con chiave pubblica e privata
            # per generare un token da salvare nei cookie che lo rende decifrabile solo dal server
            response.headers.set('Set-Cookie', f'user_access_token={hashed};')
            return response
    else:
        return render_template('register.html')

@app.route("/search")
def search():
    return "Sei nella pagina search!"

@app.route("/weather")
def weather():
    return "Sei nella pagina weather!"


if __name__ == '__main__':
    app.run("127.0.0.1", 8080, debug=True)