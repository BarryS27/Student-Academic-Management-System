import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

try:
    from scipy.interpolate import make_interp_spline
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

THEME = {
    'bg_main': '#1C1C1E',
    'bg_card': '#2C2C2E',
    'text_white': '#F2F2F7',
    'text_gray': '#8E8E93',
    'grid': '#3A3A3C',
    'cyan': '#64D2FF',
    'green': '#30D158',
    'orange': '#FF9F0A',
    'purple': '#BF5AF2',
    'red': '#FF453A',
}

def _setup_style():
    plt.rcParams.update({
        'figure.facecolor': THEME['bg_main'],
        'axes.facecolor': THEME['bg_main'],
        'axes.edgecolor': THEME['bg_main'],
        'axes.labelcolor': THEME['text_gray'],
        'xtick.color': THEME['text_gray'],
        'ytick.color': THEME['text_gray'],
        'grid.color': THEME['grid'],
        'grid.linestyle': '-',
        'grid.linewidth': 0.8,
        'grid.alpha': 0.3,
        'text.color': THEME['text_white'],
        'font.family': 'sans-serif',
        'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
        'figure.dpi': 120
    })

def _calculate_total(df):
    cols = ['Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points']
    valid_cols = [c for c in cols if c in df.columns]
    if not valid_cols:
        return pd.Series([0]*len(df))
    return df[valid_cols].sum(axis=1)

def plot_subject_breakdown(df, grade_name):
    _setup_style()
    
    if df.empty: return

    df = df.copy()
    df['Total_Score'] = _calculate_total(df)
    df = df[df['Total_Score'] > 0].sort_values('Total_Score', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    y_pos = np.arange(len(df))
    scores = df['Total_Score'].values
    courses = df['Code'].values

    ax.barh(y_pos, [max(scores)*1.1]*len(y_pos), height=0.2, color=THEME['bg_card'], align='center')

    bars = ax.barh(y_pos, scores, height=0.2, color=THEME['cyan'], alpha=1.0, align='center')

    ax.barh(y_pos, scores, height=0.4, color=THEME['cyan'], alpha=0.2, align='center')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(courses, fontsize=11, fontweight='bold')
    ax.set_xlabel('TOTAL POINTS', fontsize=9, letterspacing=2) # letterspacing 增加工业感
    
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    ax.grid(axis='x', visible=True, alpha=0.2)
    ax.grid(axis='y', visible=False)

    for i, v in enumerate(scores):
        ax.text(v + 2, i, str(int(v)), color=THEME['text_white'], va='center', fontsize=10, fontweight='bold')

    plt.title(f"{grade_name} // PERFORMANCE MATRIX", fontsize=14, fontweight='bold', color=THEME['text_gray'], loc='left', pad=20)
    plt.tight_layout()
    plt.show()

def plot_gpa_trend(full_df, selected_subjects):
    _setup_style()
    
    if full_df.empty: return

    fig, ax = plt.subplots(figsize=(10, 6))
    
    grade_map = {'G9': 1, 'G10': 2, 'G11': 3, 'G12': 4}
    colors = [THEME['cyan'], THEME['green'], THEME['orange'], THEME['purple']]
    
    plotted_any = False

    for idx, code in enumerate(selected_subjects):
        sub_df = full_df[full_df['Code'] == code].copy()
        if sub_df.empty: continue
            
        sub_df['Grade_Int'] = sub_df['Grade_Level'].map(grade_map)
        sub_df = sub_df.sort_values('Grade_Int')
        
        x = sub_df['Grade_Int'].values
        y = sub_df['Total_Score'].values
        
        if len(x) < 1: continue
        plotted_any = True
        
        line_color = colors[idx % len(colors)]

        if SCIPY_AVAILABLE and len(x) > 2:
            x_new = np.linspace(1, 4, 300)
            try:
                spl = make_interp_spline(x, y, k=2)
                y_smooth = spl(x_new)
                y_smooth = np.clip(y_smooth, 0, None)
            except:
                x_new, y_smooth = x, y
        else:
            x_new, y_smooth = x, y

        ax.plot(x_new, y_smooth, color=line_color, linewidth=6, alpha=0.15)
        ax.plot(x_new, y_smooth, color=line_color, linewidth=10, alpha=0.05)
        
        ax.plot(x_new, y_smooth, color=line_color, linewidth=2, alpha=1.0, label=code)

        ax.scatter(x, y, color=THEME['bg_main'], edgecolor=line_color, s=50, linewidth=2, zorder=10)

    if not plotted_any: return

    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(['G9', 'G10', 'G11', 'G12'], fontweight='bold')
    ax.set_xlim(0.8, 4.2)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.grid(axis='y', linestyle='-', alpha=0.15, color='white')
    ax.grid(axis='x', visible=False)
    
    plt.title("ACADEMIC TRAJECTORY // TREND", fontsize=14, fontweight='bold', color=THEME['text_gray'], loc='left', pad=20)
    
    legend = plt.legend(frameon=False, labelcolor=THEME['text_gray'], loc='upper left')
    
    plt.tight_layout()
    plt.show()

def plot_radar_distribution(df, grade_name):
    _setup_style()
    
    if df.empty: return
    
    df = df.copy()
    df['Total_Score'] = _calculate_total(df)
    df = df[df['Total_Score'] > 0]
    
    if len(df) > 6:
        df = df.sort_values('Total_Score', ascending=False).head(6)
        
    categories = df['Code'].tolist()
    values = df['Total_Score'].tolist()
    
    if not categories: return

    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    ax.set_facecolor(THEME['bg_main'])
    fig.patch.set_facecolor(THEME['bg_main'])

    ax.plot(angles, values, color=THEME['green'], linewidth=2, linestyle='-')
    ax.fill(angles, values, color=THEME['green'], alpha=0.15)
    
    ax.yaxis.grid(True, color=THEME['grid'], linestyle='--', alpha=0.3)
    ax.xaxis.grid(True, color=THEME['grid'], linestyle='-', alpha=0.3)
    
    ax.spines['polar'].set_color(THEME['grid'])
    ax.spines['polar'].set_alpha(0.3)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12, fontweight='bold', color=THEME['text_white'])
    
    ax.set_yticklabels([]) 
    
    plt.title(f"SKILL RADAR // {grade_name}", fontsize=14, fontweight='bold', color=THEME['text_gray'], pad=30)
    
    plt.tight_layout()
    plt.show()