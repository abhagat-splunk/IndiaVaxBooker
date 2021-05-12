import cowin_constants

class Appointment(object):
    def __init__(self):
        self.base_url = cowin_constants.BASE_URL

    def get_base_url(self):
        return self.base_url