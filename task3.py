import pickle
import json


products = [
    {"id": 1, "name": "Товар1", "price": 10},
    {"id": 2, "name": "Товар2", "price": 50.10},
    {"id": 3, "name": "Товар3", "price": 3},
    {"id": 4, "name": "Товар4", "price": 100},
    {"id": 5, "name": "Товар4", "price": 20}
]

with open('products.pickle', 'wb') as pf:
    pickle.dump(products, pf)

json_products = json.dumps(products, indent=4)

with open('products.json', 'w') as jf:
    jf.write(json_products)


