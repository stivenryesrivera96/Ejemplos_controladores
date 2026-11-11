from modelo import Estdiante
from vista import VistaEstudiante

class controladorEstudiante:
    def __init__(self):
        self.vista=VistaEstudiante()
        
    def enviar(self):
        doc,nom,edad,notas=self.vista.pedir_datos_estudiantes()
        
        estudiante=Estdiante(doc,nom,edad,notas)
        
        prom=estudiante.promedio()
        nombre=estudiante.getnombre()
        self.vista.mostrar_resultado(nombre,prom)
        
if __name__=="__main__":
    app=controladorEstudiante()
    app.enviar()
        
