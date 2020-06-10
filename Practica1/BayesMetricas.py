#Práctica No.1
#Descripción: Implementación de clasificadores bayesianos y basados en metricas
#Fecha de creación: 26 de noviembre del 2019
#Autor: Joaquín Domínguez Moran
#Fecha de actualización: 

#Librerias 
from scipy.spatial import distance
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import math

#Función para calcular la distancia euclidiana
#Entrada:Dos patrones
#Salida: Su distancia euclidia
def euclidianDistance(data1, data2):
	return distance.euclidean(data1, data2)

#Función para calcular la distancia city block
#Entrada:Dos patrones
#Salida: Su distancia euclidia
def CBDistance(data1, data2):
	return distance.cityblock(data1, data2)

#Función para calcular la distancia infinita
#Entrada:Dos patrones
#Salida: Su distancia euclidia
def infinitaDistance(data1, data2):
	return distance.chebyshev(data1, data2)

#Función para calcular el centrodide de una clase
#Entrada: Una clase
#Salida: Patron representativo

def centroide(clas):
	z=[]
	for x in range(4):
		aux=0
		for y in range(len(clas)):
			aux+=clas.iloc[y,x]
		aux=aux/len(clas)
		z.append(aux);
	return z
#Función para escribir un patron en un archivo
#Entrada: El nombre del archivo y el patron
def ecribirPatron(name,patron):
	values = ",".join(map(str, patron))
	f = open (name,'a')
	f.write(values)
	f.write("\n")
	f.close()
	return
#Función para clasidicar de acuerdo a la distancia
#Entrada: Una patron, dos clases y la distancia deseada
def distancia(patron,class1,class2,op):
	centro1=centroide(class1)
	centro2=centroide(class2)
	dst1=0
	dst2=0

	if op=="1":
		dst1=CBDistance(centro1,patron)
		dst2=CBDistance(centro2,patron)
	if op=="2":
		dst1=euclidianDistance(centro1,patron)
		dst2=euclidianDistance(centro2,patron)
	if op=="3":
		dst1=infinitaDistance(centro1,patron)
		dst2=infinitaDistance(centro2,patron)
	if dst1>dst2:
		print("El patron pertecene a la clase Iris-versicolor")
		patron.append("Iris-versicolor")
		ecribirPatron("Iris-versicolor.data",patron)
	else:
		print("El patron pertecene a la clase Iris-setosa")
		patron.append("Iris-setosa")
		ecribirPatron("Iris-setosa.data",patron)

#Función para estimar el clasificador basado en la teoría de la probabilidad
#Entrada: Dos clases

def probalidad(class1,class2):
	C1=len(class1)
	C2=len(class2)
	S= C1+ C2

	PC1=C1/S
	PC2=C2/S
	print("La cardinalidad de S es:")
	print(S)
	if PC1>PC2:
		print("El patron pertecene a la clase Iris-setosa")
		print("Probabilidad de C1:",PC1)
	else:
		print("El patron pertecene a la clase Iris-versicolor")
		print("Probabilidad de C2:",PC2)
	return

#Función para estimar el clasificador bayesiano simple
#Entrada: Dos clases y un conjunto de prueba
def bayesiano(class1,class2,testeo):

	espacio=pd.concat([class1, class2])
	C1=len(class1)
	C2=len(class2)
	S= C1+ C2
	PC1=C1/S
	PC2=C2/S
	print("El bayesiano simple para Iris es con base al rago sepal-length")
	print("El mínimo es:")
	min=espacio['sepal length'].min()
	print(min)
	print("El máximo es:")
	max=espacio['sepal length'].max()
	print(max)
	table=[]
	i=min
	row=[]

	while i<max:
		j=0
		for x in range(len(class1)):
			aux=float(class1.iloc[x,0])
			if abs(aux-i) < 1e-10:
				j+=1
		row.append(j)
		i+=0.1
	table.append(row)


	i=min
	row=[]	
	while i<max:
		j=0
		for x in range(len(class2)):
			aux=float(class2.iloc[x,0])
			if abs(aux-i) < 1e-10:
				j+=1
		row.append(j)
		i+=0.1
	table.append(row)
	#Generación de la tabla de frecuencias
	print("Tabla de Frecuencias")
	tb=pd.DataFrame(table,columns=["4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0","5.1","5.2","5.3","5.4","5.5","5.6","5.7","5.8","5.9","6.0","6.1","6.2","6.3","6.4","6.5","6.6","6.7","6.8","6.9","7.0"])
	print(tb)
	#Generación de la tabla de probabilidades
	print("Tabla de probabilidad")

	card1=len(class1)
	card2=len(class2)

	columns=len(tb.columns)
	for y in range(columns):
		tb.iloc[0,y]=tb.iloc[0,y]/card1

	for y in range(columns):
		tb.iloc[1,y]=tb.iloc[1,y]/card2
	print(tb)
	tb.plot(kind='bar')
	#Determinación de a que clase pertenece
	for x in range(len(testeo)):
		aux=str(testeo.iloc[x,0])
		print("Probabilidades de que el patron se clasifique en cada clase")
		pro=tb[aux]
		print(pro)

		if PC1!=0 and pro[0]!=0: 
			d1=math.log(PC1)+math.log(pro[0])
		else:
			d1=0
		if PC2!=0 and pro[1]!=0: 
			d2=math.log(PC2)+math.log(pro[1])
		else:
			d2=0

		if  d1 > d2:
			print("El patron pertenece a la clase Iris-setosa")
		else:
			print("El patron pertenece a la clase iris_versicolour")
	return

#Función para estimar el clasificador euclidiano
#Entrada: Dos clases y un conjunto de prueba
def euclidiano(class1,class2,testeo):

	#Calculo de centrodides de cada clase
	centro1=np.matrix(centroide(class1))
	centro2=np.matrix(centroide(class2))

	print("Centroide de la clase iris_setosa")
	print(centro1)
	print("Centroide de la clase iris_versicolour")
	print(centro2)
	
	ds1=0
	ds2=0
	ds=0
	#Generación de funciones discriminantes
	for x in range(len(testeo)):
		row=[]
		for y in range(4):
			row.append(testeo.iloc[x,y])
		
		row=np.matrix(row)
		dst1=np.subtract(centro1,centro2).transpose()
		ds1=np.sum(np.dot(dst1,row))

		dst2=np.subtract(centro1,centro2).transpose()
		ds2= np.sum((np.dot(dst2,(centro1+centro2)))/2)
		ds=ds1-ds2

		if ds>0:
			print("El patron pertenece a la clase Iris-setosa")
		else:
			print("El patron pertenece a la clase iris_versicolour")

		
	return

def main():
	#Inicializamos las clases con sus respectivos patrones
	col=["sepal length","sepal width","petal length","petal width","class"]
	iris_setosa=pd.read_csv("Iris-setosa.data",names=col)
	iris_versicolour=pd.read_csv("Iris-versicolor.data",names=col)
	testeo=pd.read_csv("testeo.data",names=col)

	# Diagrama de dispersion entre Petal.Length y Petal.Width 
	plt.figure(figsize=(10, 8))
	plt.scatter(iris_setosa["sepal length"],iris_setosa["sepal width"], 
				c='red', label='Setosa')
	plt.scatter(iris_versicolour["sepal length"],iris_versicolour["sepal width"], 
				c='green', label='Versicoluor')
	plt.scatter(testeo["sepal length"],testeo["sepal width"], 
				c='blue', label='testeo')
	plt.title('Tamaño del pétalo')
	plt.xlabel('Largo del pétalo (cm)')
	plt.ylabel('Ancho del pétalo (cm)')
	#Se muestra el conjunto de aprendizaje
	testeo=testeo.drop(["class"], axis=1)
	while True:
		print("Bienvenido al pograma de clasificación de iris")
		plt.show()
		print("A conitnuación se muestran los clasificadores disponibles")
		print("1.Estadísticos probabilisticos")
		print("2.Basados en métricas")
		op=input()

		if op=="1":
			print("Estás disponibles los clasificarores basados en :")
			print("1.Teoria de la probalidad")
			print("2.Bayesiano Simple")
			print("3.Euclidiano")
			op=input()
			if op=="1":
				probalidad(iris_setosa,iris_versicolour)
			elif op=="2":
				bayesiano(iris_setosa,iris_versicolour,testeo)
			elif op=="3":
				euclidiano(iris_setosa,iris_versicolour,testeo)

		else:
			print("Estás disponibles las distancias:")
			print("1.City Block")
			print("2.Euclidiana")
			print("3.Infinita")
			op=input()

			for x in range(len(testeo)):
				row=[]
				for y in range(4):
					row.append(testeo.iloc[x,y])
				distancia(row,iris_setosa,iris_versicolour,op)

		print("Si desea revisar otro clafisificador inngrese S")
		op=input()
		if op!="S":
			break;
		
	#Generación de gráfica despúes de la clasifiación
	col=["sepal length","sepal width","petal length","petal width","class"]
	iris_setosa=pd.read_csv("Iris-setosa.data",names=col)
	iris_versicolour=pd.read_csv("Iris-versicolor.data",names=col)
	plt.figure(figsize=(10, 8))
	plt.scatter(iris_setosa["sepal length"],iris_setosa["sepal width"], 
				c='red', label='Setosa')
	plt.scatter(iris_versicolour["sepal length"],iris_versicolour["sepal width"], 
				c='green', label='Versicoluor')
	plt.title('Tamaño del pétalo')
	plt.xlabel('Largo del pétalo (cm)')
	plt.ylabel('Ancho del pétalo (cm)')
	plt.show()


		
main()