import pandas  as pd


 
data = pd.read_excel('open_file.xlsx')
print("Before Execution")
df = pd.DataFrame(data)
# print(df)
# print("After Execution")

sum = df['English'] + df['Telugu'] + df['Maths'] + df['Science']

df['total'] = df['English'] + df['Telugu'] + df['Maths'] + df['Science']



avg = (df['total'])/4

df['Percentage %'] = (df['total'])/4

print(df)