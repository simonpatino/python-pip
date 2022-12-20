
# -*- coding: utf-8 -*-
nick_name= str(input(" Escribe tu nombre en la partida "))

print('Bienvenido {} a esta noble cruzada, escribe " empezar " para abordar el barco.'.format(nick_name))



start = (input("¿ Que deseas decirme? "))
if (start == "empezar") :
    print( """ Has abordado un barco por el atlantico y el oceano se pone algo turbio.
          ¡Es un calamar gigante el que nos esta atacando! -capitan, que debemos hacer!!?
          
          1- Debemos disparar con los cañones, el dolor lo espantara
          2- Debemos correr, es demaciado gigante para intentar hacer algo 
          3- Saquen la dinamita, hoy comeremos sushi""")
    option= int(input())
    if option == 1 :
              print("""POM, POM, POM. El calamar se ha molestado demaciado y decide atacar el barco...
                    HAS MUERTO JUNTO A TU TRIPULACION""")
    elif option == 2:
      
            print(""""Sabia decicion honorable caballero, el barco ha logrado escapar de los tentaculos del temible calamar.
                  HAS SALVADO A TODA TU TRUPULACION""")
    elif option == 3:
        
            explosives= int(input(" Cuantos Cartuchos de dinamita quieres usar, -¡contamos con 6 capitan! "))
            if  0 <  explosives <=6: 
                print(""" El calamar ha muerto, ¡hoy comeremos suschi trupulacion!
                      HAS SALVAD0 A TODA TU HAMBRIENTA TRIPULACION""")
            elif explosives <= 0:
                print(""" Tienes que estar bromeando
                      El calamar empieza a atacar y el barco se unde.
                      TODA TU TRUPULACION HA MUERTO""")
            elif explosives >= 6:
                print("""Dinamita insuficiente.
                      el calamar empieza a atacar y el barco se unde.
                      TODA TU TRUPULACION HA MUERTO""""")
    else:
        print("acaso quieres salirte de tu papel??")
                      
else: 
      print("Te crees muy gracioso , ¿ehg?")

    