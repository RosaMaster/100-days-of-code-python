### Send Email Project

#### Links uteís

| **Documentação**                                                                      |
| ------------------------------------------------------------------------------------- |
| [smtplib](https://docs.python.org/3/library/smtplib.html)                             |
| [datetime](https://docs.python.org/3/library/datetime.html)                           |
| [pandas](https://pandas.pydata.org/docs/)                                             |
| [random](https://docs.python.org/pt-br/3.13/library/random.html)                      |
| [201 Citações de motivação](https://www.positivityblog.com/monday-motivation-quotes/) |
| [Hospedagem - pythonanywhere](https://www.pythonanywhere.com/)                        |


####  SMTP (smtplib)

**SMTP (Simple Mail Transfer Protocol)** é um protocolo de comunicação usado para enviar e-mails pela Internet. Ele define como as mensagens de e-mail são transmitidas de um servidor de e-mail para outro. O SMTP é usado principalmente para enviar mensagens de e-mail de clientes de e-mail (como Outlook, Gmail, etc.) para servidores de e-mail e entre servidores de e-mail
No código, o módulo `smtplib` do Python é usado para enviar um e-mail. Aqui está um exemplo simplificado de como o SMTP é usado no seu código:

##### Exemplo

~~~Python
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
    connection.starttls()  # Inicia a conexão segura
    connection.login(MY_EMAIL, MY_PASSWORD)  # Faz login no servidor SMTP
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="recipient@example.com",
        msg="Subject:Hello\n\nThis is the body of the email."
    )
~~~

###### Neste exemplo:

- `smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS")` cria uma conexão com o servidor SMTP do seu provedor de e-mail.
- `connection.starttls()` inicia uma conexão segura usando TLS (Transport Layer Security).
- `connection.login(MY_EMAIL, MY_PASSWORD)` faz login no servidor SMTP usando suas credenciais de e-mail.
- `connection.sendmail(from_addr, to_addrs, msg)` envia o e-mail do endereço `from_addr` para o endereço `to_addrs` com a mensagem `msg`.

<br>

> Certifique-se de substituir `"YOUR EMAIL"`, `"YOUR PASSWORD"` e `"YOUR EMAIL PROVIDER SMTP SERVER ADDRESS"` com suas informações reais.

#### Import libs

~~~Python
from datetime import datetime
import pandas
import random
import smtplib
~~~

#### SMTP Information

| **Service** | **HOST**            |
| ----------- | ------------------- |
| `Gmail`     | smtp.gmail.com      |
| `Hotmail`   | smtp.live.com       |
| `Yahoo`     | smtp.mail.yahoo.com |


<br>

[**HOME**](#send-email-project)
