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






