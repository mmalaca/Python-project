from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb+srv://samochody:samochody1@samochody.nuj5gha.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
database = client['otomoto_db']
collection = database['items']


app= Flask(__name__,template_folder='strona',static_folder='css')


@app.route('/')
def index():
    return render_template('strona.html')

@app.route('/samochody.html')
def samochody():
  car1 = collection.find_one({"marka": "Volkswagen"})
  car2=collection.find_one({"marka": "BMW"})
  car3=collection.find_one({"marka": "Mercedes"})
  car4=collection.find_one({"marka": "Audi"})
  car5=collection.find_one({"marka": "Ford"})
  car6=collection.find_one({"marka": "Toyota"})
  return render_template('samochody.html',car1=car1,car2=car2,car3=car3,car4=car4,car5=car5,car6=car6)

@app.route('/czesci.html')
def czesci():
    part1 = collection.find_one({"marka": "Bosch"})
    part2 = collection.find_one({"marka": "Michelin"})
    part3 = collection.find_one({"marka": "Turbo"})
    part4 = collection.find_one({"marka": "NGK"})
    part5 = collection.find_one({"marka": "Mann"})
    part6 = collection.find_one({"marka": "Brembo"})
    return render_template('czesci.html',part1=part1,part2=part2,part3=part3,part4=part4,part5=part5,part6=part6)

@app.route('/motocykle.html')
def motocykle():
    motorcycle1 = collection.find_one({"model": "Honda"})
    motorcycle2 = collection.find_one({"model": "Kawasaki"})
    motorcycle3 = collection.find_one({"model": "Suzuki"})
    motorcycle4 = collection.find_one({"model": "Yamaha"})
    motorcycle5 = collection.find_one({"model": "KTM"})
    motorcycle6 = collection.find_one({"model": "Harley-Davidson"})
    return render_template('motocykle.html',motorcycle1=motorcycle1,motorcycle2=motorcycle2,motorcycle3=motorcycle3,motorcycle4=motorcycle4,motorcycle5=motorcycle5,motorcycle6=motorcycle6)
@app.route('/strona.html')
def strona():
    return render_template('strona.html')
if __name__ =='__main__':
    app.run(debug=True)
