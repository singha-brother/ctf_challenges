import json 
import pandas as pd 

rooms = []
with open('./thm_rooms.txt', 'r') as f:
    raw = f.readlines()
    for line in raw:
        data = json.loads(line)
        rooms += data["rooms"]

df = pd.DataFrame(rooms)
print(df.columns)
cols = ['id', 'image', 'title', 'description', 'code', 'users', 'type',
       'difficulty', 'upVotes', 'created', 'published',
       'freeToUse', 'businessOnly', 'headerImage', 'creator']
df["id"] = range(1, len(df) + 1)
# print(df)

df[cols].to_csv('./rooms.csv', index=False)

ids = []
tags = []
for idx, room in enumerate(rooms):
    for tag in room["tags"]:
        ids.append(idx + 1)
        tags.append(tag.strip().lower())
        # print(idx + 1, ",", tag.strip().lower())

df_tag = pd.DataFrame(data={"id": ids, "tag": tags})
# print(df_tag)
df_tag.to_csv('./tags.csv', index=False)