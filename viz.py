import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_grade_analysis(df, grade_name):
    if df.empty:
        print("No data to plot.")
        return
    
    cols = ['Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points']
    valid_cols = [c for c in cols if c in df.columns]
    
    if not valid_cols:
        print("No score columns found to plot.")
        return

    plot_df = df.copy()
    plot_df['Total_Score'] = plot_df[valid_cols].sum(axis=1)
    
    plot_df = plot_df[plot_df['Total_Score'] > 0].sort_values('Total_Score', ascending=False)
    
    if plot_df.empty:
        print("No scores available to plot yet.")
        return

    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ios_palette = sns.color_palette("pastel")

    bars = sns.barplot(
        x='Code', 
        y='Total_Score', 
        data=plot_df, 
        palette=ios_palette, 
        edgecolor=None,
        ax=ax
    )

    sns.despine(left=True, bottom=True)
    
    plt.title(f"{grade_name} Performance Analysis", fontsize=20, fontweight='bold', color='#333333', pad=20)
    plt.xlabel("Course Code", fontsize=12, color='#666666', labelpad=10)
    plt.ylabel("Total Points", fontsize=12, color='#666666', labelpad=10)
    
    ax.grid(axis='y', linestyle='--', alpha=0.3, color='gray')
    ax.grid(axis='x', visible=False)

    for container in ax.containers:
        ax.bar_label(container, padding=5, color='#666666', fontsize=10)

    fig.patch.set_facecolor('white')
    fig.patch.set_alpha(0.9) 

    plt.tight_layout()
    
    print("Opening plot window...")
    plt.show()