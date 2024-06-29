"""A tester file that allows you to generate test data for development purposes and more.
   It can modified to test any feature or potential errors, but I used to generate test data"""


from db import *
from datetime import datetime
from color_codes import color_codes
import random

def unique_id():
    last = session.query(daily_emotions).order_by(daily_emotions.unq_id.desc()).first()
    return (last.unq_id + 1)

m = int(input("how many test data do $YOU want to add? "))


def random_val():
    return random.randint(0,10)


def test_database(x):
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        
              
        
        db_list = []
        data = []
        for i in range(12):
            data.append(random_val())

        for i in range(len(data)):
            db_list.append(ints_to_string(color_codes[i], data[i]))
        #change this date ________
        add = daily_emotions(unique_id(),current_date,db_list[0],db_list[1],db_list[2],db_list[3],db_list[4],db_list[5],db_list[6],db_list[7],db_list[8],db_list[9],db_list[10],db_list[11])
        session.add(add)
        
        print("successfully added test data" + str(x))


for xm in range(m):
    test_database(xm)
    print(xm)

session.commit()
session.close()
