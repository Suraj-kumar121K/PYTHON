from person import Person

class Doctor(Person):

    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization

    # Abstract method implementation
    def work(self):
        print("Doctor treats patients")

    def doctor_details(self):
        print("Doctor ID :", self.doctor_id)
        print("Specialization :", self.specialization)

class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease
        
    def work(self):
        print("Patient takes treatment")

    def patient_details(self):
        print("Patient ID :", self.patient_id)
        print("Disease :", self.disease)