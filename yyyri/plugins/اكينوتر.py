import imp
import os
import re

try:
    import akinator
except ModuleNotFoundError:
    os.system("pip3 install akinator.py")
    import akinator

from telethon import Button
from telethon.errors import BotMethodInvalidError
from telethon.events import CallbackQuery, InlineQuery

from sbb_b import sbb_b
from ..Config import Config
from ..core.decorators import check_owner

games = {}
aki_photo = "https://telegra.ph/file/b0ff07069e8637783fdae.jpg"


@sbb_b.ar_cmd(pattern="اكينوتر(?:\s|$)([\s\S]𓆘)")
async def rozdo(e):
    sta = akinator.Akinator()
    games.update({e.chat_id: {e.id: sta}})
    try:
        m = await e.client.inline_query(
            Config.TG_BOT_USERNAME, f"aki_{e.chat_id}_{e.id}"
        )
        await m[0].click(e.chat_id)
    except BotMethodInvalidError:
        return await e.send_file(
            e.chat_id, aki_photo, caption="𓆘𓆘⌔∮ حاول مجددا مره اخرى 𓆘𓆘"
        )
    if e.out:
        await e.delete()


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(b"aki_?(.𓆘)")))
@check_owner
async def daj(e):
    adt = e.pattern_match.group(1).strip().decode("utf-8")
    dt = adt.split("_")
    ch = int(dt[0])
    mid = int(dt[1])
    await e.edit("𓆘𓆘⌔∮ جار التحقق الان انتظر𓆘𓆘")
    try:
        qu = games[ch][mid].start_game(child_mode=True)
    except KeyError:
        return await e.answer("تم إنهاء اللعبة", alert=True)
    bts = [Button.inline(o, f"aka_{adt}_{o}") for o in ["Yes", "No", "Idk"]]
    cts = [Button.inline(o, f"aka_{adt}_{o}") for o in ["Probably", "Probably Not"]]

    bts = [bts, cts]
    await e.edit(f"Q. {qu}", buttons=bts)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(b"aka_?(.𓆘)")))
@check_owner
async def rooks(e):
    mk = e.pattern_match.group(1).decode("utf-8").split("_")
    ch = int(mk[0])
    mid = int(mk[1])
    ans = mk[2]
    try:
        gm = games[ch][mid]
    except KeyError:
        await e.answer("⌔∮ انتهى الوقت !")
        return
    text = gm.answer(ans)
    if gm.progression >= 80:
        gm.win()
        gs = gm.first_guess
        text = "It's " + gs["name"] + "\n " + gs["description"]
        return await e.edit(text, file=gs["absolute_picture_path"])
    bts = [Button.inline(o, f"aka_{ch}_{mid}_{o}") for o in ["Yes", "No", "Idk"]]
    cts = [
        Button.inline(o, f"aka_{ch}_{mid}_{o}") for o in ["Probably", "Probably Not"]
    ]

    bts = [bts, cts]
    await e.edit(text, buttons=bts)


@sbb_b.tgbot.on(InlineQuery)
async def rozak(e):
    query_user_id = e.query.user_id
    query = e.text
    string = query.lower()
    if (
        query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS
    ) and string.startswith("aki"):
        ans = [
            await e.builder.photo(
                aki_photo,
                text=query,
                buttons=[Button.inline("𓅽 ابدا اللعب 𓅽", data=e.text)],
            )
        ]
        await e.answer(ans)
