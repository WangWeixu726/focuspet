# FocusPet application entry point.
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])

window = QLabel("FocusPet 正在孵化……")
window.resize(320, 180)
window.setWindowTitle("FocusPet")
window.show()

app.exec()