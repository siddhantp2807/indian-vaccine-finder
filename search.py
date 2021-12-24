import requests
import json, os
import datetime 


class Searcher :

    def __init__(self, daysfromnow = 1) :
        self.header = {'content-type' : 'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        self.date = datetime.datetime.strftime((datetime.datetime.now() + datetime.timedelta(days=daysfromnow)).date(), '%d-%m-%Y')
        self.states = json.load(open(os.path.join(os.getcwd(), 'data/districts.json')))['states']
        

    def getStateId(self, statename) :

        for state in self.states['states'] :
            if statename.lower() == state['state_name'].lower() :
                return state['state_id']

        return -1
    @property
    def districts(self) :
        dist = []
        for state in self.states :
            for dt in state['districts'] :
                dist.append(dt)
        
        return dist

    def getDistrictId(self, name) :
        
        for district in self.districts :
            if name == district['district_name'] :
                return district['district_id']

        return -1

    def pinAvail(self, pincode= 110021) :
        res = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={self.date}', headers=self.header)

        return res.json()


    def distAvail(self, dist_name) :
        res = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={self.getDistrictId(dist_name)}&date={self.date}', headers=self.header)

        return res.json()


class Vacancy :
    
    def __init__(self, obj, age_lim, dose) :
        self.center_id = obj['center_id']
        self.name = obj['name']
        self.address = ', '.join([i for i in [obj['address'], obj['block_name'], obj['district_name']] if i != "Not Applicable"])
        self.state = obj['state_name']
        self.pincode = obj['pincode']
        self.timing = f'{obj["from"]}-{obj["to"]}'
        self.fee_type = obj['fee_type']
        self.price = 0
        self.vacancies = []
        self.total_capacity = 0
        for session in obj['sessions'] :
            if session['available_capacity'] != 0 and session['min_age_limit'] == age_lim:
                self.vacancies.append(session)
            self.total_capacity += session[f'available_capacity_dose{dose}']
        if self.fee_type == "Paid" :
            self.price = obj["vaccine_fees"][0]["fee"]


        

class Parser :

    def __init__(self, object, age_lim, dose, free) :
        self.object = object
        self.age_lim = age_lim
        self.dose = dose
        self.free = free
    
    @property
    def parser(self) :
        data = []
        for obj in self.object['centers'] :
            if self.free == True and obj['fee_type'] == "Free":
                if Vacancy(obj, self.age_lim, self.dose).vacancies != [] :
                    data.append(Vacancy(obj, self.age_lim, self.dose).__dict__)
            elif self.free == False :
                if Vacancy(obj, self.age_lim, self.dose).vacancies != [] :
                    data.append(Vacancy(obj, self.age_lim, self.dose).__dict__)
        return data
    
    @property
    def Logger(self) :
        data = self.parser

        if data != [] :
            alData = json.load(open(os.path.join(os.getcwd(), "data", "log.json")))
            alData.append({'time' : datetime.datetime.now().__str__(), 'data' : data })
            json.dump(alData, open(os.path.join(os.getcwd(), "data", "log.json"), "w"))
        
        return True





