#Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?

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
print ("Prueba 1")
print("¿?")
print (yang)

#La explicacion seria la siguiente:
#Como no mencionamos a la clase Yang en ningun momento, aparece el mensaje de "Yang ha sido destruido"
#Para arreglar esto tendriamos que utilizar un print(Yang)