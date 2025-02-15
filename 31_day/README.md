### Flash Card Project

#### Links uteís

| **Documentação**                                                                              |
| --------------------------------------------------------------------------------------------- |
| [wikipedia lista](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)                  |
| [opensubtitles.org](https://www.opensubtitles.org)                                            |
| [Planilhas Online - Google Sheet](https://workspace.google.com/products/sheets/)              |
| [Github hermitdave](https://github.com/hermitdave/FrequencyWords/tree/master/content)         |
| [Google Documentação Translate](https://cloud.google.com/translate/docs/languages?hl=pt-br)   |
| [tkinter](https://docs.python.org/3/library/tkinter.html)                                     |
| [pandas](https://pandas.pydata.org/docs/)                                                     |
| [random](https://docs.python.org/pt-br/3.13/library/random.html)                              |

#### Import libs

~~~Python
from tkinter import *
import pandas
import random
~~~

#### Tradução com Google Sheet

- Selecionar célula que pretende colocar a tradução
- Incluir comando abaixo: `campo1 = texto | campo2 = linguagem atual | campo3 = linguagem final`

~~~Shell
=GOOGLETRANSLATE(A1, "en", "pt")
~~~

#### STEPS

1. [Step 1 - Create the User Interface (UI) with Tkinter](./utils/step1.md)

2. [Step 2 - Create New Flash Cards](./utils/step2.md)

3. [Step 3 - Flip the Cards](./utils/step3.md)

4. [Step 4 - Save Your Progress](./utils/step4.md)

<br>

[**HOME**](#flash-card-project)
