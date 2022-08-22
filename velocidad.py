def velocidad(tiempo, distancia):
  velocidad = distancia/tiempo
  print(f"Velocidad: ", velocidad)
  if (velocidad > 100):
    print("Alta")
  elif (velocidad <= 100 and velocidad > 40):
    print("Normal")
  elif(velocidad <= 40 and velocidad > 0):
    print("Baja")
  else:
    print("Error")

velocidad(100, 7000)