import csv
from cereal.models import ProductModel

with open('data/cereal_az.csv', 'r', newline='') as cereals:
    reader = csv.reader(cereals, delimiter=',')
    for row in reader:
        print(row)
