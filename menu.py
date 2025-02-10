import os
import database as db
import helper as elp
def iniciar():
        while True:
            os.system('cls')
            print("========================")
            print(" Bienvenido al Manager")
            print("========================")
            print("[1] Listar Clientes")
            print("[2] Buscar Cliente")
            print("[3] Añadir Cliente")
            print("[4] Modificar Cliente")
            print("[5] Borrar Cliente")
            print("[6] Cerrar el Manager")
            print("========================")
            opcion = input("> ")
            os.system('cls')

            if(opcion == '1'):
              print("Listado de clientes... \n")
              for cliente in db.Clientes.lista:
                print(F"{cliente} \n")
            if(opcion == "2"):
              print("Ingrese un dni, para buscar a su cliente: \n")
              dni= elp.leer_texto(3,3, "DNI (2 ints y 1 char).").upper()
              cliente = db.Clientes.buscar(dni)
              print(cliente) if cliente else print("Cliente no encontrado.") 
            if(opcion == '3'):
              dni = None
              print("Añadir de cliente... \n")
              while True:
                dni= elp.leer_texto(3,3, "DNI (2 ints y 1 char).").upper()
                if elp.validacion_dni(dni, db.Clientes.lista):
                  break
              nombre= elp.leer_texto(2,20, "Nombre (2 a 20 char).").capitalize()
              apellido= elp.leer_texto(2,20, "Apellido (2 a 20 char).").capitalize()
              nuevo_cliente= db.Clientes.crear(dni, nombre, apellido)
              print("Cliente Añadido correctamente ")
            if(opcion == '4'):
              print("Modificando un cliente... \n")
              dni= elp.leer_texto(3,3, "DNI (2 ints y 1 char).").upper()
              cliente_modificado = db.Clientes.buscar(dni)
              if cliente_modificado:
                print("Cliente encontrado, porfavor modifique:")
                nombre= elp.leer_texto(2,20, f"Nombre (2 a 20 char) [{cliente_modificado.nombre}]").capitalize()
                apellido= elp.leer_texto(2,20, f"Apellido (2 a 20 char) [{cliente_modificado.apellido}]").capitalize()
                db.Clientes.modificar(dni, nombre, apellido)
              else: print("")
            if(opcion == '5'):
              print("Borrando un clientes... \n")
              dni= elp.leer_texto(3,3, "DNI (2 ints y 1 char).").upper()
              cliente_borrado = db.Clientes.buscar(dni)
              if cliente_borrado:
                db.Clientes.borrar(cliente_borrado.dni)
                print("Cliente borrado.")
              else:print('cliente no encontrado')
            if(opcion == '6'):
              print("Saliendo... \n")
              break
            input("\nPresiona ENTER para continuar...")