
'''

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

'''    


import tkinter as tk
from tkinter import scrolledtext as st
import sys
import random
from tkinter import filedialog as fd
from tkinter import messagebox



class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=140, height=20, bg='black',fg="#03f943")
        self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
        self.scrolledtext2=st.ScrolledText(self.ventana1, width=140, height=20, bg='black',fg="#03f943")
        self.scrolledtext2.grid(column=0,row=1, padx=10, pady=10)       
        self.ventana1.title("KiNG_IT - SUPER ENCRIPTER")
        self.ventana1.config(background="#494341")
        self.botonDesencriptar=tk.Button(text="Desencriptar", command=self.desencriptando, bg='darkgrey',width=10,height=10,fg="#000000")
        self.botonDesencriptar.grid(row=1, column=1, sticky="e", padx=10, pady=10)
        self.botonEncriptar=tk.Button(text="Encriptar", command=self.encriptando, bg='darkgrey',width=10,height=10,fg="#000000")
        self.botonEncriptar.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        self.botonAbrir=tk.Button(text="Abrir", command=self.recuperar, bg='darkgrey',width=10)
        self.botonAbrir.grid(row=3, column=1, sticky="e", padx=10, pady=10)
        self.botonGuardar=tk.Button(text="Guardar", command=self.guardar, bg='darkgrey',width=10)
        self.botonGuardar.grid(row=3, column=2, sticky="e", padx=10, pady=10)
        self.botonBorrar=tk.Button(text="Borrar", command=self.borrar_campos, bg='darkgrey',width=10)
        self.botonBorrar.grid(row=3, column=3, sticky="e", padx=10, pady=10)
        self.ventana1.mainloop()



    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        menubar1.config(bg="red")
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones3 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Encriptar", command=self.encriptando)
        opciones1.add_command(label="Desencriptar", command=self.desencriptando)
        opciones1.add_command(label="Recuperar archivo", command=self.recuperar)
        opciones2.add_command(label="Borrar Campos", command=self.borrar_campos)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        menubar1.add_cascade(label="Edicion", menu=opciones2)
        menubar1.add_cascade(label="Ayuda", menu=opciones3)
        opciones3.add_command(label="Licencia", command=self.licencia)
        opciones3.add_command(label="Acerca de", command=self.version)


    def licencia(self):
        messagebox.showinfo("Licencia", "Su licencia esta actualizada")
        
    def version(self):
        messagebox.showinfo("Acerca de...", "602 MANAGEMENT version 1.0.0.11")
        
    def salir(self):
        valor=messagebox.askquestion("SALIR", "Desea salir del programa?")
        if valor=="yes":
            sys.exit()

    def borrar_campos(self):
        valor=messagebox.askquestion("BORRAR", "Desea borrar todos los datos?")
        if valor=="yes":
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext2.delete("1.0", tk.END)

    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext2.get ("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("todos los archivos","*.*"),("txt files","*.txt")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

    def encriptando (self):

        dicDeCaracteres = {
                               ' ':'"','a':'\n','A':'Z','á':'á','b':'n','B':'N','c':'b','C':'B','d':'|','D':'M',
        'e':'c','E':'C','é':'é','f':'!','F':'O','g':'d','G':'D','h':'@','H':'P','i':'e','I':'E','í':'í','j':'#',
        'J':'Q','k':'f','K':'F','l':'$','L':'R','m':'g','M':'G','n':'%','N':'S','o':'h','O':'H','ó':'ó','p':'^',
        'P':'T','q':'i','Q':'I','r':'&','R':'V','s':'j','S':'J','t':'u','T':'U','u':'k','U':'K','ú':'ú','v':'(',
        'V':'W','w':'l','W':'L','x':')','X':'Y','y':';','Y':'X','z':':','Z':'A','0':'z','1':'x','2':'m','3':'v',
        '4':'2','5':'o','6':'p','7':'q','8':'r','9':'s','.':'t','@':'~','-':'¿',',':'-',';':'=',':':'+','<':'{',
        '>':'}','_':'[','+':']','=':'`','[':'8',']':'?','{':',','}':'.','¿':'<','"':'>',"'":'=','(':'1',')':'3', 
        '\n':'7','?':'6','ñ':'5','Ñ':'4'}
    
        listaDeCaracteres = [
                            '=', 'a', 'A', 'b', '`', 'c', 'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 
        'd', 'h', '@', 'i', 'e', 'j', '5', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%', 'o', 'h', 'p','^', 'P', '^', 
        'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x', ')', 'y', ';', 'z', ':','0', 
        'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', 'O', '7', ',', '8', '<', '9', '.','.', 
        '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`', 'c', 'b', 'C', 'B', 'd','|', 'e','c', 
        'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', '8', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%', 'o', 'h','p', 
        '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x', ')', 'y',';', 
        'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', '7', ',', '8', '<','9', 
        '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`', 'c', 'b', 'C', 'B','d','|', 
        'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%', 'o','h', 
        'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x', ')','y', 
        ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', '7', ',', '8','<', 
        '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`', 'c', 'b', 'C','B','d', 
        '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%','o', 
        'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x',')', 
        'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', 'w', '/','7', 
        ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`','c','b', 
        'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$', 'm','g', 
        'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(','w', 
        'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6','m', 
        '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b','`','c', 
        'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$','m', 
        'g', 'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v','(', 
        'w', 'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n','6', 
        'm', '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A','b','`', 
        'c', 'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l','$', 
        'm', 'g', 'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k','v', 
        '(', 'w', 'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5','n', 
        '6', 'm', 'l', '.', '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ','=','a', 
        'A', 'b', '`', 'c', 'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j','k', 
        'f', 'l', '$', 'm', 'g', 'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't','*', 
        'u', 'k', 'v', '(', 'w', 'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v','4', 
        'b', '5', 'n', '6', 'm', '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..','l','l',
        'd', 'h', '@', 'i', 'e', 'j']

        #Creo la variable archivoTexto con el texto ingresado en el primer cuadro, creo la lista listaTextoEncrip vacia
        
        archivoTexto = self.scrolledtext1.get("1.0", tk.END)
        listaTextoEncrip = []

        #Calculo la longitud del texto, creo una lista con la cantidad, lo encripto y lo agrego a la listaTextoEncrip, (le agrego 
        # para reconocerlo)
    
        cantCaracteres = int(len(archivoTexto)-1)
        cantCaracteresDelArchivo = list(str(cantCaracteres))
        for x in cantCaracteresDelArchivo:
            xx = dicDeCaracteres.get(x)
            listaTextoEncrip.append(str(xx))
        listaTextoEncrip.append('#')

        #Para cada caracter del texto, busco su valor de encriptacion

        for r in archivoTexto:
            caracterEncriptado = dicDeCaracteres.get(r)
            listaTextoEncrip.append(str(caracterEncriptado))
            
        #Creo un contador en cero, voy incrementandolo hasta 100, buscando aleatoriamente valores para agregar al texto
        contador = 0
        while contador < cantCaracteres:
            for intAleatorio in listaDeCaracteres:
                intAleatorio = random.randint(1,100)
                caracterAleatorio = listaDeCaracteres[intAleatorio]
                contador += 1
                listaTextoEncrip.append(str(caracterAleatorio))

    # Se crea la lista y se la invierte, se imprime el texto encriptado en el segundo cuadro

        listaTextoEncrip = [''.join(list(reversed(listaTextoEncrip)))]
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert ("1.0", listaTextoEncrip) 

    def desencriptando (self):
        dicDeCaracteres = {
                               ' ':'"','a':'\n','A':'Z','á':'á','b':'n','B':'N','c':'b','C':'B','d':'|','D':'M',
        'e':'c','E':'C','é':'é','f':'!','F':'O','g':'d','G':'D','h':'@','H':'P','i':'e','I':'E','í':'í','j':'#',
        'J':'Q','k':'f','K':'F','l':'$','L':'R','m':'g','M':'G','n':'%','N':'S','o':'h','O':'H','ó':'ó','p':'^',
        'P':'T','q':'i','Q':'I','r':'&','R':'V','s':'j','S':'J','t':'u','T':'U','u':'k','U':'K','ú':'ú','v':'(',
        'V':'W','w':'l','W':'L','x':')','X':'Y','y':';','Y':'X','z':':','Z':'A','0':'z','1':'x','2':'m','3':'v',
        '4':'2','5':'o','6':'p','7':'q','8':'r','9':'s','.':'t','@':'~','-':'¿',',':'-',';':'=',':':'+','<':'{',
        '>':'}','_':'[','+':']','=':'`','[':'8',']':'?','{':',','}':'.','¿':'<','"':'>',"'":'=','(':'1',')':'3', 
        '\n':'7','?':'6','ñ':'5','Ñ':'4'}
    
        listaDeCaracteres = [
                            '=', 'a', 'A', 'b', '`', 'c', 'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 
        'd', 'h', '@', 'i', 'e', 'j', '5', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%', 'o', 'h', 'p','^', 'P', '^', 
        'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x', ')', 'y', ';', 'z', ':','0', 
        'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', 'O', '7', ',', '8', '<', '9', '.','.', 
        '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`', 'c', 'b', 'C', 'B', 'd','|', 'e','c', 
        'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', '8', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%', 'o', 'h','p', 
        '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x', ')', 'y',';', 
        'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', '7', ',', '8', '<','9', 
        '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`', 'c', 'b', 'C', 'B','d','|', 
        'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%', 'o','h', 
        'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x', ')','y', 
        ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', '7', ',', '8','<', 
        '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`', 'c', 'b', 'C','B','d', 
        '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$', 'm', 'g', 'n', '%','o', 
        'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(', 'w', 'l', 'x',')', 
        'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6', 'm', 'w', '/','7', 
        ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b', '`','c','b', 
        'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$', 'm','g', 
        'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v', '(','w', 
        'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n', '6','m', 
        '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A', 'b','`','c', 
        'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l', '$','m', 
        'g', 'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k', 'v','(', 
        'w', 'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5', 'n','6', 
        'm', '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ', '=', 'a', 'A','b','`', 
        'c', 'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j', 'k', 'f', 'l','$', 
        'm', 'g', 'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't', '*', 'u', 'k','v', 
        '(', 'w', 'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v', '4', 'b', '5','n', 
        '6', 'm', 'l', '.', '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..', ' ','=','a', 
        'A', 'b', '`', 'c', 'b', 'C', 'B', 'd', '|', 'e', 'c', 'f', '!', 'g', 'd', 'h', '@', 'i', 'e', 'j','k', 
        'f', 'l', '$', 'm', 'g', 'n', '%', 'o', 'h', 'p', '^', 'P', '^', 'q', 'i', 'r', '&', 's', 'j', 't','*', 
        'u', 'k', 'v', '(', 'w', 'l', 'x', ')', 'y', ';', 'z', ':', '0', 'z', '1', 'x', '2', 'c', '3', 'v','4', 
        'b', '5', 'n', '6', 'm', '7', ',', '8', '<', '9', '.', '.', '>', '@', '/', '-', '?', ',', '..','l','l',
        'd', 'h', '@', 'i', 'e', 'j']

        #Una vez abierto el archivo, creo la variable archivoTexto que contiene el contenido del archivo abierto, volcado en el primer cuadro

        archivoTexto = self.scrolledtext1.get("1.0", tk.END)

        listaEncriptada = (list(reversed(archivoTexto)))
    
        # Determino la cantidad de caracteres 
    
        caracteres_encriptados = list(reversed(listaEncriptada))

        cantidadCaracteresEncriptados = int(len(caracteres_encriptados))

        # Creo la variable limitador para saber la cantidad de caracteres del texto, buscando el #

        limitador = listaEncriptada.index('#')

        # Extraigo los valores que determinan la cantidad real del texto y la desencripto

        cantidad_neta = listaEncriptada[3:limitador]

        canti = []

        for i in cantidad_neta:
            for key, value in dicDeCaracteres.items():
                if i == value:
                    canti.append(key)           

        canti = int("".join(canti))

        # Elimino todos los caracteres extras

        del(listaEncriptada[0:limitador+1])
        lista_neta = listaEncriptada[0:canti]

        # Obtengo las claves del diccionario a traves de lu value

        claves = []
        for i in lista_neta:
            for key, value in dicDeCaracteres.items():
                if i == value:
                    claves.append(key)

        # Creo el Texto Final uniendo todas las claves y se imprime en el segundo cuadro, para su posterior guardado

        textoFinal = str(''.join(claves))

        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert ("1.0", textoFinal)

aplicacion1=Aplicacion() 