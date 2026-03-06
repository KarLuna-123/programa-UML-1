class Persona():#Persona (Clase Base - Abstracta)
    def __init__(self, idPersona, nombre, email, telefono):
        self.nombre = nombre
        self.idPersona = idPersona
        self.email = email
        self.telefono = telefono

class Usuario(Persona):#Usuario (Hereda de Persona)
        def __init__(self, idPersona, nombre, email, telefono, saldo, puntos_Fidelidad):
            super().__init__(idPersona, nombre, email, telefono)
            self.saldo = saldo
            self.puntos_Fidelidad = puntos_Fidelidad
            self.historialReservas = []
        def login(self):
            print(f"Bienvenido(a) {self.nombre}")
        def logout(self):
            print(f"Adios {self.nombre}")
        def actualizarDatos(self, nombre, email, telefono):
            self.nombre = nombre
            self.email = email
            self.telefono = telefono
        def agregar_saldo(self, cantidad):
            self.saldo += cantidad
            print(f"Deposito exitoso. Nuevo saldo: ${self.saldo}")        
        def crearReserva(self, reserva):
            self.historialReservas.append(reserva)
            print(f"Registro de reserva finalizado")
        def cancelarReserva(self, reserva):
            if reserva in self.historialReservas:
                self.historialReservas.remove(reserva)
                print("Cancelacion confirmada")
            else:
                print("Reserva no encontrada.")
        def consultarPromociones(self):
            if self.puntos_Fidelidad >= 100:
                print("Promoción disponible. Puedes usar tus puntos en descuentos.")
            else:
                faltan = 100 - self.puntos_Fidelidad
                print(f"Te faltan {faltan} puntos para obtener la promocion.")

class Empleado(Persona):#Empleado (Hereda de Persona)
    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario
    def login(self):
            print(f"Hola {self.nombre}")
            print(f"Tu rol es: {self.rol}")
            print(f"Identificacion: {self.idPersona}")
    def logout(self):
        print(f"Adios {self.nombre}, gracias por tu trabajo")
    def actualizarDatos(self, email, telefono, rol):
        self.email = email
        self.telefono = telefono
        self.rol = rol
    def marcar_entrada(self):
        print(f"{self.nombre} ha marcado su entrada.")
    def gestionar_funciones(self):
        if self.rol == "admin":
            print(f"{self.nombre} está gestionando las funciones")
        else:
            print("No tienes permiso para gestionar funciones")

class Espacio():#Espacio (Clase Base)
    def __init__(self, lugar):
        self.lugar = lugar
    def limpiar(self):
        print(f"Limpiar: {self.lugar}")
    def verificarDisponibilidad(self):
        print(f"Verificando disponibilidad en: {self.lugar}")

class Sala(Espacio):#Sala (Hereda de Espacio)
        def __init__(self, lugar, tipo, capacidadTotal, vip):
            super().__init__(lugar)
            self.tipo = tipo
            self.capacidadTotal = capacidadTotal
            self.vip = vip
            self.asientos_ocupados = []
        def obtenerTipoSala(self):
            print(f"Sala: {self.tipo} - Capacidad: {self.capacidadTotal} personas")
        def ajustarAforo(self, nueva_capacidadTotal):
            self.capacidadTotal = nueva_capacidadTotal
            print(f"La capacidad de la sala es de {self.capacidadTotal} personas")
        def asiento_disponible(self, asiento):
            return asiento not in self.asientos_ocupados

class ZonaComida(Espacio):#ZonaComida (Hereda de Espacio)
         def __init__(self, lugar, stock, productos):
                super().__init__(lugar)
                self.stock = stock
                self.productos = productos
         def venderProducto(self, producto):
                if producto in self.productos and self.stock > 0:
                    self.stock -= 1
                    print(f"Producto {producto} vendido quedan: {self.stock}")
                else:
                    print(f"Producto {producto} no disponible")
         def actualizarInventario(self, nuevo_stock):
                self.stock = nuevo_stock
                print(f"El inventario se ha actualizzado")

class Pelicula():
        def __init__(self, titulo, duracion, clasificacion, genero):
            self.titulo = titulo
            self.duracion = duracion
            self.genero = genero
            self.clasificacion = clasificacion
        def obtenerSinopsis(self):
            print(f"Pelicula: {self.titulo}")
            print(f"Duracion: {self.duracion} minutos")
            print(f"Genero: {self.genero}")
        def esAptaParaTodoPublico(self):
             if self.clasificacion == "A":
                print("Apta para todo publico.")
             elif self.clasificacion == "B":
                print("Apta para mayores de 12 años.")
             elif self.clasificacion == "C":
                print("Apta para mayores de 18 años.")
             else:
                print("Sin clasificar.")

class Funcion():
        def __init__(self, pelicula, sala, horario, precioBase):
            self.pelicula = pelicula
            self.sala = sala
            self.horario = horario
            self.precioBase = precioBase
        def calcularAsientosLibres(self):
            libres = self.sala.capacidadTotal - len(self.sala.asientos_ocupados)
            print(f"En la función de {self.pelicula.titulo} hay {libres} lugares disponibles")
            return libres
        def obtenerDetalles(self):
            self.pelicula.obtenerSinopsis()
            self.sala.obtenerTipoSala()
            print(f"Horario: {self.horario}")
            print(f"Precio por persona: ${self.precioBase}")

class Promocion():
        def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
            self.codigo = codigo
            self.descripcion = descripcion
            self.porcentajeDescuento = porcentajeDescuento 
            self.fechaExpiracion = fechaExpiracion
        def esValida(self):
            from datetime import date
            if date.today() <= self.fechaExpiracion:
                print(f"Promoción {self.codigo} valida hasta {self.fechaExpiracion}")
                return True
            else:
                print(f"Promocion {self.codigo} vencida")
                return False
        def aplicar_porcentajeDescuento(self, cantidad):
            if self.esValida():
                a = cantidad * (self.porcentajeDescuento / 100)
                total = cantidad - a
                print(f"Descuento de {self.porcentajeDescuento}% aplicado")
                print(f"Total a pagar: ${total:.2f}")
                return total
            return cantidad


class Reserva():
    contador = 1

    def __init__(self, usuario, funcion, asientos):
        self.idReserva = Reserva.contador
        Reserva.contador += 1
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = []
        self.estado = "pendiente"
        self.total = 0

        for a in asientos:
            if self.funcion.sala.asiento_disponible(a):
                self.asientos.append(a)
                self.funcion.sala.asientos_ocupados.append(a)
                print(f"Asiento {a} reservado")
            else:
                print(f"El asiento {a} no esta disponibke")

        self.total = len(self.asientos) * self.funcion.precioBase

    def confirmarPago(self):
        if self.estado == "pendiente":
            if self.usuario.saldo >= self.total:
                self.usuario.saldo -= self.total
                self.usuario.puntos_Fidelidad += int(self.total / 10)
                self.estado = "confirmada"
                self.usuario.crearReserva(self)
                print(f"Pago confirmado")
            else:
                print(f"Saldo insuficiente")
        else:
            print(f"Reserva: {self.estado}")

    def aplicar_porcentajeDescuento(self, promo):
        if self.estado == "pendiente":
            self.total = promo.aplicar_porcentajeDescuento(self.total)
        else:
            print("El descuento no puede aplicarse a reservas confirmadas o pagadas.")

    def generarTicket(self):
        if self.estado == "confirmada":
            print(f"TICKET RESERVA #{self.idReserva}")
            print(f"Usuario: {self.usuario.nombre}")
            print(f"Pelicula: {self.funcion.pelicula.titulo}")
            print(f"Sala: {self.funcion.sala.lugar} ({self.funcion.sala.tipo})")
            print(f"Horario: {self.funcion.horario}")
            print(f"Asientos: {self.asientos}")
            print(f"Total pagado: ${self.total:.2f}")
            print(f"Estado: {self.estado}")
        else:
            print("Ticket no disponible: reserva pendiente de validación.")