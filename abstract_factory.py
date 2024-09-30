from abc import ABC, abstractmethod
import platform

class Window(ABC):
    @abstractmethod
    def draw(self):
        pass

class WindowsWindow(Window):
    def draw(self):
        print("windos drawing window")

class MacWindow(Window):
    def draw(self):
        print("mac drawing window")  # Render a window in Mac style

class LinuxWindow(Window):
    def draw(self):
        print("linux drawing window")  # Render a window in Linux style

class Button(ABC):
    @abstractmethod
    def draw(self):
        pass

class WindowsButton(Button):
    def draw(self):
        print("windos drawing button")  # Render a button in Windows style

class MacButton(Button):
    def draw(self):
        print("mac drawing button")  # Render a button in Mac style

class LinuxButton(Button):
    def draw(self):
        print("linux drawing button")  # Render a button in Linux style
    
class AbstractFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

class WindowsFactory(AbstractFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()

class MacOSFactory(AbstractFactory):
    def create_button(self):
        return MacButton()

    def create_window(self):
        return MacWindow()

class LinuxFactory(AbstractFactory):
    def create_button(self):
        return LinuxButton()

    def create_window(self):
        return LinuxWindow()

class ApplicationUI:
    def __init__(self, factory: AbstractFactory):
        self.__factory = factory

    def create_ui(self):
        window = self.__factory.create_window()
        button = self.__factory.create_button()
        window.draw()
        button.draw()

def main():    
    platform_name = platform.system()
    if platform_name == "Linux":
        factory = LinuxFactory()
    elif platform_name == "MacOS":
        factory = MacOSFactory()
    else:
        factory = WindowsFactory()

    application = ApplicationUI(factory)
    application.create_ui()
if __name__=="__main__":
    main()