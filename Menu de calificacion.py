import pandas as pd
import numpy as np
from scipy import stats
import sys
import sqlite3
from sqlite3 import Error

op = 0
while (op!=6):
    print()
    print("1.-Registrar Alumno")
    print("2.-Calificacion y Materia")
    print("3.-Mostrar Registros")
    print("4.-Guardar Registros en la Base De Datos")
    print("5.-Salir")
    op = int(input("Dame La Opcion:"))
    if (op==1):
        
        Nombre = []
        Matricula = []
        print("Registrar Alumno")
        nom = input("Nombre: ")
        mat = input("Matricula: ")
        codigo = input("Codigo Materia: ")
        Clv_Periodo = input("Ingresa La Clave Periodo: ")
        Campo_Periodo = input("Ingresa El Periodo: ")
        Nombre.append([nom])
        Matricula.append([mat])
        
    if (op==2):
        numeroCalificaciones = int(input("Agrega sola una calificacion: "))
        suma = 0
        calificaciones = []
        Materia = []
        for i in range(0, numeroCalificaciones):
            mate = input("Nombre De La Materia:")
            Materia.append([mate])
            calificacion = int(input("ingrese calificacion" + str(i) + ":"))
            calificaciones.append(calificacion)
            suma = suma + calificacion
        promedio = suma / numeroCalificaciones
        print()
        for i in range(0, numeroCalificaciones):
            if calificaciones[i] >= 70:
                print(str(calificaciones[i])+ "calificacion aprobada")
            else:
                print(str(calificaciones[i])+ "calificacion no aprobada")
        print()
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
                print(mate, calificaciones)
    if (op==4):
        print("Guardando registros en una base de datos")
        try:
            with sqlite3.connect('TablaAlumnos.db') as conn:
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS Alumno(Matricula INTEGER PRIMARY KEY, Nombre VARCHAR(50), Clave_Periodo INTEGER);')
                c.execute('CREATE TABLE IF NOT EXISTS Periodo(Clave_Periodo INTEGER PRIMARY KEY, Periodo VARCHAR(50), FOREIGN KEY (Clave_Periodo) REFERENCES Alumno(Clave_Periodo));')
                c.execute('CREATE TABLE IF NOT EXISTS Materia(Cod_Materia INTEGER PRIMARY KEY, Nombre VARCHAR(50));')
                c.execute('CREATE TABLE IF NOT EXISTS Calif_M(Matricula INTEGER PRIMARY KEY, Cod_Materia INTEGER NOT NULL, Resultado INTEGER NOT NULL, FOREIGN KEY(Matricula) REFERENCES Alumno(Matricula), FOREIGN KEY(Cod_Materia) REFERENCES Materia(Cod_Materia));')
                print("Tabla creada exitosamente")
        except Error as e:
            print(e)
        except:
            print(f'Se produjo el siguiente error: {sys.exc_info()[0]}')
               
        try:
             with sqlite3.connect('TablaAlumnos.db') as conn:
                mi_cursor = conn.cursor()
                variable = {"Matricula":mat, "Nombre":nom, "Clave_Periodo":Clv_Periodo}
                mi_cursor.execute("INSERT INTO Alumno VALUES(:Matricula,:Nombre,:Clave_Periodo)", variable)
                
                periodos = {"Clave_Periodo":Clv_Periodo, "Periodo":Campo_Periodo}
                mi_cursor.execute("INSERT INTO Periodo VALUES(:Clave_Periodo,:Periodo)", periodos)
                
                registros =  {"Cod_Materia":codigo, "Nombre":mate}
                mi_cursor.execute("INSERT INTO Materia VALUES(:Cod_Materia,:Nombre)", registros)
                
                valores = {"Matricula":mat, "Cod_Materia":codigo, "Resultado":calificacion}
                mi_cursor.execute("INSERT INTO Calif_M VALUES(:Matricula,:Cod_Materia,:Resultado)", valores)
                print("REGISTRO NUEVO AGREGADO TABLA ALUMNO")
                print("")
        except Error as e:
            print(e)
        except:
            print(f'Se produjo el siguiente error: {sys.exc_info()[0]}')
            
        try:
            with sqlite3.connect('TablaAlumnos.db') as conn:
                mi_cursor = conn.cursor()
                mi_cursor.execute('SELECT * FROM Alumno')
                datos = c.fetchall()
                print(datos)
                      try:
                          with sqlite3.connect('TablaAlumnos.db') as conn:
                              mi_cursor = conn.cursor()
                              mi_cursor.execute('SELECT * FROM Alumno')
                #mi_cursor.execute('SELECT * FROM Periodo')
                #mi_cursor.execute('SELECT * FROM Materia')
        
                datos = mi_cursor.fetchall()
                print(datos)
        except Error as e:
            print(e)
        except:
            print(f'Se produjo el siguiente error: {sys.exc_info()[0]}')
        finally:
            conn.close()
    if (op==5):
        print("Cerrar")
        break;
