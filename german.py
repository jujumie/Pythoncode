import pandas as pd
import statsmodels.api as sm

german_df = pd.read_csv("german_credit_data.csv", sep =',')

german = german_df.rename(columns = {"Credit amount": "Credit_amount"}, inplace=False)

x = german[['Age', 'Duration']]
x = sm.add_constant(x, prepend=True)
y = german[['Credit_amount']]

model_2 = sm.OLS(y, x).fit()

print(model_2.params.round(2))
print(model_2.rsquared.round(2))
