"""FocusPet application entry point."""

import sys

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class PetWindow(QWidget):
    """A transparent, frameless window that stays above other windows."""

    def __init__(self) -> None:
        super().__init__()

        self.drag_offset: QPoint | None = None

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
        pet_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(pet_label)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Remember where the pet was grabbed with the left mouse button."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_offset = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )
            event.accept()
            return

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Move the pet while the left mouse button remains pressed."""
        if (
            self.drag_offset is not None
            and event.buttons() & Qt.MouseButton.LeftButton
        ):
            self.move(event.globalPosition().toPoint() - self.drag_offset)
            event.accept()
            return

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """Finish dragging when the left mouse button is released."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_offset = None
            event.accept()
            return

        super().mouseReleaseEvent(event)


def main() -> None:
    """Create the application and show the desktop pet."""
    app = QApplication(sys.argv)
    pet_window = PetWindow()
    pet_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
