from flask import Flask, jsonify, request, render_template
from Models import db, Barbers
from logging import exception
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\luisd\\OneDrive\\Escritorio\\Programación\\Proyecto PAS (Pagina web)\\ApiPAS\\database\\barbershop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#Aquí empiezan las rutas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/barbers", methods=["GET"])
def get_barbers():
    try:
        barbers = Barbers.query.all()
        toReturn = [barber.serialize() for barber in barbers]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/barber", methods=["GET"])
def get_barberByName():
    try:
        nameBarber = request.args["name"]
        barber = Barbers.query.filter_by(name=nameBarber).first()
        if not barber:
            return jsonify({"msg": "Este barbero no existe"}), 200
        else:
            return  jsonify(barber.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/findbarber", methods=["GET"])
def get_barbersForMoreVariables():
    try:
        fields = {}
        if "name" in request.args:
            fields["name"] = request.args["name"]
        
        if "service" in request.args:
            fields["service"] = request.args["service"]
            
        if "service_value" in request.args:
            fields["service_value"] = request.args["service_value"]

        barber = Barbers.query.filter_by(**fields).first()
        
        if not barber:
            return jsonify({"msg": "Este barbero no existe"}), 200
        else:
            return  jsonify(barber.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/addbarber", methods=["POST"])
def addbarber():
    try:
        name = request.form["name"]
        service = request.form["service"]
        service_value = request.form["service_value"]
        
        barber = Barbers(name, service, float(service_value))
        db.session.add(barber)
        db.session.commit()
        
        return jsonify(barber.serialize()), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/addbarber. Log: \n")
        return jsonify({"msg": "Algo ha salido mal"}), 500


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(debug=True, port=5000)