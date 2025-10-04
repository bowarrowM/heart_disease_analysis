from all_imports import *

#EDA PLOTS
#Plot which features peak depending on the dataset source or gender
cat_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"] # Categorical columns. Modify depending on the needs.

# Plots for dataset source
for col in cat_cols:
    plt.figure(figsize=(8,4))
    sns.countplot(data=df, x=col, hue="dataset", palette="Set2")
    plt.title(f"{col} distribution by dataset")
    plt.show()
# Summary stats
exclude = ["id", "num"]
cat_cols_dataset = [col for col in df.columns if (df[col].dtype == "object" or df[col].nunique() < 10) and col not in exclude]
cat_summary_dataset = {}
for col in cat_cols_dataset:
    cat_summary_dataset[col] = df.groupby("dataset")[col].agg(lambda x: x.value_counts().idxmax())
cat_summary_dataset = pd.DataFrame(cat_summary_dataset)

# Plots based on sex/gender (dataset ignored)
for col in cat_cols:
    plt.figure(figsize=(8,4))
    sns.countplot(data=df, x=col, hue="sex", palette="Set1")
    plt.title(f"{col} distribution by sex")
    plt.show()
# Summary stats
exclude = ["id", "dataset", "num", "sex"]
cat_cols_sex = [col for col in df.columns if (df[col].dtype == "object" or df[col].nunique() < 10) and col not in exclude]
cat_summary = {}
for col in cat_cols_sex:
    cat_summary[col] = df.groupby("sex")[col].agg(lambda x: x.value_counts().idxmax())
cat_summary = pd.DataFrame(cat_summary)

#distribution of the x (x = heart disease yes/no)
sns.countplot(x='num', data=df)
plt.title('Heart Disease Distribution')
plt.show()

