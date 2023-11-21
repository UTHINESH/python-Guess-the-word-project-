import pandas as pd
#
# data = {'Name': ['Rose', 'John', 'Jane', 'Mary'],
#         'ID': [1, 2, 3, 4],
#         'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
#         'Salary': [100000, 80000, 50000, 60000]}
#
# df = pd.DataFrame(data)
# unique_dates = df['ID'].unique()
# # x = df[['Department','Salary','ID']]
# # print(x)
# print(df)
# print(unique_dates)

a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df1 = pd.DataFrame(a)
x = df1['Student']
print(df1)
print(type(x))

