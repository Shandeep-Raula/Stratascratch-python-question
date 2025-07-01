import matplotlib.pyplot as plt


plt.figsize=(8, 8)
color_discrete_map  = {'PC': 'sienna', 'Consoles': 'rosybrown', 'Mobile': 'tan'}
color_list = df['platform'].map(color_discrete_map)

# Plot
plt.pie(
    df['market_share'],
    labels=df['platform'],
    autopct='%1.1f%%',
    startangle=90,
    colors=color_list
)
plt.title('Platform Distribution')
plt.axis('equal')
plt.show()
