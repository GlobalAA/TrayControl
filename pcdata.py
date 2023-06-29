from tkinter.messagebox import showwarning

import psutil
from psutil import _common


class Battery:
	percent: float
	power_plugged: bool

class PCData:

	@staticmethod
	def get_cpu():
		return int(psutil.cpu_percent())
	
	@staticmethod
	def get_ram():
		return int(psutil.virtual_memory().percent)

	@staticmethod
	def get_process():
		return len([x for x in psutil.process_iter()])

	@staticmethod
	def get_battery():
		battery: Battery = psutil.sensors_battery() or _common.sbattery(0, 0, True)
		return battery

	@staticmethod
	def has_battery():
		return True if psutil.sensors_battery() else False

	@staticmethod
	def battery_check():
		if not psutil.sensors_battery():
			showwarning('TrayControl message', 'Батарея не найдена!')