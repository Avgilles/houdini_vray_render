import hou
import os
# from hutil.Qt import QtWidgets
from PySide2 import QtUiTools , QtWidgets


print("loading project")

"""
def scriptPath():
    print(hou.getenv('JOB'))
    Pose = hou.getenv("POSE")
    a = Pose.split('/')
    a.remove(a[len(a)-1])
    newScriptPath = "/".join(a) + str("/")

    return (newScriptPath)

"""
scriptPath = 'C:/Users/Gilles AVRAAM/Documents/houdini19.0/scripts'

class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()
        if(hou.getenv('JOB') == None):
            self.proj = hou.getenv('HIP') + '/'
        else:
            self.proj = hou.getenv('JOB') + '/'

        # Load UI file
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(f'{scriptPath}/python/projectManager/projetManager.ui')

        # get UI elements
        self.setproj = self.ui.findChild(QtWidgets.QPushButton, "setproj_btn")
        self.proj_path = self.ui.findChild(QtWidgets.QLabel, "proj_path")
        self.proj_name = self.ui.findChild(QtWidgets.QLabel, "proj_name")
        self.scene_list = self.ui.findChild(QtWidgets.QListWidget, "scene_list")
        self.rename_btn = self.ui.findChild(QtWidgets.QPushButton, "rename_btn")

        # create connection
        self.setproj.clicked.connect(self.setproject)

        # layout
        mainLayout = QtWidgets.QVBoxLayout()

        mainLayout.addWidget(self.ui)

        # # add widget to layout
        # self.btn = QtWidgets.QPushButton('Click me')
        # mainLayout.addWidget(self.labelTitle)
        # mainLayout.addWidget(self.label)
        # mainLayout.addWidget(self.listwidget)
        # mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)

    def setproject(self):
        setjob = hou.ui.selectFile(title="Set Project", file_type=hou.fileType.Directory)
        print(setjob)

        hou.hscript("setenv JOB=" + setjob)
        self.proj = hou.getenv('JOB')

        proj_name = setjob.split('/')[-2]
        setjob = os.path.dirname(setjob)
        proj_path = os.path.split(setjob[0])

        # print(setjob)
        # print(proj_name)
        # print(proj_path)
        self.proj_name.setText(proj_name)
        self.proj_path.setText(str(setjob))

        self.onCreateInterface()

    def lanchPopup(self, item):
        pop = Popup(item, self)
        pop.show()

    def changeName(self, file):
        print(file)
        return ("newfile"+file)

    def openScene(self, item):
        print('open ' + item.data())
        hipFile = self.proj + item.data()
        print(hipFile)
        hou.hipFile.load(hipFile)

    def onCreateInterface(self):
        print("creating interface")
        self.scene_list.clear()

        for file in os.listdir(self.proj):
            if file.endswith('.hip'):
                self.scene_list.addItem(file)
                print(file)

        self.scene_list.doubleClicked.connect(self.openScene)
        print(self.scene_list)
        self.rename_btn.clicked.connect(self.lanchPopup(self.scene_list))

class Popup(QtWidgets.QDialog):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(600,300)
        self.label = QtWidgets.QLabel(name, self)