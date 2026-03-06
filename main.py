from models import *
#creacion de pelis
peli1 = Pelicula("Avengers",120,"B","Accion")
peli2 = Pelicula("Mario Bros",95,"A","Animacion")
peli3 = Pelicula("Batman",110,"B","Accion")
peli4 = Pelicula("Titanic",180,"B","Drama")
peli5 = Pelicula("Joker",122,"C","Drama")
peli6 = Pelicula("Spiderman",115,"B","Accion")
peli7 = Pelicula("Frozen",102,"A","Animacion")
peli8 = Pelicula("Avatar",160,"B","Ciencia Ficcion")
peli9 = Pelicula("Toy Story",90,"A","Animacion")
peli10 = Pelicula("Minions",85,"A","Comedia")
#salas creadas
sala1 = Sala("Sala 1","2D",50,False)
sala2 = Sala("Sala 2","3D",60,False)
sala3 = Sala("Sala 3","IMAX",70,True)
#Funciones
f1 = Funcion(peli1,sala1,"16:00",80)
f2 = Funcion(peli2,sala1,"18:00",80)
f3 = Funcion(peli3,sala2,"20:00",90)
#usuarios
u1 = Usuario(1,"Carlos","carlos@email.com","2221",500,0)
u2 = Usuario(2,"Ana","ana@email.com","2222",500,0)
u3 = Usuario(3,"Luis","luis@email.com","2223",500,0)
u4 = Usuario(4,"Maria","maria@email.com","2224",500,0)
u5 = Usuario(5,"Pedro","pedro@email.com","2225",500,0)
u6 = Usuario(6,"Laura","laura@email.com","2226",500,0)
u7 = Usuario(7,"Jorge","jorge@email.com","2227",500,0)
u8 = Usuario(8,"Sofia","sofia@email.com","2228",500,0)
u9 = Usuario(9,"Diego","diego@email.com","2229",500,0)
u10 = Usuario(10,"Elena","elena@email.com","2230",500,0)
admin = Empleado(1,"Administrador","admin@email.com","0000","EMP1","admin","9-5")
#promociones
from datetime import date
promo1 = Promocion("PROMO10","Descuento 10%",10,date(2026,12,31))
promo2 = Promocion("PROMO20","Descuento 20%",20,date(2026,12,31))
#Reservas

print("-----Asientos reservados-----")
r1 = Reserva(u1,f1,["A1","A2"])
r2 = Reserva(u2,f1,["A3"])
r3 = Reserva(u3,f2,["B1","B2","B3"])
r4 = Reserva(u4,f2,["B4"])
r5 = Reserva(u5,f3,["C1","C2"])
r6 = Reserva(u6,f3,["C3"])
r7 = Reserva(u7,f1,["A4"])
r8 = Reserva(u8,f2,["B5"])
r9 = Reserva(u9,f3,["C4"])
r10 = Reserva(u10,f1,["A5"])

u1.login()
print("\n-----PROMOCIONES-----")
r1.aplicar_porcentajeDescuento(promo1)#Prmocion aplicada
u1.consultarPromociones()

print("\n-----TICKET-----")
r1.generarTicket()#Ticket
r1.confirmarPago()#Estado

print("\n-----SINOPSIS-----")
f1.obtenerDetalles()
print("Asientos libres:", f1.calcularAsientosLibres())

print("\n-----GESTION-----")
sala1.limpiar()
admin.marcar_entrada()