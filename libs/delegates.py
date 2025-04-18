from PySide6.QtWidgets import QStyledItemDelegate, QComboBox


class ComboBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(["", "н", "о"])
        combo.activated.connect(lambda: self.commitAndCloseEditor(combo))

        return combo

    def setEditorData(self, editor, index):
        value = index.data()
        if value in ["", "н", "о"]:
            editor.setCurrentText(value)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def commitAndCloseEditor(self, editor):
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)
