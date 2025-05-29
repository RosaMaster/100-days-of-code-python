from tkinter import *
import requests


def get_quote():
    ''' Função para obter uma citação aleatória de Kanye West usando a API https://api.kanye.rest '''

    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()                       # Cria uma janela
window.title("Kanye Says...")       # Define o título da janela
window.config(padx=50, pady=50)     # Adiciona preenchimento interno

canvas = Canvas(width=300, height=414)                      # Cria um canvas
background_img = PhotoImage(file="img/background.png")      # Carrega a imagem de fundo
canvas.create_image(150, 207, image=background_img)         # Adiciona a imagem de fundo ao canvas
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white") # Adiciona o texto da citação ao canvas
canvas.grid(row=0, column=0)                                # Exibe o canvas na janela

kanye_img = PhotoImage(file="img/kanye.png")                                    # Carrega a imagem do botão
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote) # Cria um botão com a imagem de Kanye
kanye_button.grid(row=1, column=0)                                              # Exibe o botão na janela

window.mainloop()                   # Inicia o loop principal da janela
