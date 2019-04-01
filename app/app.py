from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.dialects.postgresql import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/jobcard'

db = SQLAlchemy(app)
vehicles=[]

class Vehicle(db.Model):
        __tablename__ = "vehicle"

        id = db.Column('id',db.Integer,primary_key=True)
        manufacturer = db.Column('manufacturer',db.Unicode)
        model = db.Column('model',db.Unicode)
        enginetype = db.Column('enginetype',db.Unicode)
        vehicleno = db.Column('vehicleno',db.Unicode)
        def __init__(self,id,manufacturer,model,enginetype,vehicleno):
                self.id=id
                self.manufacturer=manufacturer
                self.model=model
                self.enginetype=enginetype
                self.vehicleno=vehicleno
                
        

      
@app.route("/store",methods=['POST'])
def insert():
        data = request.get_json()
        new_vehicle=Vehicle(data['id'],data['manufacturer'],data['model'],data['enginetype'],data['vehicleno'])
        db.session.add(new_vehicle)
        db.session.commit()
        return(jsonify({"message":"LUND"}))



@app.route("/retrieve")
def get():

        varray=[]
        data = Vehicle.query.all()
        for vehicle in data:
                new_vehicle={"id":vehicle.id,
                        "manufacturer":vehicle.manufacturer,
                        "model":vehicle.model,
                        "enginetype":vehicle.enginetype,
                        "vehicleno":vehicle.vehicleno}
                varray.append(new_vehicle)
        return(jsonify(varray))
               

        

        



               




             


















app.run(port=5000,debug=True)

