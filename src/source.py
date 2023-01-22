import json
import csv
class worker:
    def __init__(self):
        self.ulist = ["userid","name","dob","gender","phone","email","address","country","salary"]
        self.ulist_def = ["Employee ID","Name of the employee","Date of birth (dd/mm/yyyy)","Gender (M/F)","Phone number","Email address","Address","Country","Salary (in Numbers no currency symbol and no comma)"]
        self.path = "/workspaces/manager_/src/db.json"
        self.userid = None
    def create_user(self):
        a = {}
        for number,i in enumerate(self.ulist_def):
            a[self.ulist[number]] = input("Enter the "+i+" : ")
        with open(self.path,"r") as f:
            i = 0 
            try:
                data = json.load(f)
                data["all"].append(a)
                data["empid"].append(a["userid"])
                with open(self.path,"w") as k:
                    json.dump(data,k,indent=4)
            except json.decoder.JSONDecodeError:
                pass
        return i
    def read_user_alldata(self):
        with open(self.path,"r") as f:
            data = json.load(f)
            dict = {"userid":[],"name":[],"dob":[],"gender":[],"phone":[],"email":[],"address":[],"country":[],"salary":[]} 
            for i in data["all"]:
                dict["userid"].append(i["userid"])
                dict["name"].append(i["name"])
                dict["dob"].append(i["dob"])
                dict["gender"].append(i["gender"])
                dict["phone"].append(i["phone"])
                dict["email"].append(i["email"])
                dict["address"].append(i["address"])
                dict["country"].append(i["country"])
                dict["salary"].append(i["salary"])
            return dict

    def read_user(self,userid):
        with open(self.path,"r") as f:
            data = json.load(f)
            for i in data["all"]:
                if int(i["userid"]) == userid:
                    return i
    def update_user(self,userid):
        with open(self.path,"r") as f:
            data = json.load(f)
            for i in data["all"]:
                if int(i["userid"]) == userid:
                    for number,j in enumerate(self.ulist_def):
                        if number == 0:
                            continue
                        i[self.ulist[number]] = input("Enter the "+j+"["+i[self.ulist[number]]+"] : ")
                        if i == "":
                            i = i[self.ulist[number]]
                    with open(self.path,"w") as k:
                        json.dump(data,k,indent=4)
                    return i
    def delete_user(self,userid):
        with open(self.path,"r") as f:
            data = json.load(f)
            for i in data["all"]:
                if int(i["userid"]) == userid:
                    data["all"].remove(i)
                    data["empid"].remove(i["userid"])
                    f.seek(0)
                    with open(self.path,"w") as k:
                        json.dump(data,k,indent=4)
                    return i
            
    def search_user(self,userid):
        with open(self.path,"r") as f:
            data = json.load(f)
            for i in data["all"]:
                if int(i["userid"]) == userid:
                    return i
    def search_user_name(self,name):
        with open(self.path,"r") as f:
            data = json.load(f)
            lst = [] 
            for i in data["all"]:
                if i["name"] == name:
                    return i
                elif i["name"].startswith(name):
                    lst.append(i)
            return lst

    def export_csv(self):
        i =None
        with open(self.path,"r") as f:
            data = json.load(f)
            with open("data.csv","w") as f:
                writer = csv.writer(f)
                writer.writerow(self.ulist)
                for i in data["all"]:
                    writer.writerow(i.values())
                    i=0
        return i