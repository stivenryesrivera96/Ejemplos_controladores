class Estudiante:
   #                    100      Pepe   15 [3,4,5,4.5]
    def _init_(self,documento,nombre,edad,notas):
        #    100 
        self.documento=documento
        #   Pepe
        self.nom=nombre
        #    15
        self.edad=edad
        #  [3,4,5,4.5]
        self.notas=notas
    #    4.1
        self.estado="Activo"
    def promedio(self):
    #    4.1                    16.5             4
      calculo_promedio=sum(self.notas)/len(self.notas)
      #          4.1
      return calculo_promedio
    
    def getnombre(self):
       return self.nom