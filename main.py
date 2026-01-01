from core import GradeSystem
from ui import ConsoleUI

def main():
    core_system = GradeSystem()
    
    app_ui = ConsoleUI(core_system)
    
    app_ui.start_loop()

if __name__ == "__main__":
    main()