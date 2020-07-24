# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecipeWidgetClaire.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recipe(object):
    def setupUi(self, Recipe):
        Recipe.setObjectName("Recipe")
        Recipe.resize(538, 341)
        self.verticalLayout = QtWidgets.QVBoxLayout(Recipe)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(Recipe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(Recipe)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Recipe)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Recipe)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Recipe)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(Recipe)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listView = QtWidgets.QListView(Recipe)
        self.listView.setObjectName("listView")
        self.horizontalLayout_3.addWidget(self.listView)
        self.textBrowser = QtWidgets.QTextBrowser(Recipe)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(Recipe)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(Recipe)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(Recipe)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(Recipe)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(Recipe)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(Recipe)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Recipe)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Recipe)
        QtCore.QMetaObject.connectSlotsByName(Recipe)

    def retranslateUi(self, Recipe):
        _translate = QtCore.QCoreApplication.translate
        Recipe.setWindowTitle(_translate("Recipe", "Form"))
        self.label.setText(_translate("Recipe", "Recipe Title"))
        self.label_3.setText(_translate("Recipe", "Servings"))
        self.label_6.setText(_translate("Recipe", "Prep Time"))
        self.label_5.setText(_translate("Recipe", "Cook Time"))
        self.label_2.setText(_translate("Recipe", "Ingredients"))
        self.label_7.setText(_translate("Recipe", "Directions"))
        self.checkBox.setText(_translate("Recipe", "Gluten Free"))
        self.checkBox_2.setText(_translate("Recipe", "Dairy Free"))
        self.checkBox_3.setText(_translate("Recipe", "Vegan"))
        self.checkBox_4.setText(_translate("Recipe", "Vegetarian"))
        self.checkBox_5.setText(_translate("Recipe", "Non-Alcoholic"))
        self.checkBox_6.setText(_translate("Recipe", "Kosher"))
        self.pushButton.setText(_translate("Recipe", "OK"))