# import json
# import requests
# import cowin_constants
# from appointment import Appointment

# class AppointmentByPincode(Appointment):
#     def __init__(self, pincode, date, date_delta=5):
#         self.__init__()
#         this.base_url = cowin_constants.BASE_URL
#         this.endpoint = cowin_constants.CALENDAR_BY_PINCODE_EP
#         this.pincode = pincode
#         this.start_date = date
#         this.end_date = date + date_delta

#     def get_metadata(self):
#         data = {}
#         data['Pincode'] = this.pincode
#         data['Start Date'] = this.start_date
#         data['End Date'] = this.end_date
#         return json.dumps(data)

#     def generate_dates(self):
            

#     def make_rest_call(self):
#         dates = self.generate_dates()
#         # https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=415001&date=12-05-2021
#         URL = "{}{}".format(this.base_url)
#         for date in dates:
            


         