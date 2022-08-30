import pytest
from .lista_estadistica import ListaEstadistica


@pytest.fixture
def estadisticas_validas():
    return ListaEstadistica([1, 2, 2, 3, 3, 4])


def test_mean(estadisticas_validas):
    assert estadisticas_validas.mean() == 2.5


def test_median(estadisticas_validas):
    assert estadisticas_validas.median() == 2.5
    estadisticas_validas.append(4)
    assert estadisticas_validas.median() == 3


def test_mode(estadisticas_validas):
    assert estadisticas_validas.mode() == [2, 3]
    estadisticas_validas.remove(2)
    assert estadisticas_validas.mode() == [3]