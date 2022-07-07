# a = 5

# zodis = "Labas"
# dar_vienas = "Šitas žodis"

# print("a lygu: " + str(a) + ", žodis: " + zodis + ", dar vienas žodis – " + dar_vienas)

# # Geresnis variantas:
# print(f"a lygu {a}, žodis: {zodis}, dar vienas žodis – {dar_vienas}")

# # kas cia?

# test = """
# Sveiki, draugai,
# Ši pastraipa nebus vykdoma.
# """

# print(test)

# test2 = """Sveiki, draugai,Ši pastraipa nebus vykdoma"""

# print(test2)

# naujas_zodis = "Code Academy"

# print(naujas_zodis[11:4:-1])
# print(naujas_zodis[:-1])

# def daugiau_nei_2(list):
#     sarasas_2 = []
#     for n in list:
#         if n > 2:
#             sarasas_2.append(n)
#     return sarasas_2

# sarasas = [4, 3, 2, 1]

# print(daugiau_nei_2(sarasas))

# naujas_sarasas = [5, 7, 10, -1, -4, 0]
# print(sarasas)
# print(daugiau_nei_2(naujas_sarasas))

# while True:
#     print("Hello world")

# def makes10(a, b):
#   if a+b==10 or a==10 or b==10:
#     return ("True")
#   else:
#     return ("False")

# print(makes10(8, 1))   

# loginis = bool()
# print(loginis)

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)

# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# import datetime
# now = datetime.datetime.now()
# nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
# skirtumas = now - nepriklausomybes_diena
# print(skirtumas.days)

class Dimensions: 
    def __init__(self, distance: int, weight: int):
        self.distance=distance
        self.weight=weight
        
    def print_measurements(self):
        print(f"distance to home {self.distance} km - you loose {self.weight} kg")

    def convert_kg_to_g(self):
        print(f"your lost weight multiplies by 1000 to {self.weight*1000}")


dimensions=Dimensions(distance=15, weight=23)
dimensions.print_measurements()
dimensions.convert_kg_to_g()

import random, string






