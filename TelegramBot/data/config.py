from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

AWARD_PREREF = 3000

# Лист админов которым будет доступен админ панел в боте
MAINADMINS = [706117669]

# Username бота
BOT_NAME = 'Tectum_robot'

# Username канал и групп
CHAT_NAME = '@tectumglobal'
CHANNEL_NAME = '@tectumdriven'

# Логин и парол инстаграм аккаунта
LOGIN_INS = 'ВАШ ЛОГИН'
PASSWORD_INS = 'ВАШ ПАРОЛ'