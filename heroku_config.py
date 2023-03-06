import os


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", "24520135"))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "116cb57d1c16eaca50ace3e397c112b9")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQF2JccADg0qaOe0XSkxiKlXq0_D1YzFrpjbUZzFeqFwRGAeEbbhh78CBp7d930qixH9yn6fQceddA1W1nLQBLS9CNvbzdtXi7PBbTxdkTBV5dgFjFKsmeH5O6xt-rJPbbdtH7j6-YbM1OCI62njesEPEcrqhfusaR8gpJ2HqmrMs3b60VL8F6xjEIXDgfUTbKTukXDvEvT0CUD1MBTPV7NxtqPc7LFvenv-v-8nTnZAJXl77EJ2-uk5LxUE1FyL7t8FqFe4VbQbBfZdZ3snwRcT3LwwAh4KnB8DT_jQMKp8AvwU6_CESll1qodnKA7A5rB2SA7TJSzTjwujxnaB86BzIn0vTgAAAAFhnzs3AA")
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://varmadivya:varmadivya@dividillu.dm5us5x.mongodb.net/?retryWrites=true&w=majority")
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "5932792631").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None), 
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "374255a5-723f-4ed5-9bbc-e0b0be85303a")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", lightning)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", "6209411779:AAHj1wUAd49glCOvVsAo28PjHSX9Frk4gAw")
    # Send .get_id in any channel to fill this value.
    COMBINED_GROUP_ID = int(os.environ.get("COMBINED_GROUP_ID", "-909422382"))
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", f"{COMBINED_GROUP_ID}",  "-909422382")
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", f"{COMBINED_GROUP_ID}",  "-909422382")
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", f"{COMBINED_GROUP_ID}",  "-909422382")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", "@user_kalyan_bot")
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", f"{COMBINED_GROUP_ID}",  "-909422382")
    if PRIVATE_GROUP_ID is not None: -909422382
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    LIGHTNING_PRO = os.environ.get("LIGHTNING_PRO", "YES")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())


class Development(Var): True
    LOGGER = True
