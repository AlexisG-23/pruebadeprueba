from json import dump
def validNum(nombre,mini,maxi):
    while True:
        try:
            aux=int(input(f"Ingrese un(a) {nombre} entre {mini} y {maxi}\n>"))
            if aux<mini or aux>maxi:
                print("Fuera de Rango")
            else:
                return aux
        except:
            print("dato entregado no solicitado")
            print(f"Por favor ingrese un(a) {nombre} entre {mini} y {maxi}")

def menu():
    print("""1.) Registrar
2.) Consultar Registro
3.) Modificar Registro
4.) Guardar y Salir
""")
    aux=validNum("opcion",1,4)
    return aux

def registroHab(diccionario):
    nombres=[]
    ruts=[]
    hab=validNum("habitacion",1,20)
    if diccionario[f"Habitacion{hab}"]["estado"]!="Disponible":
        print("Habitación no disponible.")
    else:
        print("1.- Reservar\n2.- Ocupar")
        opc=validNum("opcion",1,2)
        if opc==1:
            ruts.append(input("ingrese su rut\n>"))
            nombres.append(input("ingrese su nombre\n>"))
            diccionario[f"Habitacion{hab}"]["rut"]=ruts
            diccionario[f"Habitacion{hab}"]["nombre"]=nombres
            diccionario[f"Habitacion{hab}"]["estado"]="Reservado"
            print("Reservado correctamente")
        else:
            cant=validNum("Cantidad de personas",1,3)
            for i in range(cant):
                ruts.append(input(f"ingrese el rut del ocupante {i+1}\n>"))
                nombres.append(input(f"ingrese el nombre del ocupante {i+1}\n>"))
            diccionario[f"Habitacion{hab}"]["rut"]=ruts
            diccionario[f"Habitacion{hab}"]["nombre"]=nombres
            diccionario[f"Habitacion{hab}"]["estado"]="Ocupado"
            
def consulta(diccionario):
    cont=1
    for a in diccionario:
        print(f"Habitacion {cont}",end=": ")
        print(diccionario[a]["estado"])
        cont+=1
        
def modReg(diccionario):
    hab=validNum("habitacion",1,20)
    print(f"El estado de la habitacion {hab} es",end=" ")
    print(diccionario[f"Habitacion{hab}"]["estado"])
    if diccionario[f"Habitacion{hab}"]["estado"]=="Reservado":
        print("Cambiar estado a:\n1.- Ocupado\n2.- Disponible")
        aux=validNum("estado",1,2)
        if aux==1:
            diccionario[f"Habitacion{hab}"]["estado"]="Ocupado"

        else:
            diccionario[f"Habitacion{hab}"]["estado"]="Disponible"
            diccionario[f"Habitacion{hab}"]["rut"]=[]
            diccionario[f"Habitacion{hab}"]["nombre"]=[]
    elif diccionario[f"Habitacion{hab}"]["estado"]=="Ocupado":
        print("Cambiar estado a:\n1.- Disponible\n2.- Reservado")
        aux=validNum("estado",1,2)
        if aux==1:
            diccionario[f"Habitacion{hab}"]["estado"]="Disponible"
            diccionario[f"Habitacion{hab}"]["rut"]=[]
            diccionario[f"Habitacion{hab}"]["nombre"]=[]
        else:
            diccionario[f"Habitacion{hab}"]["estado"]="Reservado"
    print(f"El estado de la habitacion {hab} ha cambiado a",end=" ")
    print(diccionario[f"Habitacion{hab}"]["estado"])
    
def guardar(diccionario):
    cont=1
    try:
        crate=open("Hotel.json","x")
    except:
        print("Archivo ya existe")
    aux=int(input("Desea leer el archivo previo?\n1.- SI\n2.- NO\n>"))
    while aux>=3:
        aux=int(input("Numero Ingresado no Valido\nDesea leer el archivo previo?\n1.- SI\n2.- NO\n>"))
    if aux==1:
        lectura=open("Hotel.json","r")
        for a in lectura:
            print(a)
        lectura.close()
    else:
        print("Ok. :)")
    escritura=open("Hotel.json","w")
    dump(diccionario,escritura,indent=4)
    """
    for a in range(len(diccionario)):
        dump((f"Habitacion{a+1}:"),escritura,indent=4)
        dump(diccionario[f"Habitacion{cont}"]["estado"],escritura,indent=4)
        for j in range(len(diccionario[f"Habitacion{cont}"]["rut"])):
            dump(('Rut'(j+1),diccionario[f"Habitacion{cont}"]["rut"][j]),escritura,indent=4)
            dump(('Nombre'(j+1),diccionario[f"Habitacion{cont}"]["nombre"][j]),escritura,indent=4)
        cont+=1
    """
    escritura.close()
















        
