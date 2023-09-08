"""
# Project: View MD
# Description: View MD is a simple tool to view markdown files in windows.
# Version: 1.0.0
# Version Code: 1
# Since: 1.0.0
# Author: Md. Ashraful Alam Shemul
# Email: ceo@stechbd.net
# Website: https://www.stechbd.net/project/View-MD/
# Developer: S Technologies
# Homepage: https://www.stechbd.net
# Contact: product@stechbd.net
# Created: August 17, 2023
# Updated: September 8, 2023
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune
import layout


def convert_to_html(markdown):
	return mistune.html(markdown)


def sidebar():
	return ''


class HTMLViewer(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("View MD - Markdown Viewer")
		self.setGeometry(300, 100, 800, 600)

		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)

		layout = QVBoxLayout(self.central_widget)

		self.web_view = QWebEngineView()
		layout.addWidget(self.web_view)

		self.open_button = QPushButton("Open .md File")
		layout.addWidget(self.open_button)

		self.open_button.clicked.connect(self.open_md_file)

	def open_md_file(self):
		file_name, _ = QFileDialog.getOpenFileName(self, "Open .md File", "", "Markdown Files (*.md)")

		if file_name:
			with open(file_name, "r", encoding="utf-8") as f:
				md_content = f.read()
				file_name = file_name.split("/")[-1]
				self.setWindowTitle(file_name + " | View MD - Markdown Viewer")
				self.display_html(file_name, md_content)

	def display_html(self, file_name, markdown):
		html_content = convert_to_html(markdown)

		html = '<h1>' + file_name + '</h1><div><textarea>' + html_content + '</textarea></div>'

		self.web_view.setHtml(html_content + html)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	viewer = HTMLViewer()
	viewer.show()
	sys.exit(app.exec())
