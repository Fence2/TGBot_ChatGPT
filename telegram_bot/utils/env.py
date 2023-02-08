import os
from abc import ABC
from typing import Final


class Env(ABC):
    TGBOT_TOKEN: Final = os.environ.get('TGBOT_TOKEN', 'define me!')
    OPENAI_TOKEN: Final = os.environ.get('OPENAI_TOKEN', 'define me!')
    ADMIN_ID: Final = int(os.environ.get("ADMIN_ID", "define me!"))
