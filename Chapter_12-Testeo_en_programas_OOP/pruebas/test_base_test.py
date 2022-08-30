def setup_module(module):
    print("Configurando el MODULO {0} ".format(module.__name__))

def teardown_module(module):
    print("Limpiando el MODULO {0} ".format(module.__name__))

def test_una_funcion():
    print("Ejecutando una funcion")


class ClaseBase:
    def setup_class(cls):
        print("Configurando la CLASE {0} ".format(cls.__name__))

    def teardown_class(cls):
        print("Limpiando la CLASE {0} ".format(cls.__name__))

    def setup_method(self, metodo):
        print("Configurando el METODO {0} ".format(metodo.__name__))

    def teardown_method(self, metodo):
        print("Limpiando el METODO {0} ".format(metodo.__name__))

class TestClase1(ClaseBase):
    def test_metodo_1(self):
        print("Ejecutando el METODO 1-1")
    
    def test_metodo_2(self):
        print("Ejecutando el METODO 1-2")

class TestClase2(ClaseBase):
    def test_metodo_1(self):
        print("Ejecutando el METODO 2-1")
    
    def test_metodo_2(self):
        print("Ejecutando el METODO 2-2")