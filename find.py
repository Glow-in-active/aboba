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


directory = input("Input file directory: ")
f = open(directory, encoding="utf-8")
Database = []
print("Contacts loading started")
for i in f:
    Database.append(Contact(i))
print("Contacts loading finished")
while True:
    print("Select a command")
    print("1 - Search by phone number")
    print("2 - Search by email")
    print("3 - Search by name")
    print("4 - Search for all contacts that you do not have detected email or phone")
    print("5 - Search for all contacts that you do not have detected email and phone")
    print("6 - Edit contact")
    command = int(input())
    if command == 1:
        number = input("Enter phone number ")
        for i in Database:
            if i.phonenumber == number:
                print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
        print()
    if command == 2:
        email = input("Enter email ")
        for i in Database:
            if i.email == email:
                print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
        print()
    if command == 3:
        name = input("Enter name ").strip().split()
        for i in Database:
            if len(name) > 0:
                if name[0]==i.name or name[0]==i.surname or name[0]==i.patronymic:
                    if len(name)==1:
                        print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
                    else:
                        if name[1]==i.name or name[1]==i.surname or name[1]==i.patronymic:
                            if len(name)==2:
                                print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
                            else:
                                if name[1]==i.name or name[1]==i.surname or name[1]==i.patronymic:
                                    print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
        print()
    if command==4:
        for i in Database:
            if i.email=="No Data" or i.phonenumber=="No Data":
                print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
        print()
    if command==5:
        for i in Database:
            if i.email=="No Data" and i.phonenumber=="No Data":
                print(i.surname, i.name, i.patronymic, i.phonenumber, i.email)
        print()
    if command==6:
        name = input("Enter name ").strip().split()
        conindex=0
        for i in Database:
            if len(name) > 0:
                if name[0]==i.name or name[0]==i.surname or name[0]==i.patronymic:
                    if len(name)==1:
                        break
                    else:
                        if name[1]==i.name or name[1]==i.surname or name[1]==i.patronymic:
                            if len(name)==2:
                                break
                            else:
                                if name[1]==i.name or name[1]==i.surname or name[1]==i.patronymic:
                                    break
            conindex=conindex+1
        print("if you want to edit contact")
        print(Database[conindex].surname, Database[conindex].name, Database[conindex].surname, Database[conindex].phonenumber, Database[conindex].email)
        contactinfo=input("Enter new contact data else press enter and refine you request ")
        if len(contactinfo)>3:
            contactinfo = contactinfo.split(',')
            Database[conindex].personaldata = contactinfo[0].split()
            Database[conindex].phonenumber = contactinfo[1].strip()
            Database[conindex].email = contactinfo[2].strip()
            Database[conindex].surname = Database[conindex].personaldata[0].strip()
            try:
                Database[conindex].name = Database[conindex].personaldata[1].strip()
            except:
                Database[conindex].name = "No Data"
            try:
                Database[conindex].patronymic = Database[conindex].personaldata[2].strip()
            except:
                Database[conindex].patronymic = "No Data"
            if len(Database[conindex].phonenumber) < 2:
                Database[conindex].phonenumber = "No Data"
            if len(Database[conindex].email) < 2:
                Database[conindex].email = "No Data"
