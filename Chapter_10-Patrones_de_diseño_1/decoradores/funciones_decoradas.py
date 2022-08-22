import time

def llamadas_log(funcion):

    def envoltorio(*arg, **kwarg):
        ahora = time.time()

        print(
            "Llamando {0} a {1} y {2}".format(funcion.__name__, arg, kwarg)
        )
        valor_devuelto = funcion(*arg, **kwarg)

        print(
            "Ejecutada {0} en {1}ms".format(funcion.__name__, time.time() - ahora)
        )
        return valor_devuelto

    return envoltorio

