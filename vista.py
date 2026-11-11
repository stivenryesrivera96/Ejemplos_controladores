class VistaEstudiante:
    def pedir_datos_estudiantes(self):
        print("\n---Registro de estudiante ---")
        doc=int(input("Digite el docuemnto del estudiante: "))
        nom=input("Digite el nombre del estudiante ")
        edad=int(input("Digite la edad del estidiante "))
        numero_notas=int(input("Digite el número de notas del estudiante "))
        notas=[]
        
        for i in range(numero_notas):
            n=float(input(f"Digite la nota {i+1} "))
            notas.append(n)
            
        return doc,nom,edad,notas
    
    def mostrar_resultado(self,nombre,promedio):
        print(f"Promedio final del estudiante {nombre} es de {promedio:.1f}")
        
        
            
                
       