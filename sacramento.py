import pandas as pd
import statsmodels.api as sm

sac_df = pd.read_csv("sacramento.csv")

def my_recode(baths):
    if baths == 1:
        return 0
    else:
        return 1

sac_df['bathdummy'] = sac_df['baths'].apply(my_recode)

x = sac_df[['beds', 'sqft', 'price']]
x = sm.add_constant(x, prepend=True)
y = sac_df[['bathdummy']]

log_reg = sm.Logit(y, x).fit()

print(log_reg.params.round(2))
print(log_reg.pvalues.round(2))
print('The smallest p-value is for sqft')

