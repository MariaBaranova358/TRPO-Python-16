import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from patient import Hospital

class HospitalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hospital_form.ui", self) 
        
        self.hospital = Hospital()
        self.pushButton.clicked.connect(self.load_and_display_data)
        
        # Очищаем таблицу при запуске
        self.tableWidget.setRowCount(0)
    
    def load_and_display_data(self):
        self.hospital.load_from_file("patients.txt")

        for row, patient in enumerate(self.hospital.patients):
                self.tableWidget.insertRow(row)
                # Объединенное ФИО в первой колонке
                full_name = f"{patient.last_name} {patient.first_name} {patient.middle_name}"
                self.tableWidget.setItem(row, 0, QTableWidgetItem(full_name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(patient.birth_year)))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(patient.address))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(patient.diagnosis))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(patient.days)))
            
            # Автоматическое выравнивание столбцов
        self.tableWidget.resizeColumnsToContents()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HospitalApp()
    window.show()
    sys.exit(app.exec_())
