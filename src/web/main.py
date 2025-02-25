from flask import       \
    Flask,              \
    request,            \
    Response,           \
    redirect,           \
    render_template
from os.path import dirname, join
import hashlib
import sqlite3

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        hashed = hashlib.sha256(password.encode())

        connection = sqlite3.connect(DB_PATH)
        
        try:
            cursor = connection.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hashed.hexdigest()))
            row = cursor.fetchone()
            if not row: raise sqlite3.DataError()
        except sqlite3.DataError as e:
            return Response(render_template("login.html", messages=[("error", "No user found for this email and password")]))

        # Da sostituire con un redirect ad una route /user
        # Forse prima di fare il redirect si potrebbe mostrare il messaggio di registrazione avvenuta
        return Response(render_template("login.html", messages=[("success", "Successfully logged in!")]))
        
        """
        try:
            connection = sqlite3.connect(DB_PATH)
            connection.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed))
        except sqlite3.IntegrityError as e:
            connection.rollback()
            return Response(render_template("login.html", messages=[("error", "This email is already registered.")]))
        else:
            connection.commit()

            # Da sostituire con un redirect ad una route /user
            # Forse prima di fare il redirect si potrebbe mostrare il messaggio di registrazione avvenuta
            return Response(render_template("login.html", messages=[("success", "Successfully logged in!")]))
        """
    else:
        return render_template("login.html")

@app.route("/search")
def search():
    return "Sei nella pagina search!"

@app.route("/weather")
def weather():
    return "Sei nella pagina weather!"


if __name__ == '__main__':
    app.run("127.0.0.1", 8080, debug=True)