from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from windows import StartWindow

import sys


class AppContext(ApplicationContext):
    def __init__(self, *args, **kwargs):
        super(AppContext, self).__init__(*args, **kwargs)

        # background-color: rgb(200,100,150)
        style = ''' 
                QMainWindow {
                    background-color: white;
                }
                '''
        self.app.setStyleSheet(style)

        self.start_window = StartWindow(self)

    def run(self):
        self.start_window.show()
        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
