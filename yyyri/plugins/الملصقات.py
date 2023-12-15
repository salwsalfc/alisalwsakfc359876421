import asyncio
import base64
import contextlib
import io
import math
import os
import random
import re
import string
import urllib.request

import emoji as jmthonemoji
from PIL import Image
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputStickerSetID,
)

from sbb_b import Convert, sbb_b

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import crop_and_divide
from ..helpers.tools import media_type, meme_type
from ..sql_helper.globals import gvarstatus

combot_stickers_url = "https://combot.org/telegram/stickers?q="

EMOJI_SEN = [
    "Можно отправить несколько смайлов в одном сообщении, однако мы рекомендуем использовать не больше одного или двух на каждый стикер.",
    "يمكنك إرسال قائمة بعدة رموز في رسالة واحدة، لكن أنصحك بعدم إرسال أكثر من رمزين للملصق الواحد.",
    "You can list several emoji in one message, but I recommend using no more than two per sticker",
    "Du kannst auch mehrere Emoji eingeben, ich empfehle dir aber nicht mehr als zwei pro Sticker zu benutzen.",
    "Você pode listar vários emojis em uma mensagem, mas recomendo não usar mais do que dois por cada sticker.",
    "Puoi elencare diverse emoji in un singolo messaggio, ma ti consiglio di non usarne più di due per sticker.",
    "emoji",
]

KANGING_STR = "𓆘𓆘▿∲ جار نسخ الملصق الان انتظر قليلا𓆘𓆘"


def verify_cond(jmthonarray, text):
    return any(i in text for i in jmthonarray)


def pack_name(userid, pack, is_anim, is_video):
    if is_anim:
        return f"jmthon_{userid}_{pack}_anim"
    if is_video:
        return f"jmthon_{userid}_{pack}_vid"
    return f"jmthon_{userid}_{pack}"


def char_is_emoji(character):
    return character in jmthonemoji.UNICODE_EMOJI["en"]


def pack_nick(username, pack, is_anim, is_video):
    if gvarstatus("CUSTOM_STICKER_PACKNAME"):
        if is_anim:
            return f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} Vol.{pack} (Animated)"
        if is_video:
            return f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} Vol. {pack} (Video)"
        return f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} Vol.{pack}"

    if is_anim:
        return f"@{username} Vol.{pack} (Animated)"
    if is_video:
        return f"@{username} Vol. {pack} (Video)"
    return f"@{username} Vol.{pack}"


async def delpack(jmthonevent, conv, args, packname):
    try:
        await conv.send_message("/delpack")
    except YouBlockedUserError:
        await sbb_b(unblock("stickers"))
        await conv.send_message("/delpack")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packname)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message("Yes, I am totally sure.")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)


async def resize_photo(photo):
    """Resize the given photo to 512x512"""
    image = Image.open(photo)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 𓆘 scale
        else:
            scale = 512 / size2
            size1new = size1 𓆘 scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        maxsize = (512, 512)
        image.thumbnail(maxsize)
    return image


async def newpacksticker(
    jmthonevent,
    conv,
    cmd,
    args,
    pack,
    packnick,
    is_video,
    emoji,
    packname,
    is_anim,
    stfile,
    otherpack=False,
    pkang=False,
):
    try:
        await conv.send_message(cmd)
    except YouBlockedUserError:
        await sbb_b(unblock("stickers"))
        await conv.send_message(cmd)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packnick)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if is_video:
        await conv.send_file("animate.webm")
    elif is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        os.remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    if not verify_cond(EMOJI_SEN, rsp.text):
        await jmthonevent.edit(
            f"𓆘𓆘▿∲ فشل في اذافه هذه الحزمة عليك الاضافة يدويا من بوت الملصقات𓆘𓆘\n𓆘𓆘خطأ :𓆘𓆘{rsp.text}"
        )
        if not pkang:
            return None, None, None
        return None, None
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/publish")
    if is_anim:
        await conv.get_response()
        await conv.send_message(f"<{packnick}>")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message("/skip")
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message(packname)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return otherpack, packname, emoji
    return pack, packname


async def add_to_pack(
    jmthonevent,
    conv,
    args,
    packname,
    pack,
    userid,
    username,
    is_video,
    is_anim,
    stfile,
    emoji,
    cmd,
    pkang=False,
):  # sourcery skip: low-code-quality
    try:
        await conv.send_message("/addsticker")
    except YouBlockedUserError:
        await sbb_b(unblock("stickers"))
        await conv.send_message("/addsticker")
    vtry = True if is_video else None
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packname)
    x = await conv.get_response()
    while ("50" in x.message) or ("120" in x.message) or vtry:
        if vtry:
            await conv.send_file("animate.webm")
            x = await conv.get_response()
            if "50 video stickers" in x.message:
                await conv.send_message("/addsticker")
            else:
                vtry = None
                break
        try:
            val = int(pack)
            pack = val + 1
        except ValueError:
            pack = 1
        packname = pack_name(userid, pack, is_anim, is_video)
        packnick = pack_nick(username, pack, is_anim, is_video)
        await jmthonevent.edit(
            f"𓆘𓆘- تم التحويل الى الحزمة {pack} بسبب امتلاء الحزمة السابقة𓆘𓆘"
        )
        await conv.send_message(packname)
        x = await conv.get_response()
        if x.message == "Invalid set selected.":
            return await newpacksticker(
                jmthonevent,
                conv,
                cmd,
                args,
                pack,
                packnick,
                is_video,
                emoji,
                packname,
                is_anim,
                stfile,
                otherpack=True,
                pkang=pkang,
            )
    if is_video:
        os.remove("animate.webm")
        rsp = x
    elif is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        os.remove("AnimatedSticker.tgs")
        rsp = await conv.get_response()
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
        rsp = await conv.get_response()
    if not verify_cond(EMOJI_SEN, rsp.message):
        await jmthonevent.edit(
            f"𓆘𓆘- فشل في اذافه هذه الحزمة عليك الاضافة يدويا من بوت الملصقات𓆘𓆘\n𓆘𓆘خطأ :𓆘𓆘{rsp.message}"
        )
        if not pkang:
            return None, None
        return None, None
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/done")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return packname, emoji
    return pack, packname


@sbb_b.ar_cmd(pattern="ملصق(?:\s|$)([\s\S]𓆘)")
async def kang(args):
    photo = None
    emojibypass = False
    is_anim = False
    is_video = False
    emoji = None
    message = await args.get_reply_message()
    user = await args.client.get_me()
    if not user.username:
        try:
            user.first_name.encode("utf-8").decode("ascii")
            username = user.first_name
        except UnicodeDecodeError:
            username = f"jmthon_{user.id}"
    else:
        username = user.username
    userid = user.id
    if message and message.media:
        memetype = await meme_type(message)
        if memetype == "Photo":
            jmthonevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            photo = await args.client.download_media(message.photo, photo)
        elif memetype == "Static Sticker":
            jmthonevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            await args.client.download_media(message.media.document, photo)
            if message.media.document.attributes[1].alt:
                emoji = message.media.document.attributes[1].alt
                emojibypass = True
        elif memetype == "Animated Sticker":
            jmthonevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            await args.client.download_media(
                message.media.document, "AnimatedSticker.tgs"
            )
            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
                    emojibypass = True
            is_anim = True
            photo = 1
        elif memetype in ["Video", "Gif", "Video Sticker"]:
            emojibypass = False
            is_video = True
            photo = 1
            if memetype == "Video Sticker":
                attributes = message.media.document.attributes
                for attribute in attributes:
                    if isinstance(attribute, DocumentAttributeSticker):
                        if message.media.document.size > 261120:
                            jmthonevent = await edit_or_reply(
                                args, "𓆘𓆘- جار التحويل الى ملصق متحرك𓆘𓆘"
                            )
                            sticker = (
                                await Convert.to_webm(
                                    args,
                                    message,
                                    dirct="./",
                                    file="animate.webm",
                                    noedits=True,
                                )
                            )[1]
                            await edit_or_reply(
                                jmthonevent, f"`{random.choice(KANGING_STR)}`"
                            )
                        else:
                            jmthonevent = await edit_or_reply(
                                args, f"`{random.choice(KANGING_STR)}`"
                            )
                            sticker = await args.client.download_media(
                                message.media.document, "animate.webm"
                            )
                        emoji = attribute.alt
                        emojibypass = True
            else:
                jmthonevent = await edit_or_reply(
                    args, "𓆘𓆘- جار التحويل الى ملصق متحرك𓆘𓆘"
                )
                sticker = (
                    await Convert.to_webm(
                        args, message, dirct="./", file="animate.webm", noedits=True
                    )
                )[1]
                await edit_or_reply(jmthonevent, f"`{random.choice(KANGING_STR)}`")
        else:
            await edit_delete(args, "صيغة هذا الملف غير مدعومة")
            return
    else:
        await edit_delete(args, "𓆘𓆘- لا يمكنني نسخ هذا الملصق𓆘𓆘")
        return
    if photo:
        splat = ("".join(args.text.split(maxsplit=1)[1:])).split()
        emoji = emoji if emojibypass else "❤️"
        pack = 1
        if len(splat) == 2:
            if char_is_emoji(splat[0][0]):
                if char_is_emoji(splat[1][0]):
                    return await jmthonevent.edit("𓆘𓆘- عليك التأكد من اوامر الملصقات𓆘𓆘")
                pack = splat[1]  # User sent both
                emoji = splat[0]
            elif char_is_emoji(splat[1][0]):
                pack = splat[0]  # User sent both
                emoji = splat[1]
            else:
                return await jmthonevent.edit("𓆘𓆘- عليك التأكد من اوامر الملصقات𓆘𓆘")
        elif len(splat) == 1:
            if char_is_emoji(splat[0][0]):
                emoji = splat[0]
            else:
                pack = splat[0]
        packname = pack_name(userid, pack, is_anim, is_video)
        packnick = pack_nick(username, pack, is_anim, is_video)
        cmd = "/newpack"
        stfile = io.BytesIO()
        if is_video:
            cmd = "/newvideo"
        elif is_anim:
            cmd = "/newanimated"
        else:
            image = await resize_photo(photo)
            stfile.name = "sticker.png"
            image.save(stfile, "PNG")
        response = urllib.request.urlopen(
            urllib.request.Request(f"http://t.me/addstickers/{packname}")
        )
        htmlstr = response.read().decode("utf8").split("\n")
        if (
            "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
            not in htmlstr
        ):
            async with args.client.conversation("@Stickers") as conv:
                packname, emoji = await add_to_pack(
                    jmthonevent,
                    conv,
                    args,
                    packname,
                    pack,
                    userid,
                    username,
                    is_video,
                    is_anim,
                    stfile,
                    emoji,
                    cmd,
                )
            if packname is None:
                return
            await edit_delete(
                jmthonevent,
                f"𓆘𓆘- تم بنجاح نسخ الملصق\
                    \nهذه هي الحزمة الخاصة بك𓆘𓆘 [اضغط هنا](t.me/addstickers/{packname}) 𓆘𓆘والسمايل لهذا الملصق هو {emoji}𓆘𓆘",
                parse_mode="md",
                time=10,
            )
        else:
            await jmthonevent.edit("𓆘𓆘- جار جلب حزمة ثانية انتظر قليلا𓆘𓆘")
            async with args.client.conversation("@Stickers") as conv:
                otherpack, packname, emoji = await newpacksticker(
                    jmthonevent,
                    conv,
                    cmd,
                    args,
                    pack,
                    packnick,
                    is_video,
                    emoji,
                    packname,
                    is_anim,
                    stfile,
                )
            if is_video and os.path.exists(sticker):
                os.remove(sticker)
            if otherpack is None:
                return
            if otherpack:
                await edit_delete(
                    jmthonevent,
                    f"𓆘𓆘- تم النسخ في حزمة ثانية \
                    \nهذه هي الحزمة الجديدة𓆘𓆘[اضغط هنا](t.me/addstickers/{packname}) 𓆘𓆘والسمايل لهذا الملصق هو {emoji}𓆘𓆘",
                    parse_mode="md",
                    time=10,
                )
            else:
                await edit_delete(
                    jmthonevent,
                    f"𓆘𓆘- تم بنجاح نسخ الملصق\
                    \nهذه هي الحزمة الخاصة بك𓆘𓆘 [اضغط هنا](t.me/addstickers/{packname}) 𓆘𓆘والسمايل لهذا الملصق هو {emoji}𓆘𓆘",
                    parse_mode="md",
                    time=10,
                )


@sbb_b.ar_cmd(pattern="حزمة(?:\s|$)([\s\S]𓆘)")
async def pack_kang(event):
    user = await event.client.get_me()
    if user.username:
        username = user.username
    else:
        try:
            user.first_name.encode("utf-8").decode("ascii")
            username = user.first_name
        except UnicodeDecodeError:
            username = f"jmthon_{user.id}"
    photo = None
    userid = user.id
    is_anim = False
    is_video = False
    emoji = None
    reply = await event.get_reply_message()
    jmthon = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    if (
        not reply
        or await media_type(reply) is None
        or await media_type(reply) != "Sticker"
    ):
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على الملصق لنسخ الحزمة الخاصة بالملصق𓆘𓆘"
        )
    try:
        stickerset_attr = reply.document.attributes[1]
        jmthonevent = await edit_or_reply(
            event, "- جار التعرف على بيانات الملصق يرجى الانتظار"
        )
    except BaseException:
        return await edit_delete(event, "- يجب عليك الرد على ملصق اولا", 5)
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                ),
                hash=0,
            )
        )
    except Exception:
        return await edit_delete(
            jmthonevent,
            "𓆘𓆘- يجب عليك الرد على ملصق موجود في حزمة اولا𓆘𓆘",
        )
    kangst = 1
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            ),
            hash=0,
        )
    )
    noofst = get_stickerset.set.count
    blablapacks = []
    blablapacknames = []
    pack = None
    for message in reqd_sticker_set.documents:
        if "image" in message.mime_type.split("/"):
            await edit_or_reply(
                jmthonevent,
                f"𓆘𓆘- جار نسخ هذه الحزمة العملية : : {kangst}/{noofst}𓆘𓆘",
            )
            photo = io.BytesIO()
            await event.client.download_media(message, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.attributes
            ):
                emoji = message.attributes[1].alt
        elif "tgsticker" in message.mime_type:
            await edit_or_reply(
                jmthonevent,
                f"𓆘𓆘- جار نسخ هذه الحزمة العملية : : {kangst}/{noofst}𓆘𓆘",
            )
            await event.client.download_media(message, "AnimatedSticker.tgs")
            attributes = message.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
            is_anim = True
            photo = 1
        elif "video/webm" in message.mime_type:
            await edit_or_reply(
                jmthonevent,
                f"𓆘𓆘- جار نسخ هذه الحزمة العملية : : {kangst}/{noofst}𓆘𓆘",
            )
            if message.size > 261120:
                await Convert.to_webm(
                    event, message, dirct="./", file="animate.webm", noedits=True
                )
            else:
                await event.client.download_media(message, "animate.webm")
            attributes = message.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
            is_video = True
            photo = 1
        else:
            await edit_delete(jmthonevent, "- هذه الصيغة غير صالحة")
            return
        if photo:
            splat = ("".join(event.text.split(maxsplit=1)[1:])).split()
            emoji = emoji or "❤️"
            if pack is None:
                pack = 1
                if len(splat) == 1:
                    pack = splat[0]
                elif len(splat) > 1:
                    return await edit_delete(
                        jmthonevent,
                        "𓆘𓆘- عذرا تسلسل الحزمة غير صحيح يجب عليك وضع التسلسل بشكل صحيح𓆘𓆘",
                    )
            with contextlib.suppress(BaseException):
                jmthon = Get(jmthon)
                await event.client(jmthon)
            packnick = pack_nick(username, pack, is_anim, is_video)
            packname = pack_name(userid, pack, is_anim, is_video)
            cmd = "/newpack"
            stfile = io.BytesIO()
            if is_video:
                cmd = "/newvideo"
            elif is_anim:
                cmd = "/newanimated"
            else:
                image = await resize_photo(photo)
                stfile.name = "sticker.png"
                image.save(stfile, "PNG")
            response = urllib.request.urlopen(
                urllib.request.Request(f"http://t.me/addstickers/{packname}")
            )
            htmlstr = response.read().decode("utf8").split("\n")
            if (
                "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
                in htmlstr
            ):
                async with event.client.conversation("@Stickers") as conv:
                    pack, jmthonpackname = await newpacksticker(
                        jmthonevent,
                        conv,
                        cmd,
                        event,
                        pack,
                        packnick,
                        is_video,
                        emoji,
                        packname,
                        is_anim,
                        stfile,
                        pkang=True,
                    )
            else:
                async with event.client.conversation("@Stickers") as conv:
                    pack, jmthonpackname = await add_to_pack(
                        jmthonevent,
                        conv,
                        event,
                        packname,
                        pack,
                        userid,
                        username,
                        is_video,
                        is_anim,
                        stfile,
                        emoji,
                        cmd,
                        pkang=True,
                    )
            if jmthonpackname is None:
                return
            if jmthonpackname not in blablapacks:
                blablapacks.append(jmthonpackname)
                blablapacknames.append(pack)
        kangst += 1
        await asyncio.sleep(2)
    result = "𓆘𓆘- جار نسخ حزمة هذا الملصق في حزمة الملصق التالي:𓆘𓆘\n"
    for i in enumerate(blablapacks):
        result += (
            f"  •  [pack {blablapacknames[i[0]]}](t.me/addstickers/{blablapacks[i[0]]})"
        )
    await jmthonevent.edit(result)


@sbb_b.ar_cmd(pattern="فاس$")
async def pussyjmthon(event):
    message = await event.get_reply_message()
    user = await event.client.get_me()
    userid = user.id
    if not (message and message.media):
        return await edit_delete(event, "𓆘𓆘- عذرا لا يمكنني تحويل هذه الصيغة𓆘")
    memetype = await meme_type(message)
    if memetype not in ["Video", "Gif"]:
        return await edit_delete(event, "𓆘𓆘- يجب عليك الرد على فيديو او متحركة اولا𓆘𓆘")
    sticker = await Convert.to_webm(
        event,
        message,
        dirct="./",
        file="animate.webm",
    )
    await edit_or_reply(sticker[0], f"`{random.choice(KANGING_STR)}`")
    packname = f"jmthon_{userid}_temp_pack"
    response = urllib.request.urlopen(
        urllib.request.Request(f"http://t.me/addstickers/{packname}")
    )
    htmlstr = response.read().decode("utf8").split("\n")
    if (
        "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
        not in htmlstr
    ):
        async with event.client.conversation("@Stickers") as xconv:
            await delpack(
                sticker[0],
                xconv,
                event,
                packname,
            )
    await edit_or_reply(sticker[0], "𓆘𓆘- انتظر قليلا جار صنع الملصق𓆘𓆘")
    async with event.client.conversation("@Stickers") as conv:
        otherpack, packname, emoji = await newpacksticker(
            sticker[0],
            conv,
            "/newvideo",
            event,
            1,
            "jmthon",
            True,
            "❤️",
            packname,
            False,
            io.BytesIO(),
        )
    if otherpack is None:
        return
    await sticker[0].delete()
    await event.client.send_file(
        event.chat_id,
        sticker[1],
        force_document=True,
        caption=f"𓆘𓆘[معاينة الملصق](t.me/addstickers/{packname})𓆘𓆘\n𓆘𓆘سيتم حذفه عند التحويل مرة ثانية𓆘𓆘",
        reply_to=message,
    )
    if os.path.exists(sticker[1]):
        os.remove(sticker[1])


@sbb_b.ar_cmd(pattern="تحويل بملصق(?:\s|$)([\s\S]𓆘)")
async def pic2packcmd(event):
    reply = await event.get_reply_message()
    mediatype = await media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على ملصق او صورة لنقلهم في حزمة𓆘𓆘"
        )
    if (
        mediatype == "Sticker"
        and reply.document.mime_type == "applijmthonion/x-tgsticker"
    ):
        return await edit_delete(
            event,
            "𓆘𓆘- يجب عليك الرد على ملصق او صورة مع اسم الحزمة لنقلهم في حزمة لا تدعم الملصقات المتحركة𓆘𓆘",
        )
    args = event.pattern_match.group(1)
    if not args:
        return await edit_delete(
            event,
            "𓆘𓆘- يجب عليك تحديد اسم الحزمة عبر استخدام امر  .معلومات_ألملصق  لمعرفة اسم الحزمة𓆘𓆘",
        )
    jmthonevent = await edit_or_reply(event, "𓆘𓆘- جار التحويل الان انتظر قليلا𓆘𓆘")
    try:
        emoji = (re.findall(r"-e[\U00010000-\U0010ffff]+", args))[0]
        args = args.replace(emoji, "")
        emoji = emoji.replace("-e", "")
    except Exception:
        emoji = "▫️"
    chat = "@Stickers"
    name = "jmthon_" + "".join(
        random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
        for _ in range(16)
    )
    image = await Convert.to_image(
        jmthonevent, reply, dirct="./temp", file="stickers.png", noedits=True
    )
    if image[1] is None:
        return await edit_delete(
            image[0], "𓆘𓆘- غير قادر على استخراج الصورة من هذه الرسالة𓆘𓆘"
        )
    image = Image.open(image[1])
    w, h = image.size
    www = max(w, h)
    img = Image.new("RGBA", (www, www), (0, 0, 0, 0))
    img.paste(image, ((www - w) // 2, 0))
    newimg = img.resize((100, 100))
    new_img = io.BytesIO()
    new_img.name = f"{name}.png"
    images = await crop_and_divide(img)
    newimg.save(new_img)
    new_img.seek(0)
    jmthonevent = await event.edit("𓆘𓆘- جار صنع حزمة انتظر قليلا𓆘𓆘")
    async with event.client.conversation(chat) as conv:
        i = 0
        try:
            await event.client.send_message(chat, "/cancel")
        except YouBlockedUserError:
            await sbb_b(unblock("stickers"))
            await event.client.send_message(chat, "/cancel")
        await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
        await event.client.send_message(chat, "/newpack")
        await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
        await event.client.send_message(chat, args)
        await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
        for im in images:
            img = io.BytesIO(im)
            img.name = f"{name}.png"
            img.seek(0)
            await event.client.send_file(chat, img, force_document=True)
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.send_message(chat, emoji)
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.send_read_acknowledge(conv.chat_id)
            await asyncio.sleep(1)
            i += 1
            await jmthonevent.edit(
                f"𓆘𓆘- جار صنع حزمة انتظر قليلا𓆘𓆘\nالعملية: {i}/{len(images)}__"
            )
        await event.client.send_message(chat, "/publish")
        await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
        await event.client.send_file(chat, new_img, force_document=True)
        await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
        await event.client.send_message(chat, name)
        ending = await conv.wait_event(
            events.NewMessage(incoming=True, from_users=chat)
        )
        await event.client.send_read_acknowledge(conv.chat_id)
        for packname in ending.raw_text.split():
            stick_pack_name = packname
            if stick_pack_name.startswith("https://t.me/"):
                break
        await jmthonevent.edit(
            f"𓆘𓆘- تم بنجاح صنع حزمة للميديا التالية :𓆘𓆘 [{args}]({stick_pack_name})"
        )


@sbb_b.ar_cmd(pattern="معلومات_ألملصق$")
async def get_pack_info(event):
    if not event.is_reply:
        return await edit_delete(event, "يجب عليك الرد على ملصق اولا", 5)
    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على ملصق اولا لمعرفة معلوماته𓆘𓆘", 5
        )
    try:
        stickerset_attr = rep_msg.document.attributes[1]
        jmthonevent = await edit_or_reply(
            event, "𓆘𓆘- جار التعرف على المعلومات انتظر قليلا𓆘𓆘"
        )
    except BaseException:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على ملصق اولا لمعرفة معلوماته𓆘𓆘", 5
        )
    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        return await jmthonevent.edit(
            "𓆘𓆘- يجب عليك الرد على ملصق اولا لمعرفة معلوماته𓆘𓆘"
        )
    get_stickerset = await event.client(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash,
            ),
            hash=0,
        )
    )
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    OUTPUT = (
        f"𓆘𓆘عنوان الملصق :𓆘𓆘 `{get_stickerset.set.title}\n`"
        f"𓆘𓆘الاسم القصير:𓆘𓆘 `{get_stickerset.set.short_name}`\n"
        f"𓆘𓆘الرسمي:𓆘𓆘 `{get_stickerset.set.official}`\n"
        f"𓆘𓆘الارشيف:𓆘𓆘 `{get_stickerset.set.archived}`\n"
        f"𓆘𓆘الملصقات في الحزمة:𓆘𓆘 `{get_stickerset.set.count}`\n"
        f"𓆘𓆘التعابير في الملصق:𓆘𓆘\n{' '.join(pack_emojis)}"
    )
    await jmthonevent.edit(OUTPUT)
