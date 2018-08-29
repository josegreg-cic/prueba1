from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "Homepage"

fil = [
    {
        "id":1,
        "title" : "Bson"
        },

    {
        "id":2,
        "title" : "Java"
        }
]

fil2 = [
    {
        "id":3,
        "title" : "C++"
        },

    {
        "id":4,
        "title" : "Python"
        }
] 



@app.route('/getdata/<name>')
def myjson_ret(name):
    data = [ [1,2,3],
             {"a" : 1,
              "b" : 2},
              name,
              fil2]
    return jsonify(success=True, data = data)


@app.route("/llenar_encuesta", methods = ['GET'])
def foo():
    return render_template("encuesta.html")

@app.route("/mostrar_encuesta", methods = ["POST"])
def bar():
    s = request.form["r1"]
    d = request.form["r2"]
    dicc_r = {
        "resp_1"  : s,
        "resp_2"  : d
    }
    print(s,d)
    return "{0} y {1}".format(s,d)

if __name__ == "__main__":
    app.run(debug = True)