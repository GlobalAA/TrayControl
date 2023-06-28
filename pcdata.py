import psutil


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
		battery: Battery = psutil.sensors_battery()
		return battery