# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:56:19 2020

@author: USR
"""

import csv

lista_datos = []                                                                #Creamos una lista donde se almacenarán los datos


with open('synergy_logistics_database.csv','r') as archivo_csv:                 #Cargamos la base de datos
	lector = csv.reader(archivo_csv)
	for linea in lector:
		lista_datos.append(linea)                                               #Almacenamos los datos en la lista creada


###############################################################################

################ Función para el conteo de rutas #####################

def rutasTodas(direccion):
    contador = 0                                                                  #Hacemos un contador igual a cero             
    rutas_contadas = []
    conteo_rutas= []
    for ruta in lista_datos:                                                    #Ruta recorre las 19057 listas, Al pasar ruta por cada lista, en cada iteración
                                                                                #Contiene 9 elementos
        if ruta[1] == direccion:                                                #Si ruta[1] o sea dirección es igual a importación o exportación 
            ruta_actual =[ruta[2],ruta[3]]                                      #Una nueva variable llamada ruta_actual va a contener dos valores 
                                                                                #Que son los países de origen y destino
            if ruta_actual not in rutas_contadas:                               #Si ruta_actual no está en listas contadas, (Que en un 
                                                                                #inicio no lo estará), se hace la siguiente operación
                for movimiento in lista_datos:                                  #Pasar movimiento por todas las listas
                    if ruta_actual == [movimiento[2],movimiento[3]]:            #Si se repite le agregamos una al contador
                        contador +=1       
                rutas_contadas.append(ruta_actual)                              #Agregamos ruta_actual a rutas_contadas
                conteo_rutas.append([ruta[2],ruta[3],contador]) 
                contador = 0
                conteo_rutas.sort(reverse = True, key = lambda x:x[2])
    return conteo_rutas

rutas_exportacion_todas = rutasTodas('Exports')                                 #Guardamos el conteo de rutas de exportaciones en una lista
rutas_importacion_todas = rutasTodas('Imports')                                 #Guardamos el conteo de rutas de importaciones en una lista


###############################################################################


        
input('Las cinco rutas más demandas de exportación por año son (presiona Enter) \n')

input('Las rutas de exportación más solicitadas desde 2015 a 2020: \n')
for i in rutas_exportacion_todas[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'exportaciones. \n' )

print('*******************************************************************')


input('Las rutas de importación más solicitadas desde 2015 a 2020: \n')
for i in rutas_importacion_todas[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )
    
    
    
exportacionesfalso = []                                                         #Creamos dos listas provisionales
importacionesfalso = []                                                         #para exportación e importación


def direction(direccion,lista_e_i):                                             #Creamos una función para almacenar 
                                                                                #listas de exportación e importación                     
    for i in lista_datos:
        if i[1] == direccion:
            lista_e_i.append(i)
    return lista_e_i

            
exportaciones = direction('Exports',exportacionesfalso)                         #Guardamos lista de exportación
importaciones = direction('Imports',importacionesfalso)                         #Guardamos lista de importación


###############################################################################
####################### CREAMOS LISTAS POR ANHO  ##############################
###############################################################################


e2015 = []
e2016 = []
e2017 = []
e2018 = []
e2019 = []
e2020 = []
i2015 = []
i2016 = []
i2017 = []
i2018 = []
i2019 = []
i2020 = []


## Creamos dos funciones, para almacenar los datos por anhos, una de exportación y una de importación 

def anhose(anho,lista_anhos):                                               
    for i in exportaciones:
        if i [4] == anho:
            lista_anhos.append(i)
    return lista_anhos

def anhosi(anho,lista_anhos):
    for i in importaciones:
        if i [4] == anho:
            lista_anhos.append(i)
    return lista_anhos




################ Función para el conteo de rutas por anho #####################
def rutas(anhoe):
    contador = 0                                            
    rutas_contadas = []
    conteo_rutas= []
    for ruta in anhoe:
        ruta_actual =[ruta[2],ruta[3]]
        if ruta_actual not in rutas_contadas:
            for movimiento in anhoe:
                if ruta_actual == [movimiento[2],movimiento[3]]:
                    contador +=1
            rutas_contadas.append(ruta_actual)          
            conteo_rutas.append([ruta[2],ruta[3],contador]) 
            contador = 0
            conteo_rutas.sort(reverse = True, key = lambda x:x[2])

    return conteo_rutas

####################### Almacenamos las rutas obtenidas ######################

resnha2015e = rutas(anhose('2015',e2015))
resnha2016e = rutas(anhose('2016',e2016))
resnha2017e = rutas(anhose('2017',e2017))
resnha2018e = rutas(anhose('2018',e2018))
resnha2019e = rutas(anhose('2019',e2019))
resnha2020e = rutas(anhose('2020',e2020))
resnha2015i = rutas(anhosi('2015',i2015))
resnha2016i = rutas(anhosi('2016',i2016))
resnha2017i = rutas(anhosi('2017',i2017))
resnha2018i = rutas(anhosi('2018',i2018))
resnha2019i = rutas(anhosi('2019',i2019))
resnha2020i = rutas(anhosi('2020',i2020))

    
input('Las cinco rutas más demandas de exportación por año son (presiona Enter) \n')

input('Las rutas de exportación más solicitadas en 2015: \n')
for i in resnha2015e[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'exportaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de exportación más solicitadas en 2016: \n')
for i in resnha2016e[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'exportaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de exportación más solicitadas en 2017: \n')
for i in resnha2017e[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'exportaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de exportación más solicitadas en 2018: \n')
for i in resnha2018e[0:5]:
    print('La ruta de origen de ',i[0],'con destino ',i[1], 'tuvo ', i[2], 'exportaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de exportación más solicitadas en 2019: \n')
for i in resnha2019e[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'exportaciones. \n' )

print('*******************************************************************')
input('Las rutas de exportación más solicitadas en 2020: \n')
for i in resnha2020e[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'exportaciones. \n' )
    






input('Las cinco rutas más demandas de importaciones por año son (presiona Enter) \n')

input('Las rutas de importación más solicitadas en 2015: \n')
for i in resnha2015i[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de importación más solicitadas en 2016: \n')
for i in resnha2016i[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de importación más solicitadas en 2017: \n')
for i in resnha2017i[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de importación más solicitadas en 2018: \n')
for i in resnha2018i[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )
    
print('*******************************************************************')
input('Las rutas de importación más solicitadas en 2019: \n')
for i in resnha2019i[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )

print('*******************************************************************')
input('Las rutas de importación más solicitadas en 2020: \n')
for i in resnha2020i[0:5]:
    print('La ruta de origen de ',i[0],'con destino',i[1], 'tuvo ', i[2], 'importaciones. \n' )
    




valoresE_S_V = []
valoresE_N_B = []
valoresI_J_M = []
valoresI_C_J = []

def valores(direccion, origen, destino,valor):
    for x in direccion:
        if(x[2]== origen and x[3]==destino):
            valor.append(int(x[9]))
    return valor

Exp_South_Korea_Vietnam = valores(exportaciones, 'South Korea', 'Vietnam',valoresE_S_V)
Exp_Netherlands_Belgium = valores(exportaciones, 'Netherlands', 'Belgium',valoresE_N_B)

Imp_Japan_Mexico = valores(importaciones, 'Japan', 'Mexico',valoresI_J_M)
Imp_China_Japan = valores(importaciones, 'China', 'Japan',valoresI_C_J)


def promedio(lista):
    suma=0
    for valor in lista:
        suma+=valor
        return int(suma/(len(lista)))

PromedioExp1 = promedio(Exp_South_Korea_Vietnam)
PromedioExp2 = promedio(Exp_Netherlands_Belgium)
PromedioImp1 = promedio(Imp_Japan_Mexico)
PromedioImp2 = promedio(Imp_China_Japan)

listaPromedio = [['exportación','South Korea', 'Vietnam',PromedioExp1], 
                 ['exportación','Netherlands', 'Belgium',PromedioExp2], 
                 ['importación','Japan', 'Mexico', PromedioImp1],
                 ['importación','China', 'Japan', PromedioImp2]]
input('Dado lo anterior, las rutas de South Korea-Vietnam, Netherlands-Belgium son las más solicitadas de exportación, mientras que las de Japan-Mexico, China-Japan son las más solicitadas de importación.\n ')

print('Estás rutas tuvieron en promedio las siguientes ganacias por exportación e importación:')
for i in listaPromedio: 
    print('La ruta de', i[0], 'de origen en', i[1], 'hacia',i[2],'en promedio tuvo ganancias de',i[3], 'por viaje. \n' )