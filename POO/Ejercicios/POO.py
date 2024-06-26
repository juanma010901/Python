# -*- coding: utf-8 -*-
"""Taller_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UALKtOR7KCVU6BbDBUdt4lb4ajl6DmZn

# Ejercicios Taller 3

## 1. Polígono
"""

class Poligono:
  def __init__(self, lados, apotema, longitud):
    self.__lados = lados
    self.__apotema = apotema
    self.__longitud = longitud

  def calcular_area(self):
    return (1/2)*self.__lados*self.__apotema*self.__longitud

  def calcular_perimetro(self):
    return self.__lados*self.__longitud

class Triangulo(Poligono):
  def __init__(self, apotema, longitud):
    super().__init__(3, apotema, longitud)

class Hexagono(Poligono):
  def __init__(self, lados, apotema, longitud):
    super().__init__(lados, apotema, longitud)

triangulo = Triangulo(2,5)
print(triangulo.calcular_area())
print(triangulo.calcular_perimetro())

hexagono = Hexagono(5,3,4)
print(hexagono.calcular_area())
print(hexagono.calcular_perimetro())

"""## 2. Cuaderno"""

class Cuaderno:
  def __init__(self, numero_hojas):
    self.__numero_hojas = numero_hojas
    self.__hojas = ['' for n in range(self.__numero_hojas)]

  def escribir(self, texto, numero_hoja):
    if numero_hoja > self.__numero_hojas or numero_hoja == 0:
      print("Hoja no existe")
    else:
      self.__hojas[numero_hoja-1] += texto

  def borrar(self, numero_hoja):
    if numero_hoja > self.__numero_hojas or numero_hoja == 0:
      print("Hoja no existe")
    else:
      self.__hojas[numero_hoja-1] = ''

  def __str__(self):
    return f"{[str(i) for i in self.__hojas]}\n"

cuaderno = Cuaderno(5)
cuaderno.escribir("Hola Mundo!", 1)
cuaderno.escribir("Este es el segundo texto", 2)
cuaderno.borrar(1)
cuaderno.escribir("Este texto reemplaza al borrado", 1)
print(cuaderno)

"""## 3. Ejercicio Lavadero"""

class Persona:
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.__edad = edad

  @property
  def nombre(self):
    return self.__nombre

  @property
  def edad(self):
    return self.__edad

class Vehiculo:
  def __init__(self, placa, color, propietario):
    self.__placa = placa
    self.__color = color
    self.__propietario = propietario

  @property
  def propietario(self):
    return self.__propietario

  def __str__(self):
    return f"[Nombre: {self.__propietario.nombre} - Edad: {self.__propietario.edad} - Placa: {self.__placa} - Color: {self.__color}]"

class Moto(Vehiculo):
  def __init__(self, placa, color, propietario, tipo):
    super().__init__(placa, color, propietario)
    self.__tipo = tipo

  @property
  def tipo(self):
    return self.__tipo

class Carro(Vehiculo):
  def __init__(self, placa, color, propietario, puertas):
    super().__init__(placa, color, propietario)
    self.__puertas = puertas

  @property
  def puertas(self):
    return self.__puertas

class Lavadero:
  def __init__(self, nombre):
    self.__nombre = nombre
    self.__lista_vehiculos = []
    self.__ganancias = 0

  def ingresar_vehiculo(self, vehiculo):
    self.__lista_vehiculos.append(vehiculo)

  def calcular_ganancias(self):
    for vehiculo in self.__lista_vehiculos:
      if isinstance(vehiculo, Carro):
        if vehiculo.propietario.edad > 60: #Acá es mi duda puntual (si no agrego el getter del propietario en la clase de Vehiculo, no me deja acceder a la edad)
          self.__ganancias += 12000 * 0.8
        else:
          self.__ganancias += 12000
      elif isinstance(vehiculo, Moto):
        if vehiculo.propietario.edad > 60:
          self.__ganancias += 7000 * 0.8
        else:
          self.__ganancias += 7000
    return self.__ganancias

  def __str__(self):
    vehiculos_info = "\n".join(str(vehiculo) for vehiculo in self.__lista_vehiculos)
    return f"Lavadero: {self.__nombre}\n{vehiculos_info}"

p1 = Persona("Mario Bros", 65)
p2 = Persona("Luigi Bros", 59)
carro = Carro("MAR001", "Rojo", p1, 2)
moto = Moto("LUI001", "Verde", p2, 2)

lavadero = Lavadero("Reino Champiñon")
lavadero.ingresar_vehiculo(carro)
lavadero.ingresar_vehiculo(moto)

print(carro)
print(moto)

print(lavadero)
print(lavadero.calcular_ganancias())

"""## 4. Factura"""

class Persona:
  def __init__(self, id, nombre):
    self.__id = id
    self.__nombre = nombre

  @property
  def id(self):
    return self.__id

  @property
  def nombre(self):
    return self.__nombre

class Cliente(Persona):
  def __init__(self, id, nombre):
    super().__init__(id, nombre)

class Vendedor(Persona):
  def __init__(self, id, nombre):
    super().__init__(id, nombre)

class Producto:
  def __init__(self, id, nombre, precio):
    self.__id = id
    self.__nombre = nombre
    self.__precio = precio

  @property
  def id(self):
    return self.__id

  @property
  def nombre(self):
    return self.__nombre

  @property
  def precio(self):
    return self.__precio

class Factura:
  def __init__(self, nombre_tienda, cliente, vendedor):
    self.__nombre_tienda = nombre_tienda
    self.__cliente = cliente
    self.__vendedor = vendedor
    self.__productos = []
    self.__cantidad_productos = []
    self.__precio_total = 0

  def ingresar_producto(self, producto, cantidad):
    self.__productos.append(producto)
    self.__cantidad_productos.append(cantidad)

  def calcular_total(self):
    for i in range(len(self.__productos)):
      self.__precio_total += self.__productos[i].precio * self.__cantidad_productos[i]

  def __str__(self):
    factura = "*" * 50 + "\n"
    factura += f"******************* {self.__nombre_tienda} ********************\n"
    factura += "*" * 50 + "\n*"
    factura += f"Vendedor: {self.__vendedor.nombre}".center(48) + "*\n*"
    factura += f"Cliente: {self.__cliente.nombre}".center(48) + "*\n"
    factura += "*" * 50 + "\n"
    factura += f'* {"ID":4}\t{"Producto":13}\t{"Precio":10}\t{"Cantidad":8} *\n'
    for i in range(len(self.__productos)):
      factura += f"* {str(self.__productos[i].id):4}\t{self.__productos[i].nombre:13}\t{str(self.__productos[i].precio):10}\t{str(self.__cantidad_productos[i]):8} *\n"
    factura += "*" * 50 + "\n*"
    factura += f"El precio final es de: {self.__precio_total} $".center(48)  + "*\n"
    factura += "*" * 50 + "\n*"
    factura += "Gracias por comprar en nuestra tienda.".center(48) + "*\n"
    factura += "*" * 50 + "\n"
    return factura

cliente = Cliente("002", "Pedro Zapata")
vendedor = Vendedor("001", "Juan Álvarez")

p1 = Producto(1, "Leche", 2400)
p2 = Producto(2, "Pan", 1500)
p3 = Producto(3, "Carne", 9000)

factura = Factura("El Barrio", cliente, vendedor)
factura.ingresar_producto(p1,4)
factura.ingresar_producto(p2,2)
factura.ingresar_producto(p3,2)
factura.calcular_total()

print(factura)

"""## Ejercicio Bus"""

class Pasajero:
  def __init__(self, nombre, edad, genero):
    self.__nombre = nombre
    self.__edad = edad
    self.__genero = genero

  @property
  def nombre(self):
    return self.__nombre

  @property
  def edad(self):
    return self.__edad

  @property
  def genero(self):
    return self.__genero

  def __str__(self):
    return f"Nombre: {self.__nombre} - Edad: {self.__edad} - Género: {self.__genero}"

class Bus:
  def __init__(self, modelo, capacidad_max):
    self.__modelo = modelo
    self.__capacidad_max = capacidad_max
    self.__cantidad_pasajeros = 0
    self.__recaudo = 0
    self.__pasajeros = []

  def subir_pasajeros(self, *args):
    for i in args:
      if self.__capacidad_max > self.__cantidad_pasajeros:
        self.__pasajeros.append(i)
        self.__cantidad_pasajeros += 1
        if i.edad >= 60:
          self.__recaudo += 1000
        else:
          self.__recaudo += 2500

  def bajar_pasajeros(self, cantidad):
    self.__pasajeros = self.__pasajeros[cantidad:]
    self.__cantidad_pasajeros -= cantidad

  def mostrar_ganancia(self):
    return f"El dinero recaudado es de: {self.__recaudo}$."

  def __str__(self):
      info = f"El bus modelo {self.__modelo} con capacidad máxima de {self.__capacidad_max} personas, lleva {self.__cantidad_pasajeros} pasajeros:\n"
      for pasajero in self.__pasajeros:
        info += str(pasajero) + "\n"
      info += "*" * 50 + "\n"
      return info

bus = Bus("2024", 30)

p1 = Pasajero('Carlos', 45, 'Masculino')
p2 = Pasajero('Sofía', 70, 'Femenino')
p3 = Pasajero('Juan', 52, 'Masculino')
p4 = Pasajero('María', 67, 'Femenino')
p5 = Pasajero('Pablo', 48, 'Masculino')
p6 = Pasajero('Ana', 65, 'Femenino')
p7 = Pasajero('Pedro', 72, 'Masculino')
p8 = Pasajero('Marta', 55, 'Femenino')
p9 = Pasajero('Luis', 61, 'Masculino')
p10 = Pasajero('Laura', 40, 'Femenino')

bus.subir_pasajeros(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)

print(bus)

bus.bajar_pasajeros(5)

print(bus)

print(bus.mostrar_ganancia())