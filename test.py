import time
from database.db import DataBase

if __name__ == "__main__":
    try:
        users = DataBase().get_users()
        admins = DataBase().get_admins()
        channels = DataBase().get_channels()

        print("Users:")
        for user in users:
            id = user[0]
            user_id = user[1]
            name = user[2]

            print(f"{id}. {name}: {user_id}")
        
        print("\nAdmins:")
        for admin in admins:
            id = admin[0]
            admin_id = admin[1]
            adm_name = admin[2]

            print(f"{id}. {adm_name}: {admin_id}")
        
        print("\nChannels:")
        for channel in channels:
            id = channel[0]
            channel_id = channel[1]
            curl = channel[2]
            channel_name = channel[3]

            print(f"{id}. {channel_name}: {curl}: {channel_id}")
        
        time.sleep(10)
    except Exception as error:
        print(error)
        time.sleep(10)