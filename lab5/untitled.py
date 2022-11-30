from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QBrush
from PySide2.QtCore import Qt
import os
import csv
import difflib
import subprocess
from differ import DiffFile


def path_check(path):
    if not (os.path.exists(os.path.join(path, "equal.csv")) and os.path.exists(os.path.join(path, "inequal.csv"))):
        return False
    with open(os.path.join(path, "equal.csv")) as equal:
        with open(os.path.join(path, "inequal.csv")) as inequal:
            equal_dict = csv.DictReader(equal)
            inequal_dict = csv.DictReader(inequal)
            for row in equal_dict:
                if not os.path.exists(row["file1"]) or not os.path.exists(row["file2"]):
                    return False
            for row in inequal_dict:
                if not os.path.exists(row["file1"]) or not os.path.exists(row["file2"]):
                    return False
            equal.close()
            inequal.close()
    if os.path.exists(os.path.join(path, "suspect.csv")):
        with open(os.path.join(path, "suspect.csv")) as suspect:
            suspect_dict = csv.DictReader(suspect)
            for row in suspect_dict:
                if not os.path.exists(row["file1"]) or not os.path.exists(row["file2"]):
                    return False
    return True

class Window():
    def initialize(self):
        self.file_path = ""
        self.equal_list = []
        self.ui.inequalButton.setEnabled(False)
        self.ui.equalButton.setEnabled(False)
        self.ui.suspectButton.setEnabled(False)
        self.ui.openButton.setEnabled(False)
        self.ui.csvWidget.clear()

    def __init__(self):
        self.ui = QUiLoader().load('untitled.ui')
        self.cyanBrush = QBrush(Qt.cyan)
        self.yellowBrush = QBrush(Qt.yellow)
        self.greenBrush = QBrush(Qt.green)
        self.redBrush = QBrush(Qt.red)
        self.noBrush = QBrush()
        self.file_path = ""
        self.current_line = 0
        self.equal_list = []
        self.initialize()
        self.ui.openButton.clicked.connect(self.open)
        self.ui.importButton.clicked.connect(self.import_file)
        self.ui.equalButton.clicked.connect(self.set_equal)
        self.ui.inequalButton.clicked.connect(self.set_inequal)
        self.ui.endButton.clicked.connect(self.end_and_save)
        self.ui.suspectButton.clicked.connect(self.set_suspect)
        self.ui.csvWidget.itemClicked.connect(self.change_line)


    def open(self):
        subprocess.run(['python3', 'ht.py'])

    def set_code(self, line):
        DiffFile.compare_file(self.equal_list[line]["file1"], self.equal_list[line]["file2"], 'diff.html')

    def set_suspect(self):
        self.equal_list[self.current_line]["status"] = "suspect"
        self.set_color(self.current_line)

    def set_inequal(self):
        self.equal_list[self.current_line]["status"] = "inequal"
        self.set_color(self.current_line)

    def set_equal(self):
        self.equal_list[self.current_line]["status"] = "equal"
        self.set_color(self.current_line)

    def set_color(self, line):
        if self.equal_list[line]["status"] == "initial":
            if line == self.current_line:
                self.ui.csvWidget.item(line).setBackground(self.cyanBrush)
            else:
                self.ui.csvWidget.item(line).setBackground(self.noBrush)

        elif self.equal_list[line]["status"] == "equal":
            self.ui.csvWidget.item(line).setBackground(self.greenBrush)

        elif self.equal_list[line]["status"] == "inequal":
            self.ui.csvWidget.item(line).setBackground(self.redBrush)

        elif self.equal_list[line]["status"] == "suspect":
            self.ui.csvWidget.item(line).setBackground(self.yellowBrush)

    def change_line(self):
        self.current_line = self.ui.csvWidget.currentRow()
        self.set_color(self.current_line)
        self.set_code(self.current_line)
    def import_file(self):
        self.initialize()
        temp_path = QFileDialog.getExistingDirectory(None, "选取文件夹", os.getcwd())
        if path_check(temp_path):
            self.ui.importButton.setText("导入成功！")
            self.ui.inequalButton.setEnabled(True)
            self.ui.equalButton.setEnabled(True)
            self.ui.suspectButton.setEnabled(True)
            self.ui.openButton.setEnabled(True)
            self.file_path = temp_path
            equal_list = []
            with open(os.path.join(temp_path, "equal.csv")) as equal:
                equal_list = list(csv.DictReader(equal))
                equal.close()
                for i in range(len(equal_list)):
                    equal_list[i]["status"] = "initial"

            if os.path.exists(os.path.join(temp_path, "suspect.csv")):
                with open(os.path.join(temp_path, "suspect.csv")) as suspect:
                    suspect_list = list(csv.DictReader(suspect))
                    suspect.close()
                    for i in range(len(suspect_list)):
                        suspect_list[i]["status"] = "suspect"
            else:
                suspect_list = []

            self.equal_list = suspect_list + equal_list

            if len(self.equal_list) == 0:
                QMessageBox.about(self.ui,
                                  '导入错误', '当前equal.csv和suspect.csv为空'
                                  )
                self.initialize()
                return

            for i in range(len(self.equal_list)):
                self.ui.csvWidget.addItem(
                    f'File1: {self.equal_list[i]["file1"]}\nFile2: {self.equal_list[i]["file2"]}\n')
                self.set_color(i)

            self.set_color(self.current_line)
            self.set_code(self.current_line)
            self.ui.csvWidget.setCurrentRow(self.current_line)
        else:
            QMessageBox.about(self.ui,
                              '导入错误', '请检查选择文件夹是否包含equal.csv和inequal.csv\n检查其内容是否符合要求'
                              )
            self.initialize()

    def end_and_save(self):
        with open(os.path.join(self.file_path, "equal.csv"), "w") as equal:
            with open(os.path.join(self.file_path, "inequal.csv"), "a") as inequal:
                with open(os.path.join(self.file_path, "suspect.csv"), "w") as suspect:
                    equal_writer = csv.writer(equal)
                    inequal_writer = csv.writer(inequal)
                    suspect_writer = csv.writer(suspect)
                    equal_writer.writerow(["file1", "file2"])
                    suspect_writer.writerow(["file1", "file2"])
                    for item in self.equal_list:
                        if item["status"] == "inequal":
                            inequal_writer.writerow([item["file1"], item["file2"]])
                        elif item["status"] == "initial" or item["status"] == "equal":
                            equal_writer.writerow([item["file1"], item["file2"]])
                        elif item["status"] == "suspect":
                            suspect_writer.writerow([item["file1"], item["file2"]])
                equal.close()
                inequal.close()
                suspect.close()
        self.initialize()
        app = QApplication.instance()
        # 退出应用程序
        app.quit()