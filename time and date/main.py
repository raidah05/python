import random
import time 

def getrandomdate(startdate , enddate):
    print("Printing random date between", startdate, "and", enddate)
    randomgenerator = random.random()
    dateFormat = '%m/%d/%y'
    starttime = time.mktime(time.strptime(startdate,dateFormat))
    endtime = time.mktime(time.strptime(enddate,dateFormat))
    randomtime = starttime + randomgenerator * (endtime-starttime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomdate
print("Random date =", getrandomdate("1/2/2024" , "3/3/2025"))