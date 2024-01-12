# -- coding: utf-8 --

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import tkinter as tk
from tkinter import filedialog
from PyQt5 import QtWidgets, QtGui, QtCore
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.ApiButton = QtWidgets.QPushButton(self.centralwidget)
        self.ApiButton.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.ApiButton.setObjectName("ApiButton")
        self.ApiButton.clicked.connect(self.get_api_key)

        self.PDFButton = QtWidgets.QPushButton(self.centralwidget)
        self.PDFButton.setGeometry(QtCore.QRect(350, 210, 75, 23))
        self.PDFButton.setObjectName("PDFButton")
        self.PDFButton.clicked.connect(self.get_pdf_path)

        self.EnterAPI = QtWidgets.QTextBrowser(self.centralwidget)
        self.EnterAPI.setGeometry(QtCore.QRect(0, 90, 161, 31))
        self.EnterAPI.setObjectName("EnterAPI")
        self.EnterAPI_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.EnterAPI_2.setGeometry(QtCore.QRect(0, 210, 161, 31))
        self.EnterAPI_2.setObjectName("EnterAPI_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(63, 310, 351, 51))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 460, 371, 81))
        self.textBrowser.setObjectName("textBrowser")
        
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(200, 390, 75, 23))
        self.queryButton.setObjectName("queryButton")
        self.queryButton.clicked.connect(self.perform_query)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 341, 51))
        self.label.setObjectName("label")
        self.EnterAPI_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.EnterAPI_3.setGeometry(QtCore.QRect(160, 270, 161, 31))
        self.EnterAPI_3.setObjectName("EnterAPI_3")
        self.EnterAPI_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.EnterAPI_4.setGeometry(QtCore.QRect(160, 420, 161, 31))
        self.EnterAPI_4.setObjectName("EnterAPI_4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
     _translate = QtCore.QCoreApplication.translate
     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
     self.ApiButton.setText(_translate("MainWindow", "Browse"))
     self.PDFButton.setText(_translate("MainWindow", "Browse"))
     self.queryButton.setText(_translate("MainWindow", "Query"))
     self.EnterAPI.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Enter path to API</span></p></body></html>"))
     self.EnterAPI_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Enter path to PDF</span></p></body></html>"))
     self.queryButton.setText(_translate("MainWindow", "PushButton"))
     self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">AIOBC Pdf Converter</span></p></body></html>"))
     self.EnterAPI_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Querry</span></p></body></html>"))
     self.EnterAPI_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Results</span></p></body></html>"))


    def get_api_key(self):
        try:
            api_file_path = self.get_file_path("Select API Key Text File", [("Text files", "*.txt")])
            with open(api_file_path, 'r') as api_file:
                openai_api_key = api_file.readline().strip()
            os.environ["OPENAI_API_KEY"] = openai_api_key
        except FileNotFoundError:
            self.show_alert("API Key file not found.")
        except Exception as e:
            self.show_alert(f"Error reading API Key: {str(e)}")

        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'langchain', 'chains', 'llm_summarization_checker', 'prompts')
        file_path = os.path.join(base_path, 'create_facts.txt')
       

    def get_pdf_path(self):
        try:
            self.pdf_path = self.get_file_path("Select PDF File", [("PDF files", "*.pdf")])
            if not self.pdf_path:
                raise ValueError("No PDF file selected.")
        except FileNotFoundError:
            self.show_alert("PDF file not found.")
        except ValueError as ve:
            self.show_alert(str(ve))
        except Exception as e:
            self.show_alert(f"Error reading PDF file: {str(e)}")

    def show_alert(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
   

    def perform_query(self):
        query = self.textEdit.toPlainText()


        pdfreader = PdfReader(self.pdf_path)
        raw_text = ''
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                raw_text += content

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)

        embeddings = OpenAIEmbeddings()
        document_search = FAISS.from_texts(texts, embeddings)

        chain = load_qa_chain(OpenAI(), chain_type="stuff")

        docs = document_search.similarity_search(query)
        result = chain.run(input_documents=docs, question=query)

        self.textBrowser.setText(result)

    def get_file_path(self, title, filetypes):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
        return file_path
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())