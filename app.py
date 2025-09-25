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

@app.get("/subtract/<int:a>/<int:b>")
def subtract(a: int, b: int):
    total = a - b
    return render_template("subtract.html", a=a, b=b, total=total)

@app.get("/multiply/<int:a>/<int:b>")
def multiply(a: int, b: int):
    total = a * b
    return render_template("multiply.html", a=a, b=b, total=total)

if __name__ == "__main__":
    app.run(debug=True)
