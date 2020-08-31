# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class GeoRaster(QMainWindow):
    def __init__(self):
        super(GeoRaster, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
#    widget = GeoRaster()
#    widget.show()
#    label = QLabel("Map2Mesh")
#    label.show()
    sys.exit(app.exec_())
