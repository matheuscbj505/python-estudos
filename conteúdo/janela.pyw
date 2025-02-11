from tkinter import *
from PIL import Image, ImageTk

class Janela: 
    def __init__(self, raiz):
        self.fr1 = Frame(raiz)
        self.fr1.pack()
        
        # Carregar e redimensionar a imagem
        original_image = Image.open("C:/Users/mathe/Desktop/Python/interface/pyt.png")
        resized_image = original_image.resize((200, 150))  # Ajuste o tamanho conforme necessário
        self.img = ImageTk.PhotoImage(resized_image)
        
        # Cria o rótulo (label) com a imagem
        self.lb1 = Label(self.fr1, text="Hello World", background="green", font=("Times", 15, "bold", "italic"))
        self.lb1.pack()

        # Cria o botão e associa o comando para mudar o texto do rótulo
        self.bt1 = Button(self.fr1, text="Click here", command=self.muda_label)
        self.bt1.pack(side=TOP)
        
        # Cria um rótulo para a imagem, mas não o exibe inicialmente
        self.lb_img = Label(self.fr1, image=self.img)
        
        # Associa o evento de pressionar a tecla Enter à janela principal
        raiz.bind("<Return>", self.muda_label2)
        
    def muda_label(self):
        # Muda o texto do rótulo e exibe a imagem quando o botão é clicado
        self.lb1["text"] = "Deu certo"
        self.lb_img.pack()
          
    def muda_label2(self, event): 
        # Muda o texto do rótulo e exibe a imagem quando a tecla Enter é pressionada
        self.lb1["text"] = "Deu certo"
        self.lb_img.pack()

# Cria a janela principal
raiz = Tk()
Janela(raiz)
raiz.geometry("600x400+300+200")
raiz.title ("aula 50")
raiz["relief"] = RAISED
raiz["border"] = 15
raiz.mainloop()
