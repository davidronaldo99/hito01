def registrar_cliente(): #funcion para registrar cliente 
    nombre = input("Ingrese el nombre del cliente: ") # pedir el nombre al usuario 
    email = input("Ingrese el correo electrónico del cliente: ") # pedir el email al usuario
    telefono = input("Ingrese el teléfono del cliente: ") # pedir el telefono al usuario 
   

    with open('cliente.txt', 'a') as file:
        file.write(f"Nombre de cliente: {nombre}, Email: {email} Telefono:{telefono} \n")


        
def visualizar_clientes(): # funcion para ver los clientes
    with open('cliente.txt', 'r') as file:
        data = file.read()
        print(data) # Abrimos el archivo de lectura 

def buscar_cliente(): # funcion para buscar el cliente 
    nombre = input("Ingrese el nombre del cliente a buscar: ") # Le decimos al usuario que ponga el nombre del cliente para buscarlo 

    with open('cliente.txt', 'r') as file:
        for line in file:
            if f"Nombre de cliente: {nombre}" in line: 
                print(line)
                break
        else:
            print("Cliente no encontrado") # En caso de que no exista nos dira esto


def realizar_compra(): # funcion para realizar una compra (funcion clave)
    nombre_cliente = input("Ingrese el nombre del cliente que realiza la compra: ")  # pedimos el nombre al usuario 
    nacionalidad_cliente = input("Ingrese la nacionalidad del cliente (español/extranjero): ").lower() # pedimos nacionalidad en caso de que sea español se le aplicara IVA y en caso de extranjero un 20% de transporte
    productos_input = input("Ingrese los productos de la compra (ejemplo: producto1:precio, producto2:precio, ...): ") # pedimos que ingrese los productos y lso precios de estos para aplicar dicho %

    productos = dict(item.split(":") for item in productos_input.split(",")) # Usamos dict para crear una clave de letras , no usamos otra como por ejemplo str que es para valores numericos

    total_compra = sum(float(precio) for precio in productos.values()) # Calculaqmos el total de la compra  con un bucle for con el prcio y los productos 

    if nacionalidad_cliente == "español":
        total_compra += total_compra * 0.21 # Añadimos el valor del 21% en caso de que sea español 
    with open('compras.txt', 'a') as file:
        file.write(f"Cliente: {nombre_cliente}, Productos: {productos_input}, Total: {total_compra:.2f}\n") # Realizamos la aprtura del archivo con el total de compra dependiendo del precio 

def enviar_seguimiento(): # Creamos la funcion para enviar un seguimiento al cliente de su compra 
    nombre_cliente = input("Ingrese el nombre del cliente para enviar seguimiento: ") # Solicitamos el nombre de dich cliente al que quieres er enviado el sms
    nacionalidad_cliente = input("Ingrese la nacionalidad del cliente (español/extranjero): ").lower() # Le pedimos su nacionalidad 
    codigo_seguimiento = input("Ingrese el código de seguimiento del pedido: ") # Y el codigo de seguimiento 

    mensaje = (f"Su pedido con código {codigo_seguimiento} ha sido enviado.")  #Este es el mensaje que nos imprimira con el codigo de seguimiento 

    if nacionalidad_cliente != "español":
        mensaje += (f" Se ha añadido un 21% de IVA a su pedido.") # Si el cliente es español saldrá este mensaje 
    elif nacionalidad_cliente!= "extranjero":
        mensaje += (f"Se ha añadido un 20% de transporte a su pedido") # Si l cliente es extranjero le saldrá este mensaje 
    with open('seguimiento.txt', 'a') as file: # Abrimos el archivo del seguimiento 
        file.write(f"Cliente: {nombre_cliente}, SMS: {mensaje}\n") # Este es el mensaje que nos imprimira 


