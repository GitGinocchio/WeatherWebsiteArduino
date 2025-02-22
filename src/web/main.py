from flask import Flask

app = Flask(
    import_name=__name__, 
    static_folder='./static',
    template_folder='./templates',
    root_path='.'
)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/search")
def search():
    return "Sei nella pagina search!"

@app.route("/weather")
def weather():
    return "Sei nella pagina weather!"


if __name__ == '__main__':
    app.run("127.0.0.1", 8080)