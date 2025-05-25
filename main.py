import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from operator import attrgetter
from patient import Hospital

class HospitalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hospital_form.ui", self)
        
        self.hospital = Hospital()
        

        self.pushButton.clicked.connect(self.load_and_display_data)
        self.btnSort.clicked.connect(self.sort_by_last_name) 
        

        if hasattr(self, 'tableWidget'):
            self.tableWidget.setRowCount(0)
    
    def load_and_display_data(self):
        self.hospital.load_from_file("patients.txt")
        self.display_patients()

    def display_patients(self):
        if not hasattr(self, 'tableWidget'):
            return
            
        self.tableWidget.setRowCount(0)
        for row, patient in enumerate(self.hospital.patients):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(
                f"{patient.last_name} {patient.first_name} {patient.middle_name}"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(patient.birth_year)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(patient.address))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(patient.diagnosis))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(patient.days)))
        
        self.tableWidget.resizeColumnsToContents()
    
    def sort_by_last_name(self):
        """Сортирует пациентов по фамилии от А до Я"""
        if hasattr(self.hospital, 'patients'):
            self.hospital.patients.sort(key=attrgetter('last_name'))
            self.display_patients()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HospitalApp()
    window.show()
    sys.exit(app.exec_())    
