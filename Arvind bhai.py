import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_csv('March-April.2020.csv')
print (df)

#Generate a report
profile = ProfileReport(df)
profile.to_file(output_file = "Harrybhai.html")