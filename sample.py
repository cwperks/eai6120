import pandas as pd

df = pd.read_csv("311_Service_Requests_from_September_2022_to_Present.csv")

df_sample = df.sample(100000)

df_sample.to_csv("311_Service_Requests_from_September_2022_to_Present_Sample.csv")