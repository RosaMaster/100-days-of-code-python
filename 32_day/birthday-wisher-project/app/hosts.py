from enum import Enum

class Hosts(Enum):
    '''Enum class to store the SMTP hosts for the most common email providers'''

    gmail = 'smtp.gmail.com'
    hotmail = 'smtp.live.com'
    yahoo = 'smtp.mail.yahoo.com'
    outlook = 'smtp-mail.outlook.com'
    aol = 'smtp.aol.com'
    mail = 'smtp.mail.com'
    protonmail = 'smtp.protonmail.com'
