import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


class Musializer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Musializer")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e;")

        # Central label for drop zone
        self.drop_label = QLabel(
            "Drag & drop audio files here\nPress Q to quit",
            self,
            alignment=Qt.AlignCenter,
        )
        self.drop_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                border: 2px dashed #666;
                border-radius: 10px;
                padding: 20px;
            }
            QLabel:hover {
                border-color: #4CAF50;
                background-color: rgba(76, 175, 80, 0.1);
            }
        """)
        self.setCentralWidget(self.drop_label)

        # Enable drag & drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        for file_path in files:
            print(f"Dropped file: {file_path}")
        self.drop_label.setText(f"Dropped {len(files)} file(s)")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()


def main():
    app = QApplication(sys.argv)
    window = Musializer()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
