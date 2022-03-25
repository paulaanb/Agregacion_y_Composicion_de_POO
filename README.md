# Agregacion_y_Composicion_de_POO
La direccion de mi repositorio es [https://github.com/paulaanb/Agregacion_y_Composicion_de_POO]

En el hemos resuelto los tres ejercicios propuestos.

# Ejercicio 1


Enunciado:modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.
Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.




    #Empezamos a crear el codigo definiendo la clase edificio y la clase empresa
    class Edificio():
    def __init__(self, edificio):
        self.edificio = edificio
    class Empresa():
    def ciudad():
        self.ciudad = ciudad
        #Establecemos las relacioness
        print("¿Que ciudad desea destruir, New_York o Los_Angeles?")
        if ciudad == New_York
        print("New_York se ha destruido junto con los edificios A y B, y el Sr.Salim y la Sra.Xing")
        if ciudad == Los_Angeles
        print("Los_Angeles se ha destruido junto con el edificio C y el Sr.Martin")
   
    #Comando para ejecutar el programa
    print("Ejercicio1")
    print(destruccion.ciudad("New_York"))


# Ejercicio 2

Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?

    #Copiamos el codigo dado
    class Yin: pass 
    class Yang: 
        def __del__(self): 
            print("Yang ha sido destruido") 
 
    yin = Yin() 
    yang = Yang() 
    yin.yang = yang 
 
 
    print(yang) 
    print(yang is yin.yang)
    del(yang) 
    del (yin.yang) #creado para que no haya problemas
    print ("Prueba 1")
    print("¿?")
    print (yang)

    #La explicacion seria la siguiente:
    #Como no mencionamos a la clase Yang en ningun momento, aparece el mensaje de "Yang ha sido destruido"
    #Para arreglar esto tendriamos que utilizar un print(Yang)


# Ejercicio 3

En el último ejercicio de la sección sobre la herencia, se mostraron los límites de la herencia múltiple: acoplamientos de clases cuyo vínculo no es tan obvio, atajos tomados en el código que tienen mucho riesgo de error. Este ejercicio utiliza otro enfoque del problema: la asociación (ya sea composición o agregación). 
Enunciado 1: comenzando con el mismo código que el ejercicio sobre herencia múltiple, cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.
Enunciado 2: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.
Enunciado 3: modifique el código para que el programa funcione de nuevo.

    # Enunciado 1:
    #Definimos las clases que vamos a utilizar, Pared, Ventana, Casa y Cortina para que cree una clase que agrupe el comportamiento comun entre ellas
    class Pared:
        def __init__(self, orientacion):
            self.orientacion = orientacion
        
    class Ventana:
        def __init__(self, pared, superficie, acristalamiento):
            self.pared = pared
            self.superficie = superficie
            self.pared.ventanas.append(self)
            if acristalamiento is None:
                raise Exception("El acristamlamiento de la ventana es obligatoria")
            self.acristalamiento = acristalamiento

    class Casa:
        def __init__(self, paredes, orientacion, superficie):
            super().__init__(orientacion, superficie)
            self.paredes = paredes
    
        def superficie_acristalada(self):
            return sum(self.paredes.superficie)

    class Cortina:
        def __init__(self, orientacion, superficie):
            Pared.__init__(self, orientacion)
            Ventana.__init__(self, self, superficie, "Ninguna")

    # Enunciado 2: 
    #Empezamos a definir las funciones que vamos a utilizar para la instalacion de paredes, ventanas, la casa y la cortina para que modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal 
    pared_norte = Pared("NORTE") 
    pared_sur = Pared("SUR") 
    pared_este = Pared("ESTE") 
    pared_oeste = Pared("OESTE") 


    ventana_norte = Ventana(pared_norte, 0.5)
    ventana_sur = Ventana(pared_sur, 2)
    ventana_este = Ventana(pared_este, 1)  
    ventana_oeste = Ventana(pared_oeste, 1) 

    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 

    # Enunciado 3:
    #Funcion que utilizamos para imprimir el resultado para que modifique el código para que el programa funcione de nuevo.
    print(casa.superficie_acristalada()) 

