import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# =======================
# Load dataset
# =======================
df = pd.read_csv("medical_examination.csv")

# =======================
# Add overweight column
# =======================
df["overweight"] = ((df["weight"] / ((df["height"] / 100) ** 2)) > 25).astype(int)

# =======================
# Normalize cholesterol & gluc
# =======================
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

# =======================
# Categorical Plot
# =======================
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    fig = sns.catplot(
        x="variable",
        y="total",
        col="cardio",
        hue="value",
        data=df_cat,
        kind="bar"
    ).fig

    fig.savefig("catplot.png")
    return fig

# =======================
# Heat Map
# =======================
def draw_heat_map():

    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ].copy()

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        vmax=0.3,
        linewidths=0.5,
        square=True,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    fig.savefig("heatmap.png")
    return fig

if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()