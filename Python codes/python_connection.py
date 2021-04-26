  
from firebase import firebase
import datetime
import time
import serial


#connect to the firebase db
my_url = 'https://home-automation2404-default-rtdb.firebaseio.com/'
fb = firebase.FirebaseApplication(my_url, None)


while True:
    inp = input("What is the status? ")
    result = fb.patch(my_url + '', {'data': inp}) #fb.post(,) can also be used- but will create a unique key

    
    print(result)

#close the serial connection
ser.close()