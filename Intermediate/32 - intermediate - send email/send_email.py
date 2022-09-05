import smtplib

WEEK = {'segunda-feira': 0,
        'terca-feira': 1,
        'quarta-feira': 2,
        'quinta-feira': 3,
        'sexta-feira': 4,
        'sabado': 5,
        'domingo': 6,
        }


def choice_quote():
    from random import choice

    with open('quotes.txt', 'r') as file:
        all_quotes = file.readlines()
        return choice(all_quotes)


def day_of_week():
    import datetime as dt

    now = dt.datetime.now()
    day = now.weekday()
    return day


# Send email

my_email = 'pedronascimentolisboa@yahoo.com'
senha = 'ntlzrglzgzezcjmi'

if day_of_week() == WEEK['segunda-feira']:
    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=senha
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs='phlisboa2000@gmail.com',
            msg=f'Subject:One quote for your day!\n\n{choice_quote()}'
        )
