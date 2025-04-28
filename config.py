# REQUIRED CONFIG
BOT_TOKEN = "8035877917:AAFLR5oEh_HCdUSUVrVClhFLDEJgBgJeuY8"
OWNER_ID = 7465574522
TELEGRAM_API = 27394279
TELEGRAM_HASH = "90a9aa4c31afa3750da5fd686c410851"

# SEMI-REQUIRED, WE SUGGEST TO FILL IT FROM MONGODB
DATABASE_URL = "mongodb+srv://python21java:8ZFGYMKJCqAPwsiO@filestore.f876hjv.mongodb.net/?retryWrites=true&w=majority&appName=Filestore"

# OPTIONAL CONFIG
TG_PROXY = {"scheme": "socks5", "hostname": "45.140.143.77", "port": 18080, "username": "", "password": ""}
USER_SESSION_STRING = ""
DOWNLOAD_DIR = "/usr/src/app/downloads/"
CMD_SUFFIX = ""
AUTHORIZED_CHATS = ""
SUDO_USERS = ""
DEFAULT_UPLOAD = "rc"
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = True
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# INKYPINKY
DELETE_LINKS = False
FSUB_IDS = "-1002226481922"
TOKEN_TIMEOUT = 0
LOGIN_PASS = ""  # Set a password to enable login feature
PAID_CHANNEL_ID = 0
PAID_CHANNEL_LINK = ""
SET_COMMANDS = True
METADATA_KEY = ""
LOG_CHAT_ID = -1002415859244
LEECH_FILENAME_CAPTION = ""
HYDRA_IP = ""
HYDRA_API_KEY = ""
INSTADL_API = ""
MEDIA_STORE = False

# Media Tools Settings
MEDIA_TOOLS_ENABLED = False  # Enable/disable Media Tools feature

# GDrive Tools
GDRIVE_ID = ""
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# Mega credentials
MEGA_EMAIL = ""
MEGA_PASSWORD = ""

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    },
]

# Update
UPSTREAM_REPO = "https://github.com/blandk77/_"
UPSTREAM_BRANCH = "beta"

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
MEDIA_GROUP = False
USER_TRANSMISSION = False
HYBRID_LEECH = False
LEECH_FILENAME_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_FILENAME = ""
LEECH_DUMP_CHAT = "-1002204579260"
THUMBNAIL_LAYOUT = ""

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 80
WEB_PINCODE = False

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# Resource Management
FFMPEG_MEMORY_LIMIT = 2048  # Memory limit in MB (0 = no limit)
FFMPEG_CPU_AFFINITY = (
    ""  # CPU cores to use (e.g., "0-3" or "0,2,4,6"), empty = all cores
)
FFMPEG_DYNAMIC_THREADS = True  # Dynamically adjust thread count based on system load

# Auto Restart Settings
AUTO_RESTART_ENABLED = False  # Enable/disable automatic bot restart
AUTO_RESTART_INTERVAL = 24  # Restart interval in hours

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0
