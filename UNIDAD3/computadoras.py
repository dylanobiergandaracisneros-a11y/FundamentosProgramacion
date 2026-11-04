
###Consultar, buscar y agregar computadoras.###
import datetime
from datos import * 
def listar_computadoras():
    print("\n--- COMPUTADORAS ---")
    for i in range(len(computadoras)):
        print("Aula:", computadoras[i]["aula"], "ID:", computadoras[i]["id"], "Software:", computadoras[i]["programas"], "Estado:", computadoras[i]["estado"])

def buscar_software():
    programa = input("\nIngrese el software que desea buscar: ")
    print("\n--- RESULTADOS ---")
    encontrado = False
    for i in range(len(computadoras)):
        if programa.lower() in computadoras[i][2].lower():
                print("ID:", computadoras[i]["id"], "Aula:", computadoras[i]["aula"], "Software:", computadoras[i]["programas"], "Estado:", computadoras["estado"][3])
                encontrado = True

    if encontrado == False:
        print("No se encontraron computadoras con ese software.")

def solicitar_prestamo():
  print("\n--- SOLICITAR PRÉSTAMO ---")
  num_control = input("\nIngrese el número de control: ")
  encontrado1 = False
  # Buscamos si el número de control existe en nuestra lista de listas de alumnos
  for alumno in alumnos:
      if alumno["num_control"] == num_control:
          encontrado1 = True
          break

  if encontrado1:
    id_computadora = input("Ingrese el ID de la computadora: ")
    encontrado2 = False
    for i in range(len(computadoras)):
        if computadoras[i]["id"] == id_computadora:
            encontrado2 = True
            if computadoras[i]["estado"] == "Disponible":
                computadoras[i]["estado"] = "Prestada"
                software_solicitado = input("Ingrese el software que va a utilizar: ")

                # Validar si el software existe en el equipo
                if software_solicitado.lower() not in computadoras[i][2].lower():
                    print(f"El software '{software_solicitado}' no está registrado en esta computadora.")
                    respuesta = input("¿Desea agregarlo a la lista de necesidades? (s/n): ")
                    if respuesta.lower() == 's':
                        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        historial_necesidades.append([software_solicitado, fecha_actual])
                        print("-> Software agregado correctamente al historial de necesidades")
                print("Préstamo registrado correctamente.")
                print("Computadora:", computadoras[i])
                print("Aula:", computadoras[i]["aula"])
            else:
                print("La computadora no está disponible.")
            break
    if encontrado2 == False:
        print("La computadora no existe.")
  else:
    print("El alumno no existe.")

def Devolver_computadora():
  print("\n--- DEVOLVER COMPUTADORA ---")
  id_computadora = input("dame el ID de la computadora: ")
  existe = False
  for i in range(len(computadoras)):
      if computadoras[i]["id"] == id_computadora:
          existe = True
          if computadoras[i]["estado"] == "Prestada" or computadoras[i][3] == "Reservada":
                computadoras[i]["estado"] = "Disponible"
                print("la computadora", id_computadora, "ya esta lista")
          else:
                print("la computadora", id_computadora, "no esta prestada/reservada")
          break
  if existe == False:
    print("la computadora no existe", id_computadora)

def Crear_reservacion():
  print("\n--- CREAR RESERVACIÓN ---")
  num_control = input("\nIngrese el número de control: ")
  encontrado1 = False
  for alumno in alumnos:
      if alumno["id"] == num_control:
          encontrado1 = True
          break

  if encontrado1:
    id_computadora = input("Ingrese el ID de la computadora: ")
    for i in range(len(computadoras)):
        if computadoras[i]["id"] == id_computadora:
            if computadoras[i]["estado"] == "Disponible":
                computadoras[i]["estado"] = "Reservada"
                print("Reservación registrada correctamente.")
            else:
                print("La computadora no está disponible para reservación.")
            break
  else:
    print("El alumno no existe.")

def Agregar_computadora():
  print("\n--- AGREGAR COMPUTADORA ---")
  id_computadora = input("ID de la computadora: ")
  aula = input("Aula: ")
  programas = input("Software instalado: ")
  nueva_computadora = [id_computadora, aula, programas, "Disponible"]
  # Agregamos los datos como una lista dentro de la lista principal
  computadoras.append(nueva_computadora)
  print("\nComputadora agregada correctamente.")