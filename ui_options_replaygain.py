# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_replaygain.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ReplayGainOptionsPage(object):
    def setupUi(self, ReplayGainOptionsPage):
        ReplayGainOptionsPage.setObjectName(_fromUtf8("ReplayGainOptionsPage"))
        ReplayGainOptionsPage.resize(305, 317)
        self.vboxlayout = QtGui.QVBoxLayout(ReplayGainOptionsPage)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.replay_gain = QtGui.QGroupBox(ReplayGainOptionsPage)
        self.replay_gain.setObjectName(_fromUtf8("replay_gain"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.replay_gain)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label = QtGui.QLabel(self.replay_gain)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout1.addWidget(self.label)
        self.vorbisgain_command = QtGui.QLineEdit(self.replay_gain)
        self.vorbisgain_command.setObjectName(_fromUtf8("vorbisgain_command"))
        self.vboxlayout1.addWidget(self.vorbisgain_command)
        self.label_2 = QtGui.QLabel(self.replay_gain)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout1.addWidget(self.label_2)
        self.mp3gain_command = QtGui.QLineEdit(self.replay_gain)
        self.mp3gain_command.setObjectName(_fromUtf8("mp3gain_command"))
        self.vboxlayout1.addWidget(self.mp3gain_command)
        self.label_3 = QtGui.QLabel(self.replay_gain)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vboxlayout1.addWidget(self.label_3)
        self.metaflac_command = QtGui.QLineEdit(self.replay_gain)
        self.metaflac_command.setObjectName(_fromUtf8("metaflac_command"))
        self.vboxlayout1.addWidget(self.metaflac_command)
        self.label_4 = QtGui.QLabel(self.replay_gain)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.vboxlayout1.addWidget(self.label_4)
        self.wvgain_command = QtGui.QLineEdit(self.replay_gain)
        self.wvgain_command.setObjectName(_fromUtf8("wvgain_command"))
        self.vboxlayout1.addWidget(self.wvgain_command)
        self.label_5 = QtGui.QLabel(self.replay_gain)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.vboxlayout1.addWidget(self.label_5)
        self.aacgain_command = QtGui.QLineEdit(self.replay_gain)
        self.aacgain_command.setObjectName(_fromUtf8("aacgain_command"))
        self.vboxlayout1.addWidget(self.aacgain_command)
        self.vboxlayout.addWidget(self.replay_gain)
        spacerItem = QtGui.QSpacerItem(263, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(ReplayGainOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(ReplayGainOptionsPage)

    def retranslateUi(self, ReplayGainOptionsPage):
        self.replay_gain.setTitle(_translate("ReplayGainOptionsPage", "Replay Gain", None))
        self.label.setText(_translate("ReplayGainOptionsPage", "Path to VorbisGain:", None))
        self.label_2.setText(_translate("ReplayGainOptionsPage", "Path to MP3Gain:", None))
        self.label_3.setText(_translate("ReplayGainOptionsPage", "Path to metaflac:", None))
        self.label_4.setText(_translate("ReplayGainOptionsPage", "Path to wvgain:", None))
        self.label_5.setText(_translate("ReplayGainOptionsPage", "Path to aacgain:", None))

