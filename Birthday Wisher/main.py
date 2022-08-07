import random
import smtplib
import datetime as dt

my_gmail = "devopsengineerteam22@gmail.com"
gmail_password = "ifqzguudaidafcvo"
gmail_smtp = "smtp.gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)
        connection.sendmail(from_addr=my_gmail, to_addrs="faridhedayati77@yahoo.com",
                            msg=f"subject:Monday Motivation\n\n{quote}")