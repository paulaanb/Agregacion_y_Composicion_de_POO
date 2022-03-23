#En el último ejercicio de la sección sobre la herencia, se mostraron los límites de la herencia múltiple: acoplamientos de clases cuyo vínculo no es tan obvio, atajos tomados en el código que tienen mucho riesgo de error. Este ejercicio utiliza otro enfoque del problema: la asociación (ya sea composición o agregación). 
#Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.
#Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.
#Enunciado: modifique el código para que el programa funcione de nuevo.


#Definimos las clases que vamos a utilizar, Pared, Ventana, Casa y Cortina
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

#Empezamos a definir las funciones que vamos a utilizar para la instalacion de paredes, ventanas, la casa y la cortina 
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 
ventana_norte = Ventana(pared_norte, 0.5) 
ventana_oeste = Ventana(pared_oeste, 1) 
ventana_sur = Ventana(pared_sur, 2) 
ventana_este = Ventana(pared_este, 1) 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada()) 

