import datetime

def Order_number():
    cur_time = datetime.datetime.now().strftime('%y%m%d%H%M')
    #order_number = cur_time

    return cur_time