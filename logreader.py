import json, os

class Log :

    def __init__(self) :
        self.filename = 'data/log.json'
        self.data = json.load(open(os.path.join(os.getcwd(), self.filename), 'r'))

    def last(self, n=1) :
        for timenode in self.data[-n:] :
            print(f"Last run: {timenode['time']}")
            for center in timenode['data'] :
                print(f"Center: {center['name']}")
                print(f"Address: {center['address']}")
                print(f"Pincode: {center['pincode']}")
                print(f"Price: {center['price']}")
                print(f"Timing: {center['timing']}")
                print('\n')
                for vac in center['vacancies'] :

                    print(f"Date: {vac['date']}")
                    print(f"Available Capacity: {vac['available_capacity']}")
                    print(f"Vaccine: {vac['vaccine']}")
                print("\n====================================================================\n")


    def first(self, n=1) :
        for timenode in self.data[:n] :
            for center in timenode['data'] :
                print(f"Center: {center['name']}")
                print(f"Address: {center['address']}")
                print(f"Pincode: {center['pincode']}")
                print(f"Price: {center['price']}")
                print(f"Timing: {center['timing']}")
                print('\n')
                for vac in center['vacancies'] :
                
                    print(f"Date: {vac['date']}")
                    print(f"Available Capacity: {vac['available_capacity']}")
                    print(f"Vaccine: {vac['vaccine']}")
                    print('\n')
                print("\n====================================================================\n")

Log().last()