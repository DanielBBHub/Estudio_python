class Pruebas:

    def sin_vuelta(self):
        print("[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]")
        print("La funcion sin_vuelta() comienza aqui")
        print("Se va a levantar una escepcion")
        raise Exception("Siempre se levantara esta escepcion")
        #----------------------------
        print("Este segundo print nunca se ejecutara")
        raise Exception("Nunca se ejecutara esta segunda")

    def call_exceptor(self):
        print("[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]")
        print("La funcion call_exceptor() comienza aqui")
        self.sin_vuelta()
        #----------------------------
        print("A partir de la linea anterior no se ejecutara nada")


    def division_jajas(self, num):
        print("[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]")
        print("La funcion division_jajas() comienza aqui")
        try:
            return 100 / num
        except ZeroDivisionError:    
            print("--------------Segunda prueba---------------")
            print("No se puede dividir entre cero") 

    def division_jajas2(self, num):
        print("[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]")
        print("La funcion division_jajas2() comienza aqui")
        try:
            if num == 13:
                raise ValueError("13 agarramela que me crece")
            return 100 / num
        except (ZeroDivisionError, TypeError):    
            print("Introduce un numero diferente a cero")

    def division_jajas3(self, num):
        print("[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]")
        print("La funcion division_jajas3() comienza aqui")
        try:
            if num == 13:
                raise ValueError("13 agarramela que me crece")
            return 100 / num
        except ZeroDivisionError:    
            print("Introduce un numero diferente a cero")
        except TypeError:
            print("Introduce un numero")
        except ValueError:
            print("No aprendes o que chaval, el 13 no!")
            raise