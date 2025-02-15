from datetime import datetime
import pandas
import random
import smtplib
from hosts import Hosts


MY_EMAIL = "seu_email@teste.com"
MY_PASSWORD = "PASSWORD"

today = datetime.now()                      # Obtem a data e hora atuais

today_tuple = (today.month, today.day)      # Cria uma tupla com o mês e o dia atuais

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}      # Cria um dicionário com as datas de aniversário

if today_tuple in birthdays_dict:           # Verifica se a data atual está no dicionário de aniversários

    birthday_person = birthdays_dict[today_tuple]                       # Obtem os dados da pessoa que faz aniversário
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"    # Seleciona um arquivo de template de carta aleatório

    with open(file_path) as letter_file:                                # Abre o arquivo de template de carta
        contents = letter_file.read()                                   # Lê o conteúdo do arquivo
        contents = contents.replace("[NAME]", birthday_person["name"])  # Substitui o marcador de posição [NAME] pelo nome da pessoa

    with smtplib.SMTP(Hosts.gmail.value) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Feliz Aniversário {birthday_person["name"]}!\n\n{contents}"
        )
