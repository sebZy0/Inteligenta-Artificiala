from dataclasses import replace
from email import header
import requests
from bs4 import BeautifulSoup as bs
import smtplib

sender = "-0iojdsa9y2@email.com"  # secretHash2k30
subject = "Pretul a scazut la 1000 de lei"
to_addr_list = ['sebi']  # secretHash2k40
cc_addr_list = ['']


def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        serverSMTP = 'mail.x-it.ro:26'
        header = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header+message
        server = smtplib.SMTP(serverSMTP)
        server.starttls()
        server.login(sender, "09u98hjn9u98uj9um2")  # alsoSecretHash2k50
        server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        print("Error: unable to send email")
        return False


def data_scraping():
    req = requests.get(
        "https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-deep-purple-mq9x3rx-a/pd/DJDY4LMBM/?cmpid=99160")
    soup = bs(req.text, "html.parser")
    price = soup.find('p', {'class': 'product-new-price'}).text
    new_price = price[0:5]
    new_price = new_price.replace('.', '')
    print(int(new_price))
    price = int(new_price)
    price -= 5000
    if (price < 7699):
        sendemail(sender, "Pretul a scazut la: "+str(price),
                  subject, to_addr_list, cc_addr_list=[])
        print("Pretul a scazut")
    else:
        print("Pretul nu a scazut")


data_scraping()
