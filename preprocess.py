import pandas as pd
import gzip
import json
import os


def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')


all_data = []
for i in os.listdir('data'):
  print(i)

  df1 = getDF(os.path.join('data',str(i)))

  df2 = df1[['overall', 'reviewText']]
  all_data.append(df2)

  # ['overall', 'verified', 'reviewText', 'summary',

  # print(df.head(10))
result = pd.concat(all_data)

result.to_csv("final_data.csv")
