import requests
import bs4
import time
import smtplib
import getpass


class Notification():
    """
    The class have capabilities to do getting price levels of updated coin values from coinmarketcap.com,
    have methods for detecting a specified level of a coin reaching a real and up to date value of coin.
    and informing user with an e mail.
    """
    def __init__(self, url, val, e_mail, receiver, init_val=None):

        self.url = url
        self.val = val
        
        self.e_mail = e_mail
        self.receiver = receiver

        res = requests.get(self.url)
        soup = bs4.BeautifulSoup(res.text,"lxml")
        key = 'cmc-details-panel-price__crypto-price'
        value = soup.select("."+key)[0].text.split()[0]
        self.init_val = value
        
    def get_price(self):
        
        res = requests.get(self.url)
        soup = bs4.BeautifulSoup(res.text,"lxml")
        key = 'cmc-details-panel-price__crypto-price'
        value = soup.select("."+key)[0].text.split()[0]
        return value

    def notify_up(self):

        initial_val = self.get_price()
        while self.val>initial_val:

            print(initial_val)
            print('New value fetching')
            initial_val = self.get_price() 

            if initial_val>=self.val:
                # send e mail
                self.mail_sender()
                print('LEVEL REACHED AT THE TOP')
                print('LEVEL:',initial_val,'BTC')
                print('MAIL SENT')
                break
            
            else:
                time.sleep(5)

    def notify_down(self):
        
        initial_val = self.get_price()
        while self.val<initial_val:

            print(initial_val)
            print('New value fetching')
            initial_val = self.get_price() 

            if initial_val<=self.val:
                # send e mail
                self.mail_sender()
                print('LEVEL REACHED AT THE BOTTOM')
                print('LEVEL:',initial_val,'BTC')
                print('MAIL SENT')
                break
            
            else:
                time.sleep(5)
                
    def mail_sender(self):
        
        smtp_object = smtplib.SMTP('smtp.gmail.com',587)
        smtp_object.ehlo()
        smtp_object.starttls()
        e_mail = 'example@gmail.com'
        password = 'vzqtinwferaddkjq' # get the password from google acount's app password section
        smtp_object.login(e_mail,password)
        
        from_address = self.e_mail
        to_address = self.receiver
        subject = 'Level reached'+ 'FOR+'+self.url[37:-1].upper()+' BTC'
        message = 'Your specified level is reached.'
        value = self.get_price()
        msg = "Subject: " + subject + '\n' + message + '\n' + 'New Level:' + value
        smtp_object.sendmail(from_address,to_address,msg)