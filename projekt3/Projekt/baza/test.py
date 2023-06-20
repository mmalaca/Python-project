from pymongo import MongoClient
import requests
from bson.objectid import ObjectId

uri = "mongodb+srv://samochody:samochody1@samochody.nuj5gha.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
database = client['otomoto_db']
collection = database['items']

class otomoto:
    def __init__(self, marka, cena):
        self.marka = marka
        self.cena = cena

class samochody(otomoto):
    def __init__(self, marka, model, rocznik, skrzynia, cena):
        self.skrzynia = skrzynia
        self.model = model
        self.rocznik=rocznik
        super().__init__(marka, cena)

class motocykle(otomoto):
    def __init__(self,model, marka, rocznik, cena):
        self.model = model
        self.rocznik=rocznik
        super().__init__(marka, cena)

class czesci(otomoto):
    def __init__(self, marka, nazwa, stan, cena):
        super().__init__(marka, cena)
        self.nazwa = nazwa
        self.stan = stan


items = []
items.append(samochody('Volkswagen', 'Golf', 2021, 'manualna', 90000))
items.append(samochody('BMW','Seria 3',2021, 'manualna',100000))
items.append(samochody('Mercedes', 'C-Class', 2022, 'automatyczna', 120000))
items.append(samochody('Audi', 'A4', 2021, 'automatyczna', 95000))
items.append(samochody('Ford', 'Mustang', 2020, 'manualna', 80000))
items.append(samochody('Toyota', 'Camry', 2022, 'automatyczna', 90000))


items.append(motocykle('Honda', 'Sport',2020, 150000))
items.append(motocykle('Kawasaki','Sport Touring', 2021, 80000))
items.append(motocykle('Suzuki', 'GSX-R1000', 2022, 180000))
items.append(motocykle('Yamaha', 'MT-09', 2021, 100000))
items.append(motocykle('KTM', 'Duke 390', 2020, 70000))
items.append(motocykle('Harley-Davidson', 'Iron 883', 2021, 150000))

items.append(czesci('Bosch', 'Przedni hamulec', 'Nowa',100))
items.append(czesci('Michelin', 'Opona', 'Używana',50))
items.append(czesci('Turbo', 'Tłumik', 'Nowy',100))
items.append(czesci('NGK', 'Świece zapłonowe', 'Nowe',20))
items.append(czesci('Mann', 'Filtr powietrza', 'Nowy',30))
items.append(czesci('Brembo', 'Tarcze hamulcowe', 'Nowe',80))


for item in items:
    collection.insert_one(item.__dict__)

