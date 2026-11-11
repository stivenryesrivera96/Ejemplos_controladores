class Estdiante:
    
    def __init__(self,documento,nombre,edad,notas):
        
        self.documento=documento
        self.nombre=nombre
        self.edad=edad
        self.notas=notas
        
    def getnombre(self):
        return self.nombre
    
    def promedio(self):
        calculo_promedio=sum(self.notas)/(len(self.notas))
        return calculo_promedio
        
    