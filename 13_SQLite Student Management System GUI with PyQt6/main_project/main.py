from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QDialog, QComboBox, QLineEdit, QPushButton, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
from db_module import UniversalDatabase


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(410, 400)

        file_menu_item = self.menuBar().addMenu('&File')
        edit_menu_item = self.menuBar().addMenu('&Edit')
        help_menu_item = self.menuBar().addMenu('&Help')

        add_student_action = QAction(QIcon('icons/add.png'), 'Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        search_student_action = QAction(QIcon('icons/search.png'), 'Search Student', self)
        search_student_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        # layout.addWidget(self.table)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_student_action)

        # Create status bar and elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

        self.load_data()

    def cell_clicked(self):

        if not self.findChildren(QPushButton):
            edit_button = QPushButton('Edit Record')
            edit_button.clicked.connect(self.edit)

            delete_button = QPushButton('Delete Record')
            delete_button.clicked.connect(self.delete)

            self.statusbar.addWidget(edit_button)
            self.statusbar.addWidget(delete_button)

    def get_current_row(self, field_name):
        current_row = self.table.currentRow()
        if current_row >= 0:
            column_index = self.get_column_index(field_name)
            if column_index >= 0:
                item = self.table.item(current_row, column_index)
                if item:
                    return item.text()
        return None

    def get_column_index(self, field_name):
        header_labels = [self.table.horizontalHeaderItem(i).text() for i in range(self.table.columnCount())]
        if field_name in header_labels:
            return header_labels.index(field_name)
        return -1

    def load_data(self):
        # Connect to the SQLite database
        db = UniversalDatabase()
        db.connect()
        data = db.fetch_data("SELECT * FROM students")

        # Set the number of rows and columns in the table widget
        self.table.setRowCount(len(data))
        # self.table.setColumnCount(len(data[0]))

        # Populate the table widget with data
        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)

        # Close the database connection
        db.close_connection()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class AboutDialog(QMessageBox):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('About')
        content = """
        This App was written by me
        to learn PyQt6 library.
        """
        self.setText(content)
        self.setIcon(QMessageBox.Icon.Information)


class EditDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Update')
        self.setFixedSize(200, 200)
        layout = QVBoxLayout()

        # Add student name
        student_name = main_window.get_current_row('Name')
        self.student_name = QLineEdit(student_name)
        # self.student_name.setPlaceholderText('Student Name')
        layout.addWidget(self.student_name)

        # Add combo box of courses
        course = main_window.get_current_row('Course')
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course)
        layout.addWidget(self.course_name)

        # Add mobile widget
        mobile = main_window.get_current_row('Mobile')
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile)

        # Add a submit button
        button = QPushButton('Update')
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        db = UniversalDatabase()
        db.connect()
        query = 'UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s'
        values = (self.student_name.text(), self.course_name.itemText(self.course_name.currentIndex()),
                  self.mobile.text(), main_window.get_current_row('Id'))
        db.execute_query(query, values)
        db.close_connection()

        self.close()
        main_window.load_data()


class DeleteDialog(QMessageBox):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Delete Confirmation")
        self.setText("Are you sure you want to delete the selected record?")
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.setDefaultButton(QMessageBox.StandardButton.No)

        # Connect the button clicked signal to the slot
        self.buttonClicked.connect(self.handle_button_clicked)

    def handle_button_clicked(self, button):
        if button == self.button(QMessageBox.StandardButton.Yes):
            self.delete_record()

    def delete_record(self):
        db = UniversalDatabase()
        db.connect()
        query = 'DELETE FROM students WHERE id=%s'
        values = (main_window.get_current_row('Id'),)
        db.execute_query(query, values)
        db.close_connection()

        main_window.load_data()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Add')
        layout = QVBoxLayout()

        # Add student name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Student Name')
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile)

        # Add a submit button
        button = QPushButton('Register')
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):

        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()

        db = UniversalDatabase()
        db.connect()
        query = 'INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)'
        values = (name, course, mobile)
        db.execute_query(query, values)
        db.close_connection()

        self.close()
        main_window.load_data()


class SearchDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Search')
        self.setFixedSize(200, 100)
        layout = QVBoxLayout()

        # Add student name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Student Name')
        layout.addWidget(self.student_name)

        # Add a submit button
        button = QPushButton('Search')
        button.clicked.connect(self.search_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_student(self):
        name = self.student_name.text()
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            main_window.table.item(item.row(), 1).setSelected(True)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
