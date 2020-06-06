from Notification import *

# url = 'https://coinmarketcap.com/currencies/ethereum/'
url = input('ENTER URL ADDRESS OF COIN:') # paste url of an crypto coin you choosed from coinmarket.com/currencies 
# val = "0.0232850"
val = input('ENTER YOUR LEVEL:') # input your threshold level for your specific coin 

e_mail = 'sender_example@gmail.com' # give here your e mails. 
receiver = 'receiver_example@gmail.com' # sender and receiver e mails can be same

Coin = Notification(url, val, e_mail, receiver)

initial = Coin.init_val
val = Coin.val

# following code will do: 
# considers your level you specified and warn you when the real coin value reaches your level.
# and send you a notification e mail.
if val > initial:
    print('Notify Up Working')
    Coin.notify_up()
    print()
elif val < initial:
    print('Notify Down Working')
    Coin.notify_down()