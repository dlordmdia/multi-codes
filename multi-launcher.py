import os
import time
import webbrowser
import random
import qrcode
from tkinter import *
import tkinter.scrolledtext as st
import tkinter as tk
from ast import Add
from tokenize import Triple
import string
import pyperclip
import pyautogui as pt

system = True

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print("\n\n----MULTI-LAUNCHER----\n created by @dlordmdia")
    time.sleep(1)
    answer1 = input("\nQue quieres hacer?\n\na- Guess the Number\nb- Complify Calculator\nc- Anime Hack\nd- QR Code Launcher\ne- Bitcoin Miner\nf- Dlord Texts\ng- Dlord Media Launcher\nh- Password Launcher\ni- Seconds Timer\nj- Lista de Compras\nk- Media Launcher\nl- Spammer\nm- Web Cracker\nn- Simple Spammer\n\ndet- para Detalles\nx- to Exit\n- ")
    if answer1 == "a":
        play = True
        wrong = True

        os.system('cls' if os.name=='nt' else 'clear')
        print("----GUESS THE NUMBER----\n")
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')

        while  play:
            numerorand = random.randint(1, 10)
            wrong = True
            while wrong:
                start = input("-x to Exit | Which is the number? (from 1-10)\n- ")
                
                if start == "x":
                    play = False
                    wrong = False

                elif int(start) == numerorand:
                    print("You guessed it! Nice one!")
                    time.sleep(1)
                    wrong = False
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("New Game!\n")
                
                else:
                    if int(start) > numerorand:
                        print("!!Try Again!! The number is LOWER than yours.")
                        time.sleep(1.5)
                        os.system('cls' if os.name=='nt' else 'clear')
                    else:
                        print("!!Try Again!! The number is HIGHER than yours.")
                        time.sleep(1.5)
                        os.system('cls' if os.name=='nt' else 'clear')

                    wrong = True

        print("\nThanks for playing! I hope you enjoyed it!\n")
        input("Press /ENTER\ to Leave:\n")
        os.system('cls' if os.name=='nt' else 'clear')

    elif answer1 == "b":
        # Imports

        # Variables
        decidido = False
        seguir = "y"

        # Start
        print("\n----COMPLIFY CALCULATOR----\n    Made by @dlordmdia\n\n")

        # About
        print("QUE ES?\n Esto es una calculadora con un mont??n de funciones y actividades divertidas incluidas en ella!\n\nPARA QUE SIRVE?\n Con esta calculadora puedes concentrarte y personalizar tu tiempo de estudio o c??lculo!\n\n")
        input("Presiona ///ENTER\\\ para Seguir\n- ")

        # Personalizaci??n
        while not decidido:
            start = input("Que quieres personalizar?\nType -h for help\n- ")
            if start == "h":
                print("NECESITAS AYUDA?\nPresiona -m si quieres escuchar m??sica\nPresiona -l para ser Redirigido a Classroom\nPresiona -d para ser Redirigido a Google Drive\nPresiona -g para ser Redirigido a Google\nPresiona -c si quieres ver el c??digo\nPresiona -s para Saltar la Personalizaci??n o Seguir el C??lculo\nPresiona -e para cerrar la calculadora\n\n")
            if start == "m":
                dec1 = input("Que quieres escuchar?\na) M??sica chill\nb) Playlist Random\n- ")
                if dec1 == "a":
                    webbrowser.open("https://www.youtube.com/watch?v=cD0szT7pOcc")
                elif dec1 == "b":
                    webbrowser.open("https://www.youtube.com/watch?v=R2AJOOvZgbc&list=PLNawVVX6lTrQmEqCXKAFlYEHf-fveJc22")
                else:
                    print("Te habr??s equivocado de tecla... Intentalo de nuevo!")
            elif start == "c":
                print("Redirigiendo a GitHub...")
                webbrowser.open("https://github.com/dlordmdia")
            elif start == "s":
                print("Saltando Personalizaci??n...")
                time.sleep(0.5)
                print("Redirigiendo al c??lculo...\n")
                time.sleep(0.5)
                break
            elif start == "e":
                print("Gracias por usar Complify Calculator\n--Creado por @dlordmdia--\n")
                break
            elif start == "l":
                print("Redirigiendo a Classroom...\n")
                time.sleep(1)
                webbrowser.open("https://www.classroom.google.com")
            elif start == "d":
                print("Redirigiendo a Google Drive...\n")
                time.sleep(1)
                webbrowser.open("https://www.drive.google.com")
            elif start == "g":
                print("Redirigiendo a Google...\n")
                time.sleep(1)
                webbrowser.open("https://www.google.com")

        # C??lculo
        while seguir == "y":
            equation = input("\nCu??l es tu ecuaci??n?\n")
            print(f"Resultado: {eval(equation)}\n")
            time.sleep(2)
            seguir = input("Quieres hacer otro calculo? (y/n): ")
        time.sleep(0.5)
        print("\nGracias por usar Complify Calculator\n--Creado por DlordMDia--\n")
        time.sleep(1)
        print("Envi??ndote a GitHub...")
        time.sleep(1)
        webbrowser.open("https://github.com/dlordmdia")

    elif answer1 == "c":
        while True:
            os.system('cls' if os.name=='nt' else 'clear')
            start = input("\nCu??l Peli Anime quieres descargar?\n*Todas est??n disponibles*\n- ")

            if start == "carrefour" or start == "dlord":
                print("\nx-system failed... try again in x-range REPEAT\n")
                time.sleep(2)
                print("system not available or expired\nTry again until automatic download!\n")
                time.sleep(1)

            else:
                for i in range(250):
                    webbrowser.open("https:/www.pornhub.com")
                    print("BROMITA ")

            print("\nx-system failed... try again in x-range REPEAT\n")
            time.sleep(2)
            print("system not available or expired\nDownloading now:")
            time.sleep(2)
            for i in range(101):
                os.system('cls' if os.name=='nt' else 'clear')
                print(f"Proceso: {i}%")
                if i == 99:
                    time.sleep(3)

                else:
                    time.sleep(0.07)

        print("\nx-system failed... try again in x-range REPEAT\n")
        time.sleep(2)
        print("system not available or expired\nTry again until automatic download!\n")
        time.sleep(1)

    elif answer1 == "d":
        while True:
            start = input("\nQue quieres hacer?\n\nCrear -c\nubicar -f\n-x to Leave\n\n-")
            if start == "c":
                text = input("TEXTO PARA EL C??DIGO QR:\n-")
                img = qrcode.make(text)
                type(img)  
                fname = ("COMO LLAMAR EL ARCHIVO:\n-")
                img.save(f"{fname}.png")

            elif start == "f":
                print("EN CONSTRUCCI??N. VUELVE M??S TARDE")
                time.sleep(1)
                #locat = input("Qu?? archivo quieres encontrar?\nPiensa en la extensi??n al caso de ser exclusiva o")
                #def find(name, path):
                    #for root, dirs, files in os.walk(path):
                        #if name in files:
                            #return os.path.join(root, name)
            elif start == "x":
                break

    elif answer1 == "e":
        os.system('cls' if os.name=='nt' else 'clear')
        
        start = input("Quieres farmear BTC (Bitcoin)? (y/n): ")
        if start == "y":
            while True:
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.pornhub.com")
                time.sleep(0.005)

        else:
            print("No importa\n\nToma BTC...")
            while True:
                print("No importa\n\nToma BTC...")
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.pornhub.com")
                time.sleep(0.005)

    elif answer1 == "f":
        letra_a = '''
        Tengo todo preparado y montado para jugar porque soy un viciado
        Vamos a estar en l??nea  hora tras hora porque soy un gran viciado

        Tengo todo preparado y montado para jugar porque soy un viciado
        Vamos a estar en l??nea  hora tras hora porque soy un gran viciado
        Tengo todo preparado y montado para jugar porque soy un viciado
        Vamos a estar en l??nea  hora tras hora porque soy un gran viciado


        Vamos A jugar, nos vamos a juntar nos vamos a viciar, 
        nos tenemos que concentrar, para ganar
        A qu?? jugamos, pues nos lo tenemos que pensar,
        De mientras a Tetris nos podemos conectar

        Vamos a Minecraft? o vamos a un shooter
        No pagamos renta entonces invertimos en el rooter
        El vecino no lo roba porque le hemos hackeado
        Y un poco m??s tarde, al tetris nos hemos conectado

        Tremendo valor que tiene mi setup de la semana
        Yo duermo en mi silla por eso me estalvio la cama
        Auriculares profesionales para estar concentrado
        Cuando al tetris me haya conectado

        Tengo todo preparado y montado para jugar porque soy un viciado
        Vamos a estar en l??nea  hora tras hora porque soy un gran viciado
        Tengo todo preparado y montado para jugar porque soy un viciado
        Vamos a estar en l??nea  hora tras hora porque soy un gran viciado


        Queremos estar en l??nea y en directo con mucha gente
        Si nos aburrimos, se abre tetris de repente
        Sensores profesionales est??n montados
        igual que los servers al tetris conectados
        '''
        letra_b = '''Sal??amos de una forma rara,
        Hac??amos cosas as?? por la cara,
        Y te contamos qu?? hicimos,
        De qu?? forma nos divertimos

        Sal??amos de una forma rara,
        Hac??amos cosas as?? por la cara,
        Y te contamos qu?? hicimos,
        De qu?? forma nos divertimos

        Scrollea, Google fotos,
        Tantos recuerdos hasta romper los potos,
        Nos pegamos con palos de bamb?? ,
        C??mo jugamos, as?? est??s t??

        O con palos de metal a los arbustos de mierda,
        No eran robustos ni siquiera,
        Pero se col?? la peque??a bolita,
        Por ella nos hicimos bastante pupita

        Luego conducimos adentro con un coche y una gopro,
        No la vimos y nos hab??amos enfadado,
        Tambi??n por aburrimiento, De una monta??a el coche lo tiramos,
        Quer??amos romperlo aunque no podamos

        Tanto aguanta, como los patinetes,
        Los tiramos contra bordillos cuando no lo esperes,
        Aguanta tanto, pero sigo siendo confund?? le, 
        Como el Itiwitanic es sensible

        Sal??amos de una forma rara,
        Hac??amos cosas as?? por la cara,
        Y te contamos qu?? hicimos,
        De qu?? forma nos divertimos

        Sal??amos de una forma rara,
        Hac??amos cosas as?? por la cara,
        Y te contamos qu?? hicimos,
        De qu?? forma nos divertimos

        Producimos electricidad solo con tubos,
        Para qu?? usan todos sus estudios,
        Encuentra un par de tuberias y nos encargas,
        Ya ver??s cu??nto produce y en ganar no tardas


        Daban calambres, casi como el dron de mario
        Se rompi?? volando por el barrio,
        Lo tir??bamos al aire y luego lo prendemos,
        As?? es como lo rompemos

        Como las pilas, que las metimos en el agua,
        Esperando a que alg??n efecto haga,
        Nos d?? calambres y nos caigamos,
        Siendo como Sergio, ya empezamos,

        Que le roba la botella, y ten??amos que correr por ella,
        Porque Sergio en el patio se la lleva,
        Es el pasado al que quiero volver,
        Pero dudo que se pueda hacer

        Comemos palomitas pero con az??car y sal,
        Para todos menos nosotros est?? mal,
        Con la tutora, el apodo fue Planishit,
        No te lo crees pero si

        Te cuento que bugeamos un PC solo con Shul ker bo xes!
        Era en minecraft tocando tambien la bateria y era tremendo estr??s

        Sal??amos de una forma rara,
        Hac??amos cosas as?? por la cara,
        Y te contamos qu?? hicimos,
        De qu?? forma nos divertimos

        Sal??amos de una forma rara,
        Hac??amos cosas as?? por la cara,
        Y te contamos qu?? hicimos,
        De qu?? forma nos divertimos
        '''
        letra_c = '''Queremos practicar,
        Para poder ganar,
        Es la competici??n,
        Del gran mill??n.

        Queremos practicar,
        Para poder ganar,
        Es la competici??n,
        Del gran mill??n.

        Queremos practicar,
        Para poder ganar,
        Es la competici??n,
        Del gran mill??n.

        La competici??n competitiva,
        Para nosotros, la decisi??n decisiva,
        No pagamos IVA porque estamos en la fila,
        Para que nos den el premio, de la mejor rima.

        Hay que practicar para conseguir nuestros objetivos,
        Hay que imaginarse el futuro con sentido,
        No imagines, aun menos alucines,
        El camino es largo, mejor que ya camines

        No corras, correr al futuro cansa,
        A no ser la competici??n el la cancha,
        Velocidad de una lancha al caso de la bici,
        Por eso ves caminando, por el lujo o la crisis

        Queremos ganar, no por la fama y el dinero,
        Vienen los verdaderos a saludar primero,
        Todos tienes sus bajos y sus altos,
        Sobre todo en la competici??n de saltos

        Queremos practicar,
        Para poder ganar,
        Es la competici??n,
        Del gran mill??n.

        Queremos practicar,
        Para poder ganar,
        Es la competici??n,
        Del gran mill??n.

        Es el reto y se mantiene la rivalidad,
        Deja tu ego y vuelve a la realidad,
        Es la normalidad tener calma en el body,
        Nervios alterados, eso ya es otra story

        No te hinches a drogas o medicinas,
        Pregunta amablemente a tus viejitas vecinas,
        Si podrian hacerte un caldito,
        Es saludable y estar?? calentito.

        TODO OTRA VEZ MENOS LAS DOS ESTROFAS ???-??? y a??adir otro CANTAR x2'''

        getback = "Volver??s al men?? principal al Cerrar la Ventana."

        # Start

        os.system('cls' if os.name=='nt' else 'clear')

        print("\n--DLORD TEXTS--\n\n")

        while True:
            os.system('cls' if os.name=='nt' else 'clear')
            elegir = input("De Cu??l Canci??n quieres la Letra?\n-h for Help\n-")

            if elegir == "a" or elegir == "Hoy en D??a":
                os.system('cls' if os.name=='nt' else 'clear')
                print(getback)
                root = Tk()
                text_area = st.ScrolledText(root)
                text_area.grid(column = 0, pady = 10, padx = 10)
                text_area.insert(tk.INSERT,letra_a)
                text_area.configure(state ='disabled')
                root.mainloop()
            
            elif elegir == "b" or elegir == "El Pasado":
                os.system('cls' if os.name=='nt' else 'clear')
                print(getback)
                root = Tk()
                text_area = st.ScrolledText(root)
                text_area.grid(column = 0, pady = 10, padx = 10)
                text_area.insert(tk.INSERT,letra_b)
                text_area.configure(state ='disabled')
                root.mainloop()
            
            elif elegir == "c" or elegir == "La Competici??n":
                os.system('cls' if os.name=='nt' else 'clear')
                print(getback)
                root = Tk()
                text_area = st.ScrolledText(root)
                text_area.grid(column = 0, pady = 10, padx = 10)
                text_area.insert(tk.INSERT,letra_c)
                text_area.configure(state ='disabled')
                root.mainloop()
            
            elif elegir == "h":
                os.system('cls' if os.name=='nt' else 'clear')
                input("OPCIONES:\nHoy en D??a (Dlord Rap, Yaros) // -a\nEl Pasado (Dlord Rap) // -b\nLa Competici??n (Dlord Rap, Yaros) // -c\n\n//ENTER\\ to go Back\n-")
            
            elif elegir == "x":
                os.system('cls' if os.name=='nt' else 'clear')
                break
            
            elif elegir == "porno":
                    print("Disfruta cacho puta :)")
                    time.sleep(1)
                    while True:
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.pornhub.com")
                        time.sleep(0.005)

            else:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Parece que has escrito algo mal.\nIntentalo Otra Vez")
                time.sleep(1)

        os.system('cls' if os.name=='nt' else 'clear')
        print("Gracias por usarme ;)\n")

    elif answer1 == "g":
        os.system('cls' if os.name=='nt' else 'clear')

        while True:
            Loop = True
            print("\n--DLORD LAUNCHER--\n\n")
            time.sleep(1)

            what1 = input("Qu?? quieres hacer?\n\na)Ver Contenido de M??sica\nb)Ver Contenido de Aventuras y Exteriores\nc)Ver Contenido de Drones\nd)Ver contenido De Bicicleta de Monta??a\n\n-x to Leave\n-")


            if what1 =="a":
                os.system('cls' if os.name=='nt' else 'clear')
                time.sleep(1)
                print("Abriendo...  \n")
                time.sleep(1)
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.youtube.com/channel/UCdHXWPzL5MbRSDNexzbTg7w")

            elif what1 == "b":
                os.system('cls' if os.name=='nt' else 'clear')
                time.sleep(1)
                print("Abriendo...  \n")
                time.sleep(1)
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.youtube.com/channel/UCC-KnP22oPHfTt_vM4X5_6g")

            elif what1 == "c":
                os.system('cls' if os.name=='nt' else 'clear')
                time.sleep(1)
                print("Abriendo...  \n")
                time.sleep(1)
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.youtube.com/channel/UCC-KnP22oPHfTt_vM4X5_6g")
            
            elif what1 == "d":
                os.system('cls' if os.name=='nt' else 'clear')
                time.sleep(1)
                print("Abriendo...  \n")
                time.sleep(1)
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.youtube.com/channel/UCCKj17GGbXvxpnECIJPUrfg/featured")
            
            elif what1 == "x":
                os.system('cls' if os.name=='nt' else 'clear')
                break
            
            elif what1 == "h":
                while Loop:
                    os.system('cls' if os.name=='nt' else 'clear')
                    input("Has descubierto la p??gina oscura de Dlord. Esto Contiene Dar PHO, Dlord Dark, etc.\n/ENTER\ to continue\n- ")
                    os.system('cls' if os.name=='nt' else 'clear')
                    dark = input("a)Dlord PHO (M??sica agresiva y violenta)\nb)Dlord Dark (Acciones Ilegales por los exteriores)\n\n-e to get Back\n-x to Leave\n- ")
                    if dark == "a":
                        os.system('cls' if os.name=='nt' else 'clear')
                        print("Canal inactivo... Intentalo m??s tarde...")
                        time.sleep(2)
                    elif dark == "b":
                        os.system('cls' if os.name=='nt' else 'clear')
                        print("Canal inactivo... Intentalo m??s tarde...")
                        time.sleep(2)
                    elif dark == "e":
                        os.system('cls' if os.name=='nt' else 'clear')
                        Loop = False
                    else:
                        os.system('cls' if os.name=='nt' else 'clear')
                        print("Adios...")
                        exit()
        os.system('cls' if os.name=='nt' else 'clear')
        print("Hasta pronto!")

    elif answer1 == "h":
        os.system('cls' if os.name=='nt' else 'clear')
        while True:
            tirt = input("Que quieres hacer?\n\na) Crear Contrase??a\nb) Revisar Contrase??a\n\n-x to Exit\n- ")

            if tirt == "a":
                os.system('cls' if os.name=='nt' else 'clear')
                print("\n----PASSWORD GENERATOR----\n   Created by dlordmdia\n\n")
                time.sleep(1)

                # List Generator
                letters = list(string.ascii_letters)
                digits = list(string.digits)
                symbols = list(string.punctuation)

                password = ""

                length = int(input("Cuantos digitos quieres que tenga tu nueva Contrase??a? (Recomendado: 8+)\n- "))

                for i in range(length):
                    charactertype = random.randint(1, 3)
                    if charactertype == 1:
                        password += random.choice(letters)
                    elif charactertype == 2:
                        password += random.choice(digits)
                    else:
                        password += random.choice(symbols)

                print(f"Tu contrase??a es: {password}")
                passcopy = input("\nCopiar contrase??a a portapapeles? (y/n): ")
                if passcopy == "y":
                    pyperclip.copy(password)
                    print("\nCopiado!\n")
                    os.system('cls' if os.name=='nt' else 'clear')

            elif tirt == "b":
                os.system('cls' if os.name=='nt' else 'clear')
                print("\n----SAFE PASSWORD CHECKER----\n    Created by dlordmdia\n\n")
                print("Necesitas almenos 8 car??cteres")
                while True:
                    num_digits = 0
                    password = input("-x to Leave | Pon tu Contrase??a: ")
                    for character in password:
                        if character.isdigit():
                            num_digits += 1

                    if len(password) >= 8 and num_digits >= 2:
                        break

                    elif password == "x":
                        break

                    else:
                        print("\nTu contrase??a no es segura.\n")
                        time.sleep(0.4)
                        print("Int??ntalo otra vez.\n")
                        time.sleep(2)
                        os.system('cls' if os.name=='nt' else 'clear')

                print("\nTu contrase??a es segura.\n")
                time.sleep(2)
                print("\n----SAFE PASSWORD CHECKER----\n    Created by dlordmdia\n")
                os.system('cls' if os.name=='nt' else 'clear')
            
            elif tirt == "x":
                break

            print("\nGracias por usar Password Launcher!\n")

    elif answer1 == "i":
        loop = True
        while loop:
            os.system('cls' if os.name=='nt' else 'clear')
            secs = int(input("-x to leave || De cu??ntos segundos quieres que sea tu Temporizador?\nCantidad de segundos: "))
            os.system('cls' if os.name=='nt' else 'clear')
            print("-x to Leave | Temporizador en marcha!")
            for i in range(secs+1):
                if secs > 0:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("-x to Leave | Temporizador en marcha!\n")
                    print("Falta: ")
                    print(f"{secs}")
                    secs -= 1
                    time.sleep(1)
                
                elif secs == "x":
                    loop = False
            

                else:
                    os.system('cls' if os.name=='nt' else 'clear')
                    input("Se acab?? el tiempo!!\n- press /ENTER\ to exit\n- ")
                    break

                    
                    
    elif answer1 == "j":
        seguir = "y"

        lista = []
        anadiendo = False

        precio_total = 0.0
        os.system('cls' if os.name=='nt' else 'clear')
        print("\nQue quieres hacer?\n")
        time.sleep(2)
        menu1 = "\na) A??adir cosas\nb) Ver lista\nc) Ver c??digo mientras tu compra\nd) A??adir Precios\ne) Ver precio Total\nf) Eliminar Objeto de la lista\ng) Eliminar Precio\n\nPresiona /ENTER\ para salir de la lista de compras"

        print(menu1)

        while True:
            inicio = input("- ")
            if inicio == "a":
                anadiendo = True
                os.system('cls' if os.name=='nt' else 'clear')
                while anadiendo:
                    objeto = input("-x to Leave | Tu objeto: ")
                    if objeto == "x":
                        print("Saliendo...")
                        anadiendo = False
                        os.system('cls' if os.name=='nt' else 'clear')
                        print(menu1)

                    else:
                        lista.append(objeto)
                    
            elif inicio == "b":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Tienes: ")
                for item in lista:
                    print(f"- {item}")
                saleave = input("\n\n-x to Leave:\n- ")
                if saleave == "x":
                    os.system('cls' if os.name=='nt' else 'clear')
                    print(menu1)

            elif inicio == "c":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Redirigiendote a GitHub...")
                time.sleep(1)
                webbrowser.open("https://github.com/dlordmdia")
                time.sleep(3)
                os.system('cls' if os.name=='nt' else 'clear')
                print(menu1)

            elif inicio == "d":
                os.system('cls' if os.name=='nt' else 'clear')
                calculando = True
                while calculando:
                    precio = input("-x to Leave | Un precio: ")
                    if precio == "x":
                        print("Saliendo...")
                        calculando = False
                        os.system('cls' if os.name=='nt' else 'clear')
                        print(menu1)

                    else:
                        precio_total += float(precio)

            elif inicio == "e":
                os.system('cls' if os.name=='nt' else 'clear')
                xleave = input(f"Tu precio total ??s: {precio_total}???\n\n -x to Leave:\n- ")
                if xleave == "x":
                    os.system('cls' if os.name=='nt' else 'clear')
                    print(menu1)

            elif inicio == "f":
                anadiendo = True
                os.system('cls' if os.name=='nt' else 'clear')
                print("\n-x to Leave | Que Objeto quieres eliminar de la lista?")
                while anadiendo:
                    print("Tienes: ")
                    for item in lista:
                        print(f"- {item}")

                    item_to_remove = input("\nEliminas: ")
                    if item_to_remove == "x":
                        os.system('cls' if os.name=='nt' else 'clear')
                        print(menu1)
                        anadiendo = False
                    
                    else:
                        if item_to_remove in lista:
                            for item in lista:
                                if item == item_to_remove:
                                    lista.pop(lista.index(item_to_remove))
                            print("Eliminado!!\n")
                        
                        else:
                            print("Este objeto no est?? en la lista\n")

            else:
                print("\nGracias por usar la lista de compras de dlordmdia!\n\n")
                time.sleep(3)
                print("Redirigiendote a GitHub (@dlordmdia)...")
                time.sleep(1)
                webbrowser.open("https://github.com/dlordmdia")
                time.sleep(2)
                print("Abierto correctamente!\n")
                break

    elif answer1 == "k":
        decidido = False
        recdec = False

        # Intro
        print("\n----MEDIA LAUNCHER----\n\nQUE ES?\n Es un Launcher para abrir las Redes Sociales! \n\nPORQUE USARLO?\n Estalvias tiempo y puedes conseguir recomendaciones de cada ??nico tipo de Red Social!\n")

        # Inicio
        time.sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
        # Seleccionar Red Social

        while not decidido:
            respuesta1 = input("Que Red Social quieres abrir?:\ntype h for help\n- ")

            if respuesta1 == "h":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Redes disponibles:\ni) Instagram\ny) Youtube\nt) Tik Tok\ng) GitHub\ns) Spotify\nm) Mavic Pilots\n\nr) Recomendaciones\ne) Exit Media Launcher\n\n")
            elif respuesta1 == "i":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Red Social: Instagram\n Redirigiendo...\n")
                webbrowser.open("https://www.instagram.com/") 
            elif respuesta1 == "y":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Red Social: YouTube\n Redirigiendo...\n")
                webbrowser.open("https://www.youtube.com")
            elif respuesta1 == "t":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Red Social: Tik Tok\n Redirigiendo...\n")
                webbrowser.open("https://www.tiktok.com")
            elif respuesta1 == "g":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Red Social: GitHub\n Redirigiendo...\n")
                webbrowser.open("https://www.github.com")
            elif respuesta1 == "s":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Red Social: Spotify\n Redirigiendo...\n")
                webbrowser.open("https://www.spotify.com")
            elif respuesta1 == "m":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Red Social: Mavic Pilots\n Redirigiendo...\n\n")
                webbrowser.open("https://www.mavicpilots.com")
            elif respuesta1 == "r":
                os.system('cls' if os.name=='nt' else 'clear')
                recs = input("Quieres Recomendaciones de unos perfiles buenos?(y/n) \n-")
                break
            elif respuesta1 == "e":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Hasta aqu?? el Media Launcher por ahora...\nCreado por DlordMDia ")
                exit()
                

        # Recomendaciones
        if recs == "y":
            while not recdec:
                os.system('cls' if os.name=='nt' else 'clear')
                recperf = input("De qu?? Red Social quieres un perfil?\nType -h for help\n- ")

                if recperf == "h":
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Redes disponibles:\ni) Instagram\ny) Youtube\nt) Tik Tok\ng) GitHub\ns) Spotify\nm) Mavic Pilots\n\nr) Recomendaciones\ne) Exit Media Launcher\n\n")
                
                elif recperf == "i":
                    os.system('cls' if os.name=='nt' else 'clear')
                    insta = input("Red Social: Instagram\n Que quieres ver?\na) Perfiles de dron\nb) Perfiles de M??sica\n- ")
                    if insta == "a":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.instagram.com/drone.yl")
                    elif insta == "b":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.instagram.com/dlord_rap")
                    
                elif recperf == "y":
                    os.system('cls' if os.name=='nt' else 'clear')
                    yt = input("Red Social: YouTube\n Que quieres ver?\na) M??ltiples perfiles de Dron\nb) Perfiles de Rap\n- ")
                    if yt == "a":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.youtube.com/channel/UCiqY3ffR4i_a3aJj8L4Owew")
                        webbrowser.open("https://www.youtube.com/channel/UCUa5cLjlaspHPciMtEZUgZg")
                    elif yt == "b":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.youtube.com/channel/UCdHXWPzL5MbRSDNexzbTg7w")
                        webbrowser.open("https://www.youtube.com/c/YarostheLaunchpadder")
                
                elif recperf == "t":
                    os.system('cls' if os.name=='nt' else 'clear')
                    tt = input("Red Social: Tik Tok\n Qu?? quieres ver?\na) Perfil de Rap\nb)Perfil de Dron\n- ")
                    if tt == "a":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.tiktok.com/@dlord_rap")
                    elif tt == "b":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.tiktok.com/@dlordair")
                
                elif recperf == "g":
                    os.system('cls' if os.name=='nt' else 'clear')
                    git = input("Red Social: GitHub\n Quieres ir a los dos mejores perfiles de Code? (y/n)\n- ")
                    if git == "y":
                        os.system('cls' if os.name=='nt' else 'clear')
                        webbrowser.open("https://www.github.com/dlordmdia")
                        webbrowser.open("https://www.github.com/YarostheLaunchpadder")
                
                elif recperf == "s":
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Red Social: Spotify\n Redirigiendo...\n\n")
                    webbrowser.open("https://open.spotify.com/artist/0nhvWjUAY9yfW8fUcPwXIU")
                
                elif recperf == "m":
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Red Social: Mavic Pilots\n Redirigiendo...\n\n")
                    webbrowser.open("https://mavicpilots.com/members/yaros.154583/")

                elif recperf == "e":
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Hasta aqu?? el Media Launcher por ahora...\nCreado por DlordMDia ")
                    exit()


        elif recs == "n":
            os.system('cls' if os.name=='nt' else 'clear')
            print("Hasta aqu?? el Media Launcher por ahora...\nCreado por DlordMDia ")
            exit()
            
        # Fin
        os.system('cls' if os.name=='nt' else 'clear')
        print("Hasta aqu?? el Media Launcher por ahora...\nCreado por DlordMDia ")

    elif answer1 == "l":
        os.system('cls' if os.name=='nt' else 'clear')
        limit = input("Enter limit:")
        message = input("Enter message:")
        i = 0
        time.sleep(5)
        pt.press("enter")

        while i < int(limit):
            pt.typewrite(message)    
            
            pt.press("enter")

            i+=1

    elif answer1 == "m":
        os.system('cls' if os.name=='nt' else 'clear')
        print("--WEB CRACKER--")
        print("Ejecuta el C??digo de Web Cracker en un Online Python Terminal\n -x para TERMINAR")
        time.sleep(1)
        crack = input("INICIAR CRACK? (y/n) -x para TERMINAR: ")
        input("pulsa /ENTER\ para confirmar que has le??do || -x para TERMINAR||\n- ")

        if crack == "y":
            while True:
                print("???	0x0000000A")
                print("Ejecutando...")
        
        if crack == "x":
            break

        else:
            print("Gracias")
    
    elif answer1 == "n":
        while True:
            os.system('cls' if os.name=='nt' else 'clear')
            print("\n--SIMPLE-SPAMMER--\n\n")
            time.sleep(1)
            os.system('cls' if os.name=='nt' else 'clear')
            print("ctr + z to stop programm\n\n")
            what = input("Qu?? quieres escribir?\n- ")
            much = input ("Cuantas veces?\n- ")

            output = ""

            for i in range(int(much)):
                output += what + " "

            pyperclip.copy(output)
            os.system('cls' if os.name=='nt' else 'clear')
            print("El Spam se ha copiado a tu portapapeles\nctr + v para pegar el mensaje largo")
            time.sleep(2)
    
    elif answer1 == "x":
        os.system('cls' if os.name=='nt' else 'clear')
        break

    elif answer1 == "det":
        os.system('cls' if os.name=='nt' else 'clear')
        det = input("\nDe que quieres tener detalles?\n\na- Guess the Number\nb- Complify Calculator\nc- Anime Hack\nd- QR Code Launcher\ne- Bitcoin Miner\nf- Dlord Texts\ng- Dlord Media Launcher\nh- Password Launcher\ni- Seconds Timer\nj- Lista de Compras\nk- Media Launcher\nl- Spammer\nm- Web Cracker\nn- Simple Spammer\n\nx- to Exit\n- ")
        
        if det == "a":
            input("Un Juego randomizado donde tienes que adivinar el n??mero y te da la ventaja de saber si nu nombre es MAYOR QUE o MENOR QUE el primer input.\n/ENTER\ para salir\n- ")
        
        if det == "b":
            input("Calculadora compleja con muchas configuraciones!\n/ENTER\ para salir\n- ")
        
        if det == "c":
            input("Descarga todo tipo de Pel??culas Anime! \n/ENTER\ para salir\n- ")

        if det == "d":
            input("Crea un C??digo QR! \n/ENTER\ para salir\n- ")
        
        if det == "e":
            input("Mina Bitcoin Claimeando earnings de P??ginas web Gratis! \n/ENTER\ para salir\n- ")
        
        if det == "f":
            input("Lee todas las letras de las Canciones de Dlord Rap! \n/ENTER\ para salir\n- ")
        
        if det == "g":
            input("Abre todas las Plataformas de Dlord! \n/ENTER\ para salir\n- ")

        if det == "h":
            input("Crea y Comprueba una contrase??a 100% segura! \n/ENTER\ para salir\n- ")
        
        if det == "i":
            input("Temporizador medido en Segundos!\n/ENTER\ para salir\n- ")
        
        if det == "j":
            input("Crea una lista de Compras con articulos, precios, calculadora, etc! \n/ENTER\ para salir\n- ")

        if det == "k":
            input("Abre redes sociales sin tener huellas de Surf por el internet! \n/ENTER\ para salir\n- ")
        
        if det == "l":
            input("Elige la cantidad y el qu?? quieres spammear de forma simple y segura!\n/ENTER\ para salir\n- ")

        if det == "m":
            input("Rompe una p??gina Web que funcionepor Servidor con ese car??cter especial. \n/ENTER\ para salir\n- ")

        if det == "n":
            input("Un Spammer de un mesaje copiado a tu portapapeles! \n/ENTER\ para salir\n- ")

    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print("No encuentro nada correspondiente a tu b??squeda. INT??NTALO DE NUEVO!")
        time.sleep(2)

