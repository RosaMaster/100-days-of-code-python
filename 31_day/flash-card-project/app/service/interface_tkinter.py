from tkinter import *
from util.colors import Colors
import random
import pandas

current_card = {}
to_learn = {}

class InterfaceTkinter:
    '''Essa classe é responsável por criar a interface gráfica do programa.'''

    def __init__(self, to_learn):
        '''Inicializa a interface gráfica.'''

        # Configurações da janela
        self.flip_timer = 3000
        self.current_card = {}
        self.to_learn = to_learn                                                        # Lista de palavras a serem aprendidas
        self.window = Tk()                                                              # Cria a janela principal
        self.window.title("My Flash Card - By RosaMaster")                              # Define o título da janela
        self.window.config(padx=50, pady=50, bg=Colors.BACKGROUND_COLOR.value)          # Define o espaçamento interno da janela
        self.canvas = Canvas(width=800, height=526)                                     # Cria o canvas
        self.card_front_image = PhotoImage(file="images/card_front.png")                # Carrega a imagem do front card
        self.canvas.create_image(400, 263, image=self.card_front_image)                 # Adiciona a imagem ao canvas
        self.canvas.config(bg=Colors.BACKGROUND_COLOR.value, highlightthickness=0)      # Configura o canvas
        self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))   # Adiciona o título ao canvas
        self.canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))      # Adiciona a palavra ao canvas
        self.canvas.grid(row=0, column=0, columnspan=2)                                 # Posiciona o canvas na janela
        
        # Button Wrong
        self.cross_image = PhotoImage(file="images/wrong.png")                                          # Carrega a imagem do botão de errado
        self.button_wrong = Button(image=self.cross_image, highlightthickness=0, command=self)    # Cria o botão de errado
        self.button_wrong.grid(row=1, column=0)                                                         # Posiciona o botão de errado na janela

        # Button Right
        self.check_image = PhotoImage(file="images/right.png")                                          # Carrega a imagem do botão de certo
        self.button_right = Button(image=self.check_image, highlightthickness=0, command=self.right)    # Cria o botão de certo
        self.button_right.grid(row=1, column=1)                                                         # Posiciona o botão de certo na janela


        # self.canvas.create_image(400, 263, image=self.card_image)                   # Adiciona a imagem ao canvas
        # self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
        # self.card_word = self.canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
        # self.button_right = Button(text="✔", highlightthickness=0, command=self.right)
        # self.button_right.grid(row=1, column=1)
        # self.button_wrong = Button(text="❌", highlightthickness=0, command=self.wrong)
        # self.button_wrong.grid(row=1, column=0)

    # def flip_card(self):
    #     canvas.itemconfig(card_title, text="English", fill="white")
    #     canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    #     canvas.itemconfig(card_background, image=card_back_img)


    # def is_known(self):
    #     to_learn.remove(current_card)
    #     print(len(to_learn))
    #     data = pandas.DataFrame(to_learn)
    #     data.to_csv("data/words_to_learn.csv", index=False)
    #     next_card()

    def wrong(self):
        pass

    def right(self):
        self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.to_learn)
        self.canvas.itemconfig(self.card_title, text="Portugues", fill="black")
        self.canvas.itemconfig(self.card_word, text=current_card["Portugues"], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def start_and_loop(self):
        '''Inicia a interface gráfica e mantém a janela aberta.'''

        self.window.mainloop()       # Mantém a janela aberta



def main():

    with open("data/lista-de-palavras.csv") as file:
        data = pandas.read_csv(file)
        to_learn = data.to_dict(orient="records")
        #print(to_learn)

    interface = InterfaceTkinter(to_learn)
    interface.start_and_loop()


if __name__ == "__main__":
    main()

