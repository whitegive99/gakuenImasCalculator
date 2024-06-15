from hoshino import Service
from hoshino.typing import CQEvent
from .calc import calc_rank

sv = Service('学园偶像大师算分插件', help_='''
[算分] + 三维属性
例如：算分 1200 1300 1400
'''.strip())

@sv.on_prefix('算分')
async def handle_calc_rank(bot, ev: CQEvent):
    args = ev.message.extract_plain_text().strip().split()
    result = await calc_rank(args)
    await bot.send(ev, result)
