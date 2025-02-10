import pandas
import random
#from .service.interface_tkinter import InterfaceTkinter

current_card = {}
to_learn = {}

def main():
    
    with open("data/lista-de-palavras.csv") as file:
        data = pandas.read_csv(file)
        to_learn = data.to_dict(orient="records")
        print(to_learn)

    InterfaceTkinter = InterfaceTkinter(to_learn)
    #InterfaceTkinter.start_and_loop()


if __name__ == "__main__":
    main()

