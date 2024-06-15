from hoshino import Service
from hoshino.typing import CQEvent
from .calc import calc_rank

sv = Service('学园偶像大师算分插件', enable_on_default=True, bundle='娱乐')

@sv.on_prefix('算分')
async def handle_calc_rank(bot, ev: CQEvent):
    args = ev.message.extract_plain_text().strip().split()
    result = await calc_rank(args)
    await bot.send(ev, result)
