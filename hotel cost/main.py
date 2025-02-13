




def hotel_cost(nights):
    nights = input("How many nights did you stay: ")
    return 140*nights
def plane_cost(city):
    city = input("Where did you stay: ")
    if city =="Dhaka":
        return 130
    if city =="Kolkata":
        return 150
    if city =="Mumbai":
        return 180
    if city =="DElhi":
        return 190
def rental_car_cost(days):
    days = input("How many days did you stay: ")
    if days>7:
        return 40*days-50
    if days>3:
        return 40*days-20
    else:
        return 40*days

def total_cost(nights ,city,days):
    return hotel_cost + plane_cost + rental_car_cost

print( "Total cost" , total_cost)

