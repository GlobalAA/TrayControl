import re

from plyer import notification


class LoadManage:
	def __init__(self, cpu, virtual_memory, battery_percent) -> None:
		self.cpu = int(''.join(re.findall(r'\d+', cpu)))
		self.virtual_memory = int(''.join(re.findall(r'\d+', virtual_memory)))
		self.battery_percent = int(''.join(re.findall(r'\d+', battery_percent)))

	def manage(self):
		if self.cpu >= 90:
			notification.notify("TrayControl warning", "CPU load reaches 90%", timeout=3)
			
		
		if self.virtual_memory >= 90:
			notification.notify("TrayControl warning", "Virtual memory usage reached 90%", timeout=3)

		self.manage_battery()
			

	def manage_battery(self):
		if self.battery_percent <= 10:
			notification.notify("TrayControl warning", "Your battery percentage reaches 10%. You should immediately connect the device to power!", timeout=3)
			return

		elif self.battery_percent <= 20 and self.battery_percent > 10:
			notification.notify("TrayControl warning", "Your battery percentage reaches 20%. It is advisable to immediately connect the device to power!", timeout=3)
			return

		elif self.battery_percent <= 30 and self.battery_percent > 20:
			notification.notify("TrayControl warning", "Your battery percentage reaches 30%. It is advisable to immediately connect the device to power!", timeout=3)
			return
		
		elif self.battery_percent <= 40 and self.battery_percent > 30:
			notification.notify("TrayControl warning", "Your battery percentage reaches 40%", timeout=3)
			return
		
		elif self.battery_percent <= 50 and self.battery_percent > 40:
			notification.notify("TrayControl warning", "Your battery percentage reaches 40%", timeout=3)
			return

