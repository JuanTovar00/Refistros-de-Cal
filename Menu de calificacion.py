import pandas as pd
import numpy as np
import json 
from scipy import stats
op = 0
while (op!=5):
    
    print("1.-Registrar Alumno")
    print("2.-Calificacion y Materia")
    print("3.-Mostrar Registros")
    print("4.-Salir")
       
    op = int(input("Dame La Opcion:"))
 
    if (op==1):
        Nombre = []
        print("Registrar Alumno")
        nom = input("Nombre:")
        Nombre.append([nom])
    
         
    if (op==2):
        numeroCalificaciones = int(input("Dame el número total de calificaciones: "))
        suma = 0
        calificaciones = []
        Materia = []

        for i in range(0, numeroCalificaciones):
            
            Materias = input("Nombre De La Materia:")
            Materia.append([Materias])
            calificacion = int(input("ingrese calificacion" + str(i) + ":"))
            calificaciones.append(calificacion)
            suma = suma + calificacion

        promedio = suma / numeroCalificaciones

        for i in range(0, numeroCalificaciones):
                
            if calificaciones[i] >= 70:
                print(str(calificaciones[i])+ "calificacion aprobada")
            else:
                print(str(calificaciones[i])+ "calificacion no aprobada")
    
        print("Los Datos Obtenidos son: ")
        media=np.mean(calificaciones)
        mediana=np.median(calificaciones)
        moda=stats.mode(calificaciones)
        desviacionEstandar=np.std(calificaciones)
        print("La Media es :", media)
        print("La Mediana es: ", mediana)
        print("La Moda es: ", moda)
        print("La Desviacion Estandar: ", desviacionEstandar)
        print("El Promedio Del Alumno es:", promedio)
       
    if (op==3):
        print("Mostrando Registros")
        for i in Nombre:
            print(nom)
            
            for i in calificaciones:
                print(Materias, calificaciones)
        datos =json.dumps(Nombre)
        datosM =json.dumps(Materia)
        datosC =json.dumps(calificaciones)
        f = open ('notas.txt', 'w')
        f.write(datos)
        f.write(datosM)
        f.write(datosC)
        f.close()
        
        
    if (op==4):
        print("Cerrar")
        break;





