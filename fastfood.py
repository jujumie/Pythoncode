import pandas as pd
import statsmodels.api as sm

food_df = pd.read_csv("fastfood.csv", sep=',')

x = food_df[['total_fat', 'sat_fat', 'cholesterol', 'sodium']]
x = sm.add_constant(x, prepend=True)
y = food_df[['calories']]

model = sm.OLS(y, x).fit()

print(model.mse_total.round(2))
print(model.rsquared.round(2))
print(model.params.round(2))
print(model.pvalues.round(2))
