import base64
import contextlib
import io
import os

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import reply_id
from . import sbb_b, song_download

LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           المتغيرات                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>انتظر يتم العثور على المطلوب</code>"
SONG_NOT_FOUND = "<code>عذرا لم يتم العثور على المطلوب</code>"
SONG_SENDING_STRING = "<code>تم العثور على المطلوب انتظر قليلا</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@sbb_b.ar_cmd(pattern="بحث(320)?(?:\s|$)([\s\S]𓆘)")
async def song(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(
            event,
            "𓆘𓆘يجب عليك اضافة اسم المقطع الصوتي التي تريد تنزيله للامـر ، `.بحث` + العنوان𓆘𓆘",
        )
    razan = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    razanevent = await edit_or_reply(event, "𓆘𓆘⌔∮ جـارِ البحث يرجى الانتظار .  .  .𓆘𓆘")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await razanevent.edit(f"𓆘𓆘عـذراً لـم استطـع ايجـاد𓆘𓆘 {query}")
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_file, razanthumb, title = await song_download(
        video_link, razanevent, quality=q
    )
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"𓆘𓆘العنوان:𓆘𓆘 `{title}`",
        thumb=razanthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await razanevent.delete()
    for files in (razanthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


@sbb_b.ar_cmd(pattern="فيديو(?:\s|$)([\s\S]𓆘)")
async def vsong(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(
            event,
            "𓆘𓆘يجب عليك اضافة اسم المقطع الصوتي التي تريد تنزيله للامـر ، `.فيديو` + العنوان𓆘𓆘",
        )
    razan = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    razanevent = await edit_or_reply(event, "𓆘𓆘⌔∮ جـارِ البحث يرجى الانتظار .  .  .𓆘𓆘")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await razanevent.edit(f"𓆘𓆘عـذراً لـم استطـع ايجـاد𓆘𓆘 {query}")
    with contextlib.suppress(BaseException):
        razan = Get(razan)
        await event.client(razan)
    vsong_file, razanthumb, title = await song_download(
        video_link, razanevent, video=True
    )
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"𓆘𓆘العنوان:𓆘𓆘 `{title}`",
        thumb=razanthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await razanevent.delete()
    for files in (razanthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@sbb_b.ar_cmd(pattern="(ا(ل)?ا(س)?م)(?:\s|$)([\s\S]𓆘)")
async def shazamcmd(event):
    reply = await event.get_reply_message()
    mediatype = await media_type(reply)
    chat = "@DeezerMusicBot"
    delete = False
    flag = event.pattern_match.group(4)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على مقطع صوتي او فيديو لمعرفه العنوان"
        )
    razanevent = await edit_or_reply(event, "𓆘𓆘- يتم حفظ المقطع الصوتي لمعرفة عنوانه𓆘𓆘")
    name = "razan.mp3"
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await edit_delete(
            razanevent, f"𓆘𓆘حدث خطأ اثناء البحث عن الاسم:𓆘𓆘\n__{e}__"
        )

    file = track["images"]["background"]
    title = track["share"]["subject"]
    slink = await yt_search(title)
    if flag == "s":
        deezer = track["hub"]["providers"][1]["actions"][0]["uri"][15:]
        async with event.client.conversation(chat) as conv:
            try:
                purgeflag = await conv.send_message("/start")
            except YouBlockedUserError:
                await sbb_b(unblock("DeezerMusicBot"))
                purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message(deezer)
            await event.client.get_messages(chat)
            song = await event.client.get_messages(chat)
            await song[0].click(0)
            await conv.get_response()
            file = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            delete = True
    await event.client.send_file(
        event.chat_id,
        file,
        caption=f"<b>المقطع الصوتي :</b> <code>{title}</code>\n<b>الرابط : <a href = {slink}/1>اضغط هنا</a></b>",
        reply_to=reply,
        parse_mode="html",
    )
    await razanevent.delete()
    if delete:
        await delete_conv(event, chat, purgeflag)
