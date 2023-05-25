from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://samochody:samochody1@samochody.nuj5gha.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db=client["samochody"]
col=db["mazda"]





volkswagen = [
    {'_id': 1, 'marka': 'Volkswagen', 'model': 'Golf', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 90000},
    {'_id': 2, 'marka': 'Volkswagen', 'model': 'Passat', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 120000}, 
    {'_id': 3, 'marka': 'Volkswagen', 'model': 'Tiguan', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 100000}, 
    {'_id': 4, 'marka': 'Volkswagen', 'model': 'Arteon', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 150000}, 
    {'_id': 5, 'marka': 'Volkswagen', 'model': 'Polo', 'rocznik': 2020, 'skrzynia': 'manualna', 'cena': 70000}, 
    {'_id': 6, 'marka': 'Volkswagen', 'model': 'Up!', 'rocznik': 2019, 'skrzynia': 'manualna', 'cena': 50000}, 
    {'_id': 7, 'marka': 'Volkswagen', 'model': 'Touran', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 110000}, 
    {'_id': 8, 'marka': 'Volkswagen', 'model': 'ID.4', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 180000}, 
    {'_id': 9, 'marka': 'Volkswagen', 'model': 'Caddy', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 80000}, 
    {'_id': 10, 'marka': 'Volkswagen', 'model': 'California', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 200000}

]

bmw = [
    {'_id': 11, 'marka': 'BMW', 'model': 'Seria 3', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 100000},
    {'_id': 12, 'marka': 'BMW', 'model': 'Seria 5', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 150000},
    {'_id': 13, 'marka': 'BMW', 'model': 'Seria 7', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 250000},
    {'_id': 14, 'marka': 'BMW', 'model': 'X1', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 90000},
    {'_id': 15, 'marka': 'BMW', 'model': 'X3', 'rocznik': 2020, 'skrzynia': 'manualna', 'cena': 120000},
    {'_id': 16, 'marka': 'BMW', 'model': 'X5', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 180000},
    {'_id': 17, 'marka': 'BMW', 'model': 'M2', 'rocznik': 2022, 'skrzynia': 'manualna', 'cena': 200000},
    {'_id': 18, 'marka': 'BMW', 'model': 'M4', 'rocznik': 2022, 'skrzynia': 'automatyczna', 'cena': 300000},
    {'_id': 19, 'marka': 'BMW', 'model': 'i3', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 120000},
    {'_id': 20, 'marka': 'BMW', 'model': 'i8', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 400000}
]
mercedes = [
    {'_id': 21, 'marka': 'Mercedes', 'model': 'A-Class', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 110000},
    {'_id': 22, 'marka': 'Mercedes', 'model': 'C-Class', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 160000},
    {'_id': 23, 'marka': 'Mercedes', 'model': 'E-Class', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 250000},
    {'_id': 24, 'marka': 'Mercedes', 'model': 'GLE', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 180000},
    {'_id': 25, 'marka': 'Mercedes', 'model': 'GLC', 'rocznik': 2020, 'skrzynia': 'manualna', 'cena': 140000},
    {'_id': 26, 'marka': 'Mercedes', 'model': 'GLA', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 200000},
    {'_id': 27, 'marka': 'Mercedes', 'model': 'S-Class', 'rocznik': 2022, 'skrzynia': 'manualna', 'cena': 300000},
    {'_id': 28, 'marka': 'Mercedes', 'model': 'AMG GT', 'rocznik': 2022, 'skrzynia': 'automatyczna', 'cena': 400000},
    {'_id': 29, 'marka': 'Mercedes', 'model': 'G-Class', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 350000},
    {'_id': 30, 'marka': 'Mercedes', 'model': 'EQC', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 380000}
]
volvo = [
    {'_id': 31, 'marka': 'Volvo', 'model': 'S60', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 90000},
    {'_id': 32, 'marka': 'Volvo', 'model': 'S90', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 150000},
    {'_id': 33, 'marka': 'Volvo', 'model': 'XC40', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 200000},
    {'_id': 34, 'marka': 'Volvo', 'model': 'XC60', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 160000},
    {'_id': 35, 'marka': 'Volvo', 'model': 'XC90', 'rocznik': 2020, 'skrzynia': 'manualna', 'cena': 220000},
    {'_id': 36, 'marka': 'Volvo', 'model': 'V60', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 120000},
    {'_id': 37, 'marka': 'Volvo', 'model': 'V90', 'rocznik': 2022, 'skrzynia': 'manualna', 'cena': 180000},
    {'_id': 38, 'marka': 'Volvo', 'model': 'Polestar 1', 'rocznik': 2022, 'skrzynia': 'automatyczna', 'cena': 350000},
    {'_id': 39, 'marka': 'Volvo', 'model': 'Polestar 2', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 300000},
    {'_id': 40, 'marka': 'Volvo', 'model': 'XC20', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 180000}
]

mazda = [
    {'_id': 41, 'marka': 'Mazda', 'model': 'Mazda3', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 80000},
    {'_id': 42, 'marka': 'Mazda', 'model': 'Mazda6', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 130000},
    {'_id': 43, 'marka': 'Mazda', 'model': 'CX-3', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 150000},
    {'_id': 44, 'marka': 'Mazda', 'model': 'CX-5', 'rocznik': 2021, 'skrzynia': 'manualna', 'cena': 140000},
    {'_id': 45, 'marka': 'Mazda', 'model': 'CX-9', 'rocznik': 2020, 'skrzynia': 'manualna', 'cena': 180000},
    {'_id': 46, 'marka': 'Mazda', 'model': 'MX-5', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 100000},
    {'_id': 47, 'marka': 'Mazda', 'model': 'CX-30', 'rocznik': 2022, 'skrzynia': 'manualna', 'cena': 120000},
    {'_id': 48, 'marka': 'Mazda', 'model': 'RX-8', 'rocznik': 2022, 'skrzynia': 'automatyczna', 'cena': 250000},
    {'_id': 49, 'marka': 'Mazda', 'model': 'CX-50', 'rocznik': 2021, 'skrzynia': 'automatyczna', 'cena': 200000},
    {'_id': 50, 'marka': 'Mazda', 'model': 'MX-30', 'rocznik': 2020, 'skrzynia': 'automatyczna', 'cena': 160000}
]

# //wyszukiwanie konretnego query
# searchingQuery = 'chuck'
# for i in col.find({},{"_id":0,"name":1,"address":1}):
#     if searchingQuery in str(i['name']).lower():
#         print(i)
        

# //pushowanie do bazy mongodb
# y = col.insert_many(mazda)
