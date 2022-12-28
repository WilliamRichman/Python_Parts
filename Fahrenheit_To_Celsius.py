temperature_fahrenheit = [32, 212, 275]
degrees_celsius = []

for i in temperature_fahrenheit:
    x = i - 32
    r = round(x * .556)
    
    degrees_celsius.append(r)
print(degrees_celsius)