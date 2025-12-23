# https://github.com/vikashishere/YT-MLOPS-DVC-DataVersion/blob/main/mycode.py
import pandas as pd
import os 

data = {"name":['alice','bob','charlie'],
"age":[20,30,40],
"gender":['F','M','M']
}
df = pd.DataFrame(data)

#add more data for dvc - v2
df['city'] = ['av','ad','al']


data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)
print(f"csvdata saved successfully at {data_dir}")

