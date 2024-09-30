from abc import ABC, abstractmethod

# ۱. تعریف کلاس پایه برای دستگاه تهویه

class ClimateControlSystem(ABC):

    @abstractmethod
    def control(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
# ۲. کلاس‌های مختلف برای هر نوع دستگاه
class Cooler(ClimateControlSystem):
    def control(self):
        return "Cooling the house"
    def __str__(self):
        return "it is cooler"

class Heater(ClimateControlSystem):
    def control(self):
        return "Heating the house"
    def __str__(self):
        return "it is heater"
class Dehumidifier(ClimateControlSystem):
    def control(self):
        return "Dehumidifying the air"
    def __str__(self):
        return "it is dehumidifier"
# ۳. کلاس‌های کارخانه‌ای برای هر نوع دستگاه
class Factory:
    def cooler_device(self) -> ClimateControlSystem:
        return Cooler()

    def heater_device(self) -> ClimateControlSystem:
        return Heater()

    def Dehumidifier_device(self) -> ClimateControlSystem:
        return Dehumidifier()

# ۴. تابعی برای انتخاب کارخانه مناسب بر اساس شرایط
def get_climate_control_factory(temperature, humidity):
    if temperature > 24:
        return Factory().cooler_device()#,Factory().Dehumidifier_device() #my change
    elif temperature < 24:
        return Factory().heater_device()
    elif humidity > 50:
        return Factory().Dehumidifier_device()

if __name__ == "__main__":
    
    print(get_climate_control_factory(50,80))
    print(get_climate_control_factory(50,80).control())
    #print(get_climate_control_factory(50,80).create_device())
