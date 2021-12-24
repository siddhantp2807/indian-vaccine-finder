import argparse, sys
from plyer import notification
import time, json, datetime, os
from country import States
from search import Searcher, Parser

parser = argparse.ArgumentParser()


parser.add_argument("-a", "--age", help="Age of the subject", type=int)
parser.add_argument("-d","--dose", help="Enter the dose number reqd.", type=int, choices=[1, 2])
parser.add_argument("-f", "--free", help="Show only free vaccine slots", action="store_true")
parser.add_argument("-t", "--time", help="Time interval between each check", type=int, choices=[30, 60, 120, 300])


args = parser.parse_args()

if args.age < 18 :
    print("Not eligible for vaccination in India.")
    sys.exit(0)
elif args.age < 45 :
    print("Eligible for 18+ slot.")
    age_lim = 18
elif args.age >= 45 :
    print("Eligible for 45+ slot.")
    age_lim = 45

print(f"Age: {args.age}, Dose: {args.dose}, Free: {args.free}, time: {args.time}")


try : 
    json.dump(States().all, open(os.path.join(os.getcwd(), 'data/districts.json'), "w"))
except :
    print(f"{datetime.datetime.now().__str__()} : Connection Error")
    notification.notify(
        title=f"Connection lost",
        message=f"An error occured whie writing state data to json.",
        app_icon = os.path.join(os.getcwd(), 'syringe.ico'),
        timeout=15
    )

districts = [
    "Gautam Buddha Nagar"
]

while True :
    print("Starting....")
    for district in districts :
        try :
            try : 
                search = Searcher().distAvail(district)
            except :
                print(f"{datetime.datetime.now().__str__()} : Connection Error")
                notification.notify(
                    title=f"Connection lost at search",
                    message=f"An error occured while fetching data from API.",
                    app_icon = os.path.join(os.getcwd(), 'syringe.ico'),
                    timeout=15
                )
                break
            else :
                p = Parser(search, age_lim, args.dose, args.free)
                data = p.parser
                p.Logger


                if data != [] :
                    for dataset in data :

                        notification.notify(
                        title=f"{dataset['total_capacity']} Vaccine Slot(s) at Pin:{dataset['pincode']}!",
                        message = f"At: {dataset['name']}\n{dataset['address']}",
                        app_icon = os.path.join(os.getcwd(), 'syringe.ico'),
                        timeout = 15
                        )
        except :
            break
        
    print(f"{datetime.datetime.now().__str__()} : Sleeping....")
    time.sleep(args.time)




