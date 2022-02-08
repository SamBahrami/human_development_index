import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Human Development Index (HDI).csv")
end_year = 2019
years_back = 20
top_n = 10

# Load Data
years = sorted([str(end_year - i) for i in range(years_back)])
years.append("Country")
df.sort_values(by=["2019"], ascending=False, inplace=True)
df_data = df[years][:top_n]
df_data.set_index("Country", inplace=True)

print(df_data)
years = years[:-1]

# data was in strings
df_data = df_data[years].astype(float)
# if I transpose, plotting is ez
df_data = df_data.T
ax = df_data.plot(
    title="Human Development Index of the top 10 countries (2019) over the past 20 years",
    ylabel="",
    xlabel="",
    marker="o",
)
ax.set_xticks(range(0, len(df_data.index)), df_data.index)
plt.tight_layout()
plt.show()
