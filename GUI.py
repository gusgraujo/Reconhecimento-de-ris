from tkinter import *
from tkinter import Menu
from functools import partial
from PIL import Image,ImageTk
from fnc.Iris import Olho
import fnc.Iris


olho1 = Olho(r"C:\SourceCode\IrisProt\Samples\Amostra5.1.jpg",1)

olho2 = Olho(r"C:\SourceCode\IrisProt\Samples\Amostra5.jpg",2)


'''
def main_gui():

    #Cria Plat grafica
    root = Tk()
 
    root.title("Protótipo Íris")
    root.configure(background = "Gray")

    menu = Menu(root)

    item = Menu(menu)
    item.add_command(label = 'Exit')
    
    buttonA = Button(root,width = 30 , text = "ADD")
    buttonA["command"] = partial(pegar_imagem,buttonA)
    buttonA.grid(column = 1 , row = 0)

    buttonC = Button(root,width = 30 , text = "Iris Recognition")
    buttonC["command"] = partial(achar_Iris,buttonC)
    buttonC.grid(column = 1 , row = 1)
    

    buttonImg = Button(root,width = 30 , text = "Show-Image")
    buttonImg["command"] = partial(mostrar_Imagem,buttonImg)
    buttonImg.grid(column = 0 , row = 0)

    buttonImg = Button(root,width = 30 , text = "2D Gabor-Wavelets")
    buttonImg["command"] = partial(mostrar_Imagem,buttonImg)
    buttonImg.grid(column = 0 , row = 0)
    
    
    labelA = Label(root,text = "Imagem Referencia :")
    labelA.grid(column = 2 , row = 3)

  
 
    image = Image.open("C:\_SourceCode\Prototipo\Samples\lena.jpg")
    image = image.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.grid(column = 2 , row = 6)

    

    root.config(menu=item)
    #define tamanho da tela
    root.geometry("800x600")

    root.mainloop()
    
'''





def montar_inicio():

    #Cria Plat grafica

    root = Tk()
 
    root.title("Protótipo Íris")
    root.configure(background = "White")

    menu = Menu(root)

    
    
    labelA = Label(root,text = "Imagem Referencia 1 :")
    labelA.grid(column = 0 , row = 3)
    
    image = Image.open(olho1.caminho)
    image = image.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.grid(column = 0 , row = 6)


    
    labelA = Label(root,text = "Imagem Referencia 2 :")
    labelA.grid(column = 4 , row = 3)

    image = Image.open(olho2.caminho)
    image = image.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.grid(column = 4 , row = 6)


    buttonC = Button(root,width = 30 , text = "Trocar Referencia 1")
    buttonC.grid(column = 0 , row = 7)

    
    buttonA = Button(root,width = 30 , text = "Trocar Referencia 2")
    buttonA.grid(column = 4 , row = 7)
    

    
    buttonExtract = Button(root,width = 30 , text = "Extrair Feature")
    buttonExtract.grid(column = 3 , row = 7)
    
    f1 = olho1.extrairCodigo()
    f2 = olho2.extrairCodigo()


    
    labelB1 = Label(root,text ="Binarios : ")
    labelB1.grid(column = 0 , row = 8)

    
    labelF1 = Label(root,text = f1)
    labelF1.grid(column = 0 , row = 9)
    
    
    labelB2 = Label(root,text ="Binarios : ")
    labelB2.grid(column = 4 , row = 8)

    
    labelF2 = Label(root,text = f2)
    labelF2.grid(column = 4 , row = 9)


    
    buttonExtract = Button(root,width = 30 , text = "Calcular HD")
    buttonExtract.grid(column = 3 , row = 9)
    
    hd = fnc.Iris.compararHd(f1,f2)


    

    item = Menu(menu)
    
    item.add_command(label = 'ADD REF')
    item.add_command(label = 'Exit')


    
    root.config(menu=item)
    #define tamanho da tela
    root.geometry("800x600")

    root.mainloop()



