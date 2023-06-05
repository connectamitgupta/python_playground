##############################################################################################################
############# for whatsapp sending messages you need to activate environment# myenv02-whatsapp ###############
##############################################################################################################
###############
###Few reference website for python whatsapp:
#   https://betterdatascience.com/pywhatkit-python-whatsapp/ 
#   https://towardsdatascience.com/automate-whatsapp-messages-with-python-in-3-steps-d64cf0de4539
#   https://pypi.org/project/pywhatkit/

import pywhatkit
# syntax: phone number with country code, message, hour and minutes
##pywhatkit.sendwhatmsg('+919782430744','Message 2', 18, 55, 15, True, 2)

#pywhatkit.sendwhatmsg_instantly(phone_no='+919782430744',message='automatic msg by bot3')
msg=input("enter your message here: ")

# pywhatkit.sendwhatmsg_instantly(phone_no='+919782430744',message='automatic msg by bot4',tab_close=True,close_time=2)

pywhatkit.sendwhatmsg_instantly(phone_no='+919782430744',message=msg,tab_close=True,close_time=2)

##pywhatkit.text_to_handwriting("Its mind blowing \nJawab: \n2. Apa yang menjadi karakteristik atau keunikan dari algoritma swarm intelligence dibandingkan algoritma lainnya? \nJawab: Karakteristik algoritma swarm intelligence itu adalah: \na)Membuat design ulang representasi solusi \nb)Beberapa dari mekanisme alami belum dipahami \nc)Terkadang tidak mencapai solusi global optimal atau mengalami kegagalan dimana terjebak pada local optimal \nd)Setiap problem optimasi yang akan diselesaikan", rgb=(0, 0, 0))
#pywhatkit.start_server()

