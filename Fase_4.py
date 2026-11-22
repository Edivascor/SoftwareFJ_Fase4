# ==========================================================
# FASE 4 - PROGRAMACIÓN
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Empresa: Software FJ
# Autor: Grupo de trabajo
# ==========================================================

# ==========================================================
# IMPORTACIONES
# ==========================================================

from abc import ABC, abstractmethod
import logging

# ==========================================================
# CONFIGURACIÓN DEL ARCHIVO DE LOGS
# ==========================================================

logging.basicConfig(
    filename="softwarefj.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================================

class ClienteError(Exception):
    """Error relacionado con clientes"""
    pass


class ServicioError(Exception):
    """Error relacionado con servicios"""
    pass


class ReservaError(Exception):
    """Error relacionado con reservas"""
    pass


# ==========================================================
# CLASE ABSTRACTA ENTIDAD
# ==========================================================

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# ==========================================================
# CLASE CLIENTE
# ==========================================================

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        # Validar nombre
        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío.")

        # Validar correo
        if "@" not in correo:
            raise ClienteError("Correo electrónico inválido.")

        # Validar teléfono
        if not telefono.isdigit():
            raise ClienteError("El teléfono debe contener solo números.")

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Métodos GET
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_info(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )


# ==========================================================
# CLASE ABSTRACTA SERVICIO
# ==========================================================

class Servicio(ABC):

    def __init__(self, nombre):

        if not nombre:
            raise ServicioError("El nombre del servicio es obligatorio.")

        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    # Simulación de sobrecarga usando parámetros opcionales
    def calcular_total(self, impuesto=0, descuento=0):

        costo = self.calcular_costo()

        return costo + impuesto - descuento


# ==========================================================
# SERVICIO 1
# ==========================================================

class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero.")

        self.horas = horas

    def calcular_costo(self):

        return self.horas * 50000

    def descripcion(self):

        return (
            f"Reserva de sala corporativa por "
            f"{self.horas} horas."
        )


# ==========================================================
# SERVICIO 2
# ==========================================================

class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipos")

        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a cero.")

        self.dias = dias

    def calcular_costo(self):

        return self.dias * 30000

    def descripcion(self):

        return (
            f"Alquiler de equipos tecnológicos por "
            f"{self.dias} días."
        )


# ==========================================================
# SERVICIO 3
# ==========================================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, horas):

        super().__init__("Asesoría Especializada")

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero.")

        self.horas = horas

    def calcular_costo(self):

        return self.horas * 80000

    def descripcion(self):

        return (
            f"Asesoría especializada durante "
            f"{self.horas} horas."
        )


# ==========================================================
# CLASE RESERVA
# ==========================================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError(
                "La duración debe ser mayor a cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )


# ==========================================================
# LISTA GENERAL DE RESERVAS
# ==========================================================

reservas = []


# ==========================================================
# PRUEBAS DEL SISTEMA
# (10 OPERACIONES)
# ==========================================================

print("\n========== INICIO DE PRUEBAS ==========\n")

# ----------------------------------------------------------
# OPERACIÓN 1
# Cliente válido
# ----------------------------------------------------------

try:

    cliente1 = Cliente(
        "Juan Perez",
        "juan@gmail.com",
        "3001234567"
    )

    print(cliente1.mostrar_info())

except Exception as e:

    logging.error(e)
    print(e)

# ----------------------------------------------------------
# OPERACIÓN 2
# Cliente válido
# ----------------------------------------------------------

try:

    cliente2 = Cliente(
        "Maria Rodriguez",
        "maria@gmail.com",
        "3014567890"
    )

    print(cliente2.mostrar_info())

except Exception as e:

    logging.error(e)
    print(e)

# ----------------------------------------------------------
# OPERACIÓN 3
# Error nombre vacío
# ----------------------------------------------------------

try:

    cliente3 = Cliente(
        "",
        "error@gmail.com",
        "123456"
    )

except Exception as e:

    logging.error(e)
    print("ERROR:", e)

# ----------------------------------------------------------
# OPERACIÓN 4
# Error correo
# ----------------------------------------------------------

try:

    cliente4 = Cliente(
        "Pedro",
        "pedrogmail.com",
        "123456"
    )

except Exception as e:

    logging.error(e)
    print("ERROR:", e)

# ----------------------------------------------------------
# OPERACIÓN 5
# Reserva sala correcta
# ----------------------------------------------------------

try:

    sala = ReservaSala(4)

    print(sala.descripcion())

    print(
        "Costo:",
        sala.calcular_total(impuesto=10000)
    )

except Exception as e:

    logging.error(e)
    print(e)

# ----------------------------------------------------------
# OPERACIÓN 6
# Alquiler correcto
# ----------------------------------------------------------

try:

    equipo = AlquilerEquipo(5)

    print(equipo.descripcion())

except Exception as e:

    logging.error(e)

# ----------------------------------------------------------
# OPERACIÓN 7
# Asesoría correcta
# ----------------------------------------------------------

try:

    asesoria = AsesoriaEspecializada(3)

    print(asesoria.descripcion())

except Exception as e:

    logging.error(e)

# ----------------------------------------------------------
# OPERACIÓN 8
# Servicio incorrecto
# ----------------------------------------------------------

try:

    servicio_error = ReservaSala(-2)

except Exception as e:

    logging.error(e)

    print("ERROR:", e)

# ----------------------------------------------------------
# OPERACIÓN 9
# Reserva exitosa
# ----------------------------------------------------------

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        4
    )

    reserva1.confirmar()

    reservas.append(reserva1)

    print("\nReserva Exitosa")

    print(reserva1.mostrar_reserva())

except Exception as e:

    logging.error(e)

# ----------------------------------------------------------
# OPERACIÓN 10
# Reserva con error
# ----------------------------------------------------------

try:

    reserva2 = Reserva(
        cliente2,
        equipo,
        0
    )

except Exception as e:

    logging.error(e)

    print("ERROR:", e)

# ==========================================================
# EJEMPLO TRY - EXCEPT - ELSE
# ==========================================================

print("\n===== TRY - EXCEPT - ELSE =====")

try:

    cliente5 = Cliente(
        "Carlos",
        "carlos@gmail.com",
        "3124567890"
    )

except Exception as e:

    print(e)

else:

    print(
        "Cliente registrado correctamente"
    )

# ==========================================================
# EJEMPLO TRY - EXCEPT - FINALLY
# ==========================================================

print("\n===== TRY - EXCEPT - FINALLY =====")

try:

    reserva1.confirmar()

except Exception as e:

    print(e)

finally:

    print(
        "Proceso finalizado correctamente"
    )

# ==========================================================
# ENCADENAMIENTO DE EXCEPCIONES
# ==========================================================

print("\n===== EXCEPCIONES ENCADENADAS =====")

try:

    try:

        int("ABC")

    except ValueError as error_original:

        raise ClienteError(
            "Conversión inválida de edad."
        ) from error_original

except ClienteError as e:

    logging.error(e)

    print("ERROR:", e)

# ==========================================================
# DEMOSTRACIÓN DE POLIMORFISMO
# ==========================================================

print("\n===== POLIMORFISMO =====")

servicios = [
    sala,
    equipo,
    asesoria
]

for servicio in servicios:

    print("\n", servicio.nombre)

    print(servicio.descripcion())

    print(
        "Costo:",
        servicio.calcular_costo()
    )

print(
    "\nSistema ejecutado correctamente."
)