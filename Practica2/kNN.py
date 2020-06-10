
#Práctica No.2
#Descripción: Implementación del algoritmo kNN
#Fecha de creación: 25 de noviembre del 2019
#Autor: Joaquín Domínguez Moran
#Fecha de actualización: 

#Librerias 
from scipy.spatial import distance
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#Función para calcular la distancia euclidiana
#Descripción: 
#Entrada:Dos patrones
#Salida: Su distancia euclidia

def euclidianDistance(data1, data2):
	return distance.euclidean(data1, data2)  

def ecribirPatron(name,patron):
	values = ",".join(map(str, patron))
	f = open (name,'a')
	f.write(values)
	f.write("\n")
	f.close()
	return

def tableDistance(patron,class1,class2):
	table=[]
	for x in range(len(class1)):
		row=[]
		for y in range(4):
			row.append(class1.iloc[x,y])
		dst=euclidianDistance(patron,row)
		row.append(class1.iloc[x,4])
		row.append(dst)
		table.append(row)

	for x in range(len(class2)):
		row=[]
		for y in range(4):
			row.append(class2.iloc[x,y])
		dst=euclidianDistance(patron,row)
		row.append(class2.iloc[x,4])
		row.append(dst)
		table.append(row)
	return table

def selectNeighbors(testeo,k):
	return testeo.head(int(k))

def centroide(clas):
	z=[]
	for x in range(4):
		aux=0
		for y in range(len(clas)):
			aux+=clas.iloc[y,x]
		aux=aux/len(clas)
		z.append(aux);
	return z


def distanciaMinima(patron,class1,class2):
	centro1=centroide(class1)

	centro2=centroide(class2)

	dst1=euclidianDistance(centro1,patron)
	dst2=euclidianDistance(centro2,patron)
	if dst1>dst2:
		print("El patron pertecene a la clase Iris-versicolor")
		patron.append("Iris-versicolor")
		ecribirPatron("Iris-versicolor.data",patron)
	else:
		print("El patron pertecene a la clase Iris-setosar")
		patron.append("Iris-setosa")
		ecribirPatron("Iris-setosa.data",patron)
	return

def distanciaMedia(testeo,patron):

	class1=testeo[testeo['class'] == 'Iris-setosa']
	class2=testeo[testeo['class'] == 'Iris-versicolor']
	tam1=len(class1)
	tam2=len(class2)

	if tam1>0:
		promclass1=class1['distance'].sum()/ len(class1)
	else:
		promclass1=0
	if tam2>0:
		promclass2=class2['distance'].sum()/ len(class2)
	else:
		promclass2=0

	if promclass1>promclass2:
		print("El patron pertecene a la clase Iris-setosa")
		ecribirPatron("Iris-setosa.data",patron)
	else: 
		print("El patron pertecene a la clase Iris-versicolor")
		ecribirPatron("Iris-versicolor.data",patron)
	return

def clasificador(patron,testeo,clas1,clas2,):
	class1=len(testeo[testeo['class'] == 'Iris-setosa'])
	class2=len(testeo[testeo['class'] == 'Iris-versicolor'])
	if class1>class2:
		print("El patron pertecene a la clase Iris-setosa")
	elif class2>class1:
		print("El patro n pertecene a la clase Iris-versicolor")
	elif class1==class2:
		print("Surgio un empate, indique que metodo desa utilizar para el desempate")
		print("1. Distancia Minima")
		print("2. Distancia Media")
		opcion=input()
		if opcion==1:
			distanciaMinima(patron,clas1,clas2)
		else:
			distanciaMedia(testeo,patron)
	return
#Función principal 
#Descripción: Se carga el dataset de Iris
#Entrada:
#Salida: Grafica del dataset


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

	print("Bienvenido al pograma de clasificación de iris con el algoritmo k-NN")
	print("A conitnuación se muestran los histograma de las clases y el conjunto de estrenamiento")
	plt.show()
	print("Ingrese el K deseado")
	k=input()

	for x in range(len(testeo)):
		row=[]
		for y in range(4):
			row.append(testeo.iloc[x,y])
		tb=pd.DataFrame(tableDistance(row,iris_setosa,iris_versicolour),columns=["sepal length","sepal width","petal length","petal width","class", "distance"])
		tb=tb.sort_values(by='distance', ascending=True)
		neighbors= selectNeighbors(tb,k)
		print(neighbors)
		clasificador(row,neighbors,iris_setosa,iris_versicolour)
		print("Acontiuación se simulan los desempates")	
		print("Distancia Minima")
		distanciaMinima(row,iris_setosa,iris_versicolour)
		print("DistanciaMedia")	
		distanciaMedia(neighbors,row)
		
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
	


