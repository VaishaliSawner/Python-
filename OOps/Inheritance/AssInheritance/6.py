class HospitalStaff:
    def duties(self):
        pass 


class Doctor(HospitalStaff):
    def duties(self):
        print("Doctor treats patients")

class Nurse(HospitalStaff):
    def duties(self):
        print("Nurse helps doctors and takes care of patients")



d=Doctor()
d.duties()

n=Nurse()
n.duties()

