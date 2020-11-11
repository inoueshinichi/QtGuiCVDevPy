"""エントリーポイント
"""

import os
import sys


import PySide2
dir = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dir, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    # App
    app = QApplication(sys.argv)
    app_ver = QApplication.applicationVersion()
    print("Qt App ver:", app_ver)
    app_dir = QApplication.applicationDirPath()
    print("Qt App dir:", app_dir)
    app_file = QApplication.applicationFilePath()
    print("Qt App file path:", app_file)
    app_pid = QApplication.applicationPid()
    print("Qt App process id:", app_pid)
    app_name = QApplication.applicationName()
    print("Qt App name:", app_name)
    app_display_name = QApplication.applicationDisplayName()
    print("Qt App display name:", app_display_name)
    app_org_domain = QApplication.organizationDomain()
    print("Qt App org domain:", app_org_domain)
    app_org_name = QApplication.organizationName()
    print("Qt App org name:", app_org_name)
    app_platform_name = QApplication.platformName()
    print("Qt App platform name:", app_platform_name)
    app_desktop_file_name = QApplication.desktopFileName()
    print("Qt App desktop file name:", app_desktop_file_name)
    screens = QApplication.screens()
    print("Qt App associated screens:", screens)

    # MainWindow
    main_win = MainWindow()
    main_win.show()

    # Event Loop
    sys.exit(app.exec_())