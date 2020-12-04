import subproess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel('Electric GUI'))
layout.addWidget(QLineEdit()
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()

  #uninstall electric package
        pkg = app.getEntry("Package Name  ")
        proc = subprocess.Popen(f'electric uninstall {pkg}')
        output, err = proc.communicate()
    
#Install electric package
pkg = app.getEntry("Package Name  ")
      proc = subprocess.Popen(f'electric install {pkg}')
      output, err = proc.communicate()
