import json
import requests
import datetime
import time
import cowin_constants
from appointment import Appointment

class AppointmentByPincodeDate(Appointment):
    def __init__(self, pincode, date, day_delta=7):
        super(AppointmentByPincode, self).__init__()
        self.base_url = cowin_constants.BASE_URL
        self.endpoint = cowin_constants.CALENDAR_BY_PINCODE_EP
        self.pincode = pincode
        self.start_date = date
        self.start_date = datetime.datetime.strptime(self.start_date, '%d-%m-%Y')
        self.end_date = self.start_date + datetime.timedelta(days=day_delta)
        self.day_delta = day_delta

    def get_metadata(self):
        data = {}
        data['Pincode'] = self.pincode
        data['Start Date'] = self.start_date
        data['End Date'] = self.end_date
        return json.dumps(data)

    def generate_dates(self):
        dates = []
        for x in range(0,self.day_delta):
            date = self.start_date+datetime.timedelta(days=x)
            dates.append(date.strftime('%d-%m-%Y'))
        print ("Dates: {}".format(dates))
        return dates

    def get_appointments_data(self):
        dates = self.generate_dates()
        url = "{}{}".format(self.base_url,self.endpoint)
        print ("URL: {}".format(url))
        headers = {'User-agent': 'Mozilla/5.0', 'Accept-Language': 'hi_IN'}
        params = {}
        params[cowin_constants.PINCODE] = self.pincode
        request_data = ""
        for date in dates:
            params[cowin_constants.DATE] = date
            r = requests.get(url, params=params, headers=headers)
            print("{}\n{}\n{}".format(r.text, r.status_code, r))
            data = r.text
            if(r.status_code<300 and r.status_code>=200 and len(data['centers']))>0:
                request_data = r.text
            time.sleep(0.5)
        if request_data == "":
            print ("Didn't find any appointments. Will try again in a few minutes.")
        return request_data

    def get_o    


ap = AppointmentByPincodeDate("415001","12-05-2021")
appointment_data = ap.get_appointments_data()


         