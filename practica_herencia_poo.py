# Ejercicios de Herencia Simple
# Crea una clase Animal con un método hacer_sonido. Luego crea una clase Perro que herede de Animal y sobrescriba el método para hacer que el perro ladre.
"""class animal:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    def hacersonido():
        print("hace ruido")
 
class perro:
    def  __init__(self,raza) -> None:
        self.raza = raza
    def hacersonido(self):
        return("perro ladrando ......")
mi_mascota = perro("labrador")
hacer_ruido = mi_mascota.hacersonido()
print(mi_mascota.raza)    
print(hacer_ruido) """        
# Crea una clase Vehiculo que tenga atributos como marca y modelo, y un método arrancar(). Luego crea una clase Motocicleta que herede de Vehiculo y añada el atributo cilindrada.
"""class vehiculo:
    def __init__(self,marca,modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        return  f"el vehiculo { self.modelo}esta arrancando ..."
    
class motocicleta(vehiculo):
    def __init__(self, marca, modelo,cilindrada) -> None:
        super().__init__(marca, modelo) 
        self.cilindrada = cilindrada
    def __repr__(self) -> str:
        return f"la marca es : {self.marca} modelo : {self.modelo} cilindrada : {self.cilindrada}"
    
mi_moto = motocicleta("yamaha","dt","125")
print(mi_moto.cilindrada)     
print(repr(mi_moto))"""          
# Define una clase Persona con un atributo nombre y un método saludar(). Crea una clase Estudiante que herede de Persona y añada el atributo grado.
"""class persona:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    def saludar(self):
        return f"hola {self.nombre} bienvenido a mi clase de herencia simple" 
    
class Estudiante(persona):
    def __init__(self, nombre,grado) -> None:
        super().__init__(nombre)
        self.grado = grado   
    
estudiante1 = Estudiante("diego fernando","tecnologia")
saludando = estudiante1.saludar()
print(saludando)"""          
# Crea una clase Instrumento con un método tocar(). Luego crea una clase Guitarra que herede de Instrumento y sobrescriba el método para tocar una canción.
"""class Instrumeto:
    def __init__(self) -> None:
        pass
    def tocar(self):
        print("tocando instrumento")
  
class guitarra(Instrumeto):
    
    def tocar(self):
        print("tocando la guitarra")
        
mi_guitarra = guitarra()        
mi_guitarra.tocar() """           
# Crea una clase Electrodomestico con un atributo potencia. Luego crea una clase Licuadora que herede de Electrodomestico y añada un método licuar().
"""class Electrodomestico:
    def __init__(self,potencia) -> None:
        self.potencia = potencia
class Licuadora(Electrodomestico):
    def __init__(self, potencia) -> None:
        super().__init__(potencia)
    def licuar(self):
        return("licuando el jugo")    
mi_licuadora = Licuadora(15)
licuando = mi_licuadora.licuar()
print(licuando)"""                
# Define una clase Empleado con un atributo salario y un método trabajar(). Luego, crea una clase Gerente que herede de Empleado y añada un método dirigir().
"""class Empleado:
    def __init__(self,salario) -> None:
        self.salario = salario
    def trabajar(self):
        return(f"el empleado esta trabajando por un salario de {self.salario}")   
    
class gerente(Empleado):
    def __init__(self, salario) -> None:
        super().__init__(salario)
        
    def dirigir(self):
        return f"el gerente esta dirigiendo o gerenciando"
el_gerente = gerente(1500000)
dirigir = el_gerente.dirigir()
print(dirigir) """                    
# Crea una clase Computadora con los atributos marca y ram. Luego crea una clase Portatil que herede de Computadora y añada el atributo peso.
"""class computadora:
    def __init__(self,marca,ram) -> None:
         self.marca = marca
         self.ram = ram
         
class portatil(computadora):
    def __init__(self, marca, ram,peso) -> None:
        super().__init__(marca, ram)  
        self.peso = peso
    def __repr__(self) -> str:
        return f"la marca del portatil es {self.marca} memoria ram : {self.ram} con un peso de {self.peso}"
                       
mi_portatil = portatil("acer","16ram","600gms")
print(repr(mi_portatil))"""         
# Crea una clase Figura con un método area(). Luego crea una clase Cuadrado que herede de Figura y calcule el área de un cuadrado.
"""class Figura:
    def __init__(self,base,altura) -> None:
        self.base = base
        self.altura = altura
        
    def area(self):
        area = self.base * self.altura
        return area
    
class Cuadrado(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__(base, altura)
       
mi_cuadrado = Cuadrado(25,20)            
area = mi_cuadrado.area()
print(area)"""        
# Crea una clase Dispositivo con un método encender(). Luego crea una clase Telefono que herede de Dispositivo y añada un método llamar().
"""class Dispositivo:
    def __init__(self,marca,modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def encender(self):
        return f"el dispositivo ha sido encendido"
    
class telefono(Dispositivo):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
    def llamar(self):
        return f" esl telefono esta llamando ... "
    
miPhone = telefono("huawei","a56")
encendido = miPhone.encender()
llamr = miPhone.llamar()
print(encendido)
print(llamr) """               
# Crea una clase CuentaBancaria con un método mostrar_saldo(). Luego crea una clase CuentaAhorros que herede de CuentaBancaria y añada el método calcular_interes().
"""class CuentaBancaria:
    def __init__(self,titular,saldo) -> None:
        self.titular = titular
        self.saldo = saldo
    def mostrar_saldo(self):
        return f"el saldo es .{self.saldo}"
    
class Cuentadeahorros(CuentaBancaria):
    def __init__(self, titular, saldo,interes) -> None:
        super().__init__(titular, saldo)
        self.interes = interes
        
    def calcular_interes(self):
        intereses = self.saldo * self.interes /100
        return intereses
    
mi_cuenta = Cuentadeahorros("diego bolaños",4000000,10)

intereses_de_mi_cuenta = mi_cuenta.calcular_interes()    
print(intereses_de_mi_cuenta)"""                    
# Crea una clase Planta con un método crecer(). Luego crea una clase Arbol que herede de Planta y sobrescriba el método para mostrar cómo crece un árbol.
"""class planta:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    def crecer(self):
        return f"crece hasta los 2 metros"
   
class Arbol(planta):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    def crecer(self):
        return f"crece  hasta los 11 metros"
    
mi_guayacan = Arbol("guayacan amarillo")
como_crece = mi_guayacan.crecer()
print(como_crece)"""                
# Crea una clase Deporte con un método practicar(). Luego crea una clase Futbol que herede de Deporte y sobrescriba el método para practicar fútbol.
"""class Deporte:
    def __init__(self) -> None:
        pass
    def practicar(self):
        return f"practicando mi deporte"
    
class Futbol(Deporte):
    def __init__(self) -> None:
        pass
    def practicar(self):
        return f"practicando futbol"
    
jugando = Futbol()
resultado = jugando.practicar()
print(resultado)"""        
# Crea una clase Automovil con un método conducir(). Luego crea una clase Camion que herede de Automovil y sobrescriba el método para describir cómo se conduce un camión.
"""class Automovil:
    def __init__(self,marca,modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def conducir(self):
        return f"el automobil se conduce para ir en familia"
    
class Camion(Automovil):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
    def conducir(self):
        return f"el camion se conduce para trabajar"
    
mi_camion = Camion("chevrolet","2024")
respuesta = mi_camion.conducir()
print(respuesta) """               
# Crea una clase Alimento con un método consumir(). Luego crea una clase Fruta que herede de Alimento y sobrescriba el método para describir cómo se come una fruta.
"""class Alimento:
    def __init__(self,fresco) -> None:
        self.fresco = fresco
    def consumir(self):
        return f"los alimentos frescos se empacan en bolsas"
    
class Fruta(Alimento):
    def __init__(self, fresco) -> None:
        super().__init__(fresco)
    def consumir(self):
        return f"las frutas se lavan y se pelan para comer "
    
mangos = Fruta("fresco")
como_comer = mangos.consumir()
print(como_comer) """               
# Crea una clase Herramienta con un método usar(). Luego crea una clase Martillo que herede de Herramienta y sobrescriba el método para describir cómo se usa un martillo.
"""class Herramienta:
    def __init__(self,nombre) -> None:
         self.nombre = nombre
    def usar(self):
        return f"se usa para reparar"
    
class Martillo(Herramienta):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    def usar(self):
        return f"se usa para martillar o golpear fuerte"
    
mi_martillo = Martillo("martillo")
como_se_usa = mi_martillo.usar()
print(como_se_usa,mi_martillo.nombre) """                
# Ejercicios de Herencia Múltiple
# Crea una clase Volador con un método volar(), y otra clase Caminante con un método caminar(). Luego crea una clase Ave que herede de ambas y use ambos métodos.
"""class Volador:
   
    def volar(self):
        print ("estoy volando")
    
class Caminante:
    
    def caminar(self):
        print ("estoy caminando")
    
class Ave(Volador,Caminante):
    pass
    
mi_ave = Ave()
print(mi_ave)
mi_ave.volar()
mi_ave.caminar()"""           
        
# Define una clase Musico con un método tocar_instrumento(), y una clase Bailarin con un método bailar(). Luego, crea una clase Artista que herede de ambas y use ambos métodos.
"""class Musico:
    def tocar_instrumento(self):
        print("el musico esta tocando el instrumento")
        
class Bailarin:
    def bailar(self):
        print(f"el bailarin esta bailando")      
 
class Artista(Musico,Bailarin):
    def actuar(self):
        print("el artista esta actuando")
    
actor = Artista()  
actor.tocar_instrumento()
actor.bailar()
actor.actuar()"""                   
# Crea una clase EncargadoDeCompras con un método comprar(), y otra clase EncargadoDeVentas con un método vender(). Luego crea una clase GerenteTienda que herede de ambas.
"""class EncargadoDeCompras:
    def comprar(self):
        print("se esta comprando")
        
class EncargadoDeVentas:
    def vender(self):
        print("se esta vendiendo")
        
class GerenteTienda(EncargadoDeCompras,EncargadoDeVentas):
    def compraventa(self):
        print("puede comprar y vender")  
        
ariel = GerenteTienda()
ariel.comprar()
ariel.vender()
ariel.compraventa()  """                    

# 1. Clase UsuarioWeb y Programador → DesarrolladorWeb
# Cada clase debe tener dos atributos:
# UsuarioWeb: nombre, horas_navegacion
# Programador: lenguaje_favorito, proyectos
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase DesarrolladorWeb que herede de ambas.
"""class UsuarioWeb:
    def __init__(self, nombre, horas_navegacion) -> None:
        self.nombre = nombre
        self.horas_navegacion = horas_navegacion
    def usar_redes_sociales(self):
        print(f"el usuario : {self.nombre} esta activo en las redes sociales")    
    def navegar(self):
        print(f"el usuario esta navegando :{self.horas_navegacion}")
        
class Programador:
    def __init__(self, lenguaje_favorito, proyectos) -> None:
        self.lenguaje_favorito = lenguaje_favorito
        self.proyectos = proyectos
    def programar(self):
        print(f"el programador  esta programando su lenguaje favorito : {self.lenguaje_favorito}") 
    def taxtear_proyectos(self):
        print(f"el programador esta texteando el proyecto")     
        
class DesarrolladorWeb(UsuarioWeb, Programador):
    def __init__(self, nombre, horas_navegacion, lenguaje_favorito, proyectos) -> None:
        #inicializo las clases padre o superclase
        UsuarioWeb.__init__(self, nombre, horas_navegacion)                      
        Programador.__init__(self, lenguaje_favorito,proyectos)
    def desarrollarSofware(self):
        print("el desarrolador esta crando software")
        
dalto = DesarrolladorWeb("lucas", 12, "python", "ahorcado y calculadora")
dalto.navegar()
dalto.usar_redes_sociales()  
dalto.programar()   
dalto.taxtear_proyectos()  
dalto.desarrollarSofware()"""  
# 2. Clase Atleta y Cocinero → AtletaCocinero
# Cada clase debe tener dos atributos:
# Atleta: nombre, deporte
# Cocinero: especialidad, años_experiencia
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase AtletaCocinero que herede de ambas.
"""class Atleta:
    def __init__(self,nombre,deporte) -> None:
        self.nombre = nombre
        self.deporte = deporte
    def correr(self):
        print(f"el atleta {self.nombre} esta corriendo")
    def entrenar(self):
        print(f"el altleta esta entrenando {self.deporte}")
        
class Cocinero:
    def __init__(self, especialidad, años_esperiencia) -> None:
        self.especialidad = especialidad
        self.años_esperiencia = años_esperiencia
    def probar(self):
        print(f"el cocinero prueba su especialidad {self.especialidad}")
    def mostrar(self):
        print(f"el cocinero demuestra sus años {self.años_esperiencia} de experiencia")
        
class AtletaCocinero(Atleta,Cocinero):
    def __init__(self, nombre, deporte, especialidad, años_esperiencia) -> None:
        #inicializo las clases padre
        Atleta.__init__(self, nombre, deporte)      
        Cocinero.__init__(self, especialidad, años_esperiencia)
 
juan = AtletaCocinero("juan david", "atletismo", "cocina colombiana", 8)
juan.correr()     
juan.entrenar()
juan.probar() 
juan.mostrar()"""                            
# 3. Clase Pintor y Escultor → ArtistaVisual
# Cada clase debe tener dos atributos:
# Pintor: estilo, cantidad_obras
# Escultor: material_favorito, exposiciones_realizadas
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase ArtistaVisual que herede de ambas.
"""class Pintor:
    def __init__(self, estilo, cantidad_obras) -> None:
        self.estilo = estilo
        self.cantidad_obras = cantidad_obras
    def estilizar(self):
        print(f"aplicar el estilo:{self.estilo} para estilizar la pintura")
    def contar(self):
        print(f"la canttidad de obras en su carrera son {self.cantidad_obras}")
        
class Escultor:
    def __init__(self, material_favorito, exposiciones_realizadas) -> None:
        self.material_favorito = material_favorito
        self.exposiciones_realizadas = exposiciones_realizadas
    def usar(self):
        print(f"puedes usar tu material favorito : {self.material_favorito}")
    def mostrar(self):
        print(f"el escultor tiene  {self.exposiciones_realizadas} a lo largo de su carrera")
        
class ArtistaVisual(Pintor,Escultor):
    def __init__(self, estilo, cantidad_obras,material_favorito,exposiciones_realizadas) -> None:
        Pintor.__init__(self,estilo, cantidad_obras)  
        Escultor.__init__(self,material_favorito,exposiciones_realizadas)
        
djholmes = ArtistaVisual("clasico", 12, "acrilico", 4)
djholmes.estilizar() 
djholmes.contar()  
djholmes.usar()    
djholmes.mostrar() """                            
# 4. Clase Profesor y Investigador → Cientifico
# Cada clase debe tener dos atributos:
# Profesor: nombre, materia_enseñada
# Investigador: campo_investigacion, publicaciones
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase Cientifico que herede de ambas.
"""class Profesor:
    def __init__(self, nombre, materia_enseñada) -> None:
        self.nombre = nombre
        self.materia_enseñanza = materia_enseñada
    def presentarse(self):
        print(f"hola soy {self.nombre} su nuevo profesor de algoritmia")
    def validar(self):
        print(f"en el dia de hoy validaremos la materia : {self.materia_enseñanza}")
        
class Investigador:
    def __init__(self, campo_investigacion, publicaciones) -> None:
        self.campo_investigacion = campo_investigacion
        self.publicaciones = publicaciones
    def enzeñar(self):
        print(f"las  capacitaciones son de {self.campo_investigacion}")
    def evidenciar(self):
        print(f"evidenciaremos lo aprendido en las {self.publicaciones}")
        
class Cientifico(Profesor, Investigador):
    def __init__(self, nombre, materia_enseñada,campo_investigacion, publicaciones) -> None:
        #inicializo las clases padre
        Profesor.__init__(self, nombre, materia_enseñada)     
        Investigador.__init__(self, campo_investigacion, publicaciones) 
        
    def enzayar(self):
        print(f"el cientifico hace su enzayo en el laboratorio")
        
cientifico1 = Cientifico("Diego","algoritmia","ciencias de la computacion", "3 publicaciones")
cientifico1.presentarse()   
cientifico1.validar()
cientifico1.enzeñar()
cientifico1.evidenciar()   
cientifico1.enzayar() """                           
# 5. Clase Piloto y Capitan → Comandante
# Cada clase debe tener dos atributos:
# Piloto: aerolinea, horas_vuelo
# Capitan: nombre_barco, años_experiencia
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase Comandante que herede de ambas.
"""class Piloto:
    def __init__(self, aerolinea, horas_vuelo) -> None:
        self.aerolinea = aerolinea
        self.horas_vuelo = horas_vuelo
    def planificar(self):
        print(f"el piloto planifica el vuelo  para la aerolinea {self.aerolinea}")
    def comunicar(self):
        print(f"se le comunica la experiencia del piloto con sus {self.horas_vuelo} superiores ")
        
class Capitan:
    def __init__(self, nombre_barco, años_experiencia) -> None:
        self.nombre_barco = nombre_barco
        self.años_experiencia = años_experiencia
    def zarpar(self):
        print(f"el barco {self.nombre_barco} a zarpado de buenaventura")
    def inspecionar(self):                        
        print(f"sus {self.años_experiencia} años de experiencia le permiten inspecionar la nave antes de salir")
        
class Comandante(Piloto, Capitan):
    def  __init__(self, aerolinea, horas_vuelo,  nombre_barco, años_experiencia) -> None:
        #defino las clases padre
        Piloto.__init__(self, aerolinea, horas_vuelo)
        Capitan.__init__(self, nombre_barco, años_experiencia)
        
fidel = Comandante("avianca", "988 horas de vuelo", "perla negra", 24)
fidel.planificar()
fidel.comunicar()
fidel.zarpar()
fidel.inspecionar() """              
# 6. Clase Madre y Padre → Hijo
# Cada clase debe tener dos atributos:
# Madre: nombre, edad
# Padre: nombre, ocupacion
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase Hijo que herede de ambas.
"""class Madre:
    def __init__(self,nombre_madre,edad) -> None:
        self.nombre_madre = nombre_madre
        self.edad = edad
    def cocinar(self):
        print(f"{self.nombre_madre} prepara el almuerzo") 
    def aconcejar (self):
        print(f"a mis {self.edad} me gusta dar concejos a los jovenes")
        
class padre:
    def __init__(self,nombre_padre, ocupacion) -> None:
        self.nombre_padre = nombre_padre
        self.ocupacion = ocupacion
    def animar(self):
        print(f"{self.nombre_padre} anima cada fecha al deportivo cali")
    def laborar(self):
        print(f"el padre labora como {self.ocupacion}")
        
class Hijo(Madre, padre):
    def __init__(self, nombre_madre, edad, nombre_padre, ocupacion) -> None:
        super().__init__(nombre_madre, edad) 
        padre.__init__(self, nombre_padre, ocupacion)             
        
hijo1 = Hijo("maria", 30, "jose", "ebanista")
hijo1.cocinar()
hijo1.aconcejar()
hijo1.animar()
hijo1.laborar()  """                      
# 7. Clase IngenieroCivil y IngenieroIndustrial → IngenieroJefe
# Cada clase debe tener dos atributos:
# IngenieroCivil: nombre, proyectos_completados
# IngenieroIndustrial: nombre_empresa, años_experiencia
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase IngenieroJefe que herede de ambas.
"""class IngenieroCivil:
    def __init__(self,nombre, proyectos_completados) -> None:
        self.nombre = nombre
        self.proyectos_completados = proyectos_completados
    def presentarse(self):
        print(f"soy el ingeniero {self.nombre} y sere el encargado de la obra")
    def informar(self):
        print(f"me permito informar los proyectos que hemos completado {self.proyectos_completados} y entregado") 
        
class ingenieroIndustrial:
    def __init__(self, nombre_empresa, años_experiencia) -> None:
        self.nombre_empresa = nombre_empresa
        self.años_experiencia = años_experiencia
    def optmizar(self):
        print(f"el objetivo es obtimizar la producion en {self.nombre_empresa}")
    def capacitar(self):
        print(f"mis {self.años_experiencia} años de esperiencia me permiten capacitar al personal")
         
class IngenieroJefe(IngenieroCivil,ingenieroIndustrial):
    def __init__(self, nombre, proyectos_completados, nombre_empresa, años_experiencia) -> None:
        super().__init__(nombre, proyectos_completados)                               
        ingenieroIndustrial.__init__(self, nombre_empresa, años_experiencia)
        
jefe_calidad = IngenieroJefe("brayan", "linea avicola", "bucanero", 8)
jefe_producion = IngenieroJefe("juan", "planta de desposte", "cyd", 11)
jefe_calidad.presentarse()  
jefe_producion.presentarse()   
jefe_calidad.informar()
jefe_producion.informar()
jefe_calidad.optmizar()
jefe_producion.optmizar()
jefe_calidad.capacitar()
jefe_producion.capacitar()"""      
# 8. Clase Actor y Director → Cineasta
# Cada clase debe tener dos atributos:
# Actor: nombre, peliculas_actuadas
# Director: peliculas_dirigidas, premios_ganados
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase Cineasta que herede de ambas.
"""class Actor:
    def __init__(self, nombre, peliculas_actuadas) -> None:
        self.nombre = nombre
        self.peliculas_actuadas = peliculas_actuadas
    def firmar(self):
        print(f"{self.nombre} esta firmando autografos")
    def reconocer(self):
        print(f"los oscar reconocen la larga carrera de {self.nombre} y su participacion en {self.peliculas_actuadas}")        
        
class Director:
    def __init__(self,peliculas_dirigidas, premios_ganados) -> None:
        self.peliculas_dirigidas = peliculas_dirigidas
        self.premios_ganados = premios_ganados
    def supervisar(self):
        print(f"ha dirigido {self.peliculas_dirigidas} en lo largo de su carrera")
    def participar(self):
        print(f"una larga participacion le a permitido ganar {self.premios_ganados} premios")
        
class Cineasta(Actor, Director):
    def __init__(self, nombre, peliculas_actuadas, peliculas_dirigidas, premios_ganados) -> None:
        super().__init__(nombre, peliculas_actuadas)
        Director.__init__(self, peliculas_dirigidas, premios_ganados)
        
cineasta_aficionado = Cineasta("esteven", "la sierra, pepe, era una vez en mexico", "balada, alita, anatar", 3) 
cineasta_experto = Cineasta("armando", " el 5 elemento, ronrola", "titanic", 18)
cineasta_aficionado.firmar()
cineasta_experto.firmar()
cineasta_aficionado.reconocer()
cineasta_experto.reconocer() 
cineasta_aficionado.supervisar()
cineasta_experto.supervisar()
cineasta_aficionado.participar()
cineasta_experto.participar()"""                            
# 9. Clase Doctor y Cirujano → DoctorCirujano
# Cada clase debe tener dos atributos:
# Doctor: especialidad, años_experiencia
# Cirujano: cantidad_cirugias, hospital
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase DoctorCirujano que herede de ambas.
"""class Doctor:
    def __init__(self, especialidad, años_esperiencia) -> None:
        self.especialidad = especialidad
        self.años_experiencia = años_esperiencia
    def diagnosticar(self):
        print(f"segun la especialidad {self.especialidad} se le hace un diagnostico")
    def enseñar(self):
        print(f"sus {self.años_experiencia} años de esperiencia le permite compatir sus conocimientos")
      
class Cirujano:
    def __init__(self, cantidad_cirujias, hospital) -> None:
        self.cantidad_cirugias = cantidad_cirujias
        self.hospital = hospital
    def evaluar(self):
        print(f"lo primero es evaluar la cantidad de cirugias previas {self.cantidad_cirugias}") 
    def laborar(self):
        print(f"esta laborando en el hospital {self.hospital}")
        
class DoctorCirujano(Doctor, Cirujano):
    def __init__(self, especialidad, años_esperiencia, cantidad_cirujias, hospital) -> None:
        super().__init__(especialidad, años_esperiencia)  
        Cirujano.__init__(self, cantidad_cirujias, hospital)
        
internista = DoctorCirujano("pediatria", 10, 22, "san juan") 
internista.diagnosticar()
internista.enseñar()   
internista.evaluar()
internista.laborar() 
cirujano_plastico = DoctorCirujano("cirugia plastica", 15, 50, "palma real")
cirujano_plastico.diagnosticar()
cirujano_plastico.enseñar()
cirujano_plastico.evaluar()
cirujano_plastico.laborar()"""                                
# 10. Clase Maratonista y Nadador → Triatleta
# Cada clase debe tener dos atributos:
# Maratonista: record_personal, kilometros_recorridos
# Nadador: estilo_nado, competencias_ganadas
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase Triatleta que herede de ambas.
"""class Maratonista:
    def __init__(self, record_personal, kilometros_recorridos) -> None:
        self.record_personal = record_personal
        self.kilometros_recorridos = kilometros_recorridos
    def fijar(self):
        print(f"se ha fijado un nuevo recor de 60 segundos, superior al anterior de {self.record_personal}segundos")
    def registrar(self):
        print(f"se ha de registrar {self.kilometros_recorridos} km recorridos en la etapa")
        
class Nadador:
    def __init__(self, estilo_nado, competencias_ganadas) -> None:
        self.estilo_nado = estilo_nado
        self.competencias_ganadas = competencias_ganadas
    def optimizar(self):
        print(f"optimizando el estilo {self.estilo_nado} de nado ")    
    def exhibir(self):
        print(f"exhibiendo los titulos de las {self.competencias_ganadas} competencias ganadas ")
        
class Triatleta(Maratonista, Nadador):
    def __init__(self, record_personal, kilometros_recorridos, estilo_nado, competencias_ganadas) -> None:
        super().__init__(record_personal, kilometros_recorridos)
        Nadador.__init__(self, estilo_nado, competencias_ganadas)
        
pastuso = Triatleta(70, 15, "libre", 2)
paisa = Triatleta(74, 18, "mariposa", 5)
pastuso.fijar()
paisa.fijar()
pastuso.registrar()
paisa.registrar()
pastuso.optimizar()
paisa.optimizar()
pastuso.exhibir()
paisa.exhibir()"""        
                                
# 11. Clase DiseñadorGrafico y Fotografo → ArtistaMultimedia
# Cada clase debe tener dos atributos:
# DiseñadorGrafico: software_favorito, años_experiencia
# Fotografo: tipo_fotografia, cantidad_proyectos
# Tarea: Define estas clases con los atributos y métodos indicados, y luego crea la clase ArtistaMultimedia que herede de ambas.
"""class DiseñadorGrafico:
    def __init__(self, software_favorito, años_experiencia) -> None:
        self.software_favorito = software_favorito
        self.años_experiencia = años_experiencia
    def diseñar(self):
        print(f"diseña mejor con  {self.software_favorito} ya que es su software favorito ")  
    def gestionar(self):
        print(f"con sus {self.años_experiencia} años de esperiencia puede gestionar proyectos por cuenta propia")
        
class Fotografo:
    def __init__(self, tipo_fotografia, cantidad_proyectos) -> None:
        self.tipo_fotografia = tipo_fotografia
        self.cantidad_proyectos = cantidad_proyectos
    def editar(self):
        print(f"depende del tipo de fotografia: {self.tipo_fotografia} es necesario editar") 
    def exhibir(self):
        print(f"estos son todos los proyectos relizados {self.cantidad_proyectos}")
        
class ArtistaMultimedia(DiseñadorGrafico, Fotografo):
   def __init__(self, software_favorito, años_experiencia, tipo_fotografia, cantidad_proyectos) -> None:
       super().__init__(software_favorito, años_experiencia)
       Fotografo.__init__(self, tipo_fotografia, cantidad_proyectos)
       
artista1 = ArtistaMultimedia("canva", 15, "surralista", 22)
artista1.diseñar()
artista1.gestionar()
artista1.editar()
artista1.exhibir()
artista2 = ArtistaMultimedia("figma", 2, "publicitaria", 5)
artista2.diseñar()
artista2.gestionar()
artista2.editar()
artista2.exhibir()""" 
 
# herencia multinivel      
# Crea una clase Animal con un método hacer_sonido(), luego una clase Mamifero que herede de Animal, y finalmente una clase Perro que herede de Mamifero.
"""class Animal:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def hacer_sonido(self):
        print(f"haciendo sonido") 
      
class Mamifero(Animal):
    def __init__(self, nombre, edad,tamaño) -> None:
        super().__init__(nombre, edad) 
        self.tamaño = tamaño
        
class Perro(Mamifero):
    def __init__(self, nombre, edad, tamaño) -> None:
        super().__init__(nombre, edad, tamaño)
    def hacer_sonido(self):
        print(f"{self.nombre} esta ladrando")
            
        
bruno = Perro("bruno", 2, "mediano")
bruno.hacer_sonido()                
guardian = Perro("guardian", 7, "pequeño" )
guardian.hacer_sonido("""                 
# Define una clase Vehiculo, luego una clase Automovil que herede de Vehiculo, y luego una clase Taxi que herede de Automovil.
"""class vehiculo:
    def __init__(self, marca) -> None:
        self.marca = marca
    def pitar(self):
        print(f"el {self.marca} esta pitando duro")
        
class Automovil(vehiculo):
    def __init__(self, marca,color) -> None:
        super().__init__(marca)   
        self.color = color
        
class Taxi(Automovil):
    def __init__(self, marca, color, empresa) -> None:
        super().__init__(marca, color) 
        self.empresa = empresa
        
taxi01 = Taxi("hundai", "amarillo", "taxmio")
taxi01.pitar()
taxi0 = Taxi("chevrolet", " rosado", "womntaxi") 
taxi0.pitar() """                      
# Crea una clase Persona, luego una clase Empleado que herede de Persona, y finalmente una clase Gerente que herede de Empleado.
"""class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"mi nombre es {self.nombre} y tengo {self.edad}")
        
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto) -> None:
        super().__init__(nombre, edad)     
        self.puesto = puesto
    def inducir(self):
        print(f"en mi puesto como {self.puesto} me toca inducir a los nuevos") 
        
class Gerente(Empleado):
    def __init__(self, nombre, edad, puesto, departamento) -> None:
        super().__init__(nombre, edad, puesto)  
        self.departamento = departamento
    def gestionar(self):
        print(f"es mi obligacion como jefe de {self.departamento} gestionar con nomina ese tema")
        
jefe = Gerente("juan", 36, "auditor", "recursos humanos")
print(jefe)
jefe.gestionar()
jefe.inducir()
jefe.presentarse()"""                            
# Crea una clase FiguraGeometrica, luego una clase Poligono que herede de FiguraGeometrica, y luego una clase Triangulo que herede de Poligono.
"""class FiguraGeometrica:
    def __init__(self, color) -> None:
        self.color = color
        print(f"el color de la fifura geometrica es {self.color}")
        
class poligono(FiguraGeometrica):
    def __init__(self, color, numero_lados) -> None:
        super().__init__(color)        
        self.numero_lados = numero_lados
        print(f"el poligono tiene {self. numero_lados}")
        
class Triangulo(poligono):
    def __init__(self, color, numero_lados) -> None:
        super().__init__(color, numero_lados)
    
mi_triangulo = Triangulo("verde", 3)"""
                
        
# Define una clase Fruta, luego una clase Citrico que herede de Fruta, y luego una clase Naranja que herede de Citrico.
"""class Fruta:
    def __init__(self, nombre, color) -> None:
        self.nombre = nombre
        self.color = color
    def info(self):
        print(f"la fruta {self.nombre} es de color {self.color}")
        
class Citrico(Fruta):
    def __init__(self, nombre, color, acidez) -> None:
        super().__init__(nombre, color)      
        self.acidez = acidez
    def info(self):
        print(f"la fruta {self.nombre} es de color {self.color} y  con una acicez {self.acidez}")
        
class Naranja(Citrico):
    def __init__(self, nombre, color, acidez) -> None:
        super().__init__(nombre, color, acidez)
    def preparar(self):
        print(f"se esta preparando un jugo de {self.nombre}")
        
jarra_jugo = Naranja("naranja", "amarillo", "10%")
jarra_jugo.info()
jarra_jugo.preparar() """                              
# 2. Clase Electrodomestico, Lavadora y LavadoraAutomatica
# Define una clase Electrodomestico con los atributos:
# marca: marca del electrodoméstico.
# modelo: modelo del electrodoméstico.
# potencia: potencia en watts.
# Método:
# info(): retorna toda la información del electrodoméstico.
# Luego, crea una clase Lavadora que herede de Electrodomestico y agrega el atributo:
# carga: capacidad de carga en kilogramos.
# Métodos:
# Sobrescribe el método info() para incluir la carga.
# lavar(): simula el inicio de un ciclo de lavado.
# Finalmente, crea una clase LavadoraAutomatica que herede de Lavadora y agrega un método:
# programar_lavado(programa): permite programar el ciclo de lavado.
"""class Electrodomestico:
    def __init__(self, marca, modelo, potencia) -> None:
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
    def info(self):
        print(f"marca : {self.marca} modelo : {self.modelo} potencia : {self.potencia}") 
        
class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, potencia, carga) -> None:
        super().__init__(marca, modelo, potencia)    
        self.carga = carga
    def info(self):
        print(f"marca : {self.marca} modelo : {self.modelo} potencia : {self.potencia} capacidad carga : {self.carga}")
    def lavar(self):
        print("la lavadora esta lavando ...") 
        
class LavadoraAutomatica(Lavadora):
    def __init__(self, marca, modelo, potencia, carga) -> None:
        super().__init__(marca, modelo, potencia, carga)
    def programar_lavado(self):
        print("el lavado se programara en horas de la noche")
        
chalenger1 = LavadoraAutomatica("chalenger", "fortw", "1000wattas", "8kilos")
chalenger1.info()      
chalenger1.lavar()
chalenger1.programar_lavado() """                
                   
# 3. Clase Deporte, DeporteDeEquipo y Futbol
# Define una clase Deporte con los atributos:
# nombre: nombre del deporte.
# numero_jugadores: número de jugadores.
# Método:
# info(): retorna toda la información del deporte.
# Luego, crea una clase DeporteDeEquipo que herede de Deporte y agrega el atributo:
# equipo: nombre del equipo.
# Métodos:
# Sobrescribe el método info() para incluir el nombre del equipo.
# Finalmente, crea una clase Futbol que herede de DeporteDeEquipo y agrega un método:
# anotar_gol(jugador): simula la anotación de un gol por un jugador.
"""class Deporte:
    def __init__(self,nombre_deporte, numero_jugadores) -> None:
        self.nombre_deporte = nombre_deporte
        self.numero_jugadores = numero_jugadores
    def info(self):
        print(f"nombre del deporte : {self.nombre_deporte} numero de jugadores : {self.numero_jugadores}")
        
class DeporteDeEquipo(Deporte):
    def __init__(self, nombre_deporte, numero_jugadores, nombre_equipo) -> None:
        super().__init__(nombre_deporte, numero_jugadores)            
        self.nombre_equipo = nombre_deporte
    def info(self):
         print(f"nombre del deporte : {self.nombre_deporte} numero de jugadores : {self.numero_jugadores} nombre del equipo : {self.nombre_equipo}")
         
class Futbol(DeporteDeEquipo):
    def __init__(self, nombre_deporte, numero_jugadores, nombre_equipo, goleador) -> None:
        super().__init__(nombre_deporte, numero_jugadores, nombre_equipo)
        self.goleador = goleador
    def anotar_gol(self):
        print(f"el jugador {self.goleador} ha anota do goool")  
        
deporcali = Futbol("FUTBOL", 11, "deportivo cali", "montero")
deporcali.info()
deporcali.anotar_gol()"""                      
# 4. Clase Empleado, Cajero y CajeroDeBanco
# Define una clase Empleado con los atributos:
# nombre: nombre del empleado.
# id: identificación del empleado.
# salario: salario mensual.
# Método:
# info(): retorna toda la información del empleado.
# Luego, crea una clase Cajero que herede de Empleado y agrega el atributo:
# caja: número de la caja asignada.
# Métodos:
# Sobrescribe el método info() para incluir la información de la caja.
# realizar_transaccion(monto): simula la realización de una transacción.
# Finalmente, crea una clase CajeroDeBanco que herede de Cajero y agrega un método:
# abrir_caja(): simula la apertura de la caja.
"""class Empleado:
    def __init__(self, nombre, id) -> None:
        self.nombre = nombre
        self.id = id
    def info(self):
        print(f"nombre del empleado : {self.nombre} id . {self.id}")
        
class Cajero(Empleado):
    def __init__(self, nombre, id, n_caja) -> None:
        super().__init__(nombre, id) 
        self.n_caja = n_caja
    def info(self):
        print(f"nombre del empleado : {self.nombre} id : {self.id} caja numero : {self.n_caja}")
    def realizar_transacion(self):
        print("realizando una transacion ")
        
class CajeroBanco(Cajero):
    def __init__(self, nombre, id, n_caja) -> None:
        super().__init__(nombre, id, n_caja)
    def abrir_caja(self):
        print(f"{self.nombre} abriendo la caja {self.n_caja}")
 
cajero_nuevo = CajeroBanco("juan", "1524", 10)
cajero_nuevo.info()
cajero_nuevo.abrir_caja() """                   
                           
# 5. Clase Planta, Flor y Rosa
# Define una clase Planta con los atributos:
# nombre: nombre de la planta.
# tipo: tipo de planta (perenne, anual, etc.).
# Método:
# info(): retorna toda la información de la planta.
# Luego, crea una clase Flor que herede de Planta y agrega el atributo:
# color: color de la flor.
# Métodos:
# Sobrescribe el método info() para incluir el color de la flor.
# Finalmente, crea una clase Rosa que herede de Flor y agrega un método:
# fragancia(): describe la fragancia de la rosa.
"""
class Planta:
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def info(self):
        print(f"nombre de la planta {self.nombre} tipo : {self.tipo}")
  
class Flor(Planta):
    def __init__(self, nombre, tipo, color) -> None:
        super().__init__(nombre, tipo)    
        self.color = color
    def info(self):       
        print(f"nombre de la planta {self.nombre} tipo : {self.tipo} color {self.color}")

class Rosa(Flor):
    def __init__(self, nombre, tipo, color) -> None:
        super().__init__(nombre, tipo, color)
    def fragancia(self):
        print("fragancia floral")
            
mi_rosa = Rosa("rosa", "arbusto", "rojo")
mi_rosa.info()
mi_rosa.fragancia()"""        
# 6. Clase Instrumento, InstrumentoDeCuerda y Violin                   
# Define una clase Instrumento con los atributos:
# nombre: nombre del instrumento.
# tipo: tipo de instrumento (cuerda, viento, percusión, etc.).
# Método:
# info(): retorna toda la información del instrumento.
# Luego, crea una clase InstrumentoDeCuerda que herede de Instrumento y agrega el atributo:
# numero_cuerdas: número de cuerdas del instrumento.
# Métodos:
# Sobrescribe el método info() para incluir el número de cuerdas.
# Finalmente, crea una clase Violin que herede de InstrumentoDeCuerda y agrega un método:
# tocar(): simula tocar el violín.
"""class Instrumento:
    def __init__(self, nombre,tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def info(self):
        print(f"el nombre de instrumento es : {self.nombre} y es de tipo : {self.tipo}")
        
class InstrumentoDeCuerda(Instrumento):
    def __init__(self, nombre, tipo, n_cuerdas) -> None:
        super().__init__(nombre, tipo)
        self.n_cuerdas =  n_cuerdas
    def info(self):
        print(f"el nombre de instrumento es : {self.nombre} y es de tipo : {self.tipo} cantidad decuerdas : {self.n_cuerdas}") 
        
class Violin(InstrumentoDeCuerda):
    def __init__(self, nombre, tipo, n_cuerdas) -> None:
        super().__init__(nombre, tipo, n_cuerdas)
    def tocar(self):
        print(f"tocando el {self.nombre}")
                       
mi_violin = Violin("violin", "cuerda", 5)
mi_violin.info()        
mi_violin.tocar() """               
            

# Define una clase Electrodomestico con los atributos:
# marca: marca del electrodoméstico.
# modelo: modelo del electrodoméstico.
# potencia: potencia en watts.
# Método:
# info(): retorna toda la información del electrodoméstico.
# Luego, crea una clase Microondas que herede de Electrodomestico y agrega el atributo:
# capacidad: capacidad en litros.
# Métodos:
# Sobrescribe el método info() para incluir la capacidad.
# calentar(tiempo): simula el calentamiento de un alimento.
# Finalmente, crea una clase MicroondasInteligente que herede de Microondas y agrega un método:
# programar(tiempo, potencia): permite programar el tiempo y potencia para calentar.
"""class Electrodomesticos:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def info(self):
        print(f"marca : {self.marca} modelo : {self.modelo}")  
    
class Microndas(Electrodomesticos):
    def __init__(self, marca, modelo, capacidad, tiempo) -> None:
        super().__init__(marca, modelo) 
        self.capacidad = capacidad  
        self.tiempo = tiempo
    def info(self):
        print(f"marca : {self.marca} modelo : {self.modelo} capacidad : {self.capacidad} ")
    def calentar(self):
        print(f"el micro ondas esta calentando durante {self.tiempo}")
        
class MicrondasInteligente(Microndas):
    def __init__(self, marca, modelo, capacidad, tiempo,temperatura) -> None:
        super().__init__(marca, modelo, capacidad, tiempo)
        self.temperatura = temperatura
    def programar(self):
        print(f"el microondas inteligente esta programado a {self.tiempo}para hacer la cena a {self.temperatura}") 
       
mi_microondas = MicrondasInteligente("hacer", "nova", "2lts", "20 minutos", "100 grados centigrados ") 
mi_microondas.info()
mi_microondas.calentar()       
mi_microondas.programar()  """        
                            
# 8. Clase DispositivoMovil, Smartphone y iPhone
# Define una clase DispositivoMovil con los atributos:
# marca: marca del dispositivo.
# modelo: modelo del dispositivo.
# sistema_operativo: sistema operativo del dispositivo.
# Método:
# info(): retorna toda la información del dispositivo.
# Luego, crea una clase Smartphone que herede de DispositivoMovil y agrega el atributo:
# camara: resolución de la cámara.
# Métodos:
# Sobrescribe el método info() para incluir la resolución de la cámara.
# Finalmente, crea una clase iPhone que herede de Smartphone y agrega un método:
# actualizar(): simula la actualización del sistema operativo.
"""class DispositiviMovil:
    def __init__(self, marca, modelo, sistema_operativo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
    def info(self):
        print(f"marca : {self.marca} modelo : {self.modelo} sistema operativo : {self.sistema_operativo}") 
        
class Smartphone(DispositiviMovil):
    def __init__(self, marca, modelo, sistema_operativo, camara) -> None:
        super().__init__(marca, modelo, sistema_operativo)           
        self.camara = camara 
    def info(self):
        print(f"marca : {self.marca} modelo : {self.modelo} sistema operativo : {self.sistema_operativo} camara : {self.camara} pxs")
            
class Iphone(Smartphone):
    def __init__(self, marca, modelo, sistema_operativo, camara) -> None:
        super().__init__(marca, modelo, sistema_operativo, camara)
    def actualizar(self):
        print(f"actualizando el iphone {self.modelo}")
        
mi_iphone = Iphone("apple", "s15", "os", 80)
mi_iphone.info()
mi_iphone.actualizar()   
iphone6 = Iphone("apple", "s6", "so", 90)
iphone6.info()
iphone6.actualizar()"""         
# 9. Clase Herramienta, HerramientaElectrica y Taladro
# Define una clase Herramienta con los atributos:
# nombre: nombre de la herramienta.
# tipo: tipo de herramienta (manual, eléctrica).
# Método:
# info(): retorna toda la información de la herramienta.
# Luego, crea una clase HerramientaElectrica que herede de Herramienta y agrega el atributo:
# potencia: potencia en watts.
# Métodos:
# Sobrescribe el método info() para incluir la potencia.
# Finalmente, crea una clase Taladro que herede de HerramientaElectrica y agrega un método:
# perforar(): simula el proceso de perforar.
"""
class Herramienta:
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def info(self):
        print(f"nombre : {self.nombre} tipo : {self.tipo}")
       
class HerramientaHelectrica(Herramienta):
    def __init__(self, nombre, tipo, potencia) -> None:
        super().__init__(nombre, tipo)
        self.potencia = potencia
    def info(self):
        print(f"nombre : {self.nombre} tipo : {self.tipo} potencia : {self.potencia}")
        
class Taladro(HerramientaHelectrica):
    def __init__(self, nombre, tipo, potencia) -> None:
        super().__init__(nombre, tipo, potencia)
    def perforar(self):
        print("el taladro esta perforando ....")                   
                 
mi_taladro = Taladro("taladro", "electrico", "1000 watts")
mi_taladro.info()
mi_taladro.perforar()"""                 
# 10. Clase Transportes, Maritimo y Submarino        
# Define una clase Transportes con los atributos:
# tipo: tipo de transporte (aéreo, terrestre, marítimo).
# capacidad: capacidad de pasajeros.
# Método:
# info(): retorna toda la información del transporte.
# Luego, crea una clase Maritimo que herede de Transportes y agrega el atributo:
# tipo_barco: tipo de barco (yate, barco de carga).
# Métodos:
# Sobrescribe el método info() para incluir el tipo de barco.
# Finalmente, crea una clase Submarino que herede de Maritimo y agrega un método:
# sumergir(): simula la acción de sumergir el submarino.
"""class Transportes:
    def __init__(self, tipo, capacidad) -> None:
        self.tipo = tipo
        self.capacidad = capacidad
    def info(self):
        print(f"tipo de transporte : {self.tipo} capacidad de pasajeros : {self.capacidad}")
        
class Maritimo(Transportes):
    def __init__(self, tipo, capacidad, tipo_barco) -> None:
        super().__init__(tipo, capacidad)         
        self.tipo_barco = tipo_barco
    def info(self):
        print(f"tipo de transporte : {self.tipo} capacidad de pasajeros : {self.capacidad} tipo de barco : {self.tipo_barco}")
        
class Submarino(Maritimo):
    def __init__(self, tipo, capacidad, tipo_barco) -> None:
        super().__init__(tipo, capacidad, tipo_barco)
    def sumergir(self):
        print(f"el submarino se esta sumergiendo ")
        
poseidon = Submarino("maririmo", 15, "yate")
poseidon.info() 
poseidon.sumergir()  

mi_yate = Maritimo("maritimo", 10, "yate")
mi_yate.info()"""                     
           
# 11. Clase Bebida, BebidaAlcoholica y Vino
# Define una clase Bebida con los atributos:
# nombre: nombre de la bebida.
# tipo: tipo de bebida (alcohólica, no alcohólica).
# Método:
# info(): retorna toda la información de la bebida.
# Luego, crea una clase BebidaAlcoholica que herede de Bebida y agrega el atributo:
# graduacion: grado de alcohol en porcentaje.
# Métodos:
# Sobrescribe el método info() para incluir la graduación.
# Finalmente, crea una clase Vino que herede de BebidaAlcoholica y agrega un método:
# maridaje(): sugiere alimentos que combinan bien con el vino.
"""class Bebida:
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def info(self):
        print(f"nombre de la bebida : {self.nombre} tipo de bebida : {self.tipo}")
        
class BebidaAlcoholica(Bebida):
    def __init__(self, nombre, tipo, graduacion) -> None:
        super().__init__(nombre, tipo)         
        self.graduacion = graduacion
    def info(self):
        print(f"nombre de la bebida : {self.nombre} tipo de bebida : {self.tipo} graduacion : {self.graduacion}")
        
class Vino(BebidaAlcoholica):
    def __init__(self, nombre, tipo, graduacion) -> None:
        super().__init__(nombre, tipo, graduacion)
    def meridaje(self):
        print(f"es un vino para acopañar las carnes")
        
cariñoso = Vino("cariñoso de manzana", "alcoholica", " 10 grados de alcohol ")
cariñoso.info()
cariñoso.meridaje()"""                           
# 12. Clase Mascota, Perro y Labrador
# Define una clase Mascota con los atributos:
# nombre: nombre de la mascota.
# tipo: tipo de mascota (perro, gato, ave).
# Método:
# info(): retorna toda la información de la mascota.
# Luego, crea una clase Perro que herede de Mascota y agrega el atributo:
# raza: raza del perro.
# Métodos:
# Sobrescribe el método info() para incluir la raza.
# Finalmente, crea una clase Labrador que herede de Perro y agrega un método:
# ladrar(): simula el ladrido del labrador.
"""class Mascota:
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def info(self):
        print(f"nombre de la mascota: {self.nombre} tipo : {self.tipo}")
        
class Perro(Mascota):
    def __init__(self, nombre, tipo, raza) -> None:
        super().__init__(nombre, tipo)   
        self.raza = raza
        
class Labrador(Perro):
    def __init__(self, nombre, tipo, raza) -> None:
        super().__init__(nombre, tipo, raza)
    def ladrar(self):
        print(f"esta ladrando {self.nombre} el {self.raza} ....")
        
bruno = Perro("bruno", "perro", "labrador")
bruno.info()
tony = Labrador("tony", "perro", "labrador")                             
tony.info()
tony.ladrar()"""
# 13. Clase Coche, CocheDeportivo y Ferrari
# Define una clase Coche con los atributos:
# marca: marca del coche.
# modelo: modelo del coche.
# anio: año de fabricación.
# Método:
# info(): retorna toda la información del coche.
# Luego, crea una clase CocheDeportivo que herede de Coche y agrega el atributo:
# velocidad_maxima: velocidad máxima en km/h.
# Métodos:
# Sobrescribe el método info() para incluir la velocidad máxima.
# Finalmente, crea una clase Ferrari que herede de CocheDeportivo y agrega un método:
# acelerar(): simula la aceleración del Ferrari.
"""class Coche:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def info(self):
        print(f"marca del coceh : {self.marca} modelo : {self.modelo}")
        
class CocheDeportivo(Coche):
    def __init__(self, marca, modelo, velocidad_maxima) -> None:
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima
    def info(self):
        print(f"marca del coche : {self.marca} modelo : {self.modelo} velocidad_maxima = {self.velocidad_maxima}")
        
class Ferrari(CocheDeportivo):
    def __init__(self, marca, modelo, velocidad_maxima) -> None:
        super().__init__(marca, modelo, velocidad_maxima)
    def acelerar(self):
        print(f"acelerando mi {self.marca} {self.modelo} run run ....")
        
enzo = Ferrari("ferrari enzo ", 2022, "220 k/h")
enzo.info()
enzo.acelerar()
diablo = Ferrari("ferrari diablo", 2023, "240 k/m") 
diablo.info()
diablo.acelerar()"""                   
                
# 14. Clase Animal, Mamifero y Gato
# Define una clase Animal con los atributos
# nombre: nombre del animal.
# especie: especie del animal.
# Método:
# info(): retorna toda la información del animal.
# Luego, crea una clase Mamifero que herede de Animal y agrega el atributo:
# lactancia: duración de la lactancia en meses.
# Métodos:
# Sobrescribe el método info() para incluir la duración de la lactancia.
# Finalmente, crea una clase Gato que herede de Mamifero y agrega un método:
# maullar(): simula el maullido del gato.
"""class Animal:
    def __init__(self, nombre, especie) -> None:
        self.nombre = nombre
        self.especie = especie
    def info(self):
        print(f"marca : {self.nombre} especie : {self.especie}")  
        
class Mamifero(Animal):
    def __init__(self, nombre, especie, lactancia) -> None:
        super().__init__(nombre, especie)        
        self.lactancia = lactancia
    def info(self):
        print(f"nombre : {self.nombre} - especie : {self.especie} - tiempo de lactancia : {self.lactancia}")

class Gato(Mamifero):
    def __init__(self, nombre, especie, lactancia) -> None:
        super().__init__(nombre, especie, lactancia)
    def maullar(self):
        print(f"el {self.nombre} esta maullando")
        
miss = Gato("miss", "gato", "2 meses", )
miss.info()
miss.maullar()
mono = Gato("mono", "gato", "2 meses")
mono.info()
mono.maullar()"""                      
# 15. Clase Personaje, SuperHeroe y SpiderMan
# Define una clase Personaje con los atributos:
# nombre: nombre del personaje.
# universo: universo de ficción del personaje.
# Método:
# info(): retorna toda la información del personaje.
# Luego, crea una clase SuperHeroe que herede de Personaje y agrega el atributo:
# poder: poder especial del superhéroe.
# Métodos:
# Sobrescribe el método info() para incluir el poder especial.
# Finalmente, crea una clase SpiderMan que herede de SuperHeroe y agrega un método:
# trepar_paredes(): simula la habilidad de trepar paredes.
"""class Personaje:
    def __init__(self, nombre, universo) -> None:
        self.nombre = nombre
        self.universo = universo
    def info(self):
        print(f"nombre del personaje : {self.nombre} - univero = {self. universo}")
        
class SuperHeroe(Personaje):
    def __init__(self, nombre, universo, poder) -> None:
        super().__init__(nombre, universo)            
        self.poder = poder
    def info(self):
        print(f"nombre del personaje : {self.nombre} - univero = {self. universo} - poder : {self.poder}")

class Spiderman(SuperHeroe):
    def __init__(self, nombre, universo, poder) -> None:
        super().__init__(nombre, universo, poder)
    def trepar_paredes(self):
        print(f"{self.nombre} esta trepandop paredes")
peter = Spiderman("spiderman", "marvel", "tirar telaraña")  
peter.info()
peter.trepar_paredes() """       
# Ejercicios de Herencia Jerárquica
#1. Vehículo, Motocicleta, y Camión
# Define una clase Vehículo con los atributos marca y modelo, y un método para encender el vehículo.
# Crea una clase Motocicleta que herede de Vehículo y agregue el atributo cilindrada y un método para hacer un caballito.
# Crea una clase Camión que herede de Vehículo, agregue el atributo capacidad_de_carga, y un método para descargar mercancía.
"""class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def encender(self):
        print(f"encendiendo vehiculo")
        
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilidrada) -> None:
        super().__init__(marca, modelo)        
        self.cilindrada = cilidrada
    def hacer_stund(self):
        print(f"estoy haciendo estun en mi {self.marca} {self.cilindrada}")   
        
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga) -> None:
        super().__init__(marca, modelo)             
        self.capacidad_carga = capacidad_carga
    def descargar_mercancia(self):
        print(f"descargando mercancia")
        
mi_moto = Motocicleta("yamaha", 2020, 250)
mi_moto.encender()
mi_moto.hacer_stund()

mi_camion = Camion("hini", 2020, "8 toneladas")
mi_camion.encender()
mi_camion.descargar_mercancia()"""            
        
# 2. Persona, Estudiante, y Profesor
# Define una clase Persona con los atributos nombre y edad, y un método para presentarse.
# Crea una clase Estudiante que herede de Persona, agregue el atributo carrera, y un método para estudiar.
# Crea una clase Profesor que herede de Persona, agregue el atributo materia, y un método para enseñar.
"""class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"hola mi nombre es {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera) -> None:
        super().__init__(nombre, edad)      
        self.carrera = carrera
    def estudiar(self):
        print(f"{self.nombre} esta estudiando {self.carrera}")          

class Profesor(Persona):
    def __init__(self, nombre, edad, materia) -> None:
        super().__init__(nombre, edad)
        self.materia = materia
    def enseñar(self):
        print(f"{self.nombre} esta enseñando {self.materia}")
        
diego = Estudiante("DIEGO", 36, "desarrollo de software")
diego.presentarse()
diego.estudiar()
guido = Profesor("guido", 54, "fisica")
guido.presentarse()
guido.enseñar()   """         
        
# 3. Electrodoméstico, Lavadora, y Refrigerador
# Define una clase Electrodoméstico con los atributos marca y modelo, y un método para encender el aparato.
# Crea una clase Lavadora que herede de Electrodoméstico, agregue el atributo capacidad, y un método para lavar ropa.
# Crea una clase Refrigerador que herede de Electrodoméstico, agregue el atributo capacidad_en_litros, y un método para enfriar alimentos.
"""class Electrodomestico:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def encender(self):
        print(f"encendido")
        
class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, capacidad_litros) -> None:
        super().__init__(marca, modelo)        
        self.capacidad_litros = capacidad_litros
    def lavar_ropa(self):
        print(f"lavando ropa")
        
class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, capacidad_kilos) -> None:
        super().__init__(marca, modelo)
        self.capacidad_kilos = capacidad_kilos
    def enfriar(self):
        print(f"enfriando alimentos")    
        
mi_lavadora = Lavadora("haceb", "nofroster", 10)
mi_lavadora.encender()
mi_lavadora.lavar_ropa()

mi_nevera = Refrigerador("ibg", "2 en 1", "8 kilos")                        
mi_nevera.encender()
mi_nevera.enfriar()"""
# 4. Animal, Pez, y Ave
# Define una clase Animal con los atributos especie y edad, y un método para moverse.
# Crea una clase Pez que herede de Animal, agregue el atributo tipo_de_agua, y un método para nadar.
# Crea una clase Ave que herede de Animal, agregue el atributo tipo_de_plumas, y un método para volar.
"""class Animal:
    def __init__(self, especie, edad) -> None:
        self.espeacie = especie
        self.edad = edad
    def Moverse(self):
        print(f"moviendose...")
        
class Pez(Animal):
    def __init__(self, especie, edad, tipo_agua) -> None:
        super().__init__(especie, edad)        
        self.tipo_agua = tipo_agua
    def nadar(self):
        print(f"nadando ...  ")
        
class Ave(Animal):
    def __init__(self, especie, edad, tipo_plumas) -> None:
        super().__init__(especie, edad)    
        self.tipo_plumas = tipo_plumas
    def volar(self):
        print(f"volando ...") 
       
nemo = Pez("bocachico", "5 años", "acuatico")
nemo.Moverse()
nemo.nadar()
mi_ave = Ave("flamingo", "12 meses", "cortas")
mi_ave.Moverse()
mi_ave.volar()"""                       
# 5. Figura Geométrica, Cuadrado, y Círculo
# Define una clase FiguraGeometrica con un método para calcular el área (sin implementación).
# Crea una clase Cuadrado que herede de FiguraGeometrica, agregue el atributo lado, y un método para calcular el área.
# Crea una clase Círculo que herede de FiguraGeometrica, agregue el atributo radio, y un método para calcular el área.
"""class FiguraGeometrica:
    def calcular_area():
        pass
    
class Cuadrado (FiguraGeometrica):
    def __init__(self, lado) -> None:
        super().__init__() 
        self.lado = lado
    def calcular_area(self):
        area = self.lado * self.lado
        return area
    
class Circulo(FiguraGeometrica):
    def __init__(self, radio) -> None:
        super().__init__()  
        self.radio = radio 
    def calcular_area(self):
        area = 3.1416 * (self.radio ** 2)
        return area
    
mi_cuadrado = Cuadrado(12)
area_cuadrado = mi_cuadrado.calcular_area()
print(area_cuadrado)    
mi_circulo = Circulo(8)
area_circulo = mi_circulo.calcular_area()
print(area_circulo)"""        
# 6. Instrumento, Guitarra, y Piano
# Define una clase Instrumento con los atributos nombre y tipo, y un método para tocar.
# Crea una clase Guitarra que herede de Instrumento, agregue el atributo numero_de_cuerdas, y un método para afinar.
# Crea una clase Piano que herede de Instrumento, agregue el atributo tipo_de_piano, y un método para ajustar las teclas.
"""class Instrumento: 
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo 
    def tocar(self):
        print(f"tocando {self.nombre}")
        
class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, numero_cuerdas) -> None:
        super().__init__(nombre, tipo)
        self.numero_cuerdas = numero_cuerdas
    def afinar(self):
        print(f"afinando la {self.nombre} ")
        
class Piano(Instrumento):
    def __init__(self, nombre, tipo, tipo_piano) -> None:
        super().__init__(nombre, tipo)         
        self.tipo_piano = tipo_piano
    def ajustar_teclas(self):
        print(f"ajustando el {self.nombre}")
        
mi_guitarra = Guitarra("guitarra", "electrica", 5)
mi_guitarra.tocar()
mi_guitarra.afinar()
mi_piano = Piano("piano", "organo", "moderno")
mi_piano.tocar()
mi_piano.ajustar_teclas()"""
               
                
# 7. Dispositivo Móvil, Tablet, y Smartphone
# Define una clase DispositivoMovil con los atributos marca y modelo, y un método para encender.
# Crea una clase Tablet que herede de DispositivoMovil, agregue el atributo tamaño_de_pantalla, y un método para navegar por Internet.
# Crea una clase Smartphone que herede de DispositivoMovil, agregue el atributo numero_de_camaras, y un método para hacer una llamada.
"""class DispositivoMovil:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo 
    def encender(self):
        print(f"encendido ...")
        
class Tablet(DispositivoMovil):
    def __init__(self, marca, modelo, tamaño_pantalla) -> None:
        super().__init__(marca, modelo)            
        self.tamaño_pantalla = tamaño_pantalla
    def navegar(self):
        print(f"navegando por internet en mi {self.marca} {self.modelo}.. ")   
        
class Smartphone(DispositivoMovil):
    def __init__(self, marca, modelo, camaras) -> None:
        super().__init__(marca, modelo)      
        self.camaras = camaras
    def llamar(self):
        print(f"llamndo desde un {self.marca}, modelo {self.modelo}")   
        
mi_tablet = Tablet("huaei", "se11", 11)
mi_tablet.encender()
mi_tablet.navegar()    

mi_celular = Smartphone("apple", "s15", 5)
mi_celular.encender()
mi_celular.llamar() """       
# 8. Fruta, Manzana, y Banana
# Define una clase Fruta con los atributos nombre y color, y un método para describir la fruta.
# Crea una clase Manzana que herede de Fruta, agregue el atributo tipo_de_manzana, y un método para pelar.
# Crea una clase Banana que herede de Fruta, agregue el atributo madurez, y un método para cortar.
class Fruta:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    def describir(self):
        print(f"la : {self.nombre} es de color : {self.color}")
        
class Manzana(Fruta):
    def __init__(self, nombre, color, tipo_de_manzana):
        super().__init__(nombre, color)
        self.tipo_de_manzana = tipo_de_manzana
    def pelar(self):
        print(f"pelando la {self.nombre} ...") 
        
class Banana(Fruta):
    def __init__(self, nombre, color, madurez):
        super().__init__(nombre, color)
        self.madurez = madurez
    def cortar(self):
        print(f"cortando el {self.nombre}")
mi_manzana = Manzana("manzana", "verde", "chilena")
mi_manzana.describir()   
mi_manzana.pelar()
mi_babano = Banana("banano", "amarillo", "muy maduro")
mi_babano.describir()
mi_babano.cortar()                    
                        
# 9. Deporte, Baloncesto, y Voleibol
# Define una clase Deporte con los atributos nombre y numero_de_jugadores, y un método para comenzar el juego.
# Crea una clase Baloncesto que herede de Deporte, agregue el atributo altura_de_la_canasta, y un método para lanzar la pelota.
# Crea una clase Voleibol que herede de Deporte, agregue el atributo altura_de_la_red, y un método para servir.

# 10. Empleado, Ingeniero, y Administrador
# Define una clase Empleado con los atributos nombre y salario, y un método para trabajar.
# Crea una clase Ingeniero que herede de Empleado, agregue el atributo especialidad, y un método para desarrollar un proyecto.
# Crea una clase Administrador que herede de Empleado, agregue el atributo departamento, y un método para gestionar el personal.

# 11. Transportes, Auto, y Avión
# Define una clase Transportes con los atributos tipo y capacidad, y un método para mover el transporte.
# Crea una clase Auto que herede de Transportes, agregue el atributo numero_de_puertas, y un método para arrancar el motor.
# Crea una clase Avión que herede de Transportes, agregue el atributo tipo_de_motor, y un método para despegar.

# 12. Planta, Árbol, y Flor
# Define una clase Planta con los atributos nombre y tamaño, y un método para crecer.
# Crea una clase Árbol que herede de Planta, agregue el atributo tipo_de_hoja, y un método para dar sombra.
# Crea una clase Flor que herede de Planta, agregue el atributo color_de_petalos, y un método para florecer.

# 13. Herramienta, Martillo, y Destornillador
# Define una clase Herramienta con los atributos nombre y material, y un método para utilizar.
# Crea una clase Martillo que herede de Herramienta, agregue el atributo peso, y un método para clavar clavos.
# Crea una clase Destornillador que herede de Herramienta, agregue el atributo tipo_de_punta, y un método para ajustar tornillos.

# 14. Electrodoméstico, Secadora, y Licuadora
# Define una clase Electrodoméstico con los atributos marca y modelo, y un método para encender.
# Crea una clase Secadora que herede de Electrodoméstico, agregue el atributo capacidad, y un método para secar ropa.
# Crea una clase Licuadora que herede de Electrodoméstico, agregue el atributo potencia, y un método para licuar alimentos.

# 15. Vehículo, Tren, y Barco
# Define una clase Vehículo con los atributos marca y modelo, y un método para moverse.
# Crea una clase Tren que herede de Vehículo, agregue el atributo tipo_de_vía, y un método para transportar pasajeros.
# Crea una clase Barco que herede de Vehículo, agregue el atributo capacidad_de_carga, y un método para navegar.