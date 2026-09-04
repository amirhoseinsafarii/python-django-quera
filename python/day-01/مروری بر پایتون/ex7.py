
from datetime import datetime

def day_calculator(date):
    sjjad_brtd = datetime.strptime("1999-01-14", '%Y-%m-%d')

    d = datetime.strptime(date,'%Y-%m-%d' )

    if (d - sjjad_brtd).days < 0 :
        return "Not yet born"
    else:
        return (d - sjjad_brtd).days