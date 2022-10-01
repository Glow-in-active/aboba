class Contact:
    def __init__(self, contactinfo):
        contactinfo = contactinfo.split(',')
        self.personaldata = contactinfo[0].split()
        self.phonenumber = contactinfo[1].strip()
        self.email = contactinfo[2].strip()
        self.surname = self.personaldata[0].strip()
        try:
            self.name = self.personaldata[1].strip()
        except:
            self.name = "No Data"
        try:
            self.patronymic = self.personaldata[2].strip()
        except:
            self.patronymic = "No Data"
        if len(self.phonenumber) < 2:
            self.phonenumber = "No Data"
        if len(self.email) < 2:
            self.email = "No Data"