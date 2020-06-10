#Práctica No.4
#Descripción: Implementación del algoritmo LearnMatrix
#Fecha de creación: 25 de noviembre del 2019
#Autor: Joaquín Domínguez Moran
#Fecha de actualización: 

#Librerias 
from scipy.spatial import distance
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
#Función para imprimir la LearnMatrix
#Entrada: clase, patron, matrix,número de rasgos,número de patrones,patron que se desea calcular
def imprimir(clase,patron,m,p,n,i):
    print("", end="\t")
    for k in range(n):
        print(patron[i][k],end="\t")
    print("\n")

    for x in range(p):
        print(clase[i][x],end="\t")
        for y in range(n):
            if m[x][y]==1:
                print("ε",end="\t")
            elif m[x][y]==-1:
                print("-ε",end="\t")
            else:
                print(m[x][y],end="\t")
        print("\n")     
    return
#Función para la etapa de aprendizaje
#Entrada: Númmero de rasgos,número de patrones, clase y patron
#Salida: Matriz

def aprendizaje(p,n,clase,patron):
    print("Paso1: Inicializar la LearnMatrix con los elementos mij=0")
    m = np.zeros((p, n))
    print(m)
    print("Paso2: Iniciamos la fase de aprendizaje")

    for i in range(p):
        print("Iteracion: "+str(i)+" clase y:"+str(i)+"con patron x"+str(i))
        for j in range(n):
            if clase[i][i]==patron[i][j]:
                m[i][j]=1
            else:
                m[i][j]=-1
        imprimir(clase,patron,m,p,n,i)
    return m

#Función para multiplicar los patrones por la LearnMatrix
#Entrada: patron, matrix, número de rasgos y número de patrones
#Salida: Vector resultante de la multiplicación
def mult(patron,m,n,p):
    result=[]
    print()
    for x in range(p):
        sum=0
        for y in range(n):
            sum+=patron[y]*m[x][y]
        result.append(sum)
    return result
#Función para determina cual es la clase resultante
#Entrada:Patron
#Salida: Clase a la que pertenece
def max(vector):
    max=vector[0]
    index=0
    for x in range(len(vector)):
        if vector[x]>max:
            max=vector[x]
            index=x
    return index
#Función para la recuperación
#Entrada: patron, matriz, número de clases, número de patrones
def recuperacion(patron,m,n,p):
    for i in range(len(patron)):
        print("Iteracion de recuperación:  "+str(i)+" de el patron x "+str(i)+"por M")
        r=mult(patron[i],m,n,p)
        clase=max(r)

        print("Patron x"+str(i))
        print(np.matrix(patron[i]).transpose())
        print("Resultado de la multiplicacion de M por el patron x"+str(i))
        print(np.matrix(r).transpose())
        print("El patron x "+str(i)+"pertenece a la clase "+str(clase))
    return 
#Función para estimar el ruido
def ruido(patron,m,n,p):
    r=mult(patron,m,n,p)
    clase=max(r)
    print("Patron desconocido")
    print(np.matrix(patron).transpose())
    print("Resultado de la multiplicacion de M por el patron desconocido")
    print(np.matrix(r).transpose())
    print("El patron x desconocido pertenece a la clase "+str(clase))
    return 

def main():
    #Inicializamos las clases con sus respectivos patrones
    clases=pd.read_csv("clases.data")
    patrones=pd.read_csv("patrones.data")
    clase=[]
    patron=[]
    for x in range(len(clases)):
        row=[]
        for y in range(len(clases.columns)):
            row.append(clases.iloc[x,y])
        clase.append(row)

    for x in range(len(patrones)):
        row=[]
        for y in range(len(patrones.columns)):
            row.append(patrones.iloc[x,y])
        patron.append(row)
    print("Bienvenido al programa que implementa la LearnMatrix")
    p=len(clases)
    n=len(patrones.columns)

    print("El valor de p es:")
    print(p)
    print("El valor de n es:")
    print(n)
    print("Fase de aprendizaje")
    #Fase de aprendizaje 
    m=aprendizaje(p,n,clase,patron)
    print("Fase de recuperación")
    #Fase de recuperación
    recuperacion(patron,m,n,p)
    print("Fase de prueba con ruido")
    #Fase de recuperación
    while True:
        print("Ingrese el número de patron que desea alterar")
        index=input()
        pt=patron[int(index)]
        while True:
            print(np.matrix(pt).transpose())
            print("Ingrese la posición que desea alterar")
            pos=input()
            print("Ingrese valor de alteración")
            val=input()
            pt[int(pos)]=int(val)
            print(np.matrix(pt).transpose())
            print("Ingrese S si desea hacer otra alteración")
            op=input()
            if(op != "S"):
                break
        ruido(pt,m,n,p)
        print("Ingrese S si desea hacer otra prueba")
        op=input()
        if(op != "S"):
            break
main()