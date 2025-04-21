def es_bisiesto(año):

  if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    return True
  else:
    return False

año_ingresado = int(input("Ingrese un año: "))

if es_bisiesto(año_ingresado):
  print(f"El año {año_ingresado} es bisiesto")
else:
  print(f"El año {año_ingresado} no es bisiesto")
