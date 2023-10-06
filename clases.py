#Nombre: Christian Luis Gonzales Fernández
#codigo: 20182758

#Definimos las clases para cada entidad
#A través de la función __init__() e ingresamos como parámetros self, y los demas atributos

class Alumno:
    def __init__(self, nombre, pc_mac):
        self.nombre = nombre
        self.pc_mac = pc_mac

class Curso:
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado
        self.alumnos = []
        self.servidores = []

    #definimos los metodos para la clase
    def agregar_alumno(self, alumno):
        #append - para añadir
        self.alumnos.append(alumno)

    def remover_alumno(self, alumno):
        #remove - para remover
        self.alumnos.remove(alumno)

    def añadir_servidor_servicio(self, servidor):
        self.servidores.append(servidor)

class Servidor:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip
        self.servicios = []

class Servicio:
    def __init__(self, nombre, protocolo, puerto):
        self.nombre = nombre
        self.protocolo = protocolo
        self.puerto = puerto

#funcion main
if __name__ == "__main__":
    # Instanciamos un objeto de cada clase, atraves de sus constructores
    alumno1 = Alumno("Juan", "00:11:22:33:44:55")
    curso1 = Curso("Informática", "Activo")
    servidor1 = Servidor("Servidor1", "192.168.1.1")
    servicio1 = Servicio("Web", "HTTP", 80)

    #llamando los metodos de la clase Curso

    #"Agregar un alumno al curso"
    curso1.agregar_alumno(alumno1)

    #"Añadir servidor/servicio al curso"
    curso1.añadir_servidor_servicio(servidor1)

    # Imprimir información
    print("Alumno:", alumno1.nombre, "PC:", alumno1.pc_mac)
    print("Curso:", curso1.nombre, "Estado:", curso1.estado)
    print("Alumnos en el curso:", [alumno.nombre for alumno in curso1.alumnos])
    print("Servidor:", servidor1.nombre, "Dirección IP:", servidor1.direccion_ip)
