import discord
from textwrap import TextWrapper

import config


# for wrapping text
def wrap_text(width, text):
    wrapped_text = ""
    wrapper = TextWrapper(width)
    text_lines = wrapper.wrap(text)
    for line in text_lines:
        wrapped_text += "{line}\n".format(line=line)

    return wrapped_text


# returns an embed provided the data
async def get_info_embd(title, desc="", color=config.NORMAL_COLOR, footer=None, show_thumbnail=False):
    embd = discord.Embed()

    embd.color = color
    embd.title = title
    embd.description = desc

    if footer is not None:
        embd.set_footer(text=footer)

    if show_thumbnail is True:
        embd.set_thumbnail(url=f"{config.AVATAR_LINK}")

    return embd


async def get_user_id_from_ping(ping):
    user_id = ping

    ping_chars = ["<", "!", "@", ">"]
    for char in ping_chars:
        user_id = user_id.replace(char, "")

    return user_id


async def get_trade_value(pokecoins: int, shinies: int, rares: int, redeems: int) -> int:
    return int(pokecoins) + config.TRADE_ITEM_WEIGHT["shinies"] * int(shinies) + config.TRADE_ITEM_WEIGHT["rares"] * int(rares) + config.TRADE_ITEM_WEIGHT["redeems"] * int(redeems)
