# import smtplib
#
# my_email = 'pedronascimentolisboa@yahoo.com'
# senha = 'ntlzrglzgzezcjmi'
#
# with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=senha)
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg='Subject:Ola\n\nEsse e o corpo do e-mail.')
#


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(day_of_week)

my_birth = dt.datetime(year=1992, month=9, day=15)
print(my_birth)
