import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QMenu, QSystemTrayIcon

from load_check import LoadManage
from pcdata import PCData

value = 0
cpu_data: QAction | None = None
virtual_memory_data: QAction | None = None
process: QAction | None = None
battery_percent: QAction | None = None
power_plugged: QAction | None = None

def update():
	global cpu_data, virtual_memory_data, process, battery_percent, power_plugged

	if not cpu_data or not virtual_memory_data or not process or not battery_percent or not power_plugged:
		return

	cpu_data.setText(f"CPU: {PCData.get_cpu()}%")
	virtual_memory_data.setText(f"Virtual Memory: {PCData.get_ram()}%")
	process.setText(f"Process: {PCData.get_process()}")
	battery_percent.setText(f"Battery percent: {int(PCData.get_battery().percent)}%")
	power_plugged.setText(f"Power plugged: {PCData.get_battery().power_plugged}")

def load_manage():
	load_manager = LoadManage(cpu_data.text(), virtual_memory_data.text(), battery_percent.text())
	load_manager.manage()

		
def run_application():
	global cpu_data, virtual_memory_data, process, battery_percent, power_plugged
	app = QApplication(sys.argv)
	tray_icon = QSystemTrayIcon(QIcon("assets/main3.png"), parent=app)
	tray_menu = QMenu()

	cpu_data = QAction(f"CPU: {PCData.get_cpu()}%")
	virtual_memory_data = QAction(f"Virtual Memory: {PCData.get_ram()}%")
	process = QAction(f"Process: {PCData.get_process()}")
	battery_percent = QAction(f"Battery percent: {int(PCData.get_battery().percent)}%")
	power_plugged = QAction(f"Power plugged: {PCData.get_battery().power_plugged}")

	exit = QAction("Exit", triggered=lambda: app.quit())

	tray_menu.addAction(cpu_data)
	tray_menu.addAction(virtual_memory_data)
	tray_menu.addAction(process)
	tray_menu.addAction(battery_percent)
	tray_menu.addAction(power_plugged)
	tray_menu.addAction(exit)

	tray_icon.setContextMenu(tray_menu)
	tray_icon.setToolTip("TrayControl")
	tray_icon.show()

	updateTimer = QTimer()
	updateTimer.timeout.connect(update)
	updateTimer.start(500)

	loadTimer = QTimer()
	loadTimer.timeout.connect(load_manage)
	loadTimer.start(5500)

	app.exec_()


def main():
	run_application()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass