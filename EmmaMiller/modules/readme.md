## EmmaMillerBot Example plugin format
```python3
from EmmaMiller.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="Emma")
@disableable_dec("Emma")
async def _(message):
    j = "Hello there my name is Emma"
    await message.reply(j)
    

__help__ = """
<b>Hi</b>
- /hi: Hello there my name is Emma
"""
__mod_name__ = "Emma"
```

<a href="https://t.me/BotMasterOfficial"><img src="https://img.shields.io/badge/support%20group-blue.svg?style=for-the-badge&logo=Telegram">
</a> <a href="https://t.me/BotMasterOfficial"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/EmmaMillerBot"><img src="https://img.shields.io/badge/Foundbot%20on-blue.svg?style=for-the-badge&logo=Telegram">
