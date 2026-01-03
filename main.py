import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent))


from app.core import GradeSystem
from app.ui import ConsoleUI


def main():
    try:
        system = GradeSystem()
        
        ui = ConsoleUI(system)
        
        ui.start_loop()
        
    except KeyboardInterrupt:
        print("\n\n👋 Program Interrupted. Exiting...")
    except Exception as e:
        print(f"\n❌ Critical Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()