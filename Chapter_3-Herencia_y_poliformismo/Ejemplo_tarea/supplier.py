from contact import Contact

class Suplier(Contact):
    
    def order(self, order):
        print("Si tuviese funcionalidad mandaria " f"'{order}' order to '{self.name}'")