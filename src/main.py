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
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QStyle
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune
import layout


def convert_to_html(markdown):
	return mistune.html(markdown)


class ViewMD(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('View MD - Markdown Viewer')
		self.setGeometry(300, 100, 800, 600)

		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)

		layout = QVBoxLayout(self.central_widget)

		self.web_view = QWebEngineView()
		layout.addWidget(self.web_view)

		self.open_button = QPushButton('Open .md File')
		self.open_button.setStyleSheet(
			'QPushButton { font-size: 14px; padding: 10px; }'
		)
		layout.addWidget(self.open_button)

		self.open_button.clicked.connect(self.open_file)

		# Menu bar
		menu_bar = self.menuBar()

		# Menu items
		file_menu = menu_bar.addMenu('File')
		help_menu = menu_bar.addMenu('Help')

		# File menu items
		open_file_action = file_menu.addAction('Open File')
		close_file_action = file_menu.addAction('Close File')
		file_menu.addSeparator()
		exit_app_action = file_menu.addAction('Exit')

		# Help menu items
		about_app_action = help_menu.addAction('About')
		other_product_action = help_menu.addAction('Other Products')
		check_update_action = help_menu.addAction('Check for Update')

		# Menu item actions
		open_file_action.triggered.connect(self.open_file)
		close_file_action.triggered.connect(self.close_file)
		exit_app_action.triggered.connect(self.exit_app)
		about_app_action.triggered.connect(self.about_app)
		other_product_action.triggered.connect(self.other_product)
		check_update_action.triggered.connect(self.check_update)

		# Status bar
		self.status_bar = self.statusBar()
		self.status_bar.showMessage('Ready')

		# Tool bar
		tool_bar = self.addToolBar('File')
		tool_bar.addAction(open_file_action)
		tool_bar.addAction(close_file_action)
		tool_bar.addAction(exit_app_action)

		tool_bar = self.addToolBar('Help')
		tool_bar.addAction(about_app_action)
		tool_bar.addAction(other_product_action)
		tool_bar.addAction(check_update_action)

		# Shortcuts
		open_file_action.setShortcut('Ctrl+O')
		close_file_action.setShortcut('Ctrl+W')
		exit_app_action.setShortcut('Ctrl+Q')
		about_app_action.setShortcut('Ctrl+I')
		other_product_action.setShortcut('Ctrl+P')
		check_update_action.setShortcut('Ctrl+U')

		# Status tip
		open_file_action.setStatusTip('Open .md file')
		close_file_action.setStatusTip('Close .md file')
		exit_app_action.setStatusTip('Exit application')
		about_app_action.setStatusTip('About application')
		other_product_action.setStatusTip('Other products')

		# Tool tip
		open_file_action.setToolTip('Open .md file')
		close_file_action.setToolTip('Close .md file')
		exit_app_action.setToolTip('Exit application')
		about_app_action.setToolTip('About application')
		other_product_action.setToolTip('Other products')

		# Icon
		# open_file_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.Open))
		# close_file_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.Close))
		# exit_app_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.Exit))
		# about_app_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.About))
		# other_product_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.Grid))
		# check_update_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.Refresh))

		# Window icon
		# self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.Windows))

	def open_file(self):
		file_name, _ = QFileDialog.getOpenFileName(self, 'Open .md File', '', 'Markdown Files (*.md)')

		if file_name:
			with open(file_name, "r", encoding="utf-8") as f:
				md_content = f.read()
				file_name = file_name.split("/")[-1]
				self.setWindowTitle(file_name + " | View MD - Markdown Viewer")
				self.display_html(file_name, md_content)

	def display_html(self, file_name, markdown):
		html_content = convert_to_html(markdown)
		html_content = html_content.replace('<img src="', '<img width="100%" src="')
		html = layout.layout(file_name, html_content)

		self.web_view.setHtml(html)

	def close_file(self):
		self.setWindowTitle('View MD - Markdown Viewer')
		self.web_view.setHtml('')

	def exit_app(self):
		self.close()

	def check_update(self):
		self.status_bar.showMessage('Check for update')

	def other_product(self):
		self.status_bar.showMessage('Other products')

	def about_app(self):
		self.status_bar.showMessage('About app')


if __name__ == "__main__":
	app = QApplication(sys.argv)
	viewer = ViewMD()
	viewer.show()
	sys.exit(app.exec())
