import random 
import time
#Calcula el área de un rectángulo: Pide al usuario la base y la altura del rectángulo y calcula su área.
"""base = int(input("ingresa la base del rectangulo"))
altura = int(input("ingresa la altura del rectangulo"))
area = base * altura
print(area)"""
#Conversión de temperatura: Pide al usuario una temperatura en grados Celsius y conviértela a grados Fahrenheit.
"""tem_celsius = int(input("INGRESA LA TEMPERATURA EN CELCIUS\n"))
a_farenheith = (tem_celsius * 9/5) +32
print(a_farenheith)"""
    
#Suma de dos números: Pide al usuario dos números y muestra la suma de ambos.
"""num_1 = int(input("ingresa un numero\n"))
num_2 = int(input("ingresa otro numero\n"))
suma = num_1 + num_2
print(suma)"""
#Producto de tres números: Pide al usuario tres números y muestra el producto de los mismos.
"""num_1 = int(input("ingresa un numero\n"))
num_2 = int(input("ingresa otro numero\n"))
num_3 = int(input("ingresa otro numero\n"))
producto = num_1 * num_2 * num_3
print(producto)"""
#Cálculo del perímetro de un triángulo: Pide al usuario las longitudes de los tres lados de un triángulo y calcula su perímetro.
"""lado_1 = int(input("ingresa un lado\n"))
lado_2 = int(input("ingresa otro otro lado\n"))
lado_3 = int(input("ingresa el otro lado\n"))
perimetro = lado_1 + lado_2 + lado_3
print(perimetro)"""
#Cálculo de IVA: Pide al usuario el precio de un producto y calcula el precio con IVA incluido (21%).
"""precio = int(input("ingresa el precio\n"))
iva = precio * 21 /100
precio_total = precio + iva
print(precio_total)"""
#Conversión de metros a centímetros: Pide al usuario una longitud en metros y conviértela a centímetros.
"""metros = float(input("ingresa longitud en /mts\n"))
a_centimetros = metros * 100
print(f"{a_centimetros}--centimetros--")"""
#Promedio de cuatro notas: Pide al usuario cuatro notas y calcula su promedio.

"""notas = []
total_notas = 0
i = 0
while i < 4:
    nota = int(input("ingresa la nota\n"))
    notas.append(nota)
    total_notas = total_notas + nota
    i = i + 1
promedio = total_notas / len(notas)    
print(promedio)  """  
#Cálculo del área de un círculo: Pide al usuario el radio de un círculo y calcula su área.
"""radio = int(input("ingrese el radio\n"))
pi = 3.1416
area = pi  *radio**2
print(area)"""
#Calcula el salario semanal: Pide al usuario las horas trabajadas en una semana y el salario por hora, luego calcula el salario semanal.
"""horas_seman = int(input("ingrese horas trabajadas\n"))
salario_hora = 5000
salario_semanal = horas_seman * salario_hora
print(salario_semanal)"""
#Conversión de kilómetros a millas: Pide al usuario una distancia en kilómetros y conviértela a millas.
"""kilometros = int(input("ingresa los kilometros\n"))
milla = kilometros * 0.62
print(milla)"""
#Calcula el índice de masa corporal (IMC): Pide al usuario su peso y su altura, luego calcula su IMC.
"""peso = int(input("ingrese su peso"))
altura = float(input("ingrese su altura"))
imc =  peso /(altura ** 2)
print(imc)"""
#Intercambio de valores: Pide al usuario dos valores e intercámbialos.
"""valor_1 = int(input("ingresa un valor\n"))
valor_2 = int(input("ingresa otro valor\n"))
valor_1,valor_2 = valor_2, valor_1

print(f"valor1 = otro valor {valor_1} antes valor 2")
print(f"valor2 = otro valor {valor_2} antes valor 1")"""
#Cálculo de la hipotenusa: Pide al usuario los dos catetos de un triángulo rectángulo y calcula la hipotenusa.
"""cateto_1 = int(input("ingrese cateto 1\n"))
cateto_2 = int(input("ingrse cateto 2\n"))
hipotenusa = (cateto_1**2 + cateto_2**2)**0.5
print(hipotenusa)"""
#Años, meses y días vividos: Pide al usuario su edad en años y calcula cuántos meses y días ha vivido aproximadamente.
"""edad = int(input("ingrese su edad\n"))
dias = edad * 364
meses = edad *12
print(F"HAS VIVIDO {meses} MESES O {dias} DIAS ")"""
#Conversión de dólares a euros: Pide al usuario una cantidad en dólares y conviértela a euros.
"""dolares = int(input("ingresa en dolares\n"))
euro = dolares * 1/1.074
print(euro) """
#Inversión de una cadena: Pide al usuario una cadena de texto e invierte sus caracteres.
"""cadena = "diego fernando bolaños"
invertido = cadena[::-1]
print(invertido)"""
#Número de caracteres en una cadena: Pide al usuario una cadena de texto y muestra el número de caracteres que tiene.
"""cadena = input("ingresa una frase\n")
n_caractere = len(cadena)
print(n_caractere)"""
#Cálculo del perímetro y área de un cuadrado: Pide al usuario la longitud de un lado de un cuadrado y calcula su perímetro y área.
"""l_lado = int(input("ingresa longitud de lado\n"))
lados = l_lado * 4
area = l_lado ** 2
print(f"las suma de los lados es {lados} y el area es {area}")"""
#Calcula el volumen de un cilindro: Pide al usuario el radio y la altura de un cilindro y calcula su volumen.
"""radio = int(input("INGRESA EL RADIO \n"))
altura = int(input("ingresa altura\n"))
pi = 3.1416
volomen = pi * (radio ** 2) * altura    
print(volomen)"""
#Calcula la raíz cuadrada de un número: Pide al usuario un número y calcula su raíz cuadrada.
"""numero = int(input("ingresa un numero\n"))
raiz_c = numero ** 0.5
print(raiz_c)"""
#Calcula el resto de una división: Pide al usuario dos números y calcula el resto de la división del primero por el segundo.
"""primer_n = int(input("ingresa un numero\n"))
segundo_n = int(input("ingresa segundo numero\n"))
modulo = primer_n % segundo_n
print(modulo)"""
#Concatenación de dos cadenas: Pide al usuario dos cadenas de texto y muéstralas concatenadas.
"""cadena_1 = "diego "
cadena_2 = "fernando"
caoncatenacion = cadena_1 + cadena_2
print(caoncatenacion)"""

#Extracción de subcadena: Pide al usuario una cadena de texto y dos índices, luego extrae y muestra la subcadena correspondiente.
"""cadena = input("ingrese un acadena")
indice = int(input("ingrese el indice"))
caracteres_indice = cadena[indice]
print(caracteres_indice)"""
#Conversión de minutos a horas y minutos: Pide al usuario una cantidad de minutos y conviértela en horas y minutos.
"""minutos = int(input("ingresa los minutos\n"))
horas = minutos/60
print(horas)"""
#Multiplicación de un número por sí mismo: Pide al usuario un número y muestra su cuadrado.
"""numero = int(input("ingresa un unmero\n"))
al_cuadrado = numero ** 2
print(al_cuadrado)"""
#Conversión de segundos a horas, minutos y segundos: Pide al usuario una cantidad de segundos y conviértela en horas, minutos y segundos.
"""segundos = int(input("ingresa los segundos\n"))
horas = segundos // 3600
segundos_restantes = segundos%3600
minutos = segundos_restantes / 60 
segundos_restantes = segundos_restantes %60
print(horas,minutos,segundos_restantes)"""

#-----------------------------------------------------------------ejercicios enca24-------------------------------------------------------
# descuento 20%
"""precio = int(input("ingrese valor a pagar\n"))
descuento = 20
valor_descuento = (precio * descuento )/ 100
precio = precio - valor_descuento
print(f"el valor total a pagar aplicando desvuento es {precio}")"""
#hallar porcentajes
"""cantidad_h = 78
cantidad_m = 43
total_estudiantes = 121
porcentaje_hombre = (cantidad_h * 100 )/121
porcentaje_nujeres =  (cantidad_m * 100)/121
print(porcentaje_hombre,porcentaje_nujeres)"""
#encontrar area y volumen de un cilindro
"""Radio = int(input("ingrese el radio del cilindro\n"))
altura = int(input("ingrese la altura del cilindr\n"))
pi = 3.1416
volumen = 3.1416 * altura * Radio ** 2
area = 2 * pi * Radio * altura + 2 * pi  * Radio ** 2
print(f"el volumen del cilindro es {volumen}")
print(f"el area del cilindro es{area}")"""
#aplicar iva
"""valor = int(input("ingrese valor a pagar\n"))
iva = (valor * 19) / 100
print(f"el valor del iva es :{iva}")
valor = valor + iva
print(f"el total a pagar es : {valor}")"""
#cambio de moneda
"""pesos = int(input("ingrese el valor en pesos\n"))
dolar = 4.174
cambio_dolar = pesos // dolar
print(f"el total de dolares comprados con {pesos} fue {cambio_dolar}")"""
#nota final
"""nota_1 = float(input("ingrese la primera nota\n"))
nota_2 = float(input("ingrese la segunda nota\n"))
nota_3 = float(input("ingrese la tercera nota\n "))

por_nota1 = nota_1 * 0.25
por_nota2 = nota_2 * 0.45
por_nota3 = nota_3 * 0.3
nota_final = por_nota1 + por_nota2 + por_nota3

print("nota final ", nota_final)"""
# nuevo salario
"""salario_anterior = float(input("ingrese salario actual\n"))
aumento = 0.25 
valor_aumento = salario_anterior * aumento
nuevo_salario = valor_aumento + salario_anterior
print(f"el salario anterio era : {salario_anterior} el aumento fue de {valor_aumento} quedando con n salario de {nuevo_salario}")
"""
#calificacion final
"""parcial_1 = float(input("ingrese nota parcial 1"))
parcial_2 = float(input("ingrese nota parcial 2"))
parcial_3 = float(input("ingrese nota parcial 3"))
nota_examen_final  = float(input("ingresa la nota del examen final\n"))
nota_trabajo_final = float(input("ingrese nota del trabajo final\n"))

nota_parcial = ((parcial_1 + parcial_2 + parcial_3)/3) * 0.55
nota_examen_final = nota_examen_final* 0.30
nota_trabajo_final =  nota_trabajo_final* 0.15

calificacion_final_matematicas = nota_parcial + nota_examen_final + nota_trabajo_final
print(calificacion_final_matematicas)"""
#hallar el sueldo
"""sueldo_dia = 69.230
dias_laborales = 26
aportes_mensuales_totales = 11.74
sueldo_mesual = sueldo_dia * dias_laborales
aportes_mensuales_totales = (sueldo_mesual * 11.74) / 100
afp = sueldo_mesual * 0.1
ad_f_inversion = sueldo_mesual * 0.0038
seguro_invalidez = sueldo_mesual * 0.0136
print(f"sueldo mensual = {sueldo_mesual}")
print(f"total aportes mesuales = {aportes_mensuales_totales}")
print(f"aportes a fondo de pensiones = {afp}")
print(f"administradora de fondo de inversion = {ad_f_inversion}")
print(f"seguro de invalidez = {seguro_invalidez}")"""

#imprimir si no es negativo
"""numero_1 = int(input("ingrese un numero\n"))
numero_2 = int(input("ingrese el segundo numero\n"))
suma_numeros = numero_1 + numero_2
if suma_numeros > 0:
    print(f"la suma de los numeros {numero_1} y {numero_2}es {suma_numeros}")"""

#mayor de edad
"""edad = int(input("ingrese su edad\n"))
if edad > 18:
    print("puede ingresar ya eres mayor de edad\n")
else:
    print("NO puedes ingresar,eres menor de edad")"""
    
#aprobar el semestre
"""nombre = input("ingresa tu nombre :\n")
curso = input("ingrese el curso :\n")
numero_clases_semestre = int(input("ingresa total de clases por semestre\n"))
numero_clases_semestre_ausente = int(input("ingresa total de clases ausente por semestre\n"))
reprobado = (numero_clases_semestre * 20)/100
if reprobado:
    print(f"nota definitiva :0 , REPROBADA")
    print(f"numero de clases por semestre = {numero_clases_semestre} falto a mas del 20% de clases = {numero_clases_semestre_ausente}")"""
    
# visualizar 2 numeros si son psitivos
"""numero_1 = int(input("ingrese un numero\n"))
numero_2 = int(input("ingrese otro numero\n"))
if numero_1 > 0 and numero_2 > 0:
    print(f"el numero {numero_1} y el numero {numero_2} son positivos")"""
    
#hallar interes 
"""inversion = float(input("ingrese la cantidad de dinero a invertir\n"))
tasa_interes = int(input("ingrese la tasa de interes\n")) 
intereses_generados = (inversion * tasa_interes) / 100
if intereses_generados < 7000:
    print(f"intereses generados = {intereses_generados} con una inverions de  {inversion}")"""
    
#salario mensual
"""nombre_empleado = input("ingrese nombre del empleado\n")
salario_hora = float(input("ingrese pago por hora \n"))
horas_trabajadas_mes = int(input("ingrese cantidad de horas laboradas \n"))
sueldo_mensual = salario_hora * horas_trabajadas_mes
subsidio_transporte = 50000
tope_subsidio = 1800000

if sueldo_mensual > tope_subsidio:
    print(f"NOMBRE DEL EMPLEADO : {nombre_empleado}")
    print(f"EL SALARIO MENSUAL ES :{sueldo_mensual}")  
    print(f"SUBSIDIO DE TRANSPORTE :{subsidio_transporte}")
    print(f"SALARIO TOTAL : {sueldo_mensual + subsidio_transporte}") 
else:
    print(f"{sueldo_mensual} No mayor a  tope")"""       
    
# aplicar desacuento a egresado
"""nombre_estudiante = input("ingrese nombre de estudiante\n") 
valor_matricula = float(input("ingrese el valor de la matricula\n"))
egresado = input("es egresado?")
if egresado.lower() == "si":
    valor_descuento = (valor_matricula * 25 / 100)
    valor_matricula = valor_matricula - valor_descuento
    print(f"NOMBRE: {nombre_estudiante} VALOR A PAGAR CON DESCUENTO: {valor_matricula}")"""
    
#apto para el servicio militar
 
"""genero = input("ingrese su genero (M)masculino (F)femenino\n")
if genero.lower() == "m":
    edad = int(input("ingrese su edad\n"))
    if edad > 18 and edad < 26:
        print("apto para prestar servicio militar")
    else:
        print("No tienes edad para prestar el servicio militar")    
else:
    print("No eres hombre para prestar el servicio militar")"""  
    
#determinar forma de pago
"""monto_total_de_la_compra = float(input("ingrese el monto total de la compra \n"))
limite = 500000
if monto_total_de_la_compra > limite:
    dinero_propio = (monto_total_de_la_compra * 50) / 100
    credito_banco = (monto_total_de_la_compra * 30)/100     
    credito_fabricante = (monto_total_de_la_compra * 20) / 100
    print(f"DINERO PROPIO 50 % = {dinero_propio}")
    print(f"CREDITO CON EL BANCO = {credito_banco}")
    print(F"CREDITO CON EL FABRICANTE = {credito_fabricante}")
else:
    dinero_propio = (limite * 70) / 100
    credito_banco = (limite * 25)/100     
    credito_fabricante = (limite * 5) / 100
    print(f"DINERO PROPIO 70 %= {dinero_propio}")
    print(f"CREDITO CON EL BANCO = {credito_banco}")
    print(F"CREDITO CON EL FABRICANTE = {credito_fabricante}")"""
 
#descuento al por mayor
"""valor_producto = float(input("ingrese valor del producto\n"))
cantidad_compra = int(input("ingrese cantidad de la compra\n"))
if cantidad_compra > 36:
    monto_compra = valor_producto * cantidad_compra
    descuento = (monto_compra * 15 )/100 
    monto_compra_descuento = monto_compra - descuento
    print(f"monto de la compra = {monto_compra}")
    print(f"descuento 15 % = {descuento}")
    print(f"monto de la compra total mesnos descuento = {monto_compra_descuento}")
else :
    monto_compra = valor_producto * cantidad_compra
    descuento = (monto_compra * 10 )/100 
    monto_compra_descuento = monto_compra - descuento 
    print(f"monto de la compra = {monto_compra}")
    print(f"desceunto 10 % = {descuento}")
    print(f"monto de la compra menos el descuento = {monto_compra_descuento}")"""
    
#nota promocional
"""nota1 = float(input("ingrese la nota 1\n"))
nota2 = float(input("ingrese la nota 2\n"))
nota3 = float(input("ingrese la nota 3\n"))
nota4 = float(input("ingrese la nota 4\n"))
nota5 = float(input("ingrese la nota 5\n"))
nota6 = float(input("ingrese la nota 6\n"))       
nota_promocional = nota1 + nota2 + nota3 + nota4 + nota5 + nota6
print(nota_promocional)
matricula = float(input("ingrese el costo de la matricula:\n"))
if nota_promocional > 14:
    descuento = (matricula * 30) / 100
    matricula_descuento = matricula - descuento
    print(f"el valor de la matricula es :{matricula} con un descuento de 30 % {descuento} total a pagar :{matricula_descuento}")
else:
    descuento = (matricula * 10) / 100
    matricula_descuento = matricula - descuento
    print(f"el valor de la matricula es :{matricula} con un descuento de 30 % {descuento} total a pagar :{matricula_descuento}")"""
    
#descuento al azar 
"""precio_producto = int(input("ingrese el precio del producto a comprar\n"))
cantidad = int(input("ingrese la cantidad\n"))
numero_aleatorio  =   random.randint(70,78)
print(f"numero aleatorio : {numero_aleatorio}")  
if numero_aleatorio >= 74:
    total = precio_producto * cantidad
    descuento = (total*20) / 100
    print(total)
    print(f"descuento de 20 % :{descuento}")
else:    
    total = precio_producto * cantidad
    descuento = (total*10) / 100
    print(total)
    print(f"descuento del 10 % : {descuento}")"""
    
#aprobo curso
"""nota_1 = float(input("ingrese la nota 1\n"))
nota_2 = float(input("ingrese la nota 2\n"))
nota_3 = float(input("ingrese la nota 3\n"))    
promedio_notas = (nota_1 + nota_2 + nota_3) / 3
print(promedio_notas)    
if promedio_notas >= 12:
    print(f"el estudiante ha aprobado la nota promedio {promedio_notas}")
else:
    print(f"el estudiante reprobo nota con un promedio {promedio_notas}") """  
     
# factura de compra
"""iva = 19
precio_articulo = int(input("ingrese precio\n"))
cantidad = int(input("ingrese cantidad\n"))
precio_t = precio_articulo * cantidad
descuento = 0
if precio_t > 70000:
    descuento = (precio_t * 5) / 100
    precio_dcto = precio_t - descuento
impuesto_p = (precio_t * 19 )/100
total = impuesto_p + precio_t
print(f"precio de productos {precio_t}")
print(f"el total a pagar de iva es {impuesto_p}")
print(f"descuento {descuento}")
print(f"total a pagar {(precio_t + impuesto_p) - descuento}")"""

# numero par o impar
"""numero = int(input("ingrese un numero\n"))
if numero % 2 == 0:
    print("numero par")
else:
    print("numero impar")"""
    
# hallar sueldo neto y descuento provisional
"""sueldo = float(input("ingrese su sueldo\n"))
tipo_cargo = input("ingrese tipo de cargo \n") 
descuento = 0
if tipo_cargo == "administrativo":
    descuento = (sueldo * 12) / 100
    sueldo_neto = sueldo - descuento
elif tipo_cargo == "operativo":
    descuento = (sueldo * 17) / 100
    sueldo_neto = sueldo - descuento
print(f"el tipo de cargo es {tipo_cargo} con un sueldo neto  de {sueldo_neto} $ tiene un descuento de {descuento} $")"""
"""horas_d = int(input("ingrese horas diurnas laboradas\n"))
horas_n = int(input("ingrese  horas nocturnas laboradas\n"))
total_h_d = horas_d * 50
total_h_n = horas_n * 80
total_horas_laboradas = total_h_d + total_h_n
if total_horas_laboradas > 600:
    descuento = (total_horas_laboradas * 1) / 100
    total_pago = total_horas_laboradas - descuento
    print(f"el pago total es : {total_pago} se le descuenta :{descuento}")
else:    
    print(f"el pago total es {total_horas_laboradas}") """
#encuentre la comision del vendedor
"""valor_venta = float(input("ingrese valor del venta\n"))
if valor_venta < 1000:
    comision = (valor_venta * 3) / 100
    print(f"la comision por la venta de {valor_venta} es de {comision}")
            
else:
    comision = (valor_venta * 5) / 100
    print(f"la comision por la venta de {valor_venta} es de {comision}")"""
    
#condicionales compuestos    
#cobro de alquiler de vehiculo
"""km_recorrido = int(input("ingrese kilometros de recorrido\n"))
total_pagar = 3000
iva = 19
if km_recorrido < 300:
    print(f"el total a pagar por {km_recorrido} km es de {total_pagar}")
else:
    if km_recorrido > 300 and km_recorrido < 1000:
        km_adicional = km_recorrido - 300
        pagar_adicional = km_adicional * 1500
        total_pagar = total_pagar + pagar_adicional 
        impuesto_pagar = (iva * total_pagar) / 100
        total_pagar = total_pagar + impuesto_pagar
        print(pagar_adicional)
        print(f"el total a pagar por {km_recorrido} km es de {total_pagar} con un adicional de {pagar_adicional} por {km_adicional} km adicionales ")
    elif km_recorrido > 1000:
        km_adicional = km_recorrido - 1000
        pagar_adicional = km_adicional * 1000
        total_pagar = total_pagar + pagar_adicional 
        impuesto_pagar = (iva * total_pagar) / 100
        total_pagar = total_pagar + impuesto_pagar
        print(f"el total a pagar por {km_recorrido} km es de {total_pagar} con un adiconal de {pagar_adicional} por {km_adicional} km adiconal")"""


# promocionde llantas
"""cantidad_llantas = int(input("ingrese la cantidad de llantas a comprar\n"))
total_pagar = 0
if cantidad_llantas < 5:
    total_pagar = cantidad_llantas * 30000
else:
    if cantidad_llantas < 10 and cantidad_llantas > 5:
        total_pagar = cantidad_llantas * 25000
    elif cantidad_llantas >= 10:
        total_pagar = cantidad_llantas * 20000
print(f"el total a pagar es {total_pagar} por {cantidad_llantas}")"""

# promedio practicas
"""notas = []
menor_nota = 0
total = 0
for i in range(4):
    nota = float(input("ingrese la nota\n"))
    notas.append(nota)
print(notas)

for nota in notas:
    print(nota)
    menor_nota = min(notas)
    print("el numero menor es ",menor_nota)
    total = total + nota
        
notas.remove(menor_nota) 
promedio = total / len(notas)       
print(f"el promedio de las notas es : {promedio}") 
print(f"la  nota menor eliminada fue : {menor_nota}")"""

#organiza 3 numeros cual es el menor y cual es mayor
"""num_1 = int(input("ingresa el primer numero\n"))
num_2 = int(input("ingresa el segundo numero\n"))
num_3 = int(input("ingresa el tercer numero\n"))

if num_1 < num_2 and num_1 < num_3:
    print(f"el primer numero es el menor {num_1}")
else:
    if num_2 < num_1 and num_2 < num_3:
        print(f"el segundo es el numero menor {num_2}")
    else: 
        print(f"tercer es el numero menor {num_3}")

if num_1 > num_2 and num_1 > num_3:
    print(f"el primer numero es el mayor {num_1}")
else:
    if num_2 > num_1 and num_2 > num_3:
        print(f"el segundo es el numero mayor {num_2}")
    else: 
        print(f"tercer es el numero mayor {num_3}")"""
        
#   orden dencendente o acendente

"""num_1 = int(input("ingresa el primer numero\n"))
num_2 = int(input("ingresa el segundo numero\n"))
num_3 = int(input("ingresa el tercer numero\n"))

if num_1 != num_2 and num_2 != num_3:
    if num_1 < num_2 and num_2 < num_3:
        print("los numeros estan en orden ascendente")
    elif num_1 > num_2 and num_2 > num_3:
        print("los numeros estan en orden descendente")    
else:
    print("los numeros son iguales")"""
    
#calcular el valor de r
"""a = int(input("ingrese el valor de a\n"))
b = int(input("ingrese el valor de b\n"))
c = int(input("ingrese el valor de c\n"))
d = int(input("ingrese el valor de d\n"))  

valor_x = int(input("ingrese el valor de x\n"))
valor_y = int(input("ingrese el valor de y\n"))
r = 0  

if valor_x * valor_y > 0:
    r = (a * b) / (c * d)
else:
    if valor_x * valor_y == 0:
        r = (a + b) / (c + d) 
    else:
        r = (a + b) - (c + d)
print(f"el resultado de r es :{r}")               
    """
    
# eficiencia de operario
"""c_tornillos = int(input("ingrese tornillos producidos\n"))
if c_tornillos < 300:
    print("operario nivel 1") 
else:       
    if c_tornillos < 1000 and c_tornillos > 300:
        print("operario nivel 2")
    elif c_tornillos > 1000:
        print("operario nivel 3")    """
        
# determinar si tiene anemia
"""edad = int(input("ingrese la edad del paciente en meses\n"))
nivel_de_hemoglobina = float(input("ingrese nivel de hemoglobina\n"))

if edad > 0 and edad <= 1 and nivel_de_hemoglobina < 13:
    print("paciente con anemia")  
else:
    if edad > 1 and edad <= 6 and nivel_de_hemoglobina < 10:
        print("paciente con anemia")
    else:
        if edad > 6 and edad <= 12 and nivel_de_hemoglobina < 11:
            print("paciente con anemia") 
        else:
            if edad > 12 and edad <= 60 and nivel_de_hemoglobina < 11.5:
                print("paciente con anemia")   
            else:
                if edad > 60 and edad <= 120 and nivel_de_hemoglobina < 12.6:
                    print("paciente con anemia")        
                else:
                    if edad > 120 and edad <= 180 and nivel_de_hemoglobina < 13:
                        print("paciente con anemia")
                    else:
                        print("paciente sano") """
                        
#bucle while
#de 0 a 100  
"""i = 100
while i > 0:
    print(i)
    i = i - 1  """
    
#promedio de lista de positivos 
"""l_numeros = []
numero = 0
total = 0
while numero >= 0:
    numero = int(input("ingrese numero \n"))
    if numero >= 0:
        l_numeros.append(numero)
        total = total + numero
    
promedio = total / len(l_numeros)    
print(l_numeros)
print(f"total : {total} longitud de la lista . {len(l_numeros)}")  
print(f"el promedio es : {promedio}") """   

# numeros pares hasta 100
"""i = 0
while i < 100:
    if i % 2 == 0:
        print(i)
    i = i + 1""" 
    
#continuar con s
"""continuar = "s"
while continuar.lower() == "s":
    continuar = input("continuar con el programa si(S) no(N)")
    
print("seccion terminada")"""

# impares entre 0 y 100
"""i = 0
while i < 100:
    if i % 2 != 0:
        print(i)
    i = i + 1"""
    
# suma de serie con ultimo numero
"""ultimo_numero = int(input("ingrese ultimo numero \n"))
i = 0
total = 0
while i < ultimo_numero:
    if i % 2 == 0:
        total = total + i
        print(i)
    i = i + 1
    
print(f"total : {total}")"""

#imprimir hasta el numero ingresado    
"""i = 0
num_ingresado = int(input("ingrese un numero \n"))
while i <= num_ingresado:
    print(i)
    i = i + 1"""
    
# ingresar varios enunciados y contabilizarlos
"""enunciados = 0
l_enunciados = []
while True:
    enunciado = input("ingrese un enunciado o salir para terminar\n")
    if enunciado != "salir":
        l_enunciados.append(enunciado)
        enunciados = enunciados + 1
    if enunciado == "salir":
        break  
print(f"total enunciados : {enunciados}")
print(l_enunciados)"""

# tablas de multiplicar hasta el doce de un numero introducido por el usuario
"""numero = int(input("ingrese el numero\n"))  
i = 1
while i <= 12:
    print(f"{numero} x {i} : {numero * i}")
    i = i + 1   """
    
# suma de numeros pares de hasta 1000 y suma de impares hastta 100
"""suma_pares = 0
suma_impares = 0
i = 0
while i <=100:
    if i % 2 == 0:
        suma_pares = suma_pares + i
        
    else:
         suma_impares = suma_impares + i   
    print(i)
    i = i + 1 
print(f"total numeros pares : {suma_pares}")
print(f"total numerso impares  {suma_impares}")        
"""
# suma de la serie
"""numero_f = int(input("ingrese numero\n")) 
i = 0
total = 0
while i < numero_f:
    if i % 2 == 0:
        total = total + i
    i = i + 1    
print(f"la suma total es : {total}")"""

# factorial de un numero 
"""numero = int(input("ingrese un numero de 1 a 15\n"))
i = 1
factorial = 1
if numero > 0 and numero < 16:
    while i <= numero:
        factorial = factorial * i
        print(i)
        i = i + 1 
    print(factorial)                                       
else:
    print("numero fuera de rango")""" 
    
# imprimir y contabilizar los multiplos de 3 hasta el numero introducido por el usuario
"""numero = int(input("ingrese un numero \n"))
i = 1
cantidad_de_multiplos = 0
while i <= numero:
    if i % 3 == 0:
        cantidad_de_multiplos = cantidad_de_multiplos + 1
        print(i)
    i = i + 1
print(f"el total de numeros dividibles por 3 hast {numero} es  {cantidad_de_multiplos}")"""

#numero menor y numero mayor de una serie de 5 numeros introducido por teclado
"""numeros = []
i = 0
numero_mayor = 0
numero_menor = 99
while i < 5:
    numero = int(input("ingrese un numero \n"))
    numeros.append(numero)
    if numero_mayor < numero:
        numero_mayor = numero
    if numero_menor > numero:
        numero_menor = numero    
    i = i +1  
print(f"lista de numeros introducidos  : {numeros}") 
print(f"el numero mayor es : {numero_mayor}")
print(f"el numero menor es : {numero_menor}") """

# cuantos ganan mas de 100 y cuantos mas de 300, importe total de gastos de la empresa  
"""lista_sueldos = []
sueldos_mas_100 = 0
sueldos_mas_300 = 0
nomina_total = 0
while True:
    sueldo = input("ingrese el sueldo del empleado\n")
    if  sueldo == "salir":
        break
    else:
        if int(sueldo) >= 100 and int(sueldo) < 300:
            sueldos_mas_100 = sueldos_mas_100 + 1
        else:    
            if int(sueldo)>=300:
                sueldos_mas_300 = sueldos_mas_300 + 1       
    lista_sueldos.append(sueldo)
    nomina_total = nomina_total + int(sueldo)
print(f"lista de sueldos : {lista_sueldos}")    
print(f"sueldos superiores a 100 : {sueldos_mas_100}")
print(f"sueldos superiores a 300 : {sueldos_mas_300}") 
print(f"nomina total a pagar por la empresa = {nomina_total}")"""

# simular el funcionamiento de un reloj
"""hora = int(input("ingrese la hora\n"))
minutos = int(input("ingrese los minutos\n"))
segundos = int(input("ingrese los segundos\n"))

while hora < 24:
    while minutos < 60:
        while segundos < 60:
            time.sleep(1)
            print(f"{hora}:{minutos}: {segundos}")
            segundos = segundos + 1
        minutos = minutos + 1
        segundos = 0    
hora = hora + 1"""

# factorial de un numero

"""while True:
    factorial = 1
    i = 1
    numero =int(input("ingrese un numero\n"))
    while i <= numero:
        factorial = factorial * i
        i = i + 1
    print(factorial)
    #salir del bucle    
    if numero == "salir":
        break"""
        
# resto y cociente por medio de restas sucesivas
"""resto = 0
cociente = 0
numerador = int(input("ingrese numerador\n"))
denominador = int(input("ingrese el denominador\n"))
while True:
    numerador = numerador - denominador
    resto = numerador
    cociente = cociente + 1
    if numerador < denominador:
        break   
print(f"resto : {resto}")
print(f"cociente : {cociente}")"""

# suma de los 100 primeros digitos 
"""suma = 0
numero = 0
while True:
    numero = numero + 1
    print(numero)
    suma = suma + numero
    if numero >= 100:
        break   
print(suma)"""

#determinar de n elementos, cuantos son menores que 15, cuantos estan entre 25 y 45, cuantos son mayores que 50
"""i = 0
mayores_15 = 0
entre_25_45 = 0
mayores_50 = 0
while True:
    #print (i)
    i = i + 1
    if i <= 15 :
        mayores_15 = mayores_15 + 1
        print(i)
    else:
        if i > 15 and i <= 25:
            entre_25_45 = entre_25_45 + 1
            print("--",i) 
        else:
            if i > 50:
                mayores_50 = mayores_50 + 1 
                print("---",i)      
    if i > 100:
        break          
print(mayores_15)    
print(entre_25_45)
print(mayores_50)"""

# promedio de numeros pares e impares de 10 numeros ingresados por teclado
"""i = 0
n_pares = []
total_pares = 0
total_impares = 0
n_impares = []
while True:
    numero = int(input("ingrese un numero \n"))
    i = i + 1
    if i % 2 == 0 :
        n_pares.append(numero)
    else:
        if i % 2 != 0:
            n_impares.append(numero)   
    if i >= 10:
        break
    
print(n_pares) 
for num in n_pares:
    total_pares = total_pares + num
print("total numeros pares :",total_pares)  
promedio_p = total_pares / len(n_pares)
print("promedio numeros pares :",promedio_p)
  
print(n_impares)
for num in n_impares:
    total_impares = total_impares + num
print("total numeros impares :",total_impares) 
promedio_imp = total_impares / len(n_impares)
print("promedio numeros impares :",promedio_imp) """ 

# convertir galones en litros
"""lts = 3.785
gln = 20
while True:
    print(f"{gln} galon(es) equivalen a {lts * gln} ")
    gln = gln + 1
    if gln > 30:
        break """
        
# listar numeros positivos y negativos de una lista ingresada por el ususario
"""lista_numeros = []
lista_numeros_p = []
lista_numeros_n = []
i = 0
while True:
    numero = int(input("ingrese un numero\n")) 
    lista_numeros.append(numero)
    if numero > 0:
        lista_numeros_p.append(numero)
    else:
        lista_numeros_n.append(numero)
    
    
    i = i + 1
    if i >= 10:    
        break    
print(f"numeros en lista : {lista_numeros}") 
print(f"numeros positivos de la lista : {lista_numeros_p}")
print(f"numeros negativos de la lista : {lista_numeros_n}")  """

# suma de numeros pares entre 1 y 200
"""suma_pares = 0
for numero in range(201):
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
        print(numero)
print(suma_pares)""" 

# promedio de 9 numeros ingresado por teclado
"""numero = 0
numeros_ingresados = []
total_num = 0
for num in range(9):
    numero = int(input("ingrese un numero\n"))
    numeros_ingresados.append(numero)
    total_num = total_num + numero
print(f"numeros ingresados por el teclado = {numeros_ingresados}")
promedio = total_num / len(numeros_ingresados)
print(total_num, len(numeros_ingresados))        
print(promedio)"""

#factorial entre 2 y 12 
"""total = 1
numero = int(input("ingrese un numero de 2 a 12 \n"))
if numero >= 2 and numero <= 12:
    for i in range(1,numero + 1) :
        print(i)
        total = total * i
else:
    print("--numero fuera de rango--")        
print(f"factorial de {numero} es :{total}") """    

# determinar si un numero ingresado por teclado es primo
"""numero = int(input("ingrese un numero\n"))
es_primo = 0
if numero <= 1:
    print("el numero no es primo")
elif numero == 2:
    print("el numero es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("el numero es primo")
    else:
        print("el numero no es primo")"""
# tabla de multiplicar de unnumero hasta 12
"""numero = int(input("ingrese un numero\n"))
for i in range(1,13):
    print(f"{numero} x {i} = {numero * i}") """       
        
                
            
    
         
    


    
     
      
           
 
  
         
    


        
        
                
         
        
                        
    
        
        


        
    
    
             
        