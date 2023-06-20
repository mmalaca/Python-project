from flask import Flask, render_template, request, redirect
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

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')


@app.route('/process_checkout', methods=['POST'])
def process_checkout():
    imie = request.form.get('imie')
    nazwisko = request.form.get('nazwisko')
    ulica = request.form.get('ulica')
    numer_domu = request.form.get('numer_domu')
    numer_mieszkania = request.form.get('numer_mieszkania')
    miasto = request.form.get('miasto')
    numer_karty = request.form.get('numer_karty')
    cvv = request.form.get('cvv')
    data_zakonczenia = request.form.get('data_zakonczenia')

    imie_error = None
    nazwisko_error = None
    ulica_error = None
    numer_domu_error = None
    numer_mieszkania_error = None
    miasto_error = None
    numer_karty_error = None
    cvv_error = None
    data_zakonczenia_error = None

    # Sprawdzenie poprawności danych
    if len(imie) < 3:
        imie_error = "Imię musi zawierać co najmniej 3 znaki."

    if len(nazwisko) < 3:
        nazwisko_error = "Nazwisko musi zawierać co najmniej 3 znaki."

    if len(ulica) == 0:
        ulica_error = "Wprowadź nazwę ulicy."
    elif not ulica.isalpha():
        ulica_error = "Nazwa ulicy może zawierać tylko litery."

    if len(numer_domu) == 0:
        numer_domu_error = "Wprowadź numer domu."
    elif not numer_domu.isnumeric():
        numer_domu_error = "Numer domu musi być liczbą."

    if numer_mieszkania and not numer_mieszkania.isnumeric():
        numer_mieszkania_error = "Numer mieszkania musi być liczbą."

    if len(miasto) == 0:
        miasto_error = "Wprowadź nazwę miasta."
    elif not miasto.isalpha():
        miasto_error = "Nazwa miasta może zawierać tylko litery."

    if len(numer_karty) != 16 or not numer_karty.isnumeric():
        numer_karty_error = "Numer karty kredytowej musi składać się z 16 cyfr."

    if len(cvv) != 3 or not cvv.isnumeric():
        cvv_error = "CVV musi składać się z 3 cyfr."

    if len(data_zakonczenia) != 7:
        data_zakonczenia_error = "Nieprawidłowy format daty zakończenia."

    if imie_error or nazwisko_error or ulica_error or numer_domu_error or numer_mieszkania_error or miasto_error or numer_karty_error or cvv_error or data_zakonczenia_error:
        return render_template('checkout.html', imie_error=imie_error, nazwisko_error=nazwisko_error, ulica_error=ulica_error, numer_domu_error=numer_domu_error, numer_mieszkania_error=numer_mieszkania_error, miasto_error=miasto_error, numer_karty_error=numer_karty_error, cvv_error=cvv_error, data_zakonczenia_error=data_zakonczenia_error)

    return render_template('process_finished.html', imie=imie, nazwisko=nazwisko, ulica=ulica, numer_domu=numer_domu, numer_mieszkania=numer_mieszkania, miasto=miasto, numer_karty=numer_karty, cvv=cvv, data_zakonczenia=data_zakonczenia)


if __name__ =='__main__':
    app.run(debug=True)
