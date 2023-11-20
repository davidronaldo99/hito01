from aplicacioncliente import* # Importamos el programa principal

def menu(): # Creamos la funcion del menu 

 while True: # Creamos las opciones
  print("1. Registrar Cliente")
  print("2. Ver Clientes")
  print("3. Buscar Cliente")
  print("4. Realizar Compra") 
  print("5. Enviar Seguimiento")
  print("6. Salir")

  opcion = input("Seleccione una opción: ") # Le decimos al usuario que nos de una opcion 

  if opcion == "1":
     registrar_cliente() # En caso del 1 se ejecuta la funcion registar_cliente
  elif opcion == "2":
    visualizar_clientes() # En caso de que sea 2 se ejecuta la funcion visualizar _clientes
    
  elif opcion == "3":
   buscar_cliente() # En caso de que sea 3 se ejecuta la funcion buscar_cliente

  elif opcion == "4":
   realizar_compra() # En caso de que sea 4 se ejecuta la funcion realizar_compra

  elif opcion == "5":
   enviar_seguimiento() # En caso de qye se 5 se ejecuta la funcion enviar_seguimiento 
  elif opcion == "6":
     break # Ponemos un break para romper el bucle en caso de que sea 6 ya que esta opcion es para salir del programa
  else:
   print("Opción inválida. Intente de nuevo.")

menu() 