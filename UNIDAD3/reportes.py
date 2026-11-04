###Generar estadísticas e informes de necesidades de software.###


from datos import *
def historial_prestamos():
  print("\n--- HISTORIAL DE PRÉSTAMOS ---")
  print("\n--- COMPUTADORAS ---")
  for i in range(len(computadoras)):
        print("Aula:", computadoras[i]["aula"], "ID:", computadoras[i]["id"], "Software:", computadoras[i]["programas"], "Estado:", computadoras[i]["estado"])

def Necesidades_de_Software():
    print("\n--- HISTORIAL DE NECESIDADES ---")
    if len(historial_necesidades) == 0:
        print("No hay registros en el historial.")
    else:
        for i in range(len(historial_necesidades)):
            print(f"{i + "aula"} | Programa: {historial_necesidades[i]["id"]} | Fecha: {historial_necesidades[i]["aula"]} |")

def mostrar_estadisticas():
    print("\n======= Estadísticas por programa ===========")
    conteo_programas = {}
    for prestamo in nuevo_prestamo:
        prog = prestamo["aula"].strip()
        conteo_programas[prog] = conteo_programas.get(prog, 0) + 1

    for prog, veces in conteo_programas.items():
        print(f"{prog.lower()} : {veces} veces")

    print("\n======= Estadísticas por carrera ===========")
    conteo_carreras = {}
    for prestamo in nuevo_prestamo:
        num_ctrl_prestamo = prestamo[0]
        carrera_alumno = "Desconocida"
        for alumno in alumnos:
            if alumno[0] == num_ctrl_prestamo:
                carrera_alumno = alumno[2]
                break
        conteo_carreras[carrera_alumno] = conteo_carreras.get(carrera_alumno, 0) + 1

    for carrera, veces in conteo_carreras.items():
        print(f"{carrera}: {veces} veces")

