# Agregacion_y_Composicion_de_POO
La direccion de mi repositorio es [https://github.com/paulaanb/Agregacion_y_Composicion_de_POO]

En el hemos resuelto los tres ejercicios propuestos.

#Ejercicio 1

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


#Ejercicio 2

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