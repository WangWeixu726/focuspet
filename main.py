"""FocusPet application entry point."""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class PetWindow(QWidget):
    """A transparent, frameless window that stays above other windows."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("FocusPet")
        self.setFixedSize(220, 220)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        pet_label = QLabel("🐣")
        pet_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pet_label.setStyleSheet("font-size: 96px; background: transparent;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(pet_label)


def main() -> None:
    """Create the application and show the desktop pet."""
    app = QApplication(sys.argv)
    pet_window = PetWindow()
    pet_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
