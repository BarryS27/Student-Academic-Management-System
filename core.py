import pandas as pd
import numpy as np
import config

class GradeSystem:
    def __init__(self):
        self.data = {} 
        self._load_all_data()

    def _safe_load(self, filename, col_type):
        try:
            return pd.read_csv(filename)
        except FileNotFoundError:
            print(f"[System] File {filename} not found. Created new.")
            default_cols = config.COLUMNS.get(col_type, [])
            return pd.DataFrame(columns=default_cols)

    def _load_all_data(self):
        for grade in ['G9', 'G10', 'G11', 'G12']:
            self.data[grade] = self._safe_load(config.FILES[grade], 'Grades')
        
        self.data['Self_Dev'] = self._safe_load(config.FILES['Self_Dev'], 'Self_Dev')
        self.data['Dream_Schools'] = self._safe_load(config.FILES['Dream_Schools'], 'Dream_Schools')
        self.data['Dream_Majors'] = self._safe_load(config.FILES['Dream_Majors'], 'Dream_Majors')

    def save_all(self):
        try:
            for key, filename in config.FILES.items():
                if key in self.data:
                    self.data[key].to_csv(filename, index=False)
            return True, "All changes saved successfully."
        except Exception as e:
            return False, str(e)

    def get_data(self, key):
        return self.data.get(key)

    def add_row(self, key, row_data):
        if key not in self.data:
            return False
        
        new_df = pd.DataFrame([row_data])
        self.data[key] = pd.concat([self.data[key], new_df], ignore_index=True)
        return True

    def update_cell(self, key, row_idx, col_name, new_value):
        df = self.data.get(key)
        if df is None or row_idx >= len(df) or col_name not in df.columns:
            return False
        
        col_idx = df.columns.get_loc(col_name)
        df.iat[row_idx, col_idx] = new_value
        return True