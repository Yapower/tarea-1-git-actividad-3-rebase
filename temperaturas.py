print("Conversor de temperaturas")

temperaturas = [20, 25, 30]

print("Temperaturas:", temperaturas)

def celsius_fahrenheit(c):
    return c * 9 / 5 + 32


def celsius_kelvin(c):
    return c + 273.15


def promedio(datos):
    return sum(datos) / len(datos)
