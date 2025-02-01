from core.env import env

BOT_TOKEN = env.parse_str('BOT_TOKEN')

MONGO_URL = env.parse_str('MONGO_URL')
MONGO_DB_NAME = env.parse_str('MONGO_DB_NAME')