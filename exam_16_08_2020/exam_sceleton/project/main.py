from system import System

s = System()

s.register_power_hardware("HDD", 200, 200)
s.register_heavy_hardware("SSD", 400, 400)
print(s.analyze())
s.register_light_software("HDD", "Test", 0, 10)
s.register_express_software("HDD", "Test3", 50, 100)
s.register_light_software("SSD", "Windows", 20, 50)
s.register_express_software("SSD", "Linux", 50, 100)
s.register_light_software("SSD", "Unix", 20, 50)
print(s.analyze())
s.release_software_component("SSD", "Linux")
print(s.system_split())
