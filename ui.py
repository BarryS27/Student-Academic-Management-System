import numpy as np

class ConsoleUI:
    def __init__(self, manager):
        self.manager = manager
        self.numeric_cols = ['Weight', 'Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points']

    def _get_input(self, prompt, is_float=False):
        val = input(prompt).strip()
        if val == '':
            return np.nan
        if is_float:
            try:
                return float(val)
            except ValueError:
                print(f"Invalid number for {prompt.strip()}, storing as NaN.")
                return np.nan
        return val

    def page_add(self):
        print("\n---------- [ Add_Course_Info ] ----------")
        grade = input('Please enter the grade you want to add info to: ').strip()
        
        if self.manager.get_data(grade) is None:
            print("Invalid grade. Please enter one of:", ['G9', 'G10', 'G11', 'G12'])
            return

        print(f"Adding info to {grade}...")
        
        row_data = {
            'Sem': input('Pls enter its semester: '),
            'Level': input('Pls enter its level: '),
            'Code': input('Pls enter its code: '),
            'Course': input('Pls enter its course: '),
            'Weight': self._get_input('Pls enter its weight (or press Enter to leave blank): ', is_float=True),

            'Q1_Points': self._get_input('Pls enter Q1_Points (or press Enter to leave blank): ', is_float=True),
            'Q2_Points': self._get_input('Pls enter Q2_Points (or press Enter to leave blank): ', is_float=True),
            'Q3_Points': self._get_input('Pls enter Q3_Points (or press Enter to leave blank): ', is_float=True),
            'Q4_Points': self._get_input('Pls enter Q4_Points (or press Enter to leave blank): ', is_float=True),
        }

        print("\nNew row preview:")
        for k, v in row_data.items():
            print(f"{k}: {v}")

        yes_no = input('Are you going to add this row? (y/n): ')
        if yes_no == 'y':
            self.manager.add_row(grade, row_data)
            self.manager.save_all()
            print(f'{grade} info updated successfully. \n')
            print(self.manager.get_data(grade))
        else:
            return

    def page_edit(self):
        print("\n---------- [ Edit_Course_Info ] ----------")
        grade = input('Please enter the grade you want to edit: ').strip()
        df = self.manager.get_data(grade)
        
        if df is None or df.empty:
            print(f'No data for grade {grade}')
            return

        print('Current data: ')
        print(df.to_string(index=True))

        try:
            row_input = input('Please enter the row index where you want to edit (1-based): ').strip()
            row_index = int(row_input) - 1 # 关键修正：减1
            if row_index < 0 or row_index >= len(df):
                print('Invalid row number.')
                return
        except ValueError:
            print('Please enter a valid number.')
            return

        print('Columns you can edit: ')
        print(', '.join(df.columns))

        col = input('Please enter the column you want to edit: ').strip()
        if col not in df.columns:
            print('Invalid column name.')
            return

        new_value_input = input('Please enter the new value: ').strip()
        new_value = new_value_input

        if col in self.numeric_cols:
            try:
                new_value = float(new_value_input)
            except ValueError:
                print('Invalid number format for this column.')
                return

        yes_no = input('Please confirm you want to change the value (y/n): ').strip()
        if yes_no != 'y':
            print('Edit cancelled.')
            return

        success = self.manager.update_cell(grade, row_index, col, new_value)
        if success:
            self.manager.save_all()
            print('Edit successful!')
            print(f'Updated row:\n{self.manager.get_data(grade).iloc[row_index]}')
        else:
            print("System Error: Update failed.")

    def start_loop(self):
        while True:
            print("\n---------- My Management System ----------")
            print("1. [ Add_Course_Info ]")
            print("2. [ Edit_Course_Info ]")
            print("3. [ Auto_Save & Exit ]")
            
            choice = input('Please enter index number: ').strip()
            
            if choice == '1':
                self.page_add()
            elif choice == '2':
                self.page_edit()
            elif choice == '3':
                self.manager.save_all()
                print('Saved.')
                break
            else:
                print('No such operation.')