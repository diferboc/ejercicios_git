# Ejercicios de polimorfismo en tiempo de ejecución (sobreescritura de métodos):
# Crea una clase Animal con el atributo nombre. Luego, crea clases Perro y Gato que sobrescriban el método sonido(), el cual devuelve el sonido que hace cada animal.
"""class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    def sonido(self):
        print("haciendo sonido )))")
 
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def sonido(self):
        return f"{self.nombre} esta ladrando )))))"
        
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def sonido(self):
        return f"{self.nombre} esta mauyando )))"
        
bruno = Perro("bruno")
mono = Gato("mono")
perro_ladrando = bruno.sonido()
gato_mauyando = mono.sonido() 
print(perro_ladrando)
print(gato_mauyando)"""                                   
# Crea una clase Vehiculo con el atributo velocidad_maxima. Luego, crea las clases Coche y Moto que sobrescriban el método tipo(), devolviendo el tipo de vehículo correspondiente.
"""class Vehiculo:
    def __init__(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima
    def tipo_de_vehiculo(self):
        return f"es un vehiculo"
    
class Coche(Vehiculo):
    def __init__(self, velocidad_maxima):
        super().__init__(velocidad_maxima)
    def tipo_de_vehiculo(self):
        return f"es un vehiculo tipo coche"
        
class Moto(Vehiculo):
    def __init__(self, velocidad_maxima):
        super().__init__(velocidad_maxima)
       
    def tipo_de_vehiculo(self):
        return f"es un vehiculo tipo moto" 
        
renault_4 = Coche("120 k/h")
tipo_es = renault_4.tipo_de_vehiculo()
velocidad_max_coche = renault_4.velocidad_maxima
print(velocidad_max_coche)
print(tipo_es)
nkd = Moto("150 k/h")
tipo = nkd.tipo_de_vehiculo()
print(tipo)
print(nkd.velocidad_maxima)"""
                           
# Crea una clase Empleado con el atributo nombre. Luego, crea las clases Ingeniero y Doctor que sobrescriban el método salario(), devolviendo el salario según la profesión.
"""class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def salario(self):
        return(f"el empleado {self.nombre} tiene un salario de 1500.000")
    
class Ingeniero(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
    def salario(self):
        return (f"el ingeniero {self.nombre} tiene un salario de 2500.000") 
   
class Doctor(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
    def salario(self):
        return (f"el doctor {self.nombre} tiene un salario de 5000.000")     
                   
carlos_emp = Empleado("carlos")
ver_salario_emp = carlos_emp.salario()
print(ver_salario_emp)                   
andrey_ing = Ingeniero("andrey")
ver_salario = andrey_ing.salario()
print(ver_salario)
juan_doc = Doctor("juan")
ver_salario_doc = juan_doc.salario()
print(ver_salario_doc)  """                 
       
# Crea una clase Instrumento con el atributo nombre. Luego, crea las clases Guitarra y Piano que sobrescriban el método tocar(), devolviendo cómo se toca el instrumento.
"""class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
    def tocar(self):
        print(f"tocando el {self.nombre}")
        
class Guitarra(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre) 
    def tocar(self):
        return f"tocando la {self.nombre} cuerda a cuerda..."
        
class Piano(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)
    def tocar(self):
        return f"tocando el {self.nombre} tecla a tecla..."
        
mi_guitarra = Guitarra("guitarra electrica")
tocando_guitarra = mi_guitarra.tocar()
print(tocando_guitarra) 
mi_piano = Piano("piano")
tocando_piano = mi_piano.tocar()
print(tocando_piano) """                                 
# Crea una clase Figura con el atributo color. Luego, crea las clases Rectangulo y Circulo que sobrescriban el método area(), calculando el área de cada figura.
"""class Figura:
    def __init__(self, color):
        self.color = color
    def area(self):
        raise
class Rectangulo(Figura):
    def __init__(self, color,base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura    
    def area(self):
        area = self.base * self.altura
        return area            
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)    
        self.radio = radio
    def area(self):
        area = 3.1416 * (self.radio ** 2)
        return area
mi_rectangulo = Rectangulo("verde", 20, 10)
area_rec = mi_rectangulo.area()
print(area_rec)     
mi_circulo = Circulo("azul", 18)
area_cir = mi_circulo.area()
print(area_cir) """  
# Crea una clase Juego con el atributo nombre. Luego, crea las clases Futbol y Baloncesto que sobrescriban el método reglas(), explicando las reglas básicas de cada deporte.
"""class Juego:
    def __init__(self,nombre):
        self.nombre = nombre
    def reglas(self):
        raise
class Futbol(Juego):
    def __init__(self, nombre):
        super().__init__(nombre)  
    def reglas(self):
        return f"45 minutos cada tiempo de 11 jugadores cada equipo" 
class Baloncesto(Juego):
    def __init__(self, nombre):
        super().__init__(nombre)
    def reglas(self):
        return f"30 minutos cada tiempo de 5 jugadores cada equipo"   
    
deporte_favorito = Futbol("futbol")
reglas_fut = deporte_favorito.reglas()
print(reglas_fut)
deporte_americano = Baloncesto("baloncesto")
reglas_bal = deporte_americano.reglas()
print(reglas_bal)"""                  
# Crea una clase Comida con el atributo ingredientes. Luego, crea las clases Pizza y Helado que sobrescriban el método preparar(), explicando cómo se prepara cada comida.
"""class Comida:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    def preparar(self):
        raise
    
class Pizza(Comida):
    def __init__(self, ingredientes):
        super().__init__(ingredientes)
    def preparar(self):
        return f"amasar hasta hallar contextura de lamasa y agregar tomate salsas y salami"
    
class Helado(Comida):
    def __init__(self, ingredientes):
        super().__init__(ingredientes)
    def preparar(self):
        return f"licuar con mucha fruta agregar al molde y meter a congelacion por 12 horas"
    
pizza_hut = Pizza("harina, huevos, tomate, salami")
prparar_p = pizza_hut.preparar()
print(prparar_p)
ventonini = Helado("fruta, leche")
prepara_h = ventonini.preparar()
print(prepara_h) """                       
    
# Crea una clase Transporte con el atributo capacidad. Luego, crea las clases Bus y Bicicleta que sobrescriban el método descripcion(), explicando las capacidades y usos de cada transporte.
"""class Transporte:
    def __init__(self, capacidad):
        self.capacidad = capacidad
    def descripcion(self):
        raise
        
class Bus(Transporte):
    def __init__(self, capacidad):
        super().__init__(capacidad)
    def descripcion(self):
        capacidades = "para movilizar 42 personas"
        usos = "se usa en todo el mundo para transporte masivo"
        return capacidades, usos
class Bicicleta(Transporte):
    def __init__(self, capacidad):
        super().__init__(capacidad)
    def descripcion(self):
        capacidades = "sin combustible para 2 personas"
        usos = "se usa en todo el mundo por su economia y ya que sirve para ejercitarse"  
        return capacidades, usos
sultana = Bus(42)
descripcion_bus = sultana.descripcion()
print(descripcion_bus)
canondale = Bicicleta(2)
descripcion_bici = canondale.descripcion()
print(descripcion_bici)   """              
                    
            
# Crea una clase Empleado con el atributo puesto. Luego, crea las clases Gerente y Programador que sobrescriban el método responsabilidades(), describiendo las funciones de cada puesto.
class Empleado:
    def __init__(self, puesto):
        self.puesto = puesto
    def responsabilidades(self):
        raise
    
class Gerente(Empleado):
    def __init__(self, puesto):
        super().__init__(puesto)
    def responsabilidades(self):
        return f"garantizar la operacion de la tienda y rsponsablizarce de la caja"


class Programador(Empleado):
    def __init__(self, puesto):
        super().__init__(puesto)  
    def responsabilidades(self):
        return f"garantizar la operatividad de la plataforma web"
    
luis_gerente = Gerente("gerente")
respon_gerente = luis_gerente.responsabilidades()
print(respon_gerente)
diego_programador = Programador("programador")
respon_programador =diego_programador.responsabilidades()
print(respon_programador)                     
# Crea una clase Animal con el atributo especie. Luego, crea las clases León y Elefante que sobrescriban el método hablar(), devolviendo el sonido que hacen.

# Crea una clase Electrodomestico con el atributo marca. Luego, crea las clases Lavadora y Refrigerador que sobrescriban el método funcion(), describiendo cómo funciona cada uno.

# Crea una clase Jugador con el atributo nombre. Luego, crea las clases Guerrero y Arquero que sobrescriban el método ataque(), explicando el tipo de ataque que realizan.

# Crea una clase Herramienta con el atributo material. Luego, crea las clases Martillo y Destornillador que sobrescriban el método usar(), explicando cómo se usa cada herramienta.

# Crea una clase Dispositivo con el atributo modelo. Luego, crea las clases Computadora y Tablet que sobrescriban el método encender(), describiendo cómo se enciende cada uno.

# Crea una clase Persona con el atributo nombre. Luego, crea las clases Estudiante y Profesor que sobrescriban el método trabajar(), explicando qué hacen en su día a día.

# Crea una clase Vehiculo con el atributo ruedas. Luego, crea las clases Bicicleta y Coche que sobrescriban el método moverse(), explicando cómo se mueven.

# Crea una clase Electrodomestico con el atributo potencia. Luego, crea las clases Microondas y Licuadora que sobrescriban el método usar(), describiendo el uso de cada uno.

# Crea una clase Figura con el atributo nombre. Luego, crea las clases Triangulo y Cuadrado que sobrescriban el método area(), calculando el área de cada figura.

# Crea una clase Herramienta con el atributo peso. Luego, crea las clases Sierra y Taladro que sobrescriban el método operar(), explicando cómo operan.

# Crea una clase Alimento con el atributo tipo. Luego, crea las clases Fruta y Carne que sobrescriban el método nutrientes(), describiendo los nutrientes principales.

# Crea una clase Vehiculo con el atributo modelo. Luego, crea las clases Avion y Barco que sobrescriban el método viajar(), describiendo cómo viaja cada uno.

# Crea una clase Animal con el atributo nombre. Luego, crea las clases Serpiente y Rana que sobrescriban el método habitar(), describiendo dónde viven.

# Crea una clase Electrodomestico con el atributo consumo. Luego, crea las clases Plancha y Ventilador que sobrescriban el método funcionar(), describiendo el funcionamiento.

# Crea una clase Juego con el atributo duracion. Luego, crea las clases Ajedrez y Damas que sobrescriban el método reglas(), explicando las reglas.

# Crea una clase Transporte con el atributo combustible. Luego, crea las clases Tren y Moto que sobrescriban el método viajar(), describiendo cómo funcionan.

# Crea una clase Persona con el atributo edad. Luego, crea las clases Niño y Adulto que sobrescriban el método actividad(), describiendo las actividades que realizan.

# Crea una clase Instrumento con el atributo material. Luego, crea las clases Trompeta y Saxofón que sobrescriban el método sonido(), explicando cómo suenan.

# Crea una clase Comida con el atributo sabor. Luego, crea las clases Sopa y Pastel que sobrescriban el método preparar(), explicando cómo se preparan.

# Crea una clase Jugador con el atributo nivel. Luego, crea las clases Mago y Guerrero que sobrescriban el método habilidad(), describiendo sus habilidades.

# Crea una clase Vehiculo con el atributo motor. Luego, crea las clases Camion y Motocicleta que sobrescriban el método cargar(), describiendo cómo transportan cosas.

# Crea una clase Animal con el atributo peso. Luego, crea las clases Tigre y Mono que sobrescriban el método comer(), describiendo qué comen.

# Crea una clase Electrodomestico con el atributo tamaño. Luego, crea las clases Televisor y Aspiradora que sobrescriban el método encender(), explicando cómo se usan.

# Crea una clase Figura con el atributo bordes. Luego, crea las clases Pentágono y Hexágono que sobrescriban el método area(), calculando el área.

# Crea una clase Persona con el atributo profesion. Luego, crea las clases Artista y Científico que sobrescriban el método trabajar(), explicando qué hacen.

# Crea una clase Vehiculo con el atributo puertas. Luego, crea las clases Sedán y Coupe que sobrescriban el método arrancar(), explicando cómo funcionan.

# Crea una clase Dispositivo con el atributo bateria. Luego, crea las clases Smartphone y Laptop que sobrescriban el método cargar(), explicando cómo se cargan.

# Ejercicios de polimorfismo en tiempo de compilación (simulado):
# Crea una clase Calculadora que tenga un método sumar() con diferentes cantidades de argumentos usando *args.

# Crea una clase Compras que tenga un método total() con un argumento por defecto para aplicar descuento.

# Crea una clase Cliente con el método registrar() que reciba distintos argumentos (*args).

# Crea una clase Banco con un método transaccion() que reciba un número variable de cuentas (*args).

# Crea una clase Carrito con un método agregar_producto() que acepte uno o más productos a la vez.

# Crea una clase Empresa con un método contratar() que acepte diferentes números de empleados con *args.

# Crea una clase Profesor con un método evaluar() que reciba distintas cantidades de estudiantes usando *args.

# Crea una clase Restaurante con un método pedir() que reciba uno o más platos como argumentos.

# Crea una clase Evento con un método asistir() que permita agregar uno o más participantes.

# Crea una clase Hotel con un método reservar_habitacion() que reciba distintos números de noches.

# Crea una clase Tienda con un método aplicar_descuento() que tenga un argumento opcional para cupones.

# Crea una clase Biblioteca con un método prestar_libros() que permita prestar varios libros con *args.

# Crea una clase Aeropuerto con un método chequear_vuelo() que reciba uno o más vuelos.

# Crea una clase Paciente con un método agendar_cita() que reciba un número opcional de días de espera.

# Crea una clase Hospital con un método ingresar_paciente() que reciba uno o más pacientes.

# Crea una clase Curso con un método agregar_estudiante() que acepte una cantidad variable de estudiantes.

# Crea una clase Servicio con un método contratar() que reciba uno o más servicios contratados.

# Crea una clase Docente con un método asignar_tareas() que acepte una cantidad variable de tareas con *args.

# Crea una clase Academia con un método matricular() que permita recibir varios cursos al mismo tiempo.

# Crea una clase Concierto con un método comprar_entrada() que acepte uno o más tipos de entradas.

# Crea una clase Transportista con un método entregar_paquetes() que acepte varios destinos.

# Crea una clase Cine con un método vender_boletos() que permita vender varios boletos a la vez.

# Crea una clase Partido con un método anotar_gol() que acepte uno o más jugadores como argumentos.

# Crea una clase Supermercado con un método cobrar() que acepte uno o más productos con *args.

# Crea una clase Negocio con un método comprar() que reciba uno o más productos y aplique un descuento opcional.

# Crea una clase Subasta con un método ofertar() que acepte varios postores al mismo tiempo.

# Crea una clase Carrera con un método participar() que reciba uno o más corredores con *args.

# Crea una clase Inmobiliaria con un método comprar_casa() que reciba una cantidad opcional de casas.

# Crea una clase Fabricante con un método producir() que acepte diferentes cantidades de productos.

# Crea una clase Conferencia con un método inscribir() que permita inscribir varios participantes al mismo tiempo.

# Crea una clase Distribuidor con un método entregar_producto() que acepte uno o más productos con *args.

# Crea una clase Viaje con un método reservar() que reciba varias fechas o destinos.

# Crea una clase Revista con un método suscribirse() que acepte uno o más lectores.

# Crea una clase Factura con un método calcular() que acepte una cantidad variable de ítems.

# Crea una clase Restaurante con un método preparar_plato() que acepte uno o más ingredientes con *args.

# Crea una clase Oficina con un método enviar_correo() que acepte uno o más destinatarios.






