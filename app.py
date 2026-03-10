from flask import Flask, render_template, request

app = Flask(__name__)

jobs = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        company = request.form["company"]

        job = {"title": title, "company": company}
        jobs.append(job)

    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
