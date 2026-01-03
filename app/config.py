from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "mydata"
DATA_DIR.mkdir(parents=True, exist_ok=True)


FILES = {
    'G9': DATA_DIR / 'G9.csv',
    'G10': DATA_DIR / 'G10.csv',
    'G11': DATA_DIR / 'G11.csv',
    'G12': DATA_DIR / 'G12.csv',
    'Self_Dev': DATA_DIR / 'Self_Dev.csv',
    'Dream_Schools': DATA_DIR / 'Dream_Schools.csv',
    'Dream_Majors': DATA_DIR / 'Dream_Majors.csv'
}


DEFAULT_SYSTEM_PROMPT = """
You are an expert Academic Advisor for US High School students. 
Analyze the student's grades and goals. Be encouraging but realistic. 
Keep answers concise and actionable.
"""


COLUMNS = {
    'Grades': ['Sem', 'Level', 'Code', 'Course', 'Weight', 'Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points'],
    'Self_Dev': ['Course', 'From', 'Skill', 'Status', 'Proficiency'],
    'Dream_Schools': ['University', 'School'],
    'Dream_Majors': ['Major']
}


TABLE_MAPPING = {
    'G9': 'Grades', 'G10': 'Grades', 'G11': 'Grades', 'G12': 'Grades',
    'Self_Dev': 'Self_Dev', 'Dream_Schools': 'Dream_Schools', 'Dream_Majors': 'Dream_Majors'
}


NUMERIC_COLS = [
    'Weight', 'Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points', 'Proficiency'
]