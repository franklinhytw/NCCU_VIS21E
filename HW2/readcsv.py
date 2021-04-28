import csv

obj = {}

with open('dataset.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.DictReader(csvfile)
    
  for row in rows:   
    obj[row["民國年別"]] = row
    obj[row["民國年別"]].pop("民國年別", None)
   
result = {"戶數": {},"人口數": {},"戶量": {},"人口密度": {},"出生人數": {},"死亡人數": {},"結婚對數": {},"離婚對數": {}} 

for key, value in obj.items():
    # result["戶數"][key] = value["戶數"]
        
    for vkey, vvalue in value.items():
        tmp = {}
        tmp[key] = vvalue
        # print(tmp)
        result[vkey].update(tmp)
        # print(vkey)
        
        # d = {}
        # d["name"] = vkey
        # d["value"] = vvalue
        
        # arr.append(d)
# print(result)
rs = []
for key, value in result.items():
    data = []
    print(key)
    for vkey, vvalue in value.items():
        tmp = {}
        tmp['name'] = vkey
        tmp['value'] = vvalue
        data.append(tmp)
        
        
    rs.append(data)
print(rs)