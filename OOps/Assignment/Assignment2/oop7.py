class Patient:
    
    __total_patients = 0


    def __init__(self, patient_id, name, disease, doctor_assigned):
    
        self.__patient_id = patient_id
        self.__name = name
        self.__disease = disease
        self.__doctor_assigned = doctor_assigned

        
        Patient.__total_patients += 1

    
    def display_details(self):
        print("Patient ID:", self.__patient_id)
        print("Name:", self.__name)
        print("Disease:", self.__disease)
        print("Doctor Assigned:", self.__doctor_assigned)

    def change_doctor(self, new_doctor):
        self.__doctor_assigned = new_doctor
        print("Doctor changed successfully.")

    
    @classmethod
    def from_string(cls, patient_data):
        
        patient_id, name, disease, doctor = patient_data.split(",")
        return cls(patient_id, name, disease, doctor)

    
    @classmethod
    def get_total_patients(cls):
        return cls.__total_patients



p1 = Patient("P101", "Sohan", "Fever", "Dr. Pihu")


p2 = Patient.from_string("P102,Riya,Malaria,Dr. Preet")


p1.display_details()
print()

p2.display_details()
print()


p1.change_doctor("Dr. Priya")
p1.display_details()
print()


print("Total Patients Admitted:", Patient.get_total_patients())