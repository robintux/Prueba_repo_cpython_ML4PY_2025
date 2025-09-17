# Carguemos los datos
import pandas as pd
cpython = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/cpython_commit_history_pre.csv")

# Creamos columnas para obtener informacion temporal
cpython['date'] = pd.to_datetime(cpython['date'], utc = True)
cpython['year'] = cpython['date'].dt.year
cpython['month'] = cpython['date'].dt.to_period('M')

# 1. Evolución temporal de commits
import matplotlib.pyplot as plt

# Gráfico de commits por año
commits_by_year = cpython.groupby('year').size()
plt.figure(figsize=(14,6))
commits_by_year.plot(kind='line', marker='o')
plt.title("Evolution of Commits to CPython by Year")
plt.xlabel("Year")
plt.ylabel("Number of Commits")
plt.grid(True)
plt.savefig("Cpython_num_commits_year.png", dpi = 300)
plt.show()

#  Top 10 contribuyentes históricos
top_authors = cpython['author'].value_counts().head(10)
plt.figure(figsize=(10,6))
top_authors.plot(kind='barh', color='skyblue')
plt.title("Top 10 Contributors to CPython (by number of commits)")
plt.xlabel("Number of Commits")
plt.gca().invert_yaxis()
plt.savefig("Cpython_top10_developers.png", dpi = 300)
plt.show()

# =============================================================================
# Cambios agregados en otra computadora (Sistema Operativo : Windows 11)
# =============================================================================

# Análisis de complejidad: Líneas añadidas/eliminadas por año
cpython['net_changes'] = cpython['lines_added'] - cpython['lines_removed']
annual_changes = cpython.groupby('year')[['lines_added', 'lines_removed', 'net_changes']].sum()

fig, ax = plt.subplots(figsize=(14,6))
ax.bar(annual_changes.index, annual_changes['lines_added'], label='Added', alpha=0.7)
ax.bar(annual_changes.index, -annual_changes['lines_removed'], label='Removed', alpha=0.7)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_title("Net Code Changes in CPython per Year")
plt.savefig("Cpython_cambios_por_year", dpi = 300)

ax.legend()
plt.show()

# Esto es un nuevo cambio en un notebook de kaggle 



