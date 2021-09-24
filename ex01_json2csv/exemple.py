import pandas as pd
df = pd.read_json (r'C:\Users\samil\Documents\python\hi-python\ex01_json2csv\exemple.json')
df.to_csv (r'C:\Users\samil\Documents\python\hi-python\ex01_json2csv\exemple.csv', index = None)