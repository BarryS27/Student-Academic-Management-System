import numpy as np
import pandas as pd
from tabulate import tabulate
from . import config
from . import viz

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
            return
        
        self._display_df(df)
        
        try:
            row_input = input(f"🗑️  Enter ROW Number to DELETE (1-{len(df)}): ").strip()
            if row_input.lower() == 'q': return

            r_idx = int(row_input) - 1
            
            if 0 <= r_idx < len(df):
                if input(f"⚠️ Delete Row {row_input}? (y/n): ").lower() == 'y':
                    if self.manager.delete_row(table_name, r_idx):
                        self.manager.save_all()
                        print("🗑️  Row deleted.")
            else:
                print("❌ Invalid row number.")
        except ValueError:
            print("❌ Invalid input.")

    def page_viz(self):
        print("\n📊 --- Visualization Hub ---")
        print("1. Subject Breakdown (Thin Bar Chart) - View specific grade performance")
        print("2. GPA Trend (Smooth Line) - View progress from G9 to G12")
        print("3. Grade Distribution (Radar Chart) - View subject balance")
        
        choice = input("\n👉 Select Chart Type (1-3): ").strip()
        
        grade_tables = [k for k in config.FILES.keys() if k.startswith('G')]

        if choice == '1':
            grade_name = self._print_menu(grade_tables, "Select Grade")
            if grade_name:
                df = self.manager.get_data(grade_name)
                viz.plot_subject_breakdown(df, grade_name)

        elif choice == '2':
            print("\n🔄 Loading history data...")
            full_df = self.manager.get_all_grades_combined()
            
            if full_df.empty:
                print("⚠️ No data found across G9-G12.")
                return

            print("\nExisting Subjects across years:")
            unique_codes = sorted(full_df['Code'].unique().tolist())
            print(f"[{', '.join(unique_codes)}]")
            
            user_input = input("\n✍️  Enter Subject Codes to track (comma separated, e.g., 'MA101, ENG09'): ").strip()
            if not user_input: return
            
            selected_codes = [s.strip() for s in user_input.split(',')]
            viz.plot_gpa_trend(full_df, selected_codes)

        elif choice == '3':
            grade_name = self._print_menu(grade_tables, "Select Grade for Radar Analysis")
            if grade_name:
                df = self.manager.get_data(grade_name)
                viz.plot_radar_distribution(df, grade_name)
                
        else:
            print("❌ Invalid selection.")

    def page_ai_chat(self):
        print("\n🤖 --- AI Academic Advisor ---")
        print("⚠️  Privacy Notice: Your query will be sent to OpenAI servers.")
        
        confirm = input("👉 Proceed to chat? (y/n): ").strip().lower()
        if confirm != 'y':
            print("🚫 Cancelled.")
            return

        print("\n[Persona Configuration]")
        print(f"Default Style: Professional, Concise, Direct.")
        
        custom_sys = input("👉 Enter custom persona (or press ENTER to use Default): ").strip()
        
        print("\n📝 What's your question?")
        user_query = input(">>> ").strip()
        
        if not user_query:
            print("⚠️ Question cannot be empty.")
            return

        print("\n🔄 Connecting to Neural Network...")
        
        response = self.manager.ask_ai(user_query, custom_sys)
        
        print("\n" + "="*40)
        print("💡 INSIGHT:")
        print("-" * 40)
        print(response)
        print("="*40 + "\n")
        
        input("Press Enter to continue...")

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
            print("6. 🤖 Chat with AI") 
            print("7. 🚪 Exit")
            
            choice = input("\n👉 Select operation (1-7): ").strip()
            
            if choice == '1': self.page_show()
            elif choice == '2': self.page_add()
            elif choice == '3': self.page_edit()
            elif choice == '4': self.page_delete()
            elif choice == '5': self.page_viz()
            elif choice == '6': self.page_ai_chat()
            elif choice == '7':
                self.manager.save_all()
                print("👋 Bye! All data saved.")
                break
            else:
                print("❌ Invalid choice.")