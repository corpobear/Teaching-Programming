import time
import string
import datetime as dt





text = "nejaky nahodny text"

text = text.replace(" ", "_").split("_")[1].replace("y", "i")


print(text)

zoznam = text.split(" ")
print(zoznam)



print(text)

text = text.replace(" ", "_")

print(text)

text = text.upper()

print(text)

today = dt.datetime.now() - dt.timedelta(days=5)
nazov = 'subor'
extension = 'xlsx'

print(type(today))

stlpec = 'name'
tabulka = 'users'
hodnota = 5



def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start}")
        return result
    return wrapper

@decorator
def funckia(x, y):
    return x + y


a = 20

b = 30

print(funckia(a, b))
