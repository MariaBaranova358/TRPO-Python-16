class Patient:
    def __init__(self, last_name, first_name, middle_name, birth_year, address, diagnosis, days):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_year = birth_year
        self.address = address
        self.diagnosis = diagnosis
        self.days = days

class Hospital:
    def __init__(self):
        self.patients = []
    
    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('/')
                    self.patients.append(Patient(
                        parts[0], parts[1], parts[2], 
                        int(parts[3]), parts[4], parts[5], int(parts[6])
                    ))
