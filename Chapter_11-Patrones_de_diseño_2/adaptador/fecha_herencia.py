import datetime

class FechaHerencia(datetime.date):
    def split(self, char):
        return self.year, self.month, self.day