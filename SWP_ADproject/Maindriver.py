##Adventure Design Assignment
##Software Project2
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Codechecker import Codechecker
import time

class MainDriver(QWidget):

    def __init__ (self):
        super().__init__()
        self.string = [] #고친 파일 내용을 담을 리스트 초기화
        self.initUI()
        self.check = Codechecker()

    def initUI(self):

        # 1 line UI
        self.fileLineEdit = QTextEdit()
        self.fileLineEdit.setReadOnly(True)
        self.fileLineEdit.setFixedSize(500, 700)
        self.resultLineEdit = QTextEdit()
        self.resultLineEdit.setReadOnly(True)
        self.resultLineEdit.setFixedSize(500, 700)
        hbox = QHBoxLayout()
        hbox.addWidget(self.fileLineEdit)
        hbox.addWidget(self.resultLineEdit)

        # 2 line UI
        self.openbutton = QPushButton("File Open")
        self.clickbutton = QPushButton("CLICK")
        self.clickbutton.setEnabled(False)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.openbutton)
        hbox1.addWidget(self.clickbutton)

        # 3 line UI
        self.taglabel = QLabel("코드 규칙 출처 - \t  국민대 소프트웨어 프로젝트 2")
        self.statuslabel = QLabel("Status Message:")
        self.saveButton = QPushButton("SAVE")

        self.saveButton.setEnabled(False)
        self.statusLineEdit = QLineEdit()
        self.statusLineEdit.setReadOnly(True)
        self.statusLineEdit.setAlignment(Qt.AlignCenter)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.taglabel)
        hbox2.addStretch()
        hbox2.addWidget(self.statuslabel)
        hbox2.addWidget(self.statusLineEdit)
        hbox2.addWidget(self.saveButton)
        # 세로 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

        # 이벤트 핸들러
        self.openbutton.clicked.connect(self.openbuttonClicked)
        self.clickbutton.clicked.connect(self.clickbuttonClicked)
        self.saveButton.clicked.connect(self.saveButtonClicked)

    def openbuttonClicked(self):
        self.resultLineEdit.clear() #파일 다시 불러오면 결과창 초기
        self.saveButton.setEnabled(False)
        self.string = []
        faddress = QFileDialog.getOpenFileName(self)
        self.fname = faddress[0].split('/')[-1]
        try:
            f = open(self.fname, 'r')
        except:
            self.taglabel.setText("Error = FileNotFoundError")
            self.statusLineEdit.setText("해당 파일이 같은 디렉토리에 있는지 확인해주세요.")
        else:
            data = f.read()
            self.taglabel.setText("코드 규칙 출처 - \t  국민대 소프트웨어 프로젝트 2")
            self.fileLineEdit.setText(data)
            self.statusLineEdit.setText('open = ' + faddress[0])
            self.clickbutton.setEnabled(True)

    def clickbuttonClicked(self):
        f = open(self.fname, 'r')
        for line in f:
            for character in line:
                if ';' in line:
                    line = self.check.semiclone(line)
                elif character in self.check.operator_Character:
                    line = self.check.operator_check(line)
                elif character in self.check.special_Character:
                    line = self.check.special_check(line)
                elif character in self.check.bracket_Character:
                    line = self.check.bracket_check(line)

            if line.strip().find(self.check.import_Character[0]) == 0 or line.strip().find(
                    self.check.import_Character[1]) == 0:
                line = self.check.import_check(line)
            elif line.strip().find(self.check.class_Character) == 0:
                line = self.check.class_check(line)
            elif line.strip().find(self.check.def_Character) == 0:
                line = self.check.def_check(line)
            elif line.strip().find(self.check.return_Character) == 0:
                line = line.replace('return(', 'return (')
                line = self.check.return_check(line)
            self.string.append(line)

        for i in range(len(self.string)):
            if '\n' not in self.string[i]:
                self.string[i] += '\n'
        f.close()
        self.saveButton.setEnabled(True)
        self.clickbutton.setEnabled(False)
        self.resultLineEdit.setText(''.join(self.string)) #string리스트를 문자열로 변환 후 표시
        self.statusLineEdit.setText("저장하려면 SAVE를 누르세요.")

    def saveButtonClicked(self):
        self.saveButton.setEnabled(False)
        self.statusLineEdit.setText("저장되었습니다.")
        string = self.resultLineEdit.toPlainText() #resultLineEdit의 텍스트를 저장
        self.writefile(string)
        self.showfile()

    def writefile(self, string):
        f = open(self.fname, 'w')
        for i in string:
            f.write(i)
        f.close()

    def showfile(self):
        f = open(self.fname, 'r')
        output = f.read()
        self.resultLineEdit.setText(output)
        f.close()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    game = MainDriver()
    game.setWindowTitle('Python Code Checker')
    game.show()
    sys.exit(app.exec_())