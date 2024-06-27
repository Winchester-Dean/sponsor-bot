from database.db import DataBase

channels = DataBase().get_channels_id()
for channel in channels:
    for chid in channel:
        print(f"-100{chid}")
