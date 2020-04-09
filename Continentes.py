# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# encoding: latin1
"""
Created on Wed Apr  8 08:39:15 2020

@author: HCK - Michael Porras - Diego Huertas
"""


import codecs
import os
import time
import random
#from random import randint
opc = 0

#Header
def cabeza():
    os.system('cls')
    print("Fecha: ", time.strftime('%x'), "  Hora: ", time.strftime('%X'))
    print("Base de Conocimiento -BC- PAISES DEL MUNDO")
    print("===============================================================================\n")

# Menu Carga de archivo
def menu1():
    while True:
        global opc
        #os.system('cls')
        print('\n\n\n\n')
        cabeza()
        print(' 1. Cargar las listas Continentes y Paises.')
        print('99. Terminar')
           
        try:
            opc = int(input("Digite opción deseada ==> "))
            if opc == 1 or opc == 99:
               break
            else:
                print('Opción fuera de rango... Revise')
                input('Pulse <Enter> para continuar...')
                continue
        except: 
            continue
    #return(opc)    
   
def menu():
    while True:
        global opc
        os.system('cls')
        print('\n\n\n\n')
        cabeza()
        print('Manejo de archivos...')
        print('================================================================\n')
        print ("2. Paises por continente")
        print ("3. País con mayor/menor extensión por cada continente,")
        print (" extensión total continente.")
        print ("4. País con mayor/menor número de habitantes por cada continente,")
        print ("habitantes por continente.")
        print ("5. Consultar información sobre un país")
        print ("-------- Diálogo interactivo máquina vs usuario ------------")
        print ("6. Capital de un país seleccionado al azar")
        print ("7. Gentilicio de un país seleccionado al azar")
        print ("8. Cuál país tiene como capital... seleccionada al azar")
        print ("9. Cuál país tiene como gentilicio... seleccionado al azar")
        print ("10. A cuál continente pertenece un país seleccionado al azar.")
        print ("11. Ayudas...")
        print ("12. Acerca de...")
        print ("99. Terminar. \n")
           
        try:
            opc = int(input("Digite opción deseada ==> "))
            if (opc > 1 and opc <= 14) or opc == 99 :
               break
            else:
                print('Opción fuera de rango... Revise')
                input('Pulse <Enter> para continuar...')
                continue
        except: 
            continue
    #return(opc)
    
#Opcion 1 del menu 
def cargaListas() :
    cabeza()
    global nombre
    print("Cargar listas de Continentes y Paises.")
    nombre = input("Nombre del archivo a cargar: ")
    try:
        global Lcontinente
        global Lpais
        global swfile  
        swfile = False
        ctr = 0
        Lcontinente.clear()
        Lpais.clear()
        with codecs.open(nombre,"r","utf-8") as study:
            for line in study:
                ctr += 1
                if line.startswith("#"):
                    continue  
                line = line.rstrip() #remueve espacios a la derecha de la cadena
                line = line.split(",")
                if(len(line) == 2):
                    Lcontinente.append(line)
                    continue
                elif(len(line) > 8): 
                    Lpais.append(line)
                    continue
                else:
                    print('Línea incorrecta en el archivo ....',ctr)
        swfile = True  
        print('Cargadas las listas Continentes y Paises')
        print('El número de Continentes es ',len(Lcontinente))
        print('La número de paises es ',len(Lpais))
        input('Pulse <Enter> para continuar...')                 
    except:
        print("No existe el archivo.. ", nombre)
        input("Pulse <Enter> para continuar...")
        os.system("cls")

#Opcion 2  del menu
def show_country_by_continent():
    cabeza()
    print("Lista los paises por cada continente...")
    print("=======================================\n")
    for i in range(len(Lcontinente)):
        #line = Lcontinente[i]
        #tam = len(line)
        #if tam == 2:
        print("\nLos paises del continente, ", i+1, " - ", Lcontinente[i][1], "son:" )
        print("=======================================\n")
        for j in range(len(Lpais)):
            if Lpais[j][0] == Lcontinente[i][0]:
                print(Lpais[j][2], " -> " ,Lpais[j][3])
        input("Enter para para continuar ")
        


#Opcion 3 del menu
def show_country_with_higher_and_lower_extension():
    country_May = 0
    country_Men = 100000000
    country_name_may = ""
    country_name_men = ""
    totalContinents = 0
    
    for i in range(len(Lcontinente)):
        cabeza()
        higher_extension = 0
        lower_extension = 0
        country_higher_extension = ""
        country_lower_extension = ""
        totalContinent = 0
        print("\nMuestra país con mayor/menor extensión en kms. cuadrados.")
        print("Muestra la extensión total del continente.")
        print("=======================================\n")
        print("\nInformación continente", Lcontinente[i][1])
        print("=======================================\n")
        
        for j in range(len(Lpais)):
            pais_mayor_ext = int(Lpais[j][4])
            if Lpais[j][0] == Lcontinente[i][0]:
                totalContinent = pais_mayor_ext + totalContinent
                if pais_mayor_ext > higher_extension: 
                    higher_extension = pais_mayor_ext
                    country_higher_extension = Lpais[j][2]
                    
        totalContinents = totalContinent + totalContinents
        if higher_extension > country_May:
            country_May = higher_extension
            country_name_may = country_higher_extension
        
        lower_extension = 100000000
        for k in range(len(Lpais)):
            pais_menor_ext = int(Lpais[k][4])
            if Lpais[k][0] == Lcontinente[i][0]:
                if pais_menor_ext < lower_extension: 
                    lower_extension = pais_menor_ext
                    country_lower_extension = Lpais[k][2]
        if lower_extension < country_Men:
            country_Men = lower_extension
            country_name_men = country_lower_extension
            
        #print("País con mayor extensión es", country_higher_extension, f", extensión {higher_extension:,.0f}" , "Kms. Cuadrados")
        print("País con mayor extensión es", country_higher_extension, "extension {:06,.0f}".format(higher_extension) , "Kms. Cuadrados")
        print("País con menor extensión es", country_lower_extension, "extensión ", lower_extension, "Kms. Cuadrados")
        print("Extensión total del continente", ",extensión {:06,.0f}".format(totalContinent), "Kms. Cuadrados")
        input("Pulse <Enter> para continuar...")
        
    print("País con mayor extensión del mundo es", country_name_may, "extension {:06,.0f}".format(country_May), "Kms. Cuadrados")
    print("País con menor extensión del mundo es", country_name_men, "extension ",country_Men, "Kms. Cuadrados")
    print("Extensión total del mundo", "extension {:06,.0f}".format(totalContinents), "Kms. Cuadrados")
    input("Pulse <Enter> para continuar...")
    
#Opcion 4 del menu
def show_country_with_higher_and_lower_poblation():
    
    cabeza()  
    country_May = 0
    country_Men = 100000000
    country_name_may = ""
    country_name_men = ""
    totalContinents = 0
    
    for i in range(len(Lcontinente)):
        cabeza()
        higher_extension = 0
        lower_extension = 0
        country_higher_extension = ""
        country_lower_extension = ""
        totalContinent = 0
        print("\nMuestra país con mayor/menor población.")
        print("Muestra la poblacion total del continente.")
        print("=======================================\n")
        print("\nInformación continente", Lcontinente[i][1])
        print("=======================================\n")
        
        for j in range(len(Lpais)):
            pais_mayor_ext = int(Lpais[j][7])
            if Lpais[j][0] == Lcontinente[i][0]:
                totalContinent = pais_mayor_ext + totalContinent
                if pais_mayor_ext > higher_extension: 
                    higher_extension = pais_mayor_ext
                    country_higher_extension = Lpais[j][2]
                    
        totalContinents = totalContinent + totalContinents
        if higher_extension > country_May:
            country_May = higher_extension
            country_name_may = country_higher_extension
        
        lower_extension = 100000000
        for k in range(len(Lpais)):
            pais_menor_ext = int(Lpais[k][7])
            if Lpais[k][0] == Lcontinente[i][0]:
                if pais_menor_ext < lower_extension: 
                    lower_extension = pais_menor_ext
                    country_lower_extension = Lpais[k][2]
        if lower_extension < country_Men:
            country_Men = lower_extension
            country_name_men = country_lower_extension
        print("País con mayor población es", country_higher_extension, ", población {:06,.0f}".format(higher_extension))
        print("País con menor población es", country_lower_extension, ", población {:06,.0f}".format(lower_extension))
        print("Población total del continente {:06,.0f}".format(totalContinent) , "Kms. Cuadrados")
        input("Pulse <Enter> para continuar...")
        
    print("País con mayor extensión del mundo es", country_name_may, ", extensión {:06,.0f}".format(country_May))
    print("País con menor extensión del mundo es", country_name_men, ", extensión {:06,.0f}".format(country_Men))
    print("Población total del mundo {:06,.0f}".format(totalContinents))
    input("Pulse <Enter> para continuar...")

    
#Opcion 5 del menu
def search_information_of_countries():
    #os.system('cls')
    cabeza()
    print('Muestra toda la información de un pais...')
    nom = input('Digite nombre -parte del nombre- del país: ')
    siesta = False
    for i in range(0,len(Lpais)):
        if nom in Lpais[i][2]:
            siesta = True
            line = Lpais[i]
            tamano = len(line)
            cod_continente = int(Lpais[i][0])
            name_continente = ""
            for j in range(len(Lcontinente)):
                if cod_continente == int(Lcontinente[j][0]):
                    name_continente = Lcontinente[j][1]
            print("Información sobre el país:", Lpais[i][2])
            print("  Pertenece al continente:", name_continente)
            print("           Código de país:", Lpais[i][1])
            print("            La capital es:", Lpais[i][3])
            print("Extensión en kms. cuadra.: {:06,.0f}".format(int(Lpais[i][4])))
            print("         El gentilicio es:", Lpais[i][5])
            print("             La moneda es:", Lpais[i][6])
            print("  El número de habitantes: {:06,.0f}".format(int(Lpais[i][7])))
            print("          Los limites son:")
            for j in range(8,tamano):
                print( "        *",Lpais[i][j])
            input('Pulse <Enter> para continuar..')
            cabeza()
    if not siesta:
        print('No hay pais con el nombre',nom)
   
    
#Opcion 6 del menu   
def capital_random():
        correcto = False
        contador = 1
        correctas = 0
        incorrectas = 0
        promedio = 0.0
        while(not correcto):
            os.system('cls')
            cabeza()
            print("Selecciona un País al azar y pregunta por su capital...")
            posicion = random.randint(0, int(len(Lpais)))
            pais = Lpais[posicion][2]
            capital = Lpais[posicion][3]
            print("La capital de", pais,  "es:")
            res = input(":")
            
            if res == capital:
                print("Correcto... Sabe de Geografía!!")
                correctas = correctas + 1
            else:
                print("Incorrecto... No Sabe de Geografía!!")
                print("La capital de", pais,  "es:", capital)
                incorrectas =  incorrectas + 1
                
            opc = input("Continuar(SsNn)?")
            
            try:
                if (opc == 's' or opc == 'S'):
                    contador = contador + 1
                    correcto = False
                elif (opc == 'n' or opc == 'N'):
                    promedio = (correctas/contador)*100
                    print("Preguntas realizadas:", contador)
                    print("Respuestas Correctas:", correctas, "- Respuestas Incorrectas:", incorrectas)
                    print("Porcentaje:", promedio)
                    input("Pulse <Enter> para continuar...")
                    break
                else:
                    print('Error, introduce una opción valida')
                    input("Pulse <Enter> para continuar...")
                    continue
                
            except:
                continue
#Opcion 7 del menu   
def gentilicio_random():
        correcto = False
        contador = 1
        correctas = 0
        incorrectas = 0
        promedio = 0.0
        while(not correcto):
            os.system('cls')
            cabeza()
            print("Selecciona un País al azar y pregunta por su gentilicio...")
            posicion = random.randint(0, int(len(Lpais)))
            pais = Lpais[posicion][2]
            capital = Lpais[posicion][5]
            print("El gentilicio de los nacidos en", pais, "es:")
            res = input(":")
            
            if res == capital:
                print("Correcto... Sabe de Geografía!!")
                correctas = correctas + 1
            else:
                print("Incorrecto... No Sabe de Geografía!!")
                print("La capital de", pais,  "es:", capital)
                incorrectas =  incorrectas + 1
                
            opc = input("Continuar(SsNn)?")
            
            try:
                if (opc == 's' or opc == 'S'):
                    contador = contador + 1
                    correcto = False
                elif (opc == 'n' or opc == 'N'):
                    promedio = (correctas/contador)*100
                    print("Preguntas realizadas:", contador)
                    print("Respuestas Correctas:", correctas, "- Respuestas Incorrectas:", incorrectas)
                    print("Porcentaje:", promedio)
                    input("Pulse <Enter> para continuar...")
                    break
                else:
                    print('Error, introduce una opción valida')
                    input("Pulse <Enter> para continuar...")
                    continue
                
            except:
                continue
#Opcion 8 del menu   
def pais_random():
        correcto = False
        contador = 1
        correctas = 0
        incorrectas = 0
        promedio = 0.0
        while(not correcto):
            os.system('cls')
            cabeza()
            print("Selecciona una Capital al azar y pregunta por el País...")
            posicion = random.randint(0, int(len(Lpais)))
            capital = Lpais[posicion][3]
            pais = Lpais[posicion][5]
            print(capital, "es la capital de: ")
            res = input(":")
            
            if res == pais:
                print("Correcto... Sabe de Geografía!!")
                correctas = correctas + 1
            else:
                print("Incorrecto... No Sabe de Geografía!!")
                print(capital, "es la capital de: ", pais)
                incorrectas =  incorrectas + 1
                
            opc = input("Continuar(SsNn)?")
            
            try:
                if (opc == 's' or opc == 'S'):
                    contador = contador + 1
                    correcto = False
                elif (opc == 'n' or opc == 'N'):
                    promedio = (correctas/contador)*100
                    print("Preguntas realizadas:", contador)
                    print("Respuestas Correctas:", correctas, "- Respuestas Incorrectas:", incorrectas)
                    print("Porcentaje:", promedio)
                    input("Pulse <Enter> para continuar...")
                    break
                else:
                    print('Error, introduce una opción valida')
                    input("Pulse <Enter> para continuar...")
                    continue
                
            except:
                continue
#Opcion 9 del menu   
def gentilicio_pais_random():
        correcto = False
        contador = 1
        correctas = 0
        incorrectas = 0
        promedio = 0.0
        while(not correcto):
            os.system('cls')
            cabeza()
            print("Selecciona un Gentilicio al azar y pregunta por el País...")
            posicion = random.randint(0, int(len(Lpais)))
            gentilicio = Lpais[posicion][5]
            pais = Lpais[posicion][2]
            print(gentilicio, "es el gentilicio de: ")
            res = input(":")
            
            if res == pais:
                print("Correcto... Sabe de Geografía!!")
                correctas = correctas + 1
            else:
                print("Incorrecto... No Sabe de Geografía!!")
                print(gentilicio, "es el gentilicio de los nacidos en:", pais)
                incorrectas =  incorrectas + 1
                
            opc = input("Continuar(SsNn)?")
            
            try:
                if (opc == 's' or opc == 'S'):
                    contador = contador + 1
                    correcto = False
                elif (opc == 'n' or opc == 'N'):
                    promedio = (correctas/contador)*100
                    print("Preguntas realizadas:", contador)
                    print("Respuestas Correctas:", correctas, "- Respuestas Incorrectas:", incorrectas)
                    print("Porcentaje:", promedio)
                    input("Pulse <Enter> para continuar...")
                    break
                else:
                    print('Error, introduce una opción valida')
                    input("Pulse <Enter> para continuar...")
                    continue
                
            except:
                continue
#Opcion 10 del menu   
def pais_continente_random():
        correcto = False
        contador = 1
        correctas = 0
        incorrectas = 0
        promedio = 0.0
        while(not correcto):
            os.system('cls')
            cabeza()
            print("Selecciona un País al azar y pregunta por el Continente al cual pertenece...")
            posicion = random.randint(0, int(len(Lpais)))
            pais = Lpais[posicion][2]
            cod_continente = Lpais[posicion][0]
            for i in range(len(Lcontinente)):
                if cod_continente == Lcontinente[i][0]:
                    continente = Lcontinente[i][1]
                    print(continente)
            print(pais, "pertenece al continente de: ")
            res = input(":")
            
            if res == continente:
                print("Correcto... Sabe de Geografía!!")
                correctas = correctas + 1
            else:
                print("Incorrecto... No Sabe de Geografía!!")
                print(pais, "pertenece al continente de:", continente)
                incorrectas =  incorrectas + 1
                
            opc = input("Continuar(SsNn)?")
            
            try:
                if (opc == 's' or opc == 'S'):
                    contador = contador + 1
                    correcto = False
                elif (opc == 'n' or opc == 'N'):
                    promedio = (correctas/contador)*100
                    print("Preguntas realizadas:", contador)
                    print("Respuestas Correctas:", correctas, "- Respuestas Incorrectas:", incorrectas)
                    print("Porcentaje:", promedio)
                    input("Pulse <Enter> para continuar...")
                    break
                else:
                    print('Error, introduce una opción valida')
                    input("Pulse <Enter> para continuar...")
                    continue
                
            except:
                continue                

#pcion 11     
def helpe():
    cabeza()
    print("Sencilla Base de Conocimientos sobre paises de los cinco continentes")
    print("La entrada al programa es un archivo plano con la siguiente estructura\n")
    print("código continente,nombre continente\n")
    print("-> Se pueden ingresar los paises que se deseen con la siguiente estructura\n")
    print("cód_continente,cód_País,País,Capital,Extensión,Gentilicio,Moneda,Población,Limites\n")
    print("NOTA: Los valores se deben ingresar sin espacios y separados por coma(,)")
        
    input('Pulse <Enter> para continuar..') 
    
#opcion 12
def acercade():
    os.system('cls')
    cabeza() 
    print('Programa realizado por MiStPoPe')
    print('Estudiante del Programa de Ingeniería de Sistemas')
    print('Universidad Autónoma de Colombia')
    print('Facultad de Ingenierías - Abril de 2020')
    print('Email porras0696@gmail.com - michael.porras@fuac.edu.co')
    input('Pulse <Enter> para continuar...')        
             
#aqui inicia....
if __name__ == "__main__":
    opc = 0  
    Lcontinente = []  
    Lpais = []
    swfile = False
    swgraba = False
    while True:
        #if not swfile:
        #    menu1()
        #else:    
        menu1()
        if opc == 1:
            if swfile:
                input('Ya se cargaron las listas en memoria <Enter> para continuar...')
            else:    
            #lista = cargaBC()
                cargaListas()
           # swfile = True
            while True: 
                menu()
                if opc == 2:
                    if not swfile:   #if swfile == False:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        show_country_by_continent()      
                if opc == 3:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        show_country_with_higher_and_lower_extension()
                if opc == 4:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        show_country_with_higher_and_lower_poblation()       
                if opc == 5:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        search_information_of_countries()
                if opc == 6:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        capital_random()
                if opc == 7:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        gentilicio_random()  
                if opc == 8:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        pais_random() 
                if opc == 9:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        gentilicio_pais_random() 
                if opc == 10:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        pais_continente_random()     
                if opc == 11:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        helpe()          
                if opc == 12:
                    if not swfile:
                        input('No hay listas en memoria, <Enter> para continuar...')
                    else:
                        acercade()       
                if opc == 99:
                    #if swgraba:
                        #print('Es necesario salvar registros ...')
                        #archi_plano()
                    break
        if opc == 99:
            print("=D")
            break
        