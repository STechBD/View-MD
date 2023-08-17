import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune


def out(markdown):
    return mistune.html(markdown)


class HTMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HTML Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # Load and display HTML content
        self.md = "# List\n" \
                  "* Item 1\n" \
                  "* Item 2"
        self.output = out(self.md)
        self.load_html_content(self.output)

    def load_html_content(self, html_content):
        self.web_view.setHtml(html_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = HTMLViewer()
    viewer.show()
    sys.exit(app.exec())
