
import pandas as pd
df = pd.read_csv('Salary_Data.csv')
x = df['YearsExperience']
x = x.values
x = x.reshape(30,1)
y = df['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
model.coef_
predicted_value = model.predict([[2.5]])
print("Predited salary for feature value 2.5")
print(predicted_value)





