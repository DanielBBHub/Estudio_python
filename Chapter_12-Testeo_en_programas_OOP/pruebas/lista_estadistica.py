from collections import defaultdict

class ListaEstadistica(list):
    def mean(self):
        return sum(self) / len(self)

    def median(self):
        if len(self) % 2:
            return self[int(len(self) / 2)]
        else:
            indice = int(len(self) / 2)
            return (self[indice] + self[indice + 1]) / 2

    def mode(self):
        frequs = defaultdict(int)
        for v in self:
            frequs[v] += 1
        
        mode_freq = max(frequs.values())
        modes = []
        for llave, valor in frequs.items():
            if valor == mode_freq:
                modes.append(llave)
        
        return modes