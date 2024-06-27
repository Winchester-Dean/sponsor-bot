import time
from database.db import DataBase

if __name__ == "__main__":
    try:
        DataBase().add_new_user(6099758454, "Dean")
        DataBase().add_new_admin(6099758454, "Dean")
        DataBase().add_new_channel(
            2068044078,
            "https://t.me/DBoyTeam",
            "𝘿𝘽𝙤𝙮 𝙏𝙚𝙖𝙢"
        )
        DataBase().add_new_channel(
            2039489504,
            "https://t.me/Best_Serwers",
            "Best Serwers 🇹🇲"
        )
        DataBase().add_new_channel(
            1656388346,
            "https://t.me/universal_vpns1",
            "ֆʟօա & ʀɛʋɛʋʀɮ ʍʊֆɨƈ"
        )
        DataBase().add_new_channel(
            1887276118,
            "https://t.me/mega_serverss",
            "𝗠𝗘𝗚𝗔 𝗦𝗘𝗥𝗩𝗘𝗥𝗦 🛡"
        )

        '''
        users = DataBase().get_users()
        users_id = DataBase().get_users_id()

        print(users_id)

        print("Users:")
        for user in users:
            id = user[0]
            user_id = user[1]
            name = user[2]

            print(f"{id}. {name}: {user_id}")

        uid = 45678956677
        if (uid, ) not in users_id:
            print(uid)'''
    except Exception as error:
        print(error)
