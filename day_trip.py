import random

def main():
    destination_list = ["Philly","Chicago","NYC","Myrtle Beach"]
    restaurant_list = ["Rocky's", "Boka", "Lombardi's", "Sam Snead's"]
    transportation_list = ["tram", "bus", "subway", "taxi"]
    entertainment_list = ["skydiving", "bowling", "movies", "arcade"]
    #greeting
    print("Hi there, Welcome to Lamelza travel.")
    print("Where we make your dream vacations comes true!")
    print("")

    destination = get_destination(destination_list)
    restaurant = get_restaurant(restaurant_list)
    trip = get_transportation(transportation_list)
    entertainment = get_entertainment(entertainment_list)

    print("Destination:", destination)
    print("Restaurant:", restaurant)
    print("Transportation:", trip)
    print("Entertainment:", entertainment)

    print("")

    answer = input("Are you happy with this itinerary? ")

    if answer == "yes":
        print("")
        print("Great!" " Happy travels from us to YOU!")

    elif answer != "yes":
        print("")
        print("Okay, no problem." " We are here to help.")
        print("")
    
        trip_response = input("What part of your trip would you like to change? "
        "Type '1' for destination, type '2' for restaurant, type '3' for transportation, or type '4' for entertainment? ")

        if trip_response == "1":
            print("We will now pick a new destination!")
            destination = get_destination(destination_list)
            print("This is your new destination:", destination)
            answer = input("Are you happy with this new choice? 'yes' or 'no'? ")
            #while loop to assist user in selecting another random choice
            while answer == "no":
                print("We will now pick a new destination!")
                destination = get_destination(destination_list)
                print("This is your new destination:", destination)
                answer = input("Are you happy with this new choice? 'yes' or 'no'? ")
            else:
                if answer == "yes":
                    print("Wonderful, happy travels!")


        elif trip_response == "restaurant":
            print("We will now pick a different restaurant!")
        elif trip_response == "transportation":
            print("We will pick a different mode of transportation!")
        elif trip_response == "entertainment":
            print("A new form of entertainment on it's way!")
                          
    

    





def get_destination(destination_list):
    d1 = random.choice(destination_list)
    return d1

def get_restaurant(restaurant_list):
    r1 = random.choice(restaurant_list)
    return r1

def get_transportation(transportation_list):
    t1 = random.choice(transportation_list)
    return t1

def get_entertainment(entertainment_list):
    e1 = random.choice(entertainment_list)
    return e1

main()












