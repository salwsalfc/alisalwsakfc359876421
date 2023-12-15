#  =============================
#  == sbb_b - QHR_1  -  RR7PP =
#  =============================


import asyncio
import os
import re

from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import changemymind, deEmojify, kannagen, moditweet, reply_id, trumptweet, tweets

plugin_category = "fun"


@sbb_b.ar_cmd(
    pattern="ترامب(?:\s|$)([\s\S]𓆘)",
    command=("ترامب", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}ترامب <text>",
        "examples": "{tr}trump  is One of the Popular sbb_b",
    },
)
async def nekobot(cat):
    "trump tweet sticker with given custom text_"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "⌯︙يجب ان تكتب نص اولا", 5)
    cate = await edit_or_reply(cat, "⌯︙جار طلب تغريدة من ترامب...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await trumptweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@sbb_b.ar_cmd(
    pattern="مودي(?:\s|$)([\s\S]𓆘)",
    command=("مودي", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}مودي <نص>",
        "examples": "{tr}مودي جمثون الاصلي",
    },
)
async def nekobot(cat):
    "modi tweet sticker with given custom text"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "𓆘𓆘⌯︙يجـب كـتابة نـص اولا", 5)
    cate = await edit_or_reply(cat, "⌯︙جاري طلب تغريدة من مودي...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await moditweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@sbb_b.ar_cmd(
    pattern="بنر(?:\s|$)([\s\S]𓆘)",
    command=("بنر", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}غير عقلي <text>",
        "examples": "{tr}غير عقلي Catsbb_b is One of the Popular sbb_b",
    },
)
async def nekobot(cat):
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "⌯︙اعـطيني نص اولا", 5)
    cate = await edit_or_reply(cat, "⌯︙يتـم عـمل البـنر انتـظر...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await changemymind(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@sbb_b.ar_cmd(
    pattern="كانا(?:\s|$)([\s\S]𓆘)",
    command=("كانا", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}كانا text",
        "examples": "{tr}kanna  is One of the Popular sbb_b",
    },
)
async def nekobot(cat):
    "kanna chan sticker with given custom text"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cat, "⌯︙اوني شان ما ذا تريد ان اكتب", 5)
    cate = await edit_or_reply(cat, "⌯︙كانا تشان تكتب نصك...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await kannagen(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@sbb_b.ar_cmd(
    pattern="تويت(?:\s|$)([\s\S]𓆘)",
    command=("تويت", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}تويت <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; is One of the Popular sbb_b",
    },
)
async def nekobot(cat):
    "The desired person tweet sticker with given custom text"
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)

    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                cat,
                "⌯︙𓆘𓆘يجـب كتـابة الامـر بشكـل صحـيح𓆘𓆘\n `.تويت المعرف ; النص` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            cat,
            "⌯︙𓆘𓆘يجـب كتـابة الامـر بشكـل صحـيح𓆘𓆘\n`.تويت المعرف ; النص`",
            5,
        )
        return
    cate = await edit_or_reply(cat, f"⌯︙جار الطلب من {username} للتغريد...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await tweets(text, username)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)
