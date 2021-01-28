"""
main.py -- Launching point for automated distribution package (FBS).
Copyright (C) 2021  Paul Sirri <paulsirri@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from fbs_runtime.application_context.PyQt5 import ApplicationContext
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
