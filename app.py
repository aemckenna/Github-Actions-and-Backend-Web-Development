from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.get("/")
def home():
    a, b = 2, 3
    s = a + b
    return render_template("index.html", a=a, b=b, s=s)

@app.get("/add/<int:a>/<int:b>")
def add(a: int, b: int):
    total = a + b
    return render_template("add.html", a=a, b=b, total=total)

@app.get("/reverse")
def reverse():
    text = request.args.get("text", "")
    reversed_text = text[::-1]
    return render_template("reverse.html", text=text, reversed_text=reversed_text)

@app.get("/about")
def about():
    pages = [
        ("Home", url_for("home")),
        ("Add", url_for("add", a=7, b=5)),
        ("Reverse", url_for("reverse") + "?text=Flask"),
        ("About", url_for("about")),
    ]
    return render_template("about.html", pages=pages)

if __name__ == "__main__":
    app.run(debug=True)
