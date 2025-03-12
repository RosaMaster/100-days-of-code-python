### API Endpoints AND API Parameters

#### Links uteís

| **Documentação**                                                                                              |
| ------------------------------------------------------------------------------------------------------------- |
| [smtplib](https://docs.python.org/3/library/smtplib.html)                                                     |
| [datetime](https://docs.python.org/3/library/datetime.html)                                                   |
| [lib requests](https://pypi.org/project/requests/)                                                            |
| [Python String split() Method](https://www.w3schools.com/python/ref_string_split.asp)                         |
| [Sunset and sunrise times API](https://sunrise-sunset.org/api)                                                |
| [https://kanye.rest/](https://kanye.rest/)                                                                    |
| [Requests: HTTP for Humans](https://docs.python-requests.org/en/latest/)                                      |
| [Latitude and Longitude Finder](https://www.latlong.net/)                                                     |
| [Reverse Geocoding Convert Lat Long to Address](https://www.latlong.net/Show-Latitude-Longitude.html)         |
| [HTTP Status Codes Glossary](https://www.webfx.com/web-development/glossary/http-status-codes/)               |
| [Mozilla Firefox Browser](https://www.mozilla.org/en-GB/firefox/new/)                                         |
| [JSON Viewer](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)          |
| [International Space Station Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)      |
| [API](https://pt.wikipedia.org/wiki/Interface_de_programa%C3%A7%C3%A3o_de_aplica%C3%A7%C3%B5es)               |
| [International Space Station - ISS](https://pt.wikipedia.org/wiki/Esta%C3%A7%C3%A3o_Espacial_Internacional)   |
| [yahoo! developer api](https://developer.yahoo.com/api/)                                                      |
| [coinbase api](https://www.coinbase.com/pt-br/developer-platform/products/exchange-api)                       |
| [Rapid API NBA](https://rapidapi.com/api-sports/api/api-nba)                                                  |


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
