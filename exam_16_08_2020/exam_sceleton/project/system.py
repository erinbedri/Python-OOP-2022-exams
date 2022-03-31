from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(new_express_software)
                System._software.append(new_express_software)
                return

        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(new_light_software)
                System._software.append(new_light_software)
                return

        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]

        if hardware and software:
            hardware[0].uninstall(software[0])
            System._software.remove(software[0])
            return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"

        total_operational_memory = f"{sum([software.memory_consumption for software in System._software])} / " \
                                   f"{sum([hardware.memory for hardware in System._hardware])}"

        result += f"Total Operational Memory: {total_operational_memory}\n"

        total_capacity_taken = f"{sum([software.capacity_consumption for software in System._software])} / " \
                               f"{sum([hardware.capacity for hardware in System._hardware])}"

        result += f"Total Capacity Taken: {total_capacity_taken}"

        return result

    @staticmethod
    def system_split():
        result = ""

        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: " \
                      f"{len([software for software in hardware.software_components if software.software_type == 'Express'])}\n"
            result += f"Light Software Components: " \
                      f"{len([software for software in hardware.software_components if software.software_type == 'Light'])}\n"
            result += f"Memory Usage: " \
                      f"{sum([software.memory_consumption for software in hardware.software_components])} / {hardware.memory}\n"
            result += f"Capacity Usage: " \
                      f"{sum([software.capacity_consumption for software in hardware.software_components])} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"

            software_components = [software.name for software in hardware.software_components]
            if software_components:
                result += f"Software Components: {', '.join(software_components)}\n"
            else:
                result += "Software Components: None\n"

        return result

