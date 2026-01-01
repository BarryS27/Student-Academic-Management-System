import numpy as np
import pandas as pd
from tabulate import tabulate
import config
import viz

class ConsoleUI:
    def __init__(self, manager):
        self.manager = manager

    def _print_menu(self, options, title=None):
        if title:
            print(f"\n🔹 --- {title} ---")
        
        opts_list = list(options)
        if not opts_list:
            print("  (No options available)")
            return None

        for idx, opt in enumerate(opts_list, 1):
            print(f"  {idx}. {opt}")
        
        while True:
            choice = input(f"\n👉 Select (1-{len(opts_list)}) or 'q' to back: ").strip()
            if choice.lower() in ['q', 'exit']:
                return None
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(opts_list):
                    return opts_list[idx]
                else:
                    print(f"❌ Invalid number. Please enter 1-{len(opts_list)}.")
            except ValueError:
                print("❌ Please enter a number.")

    def _display_df(self, df):
        if df.empty:
            print("\n📭 [Table is Empty]")
            return
        
        display_df = df.copy()
        display_df.index = np.arange(1, len(df) + 1)
        
        print("\n" + tabulate(display_df, headers='keys', tablefmt='rounded_outline', showindex=True))
        print(f"  (Total Rows: {len(df)})\n")

    def _get_input(self, col_name):
        is_numeric = col_name in config.NUMERIC_COLS
        prompt = f"✍️  Enter value for '{col_name}'" + (" (number): " if is_numeric else ": ")
        
        while True:
            val = input(prompt).strip()
            if val == '':
                return np.nan
            
            if is_numeric:
                try:
                    return float(val)
                except ValueError:
                    print(f"❌ '{val}' is not a number. Please try again.")
                    continue
            return val


    def page_add(self):
        # 1. 选表
        table_name = self._print_menu(config.FILES.keys(), "Select Table to Add")
        if not table_name: return

        col_key = config.TABLE_MAPPING.get(table_name)
        columns = config.COLUMNS.get(col_key)

        print(f"\n📝 Adding new row to [{table_name}]...")
        row_data = {}
        
        for col in columns:
            row_data[col] = self._get_input(col)

        print("\nNew Row Preview:")
        print(row_data)

        if input('\n💾 Save this row? (y/n): ').lower() == 'y':
            self.manager.add_row(table_name, row_data)
            self.manager.save_all()
            print(f"✅ Saved to {table_name}.")
        else:
            print("🚫 Cancelled.")

    def page_edit(self):
        table_name = self._print_menu(config.FILES.keys(), "Select Table to Edit")
        if not table_name: return

        df = self.manager.get_data(table_name)
        if df.empty:
            print("⚠️ Table is empty.")
            return

        self._display_df(df)

        while True:
            try:
                row_input = input(f"👉 Select Row Number to Edit (1-{len(df)}) or 'q': ").strip()
                if row_input.lower() == 'q': return
                
                row_idx = int(row_input) - 1
                if 0 <= row_idx < len(df):
                    break
                print("❌ Invalid row number.")
            except ValueError:
                print("❌ Please enter a number.")

        print(f"\nChecking Row #{row_input}:")
        current_row = df.iloc[row_idx]
        print(tabulate(pd.DataFrame([current_row]), headers='keys', tablefmt='simple'))

        col_name = self._print_menu(df.columns, "Select Column to Change")
        if not col_name: return

        print(f"\nOld Value: {df.iat[row_idx, df.columns.get_loc(col_name)]}")
        new_val = self._get_input(col_name)
        
        if self.manager.update_cell(table_name, row_idx, col_name, new_val):
            self.manager.save_all()
            print("✅ Edit saved.")
        else:
            print("❌ System Error.")

    def page_delete(self):
        table_name = self._print_menu(config.FILES.keys(), "Select Table to Delete From")
        if not table_name: return

        df = self.manager.get_data(table_name)
        if df.empty:
            print("⚠️ Table is empty.")
        
        self._display_df(df)
        
        try:
            row_input = input(f"🗑️  Enter ROW Number to DELETE (1-{len(df)}): ").strip()
            if row_input.lower() == 'q': return

            r_idx = int(row_input) - 1
            
            if 0 <= r_idx < len(df):
                confirm = input(f"⚠️  Are you sure you want to PERMANENTLY delete Row {row_input}? (y/n): ")
                if confirm.lower() == 'y':
                    if self.manager.delete_row(table_name, r_idx):
                        self.manager.save_all()
                        print("🗑️  Row deleted.")
                else:
                    print("🚫 Cancelled.")
            else:
                print("❌ Invalid row number.")
        except ValueError:
            print("❌ Invalid input.")

    def page_viz(self):
        grade_tables = [k for k in config.FILES.keys() if k.startswith('G')]
        
        if not grade_tables:
            print("No grade tables found in config.")
            return

        grade_name = self._print_menu(grade_tables, "Select Grade to Visualize 📊")
        if not grade_name: return

        df = self.manager.get_data(grade_name)
        print(f"\n🎨 Generating graph for {grade_name}...")
        
        viz.plot_grade_analysis(df, grade_name)

    def page_show(self):
        table_name = self._print_menu(config.FILES.keys(), "Select Table to View")
        if table_name:
            df = self.manager.get_data(table_name)
            self._display_df(df)
            input("Press Enter to continue...")

    def start_loop(self):
        while True:
            print("\n" + "="*40)
            print(" 🎓 Student Academic Manager (SAMS)")
            print("="*40)
            print("1. 👁️  View Data Table")
            print("2. ➕ Add Info")
            print("3. ✏️  Edit Info")
            print("4. 🗑️  Delete Info")
            print("5. 📊 Visualize Data (Charts)")
            print("6. 🚪 Exit")
            
            choice = input("\n👉 Select operation (1-6): ").strip()
            
            if choice == '1': self.page_show()
            elif choice == '2': self.page_add()
            elif choice == '3': self.page_edit()
            elif choice == '4': self.page_delete()
            elif choice == '5': self.page_viz()
            elif choice == '6':
                self.manager.save_all()
                print("👋 Bye! All data saved.")
                break
            else:
                print("❌ Invalid choice.")