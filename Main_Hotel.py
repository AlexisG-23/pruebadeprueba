from funciones3 import*
hotel={}
for i in range(1,21):
    hotel[f"Habitacion{i}"]={"estado":"Disponible","rut":[],"nombre":[]}
print(hotel)

while True:
    opc=menu()
    if opc==1:
        registroHab(hotel)
    if opc==2:
        consulta(hotel)
    if opc==3:
        modReg(hotel)
    if opc==4:
        guardar(hotel)
        break


