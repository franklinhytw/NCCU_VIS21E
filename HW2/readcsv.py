import csv

obj = {}

with open('dataset.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.DictReader(csvfile)
  
  for row in rows:
    print(row)