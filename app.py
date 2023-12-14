
class Objeto:
  def __init__(self):
    self.pos_x = 0
    self.pos_y = 0
    self.masa = 0
    self.velocidad = 0
    self.aceleracion = 0

class Calculadora:
  def __init__(self):
    self.n = 0
    self.objetos = []
    self.masa_total = []

  def pedir_datos(self):
    self.n = int(input("Ingrese la cantidad de masas en la bolsa: "))
    
    for _ in range(self.n):
      self.objetos.append(Objeto())

    self.masa_total = 0
    print("Ingrese las masas de los {} objetos".format(self.n))
    for i in range(self.n):
      mi = float(input())
      self.masa_total += mi
      self.objetos[i].masa = mi

    print("Ingrese las posiciones (x, y) de los {} objetos".format(self.n))
    for _ in range(self.n):
      px, py = map(float, input().split())
      self.objetos[i].pos_x = px
      self.objetos[i].pos_y = py

    print("Ingrese las velocidades de los {} objetos".format(self.n))
    for i in range(self.n):
      self.objetos[i].velocidad = float(input())

    print("Ingrese las aceleraciones de los {} objetos".format(self.n))
    for i in range(self.n):
      self.objetos[i].aceleracion = float(input())

  def hallar_posicion_x_cm(self):
    sumatoria = 0
    for i in range(self.n):
      sumatoria += self.objetos[i].masa * self.objetos[i].pos_x
    return sumatoria / self.masa_total

  def hallar_posicion_y_cm(self):
    sumatoria = 0
    for i in range(self.n):
      sumatoria += self.objetos[i].masa * self.objetos[i].pos_y
    return sumatoria / self.masa_total

  def hallar_velocidad_cm(self):
    sumatoria = 0
    for i in range(self.n):
      sumatoria += self.objetos[i].masa * self.objetos[i].velocidad
    return sumatoria / self.masa_total

  def hallar_aceleracion_cm(self):
    sumatoria = 0
    for i in range(self.n):
      sumatoria += self.objetos[i].masa * self.objetos[i].aceleracion
    return sumatoria / self.masa_total

  def hallar_cantidad_de_movimiento_cm(self):
    sumatoria = 0
    for i in range(self.n):
      sumatoria += self.objetos[i].masa * self.objetos[i].velocidad
    return sumatoria

  def hallar_fuerza_cm(self):
    sumatoria = 0
    for i in range(self.n):
      sumatoria += self.objetos[i].masa * self.objetos[i].aceleracion
    return sumatoria

  def mostrar_opciones(self):
    while True:
        print("***** MENU *****")
        print("1) Hallar posicion en x del centro de masa")
        print("2) Hallar posicion en y del centro de masa")
        print("3) Hallar velocidad del centro de masa")
        print("4) Hallar aceleracion del centro de masa")
        print("5) Hallar cantidad de movimiento del centro de masa")
        print("6) Hallar fuerza del centro de masa")
        print("7) Salir")

        op = input("Digite el numero de la opcion que desea realizar: ")
        if op == "1":
            res = self.hallar_posicion_x_cm()
            print("El centro de masa se ubica en x en la posicion {}".format(res))
        elif op == "2":
            res = self.hallar_posicion_y_cm()
            print("El centro de masa se ubica en y en la posicion {}".format(res))
        elif op == "3":
            res = self.hallar_velocidad_cm()
            print("El centro de masa tiene una velocidad de {} m/s".format(res))
        elif op == "4":
            res = self.hallar_aceleracion_cm()
            print("El centro de masa tiene una aceleracion de {} m/s^2".format(res))
        elif op == "5":
            res = self.hallar_cantidad_de_movimiento_cm()
            print("El centro de masa tiene una cantidad de movimiento de {} kg * m/s".format(res))
        elif op == "6":
            res = self.hallar_fuerza_cm()
            print("El centro de masa tiene una fuerza de {} N".format(res))
        elif op == "7":
            return

if __name__ == "__main__":
    mi_calc = Calculadora()
    mi_calc.pedir_datos()
    mi_calc.mostrar_opciones()
