###Mostrar el menú y coordinar la ejecución del programa.###

from computadoras import *
from reportes import *
# MENÚ PRINCIPAL
opcion = 0
while opcion != 10:
    print("\n=================================")
    print("      SISTEMA DE PRÉSTAMOS")
    print("=================================")
    print("1. Consultar computadoras")
    print("2. Buscar por software")
    print("3. Solicitar préstamo")
    print("4. Devolver computadora")
    print("5. Crear reservación")
    print("6. Agregar computadora")
    print("7. historial de prestamos")
    print("8. Necesidades de Software")
    print("9. Estadisticas")
    print("10. Salir")
    print("=================================")
    opcion = int(input("Seleccione una opción: "))

    # 1. Consultar computadoras
    if opcion == 1:
        listar_computadoras()
    # 2. Buscar por software
    elif opcion == 2:
        buscar_software()
    # 3. Solicitar préstamo
    elif opcion == 3:
        solicitar_prestamo()
    # 4. Devolver computadora
    elif opcion == 4:
        Devolver_computadora()
    # 5. Crear reservacion
    elif opcion == 5:
        Crear_reservacion()
    # 6. Agregar computadora
    elif opcion == 6:
        Agregar_computadora()
    #7. historial de prestamos
    elif opcion == 7:
        historial_prestamos()
    #8. Necesidades de Software
    elif opcion == 8:
        Necesidades_de_Software()
    #9. Estadisticas
    elif opcion == 9:
        mostrar_estadisticas()
    # 10. Salir
    elif opcion == 10:
        print("\nGracias por utilizar el sistema.")
    else:
        print("\nOpción no válida.")