### API Pratice - Creating a GUI Quiz App

#### Links uteís

| **Documentação**                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------- |
| [Open Trivia Database](https://opentdb.com/)                                                                          |
| [HTML Entities](https://www.w3schools.com/html/html_entities.asp)                                                     |
| [HTML Escape / Unescape](https://www.freeformatter.com/html-escape.html#google_vignette)                              |
| [HTML Escape / Unescape](https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string)           |
| [How to wrap text within Tkinter Text Box?](https://www.geeksforgeeks.org/how-to-wrap-text-within-tkinter-text-box/)  |
| [How to wrap text within Tkinter Text Box?](https://www.geeksforgeeks.org/how-to-disable-enable-a-button-in-tkinter/) |

####  API

**API (Application Programming Interface)** é um conjunto de definições e protocolos que permite que diferentes softwares se comuniquem entre si. As APIs definem os métodos e dados que os desenvolvedores podem usar para interagir com um serviço, biblioteca ou sistema operacional

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

###### kanye-quotes-api-project

~~~Python
import requests
from datetime import datetime
import smtplib
import time
~~~

###### iss-overhead-notifier-project

~~~Python
import requests
from datetime import datetime
import smtplib
import time
~~~

#### SMTP Information

| **Service** | **HOST**            |
| ----------- | ------------------- |
| `Gmail`     | smtp.gmail.com      |
| `Hotmail`   | smtp.live.com       |
| `Yahoo`     | smtp.mail.yahoo.com |


<br>

[**HOME**](#api-endpoints-and-api-parameters)
