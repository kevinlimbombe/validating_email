import pandas as pd

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

df = pd.read_csv('email_list.csv')

df_filter = df[df.email.str.match(regex)]
		
df_filter.to_csv(r'C:\Users\limbo\Desktop\export_validation.csv', index = False, header=True)