
from RADHAMUSIC.core.bot import VISHNU
from RADHAMUSIC.core.dir import dirr
from RADHAMUSIC.core.git import git
from RADHAMUSIC.core.userbot import Userbot
from RADHAMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VISHNU()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
