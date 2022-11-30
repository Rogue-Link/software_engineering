from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

if __name__ == '__main__':
    import sys
    url = "file://" + sys.path[0] + "/diff.html"
    app = QtWidgets.QApplication(sys.argv)
    view = QtWebEngineWidgets.QWebEngineView()
    view.load(QtCore.QUrl(url))
    view.show()
    sys.exit(app.exec_())