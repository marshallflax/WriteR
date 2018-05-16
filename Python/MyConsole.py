from wx.aui import AuiManager, AuiPaneInfo

class MyConsole:
    def __init__(self, parent):
        self.console = parent.CreateTextCtrl("")
        self.console.SetEditable(False)
        parent._mgr.AddPane(self.console, AuiPaneInfo().Name("console")
                          .Caption("Console").Bottom().Layer(1).Position(1).CloseButton(True)
                          .MinimizeButton(True).Hide())
        parent._mgr.GetPane("console").Hide().Bottom().Layer(0).Row(0).Position(0)

    def Reset(self):
        self.console.setValue('')

    def write(self, text):
        self.console.write(text)

    def CreateWriteText(self, text):
        self.console.write(text)
