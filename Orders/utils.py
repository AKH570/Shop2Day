import datetime

def Order_number(pk):
    cur_time = datetime.datetime.now().strftime('%y%m%d%H%M')
    order_number = cur_time + str(pk)

    return order_number