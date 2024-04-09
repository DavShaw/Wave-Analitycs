import pandas as pd
import json

with open('sounddata.json', 'r') as file:
    data = json.load(file)

# Replace strings for numbers
# david 0
# cristian 1
# christian 2

records = []
for key, value in data.items():
    for sample_id, sample_data in value.items():
        record = {'person': key, 'segment': int(sample_id)}
        record.update(sample_data)
        records.append(record)

df = pd.DataFrame(records)

print(df)
