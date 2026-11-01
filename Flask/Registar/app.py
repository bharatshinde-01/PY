from flask import Flask , render_template , request 
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        emil = request.form["email"]
        course = request.form["course"]
        year = request.form["year"]

        print("Name :",name)
        print("Email:",emil)
        print("Course:",course)
        print("Year :",year)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
