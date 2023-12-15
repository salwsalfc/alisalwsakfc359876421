import asyncio
import io
import logging
import os
import time
from datetime import datetime
from io import BytesIO
from shutil import copyfile

import fitz
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from pymediainfo import MediaInfo
from telethon import types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.tl.functions.messages import SendMediaRequest
from telethon.utils import get_attributes

from sbb_b import Convert, sbb_b

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, meme_type, progress, thumb_from_audio
from ..helpers.functions import unsavegif
from ..helpers.utils import _format, _jmthonutils, parse_pre, reply_id

if not os.path.isdir("./temp"):
    os.makedirs("./temp")


LOGS = logging.getLogger(__name__)
PATH = os.path.join("./temp", "temp_vid.mp4")

thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


@sbb_b.ar_cmd(pattern="دائري ?((-)?s)?$")
async def video_jmthonfile(event):  # sourcery no-metrics
    reply = await event.get_reply_message()
    args = event.pattern_match.group(1)
    jmthonid = await reply_id(event)
    if not reply or not reply.media:
        return await edit_delete(event, "𓆘𓆘- يجب عليك الرد على وسائط مدعومة𓆘𓆘")
    mediatype = await media_type(reply)
    if mediatype == "Round Video":
        return await edit_delete(
            event,
            "𓆘𓆘- يجب عليك الرد على وسائط فيديو عادي وليس دائري انت غبي تحول من دائري لدائري𓆘𓆘؟؟",
        )
    if mediatype not in ["Photo", "Audio", "Voice", "Gif", "Sticker", "Video"]:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على ميديا من صورة او فيديو الخ𓆘𓆘"
        )
    flag = True
    jmthonevent = await edit_or_reply(event, "- يتم التحويل انتظر قليلا")
    jmthonfile = await reply.download_media(file="./temp/")
    if mediatype in ["Gif", "Video", "Sticker"]:
        if not jmthonfile.endswith((".webp")):
            if jmthonfile.endswith((".tgs")):
                await Convert.to_gif(event, jmthonfile, file="circle.mp4", noedits=True)
                jmthonfile = "./temp/circle.mp4"
            media_info = MediaInfo.parse(jmthonfile)
            aspect_ratio = 1
            for track in media_info.tracks:
                if track.track_type == "Video":
                    aspect_ratio = track.display_aspect_ratio
                    height = track.height
                    width = track.width
            if aspect_ratio != 1:
                crop_by = min(height, width)
                await _jmthonutils.runcmd(
                    f'ffmpeg -i {jmthonfile} -vf "crop={crop_by}:{crop_by}" {PATH}'
                )
            else:
                copyfile(jmthonfile, PATH)
            if str(jmthonfile) != str(PATH):
                os.remove(jmthonfile)
            try:
                jmthonthumb = await reply.download_media(thumb=-1)
            except Exception as e:
                LOGS.error(f"circle - {e}")
    elif mediatype in ["Voice", "Audio"]:
        jmthonthumb = None
        try:
            jmthonthumb = await reply.download_media(thumb=-1)
        except Exception:
            jmthonthumb = os.path.join("./temp", "thumb.jpg")
            await thumb_from_audio(jmthonfile, jmthonthumb)
        if jmthonthumb is not None and not os.path.exists(jmthonthumb):
            jmthonthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, jmthonthumb)
        if (
            jmthonthumb is not None
            and not os.path.exists(jmthonthumb)
            and os.path.exists(thumb_loc)
        ):
            flag = False
            jmthonthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, jmthonthumb)
        if jmthonthumb is not None and os.path.exists(jmthonthumb):
            await _jmthonutils.runcmd(
                f"""ffmpeg -loop 1 -i {jmthonthumb} -i {jmthonfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf \"scale=\'iw-mod (iw,2)\':\'ih-mod(ih,2)\',format=yuv420p\" -shortest -movflags +faststart {PATH}"""
            )
            os.remove(jmthonfile)
        else:
            os.remove(jmthonfile)
            return await edit_delete(
                jmthonevent, "𓆘𓆘- يجب ان يكون المقطع الصوتي يحتوي على خلفية𓆘𓆘", 5
            )
    if mediatype in [
        "Voice",
        "Audio",
        "Gif",
        "Video",
        "Sticker",
    ] and not jmthonfile.endswith((".webp")):
        if os.path.exists(PATH):
            c_time = time.time()
            attributes, mime_type = get_attributes(PATH)
            ul = io.open(PATH, "rb")
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, jmthonevent, c_time, "Uploading....")
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type="video/mp4",
                attributes=[
                    types.DocumentAttributeVideo(
                        duration=0,
                        w=1,
                        h=1,
                        round_message=True,
                        supports_streaming=True,
                    )
                ],
                force_file=False,
                thumb=await event.client.upload_file(jmthonthumb)
                if jmthonthumb
                else None,
            )
            sandy = await event.client.send_file(
                event.chat_id,
                media,
                reply_to=jmthonid,
                video_note=True,
                supports_streaming=True,
            )

            if not args:
                await unsavegif(event, sandy)
            os.remove(PATH)
            if flag:
                os.remove(jmthonthumb)
        await jmthonevent.delete()
        return
    data = reply.photo or reply.media.document
    img = io.BytesIO()
    await event.client.download_file(data, img)
    im = Image.open(img)
    w, h = im.size
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    img.paste(im, (0, 0))
    m = min(w, h)
    img = img.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((10, 10, w - 10, h - 10), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(2))
    img = ImageOps.fit(img, (w, h))
    img.putalpha(mask)
    im = io.BytesIO()
    im.name = "jmthon.webp"
    img.save(im)
    im.seek(0)
    await event.client.send_file(event.chat_id, im, reply_to=jmthonid)
    await jmthonevent.delete()


@sbb_b.ar_cmd(pattern="(لصورة|تحويل صورة)$")
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على فيديو او ملصق او مقطع صوتي لتحويله صورة𓆘𓆘"
        )
    output = await Convert.to_image(
        event,
        reply,
        dirct="./temp",
        file="jmthonconverter.png",
    )
    if output[1] is None:
        return await edit_delete(
            output[0], "𓆘𓆘- يجب الرد على ملصق او فيديو او مقطع صوتي اولا𓆘𓆘"
        )
    await event.client.send_file(event.chat_id, output[1], reply_to=reply_to_id)
    os.remove(output[1])
    await output[0].delete()


@sbb_b.ar_cmd(pattern="(لملصق|تحويل ملصق)$")
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على صورة او ميديا لتحويله الى ملصق𓆘𓆘"
        )
    output = await Convert.to_image(
        event,
        reply,
        dirct="./temp",
        file="itos.png",
    )
    if output[1] is None:
        return await edit_delete(output[0], "𓆘𓆘- يجب ان تقوم بالرد على الميديا اولا𓆘𓆘")
    meme_file = (
        await Convert.to_sticker(event, output[1], file="sticker.webp", noedits=True)
    )[1]
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()


@sbb_b.ar_cmd(pattern="لملف ([\s\S]𓆘)")
async def get(event):
    name = event.text[5:]
    if name is None:
        await edit_or_reply(event, "الاستخدام:  `.لملف` + اسم الملف بالرد على نص")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await edit_or_reply(event, "الاستخدام:  `.لملف` + اسم الملف بالرد على نص")


@sbb_b.ar_cmd(pattern="لكتابة$")
async def get(event):
    reply = await event.get_reply_message()
    mediatype = await media_type(reply)
    if mediatype != "Document":
        return await edit_delete(event, "𓆘𓆘- يجب عليك الرد على ملف لأستخراج النص𓆘𓆘")
    file_loc = await reply.download_media()
    file_content = ""
    try:
        with open(file_loc) as f:
            file_content = f.read().rstrip("\n")
    except UnicodeDecodeError:
        pass
    except Exception as e:
        LOGS.info(e)
    if file_content == "":
        try:
            with fitz.open(file_loc) as doc:
                for page in doc:
                    file_content += page.getText()
        except Exception as e:
            if os.path.exists(file_loc):
                os.remove(file_loc)
            return await edit_delete(event, f"𓆘𓆘خطأ𓆘𓆘\n__{e}__")
    await edit_or_reply(
        event,
        file_content,
        parse_mode=parse_pre,
        aslink=True,
        noformat=True,
        linktext="𓆘𓆘عزيزي المستخدم انت لست مفعل تلجرام بريميوم لذلك لا يمكنني كتابه نصوص الملف برسالة لذلك تم وضعها في الموقع\nالرابط :𓆘𓆘",
    )
    if os.path.exists(file_loc):
        os.remove(file_loc)


@sbb_b.ar_cmd(pattern="الملف لصورة$")
async def on_file_to_photo(event):
    target = await event.get_reply_message()
    try:
        image = target.media.document
    except AttributeError:
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على صورة بشكل ملف لتحويلها الى صورة عادية𓆘𓆘"
        )
    if not image.mime_type.startswith("image/"):
        return await edit_delete(
            event, "𓆘𓆘- يجب عليك الرد على صورة بشكل ملف لتحويلها الى صورة عادية𓆘𓆘"
        )
    if image.mime_type == "image/webp":
        return await edit_delete(event, "𓆘𓆘- للملصقات استخدم امر تحويل الصورة𓆘𓆘")
    if image.size > 10 𓆘 1024 𓆘 1024:
        return
    jmthont = await edit_or_reply(event, "𓆘𓆘- جار التحويل انتظر قليلا𓆘𓆘")
    file = await event.client.download_media(target, file=BytesIO())
    file.seek(0)
    img = await event.client.upload_file(file)
    img.name = "image.png"
    try:
        await event.client(
            SendMediaRequest(
                peer=await event.get_input_chat(),
                media=types.InputMediaUploadedPhoto(img),
                message=target.message,
                entities=target.entities,
                reply_to_msg_id=target.id,
            )
        )
    except PhotoInvalidDimensionsError:
        return
    await jmthont.delete()


@sbb_b.ar_cmd(pattern="(تحويل متحركة|لمتحركة)$")
async def _(event):
    jmthonreply = await event.get_reply_message()
    memetype = await meme_type(jmthonreply)
    if memetype == "Gif":
        return await edit_delete(event, "𓆘𓆘- يبدو انها متحركة بالاصل𓆘𓆘")
    if memetype not in [
        "Round Video",
        "Animated Sticker",
        "Video Sticker",
        "Video",
    ]:
        return await edit_delete(
            event,
            "𓆘𓆘- يجب ان تكون الميديا ملصق متحرك او ملصق فيديو او حتى فيديو لتحويله لمتحركة𓆘𓆘",
        )
    jmthonevent = await edit_or_reply(
        event,
        "𓆘𓆘- جار التحويل الى متحركة قد يأخذ وقت قليل𓆘𓆘",
        parse_mode=_format.parse_pre,
    )
    reply_to_id = await reply_id(event)
    jmthonfile = await event.client.download_media(jmthonreply)
    final = await Convert.to_gif(event, jmthonfile, file="animation.mp4", noedits=True)
    jmthongif = final[1]
    if jmthongif is None:
        return await edit_delete(
            jmthonevent, "𓆘𓆘- لا يمكنني تحويل هذا النوع من الميديا الى متحركة𓆘𓆘"
        )
    sandy = await event.client.send_file(
        event.chat_id,
        jmthongif,
        support_streaming=True,
        force_document=False,
        reply_to=reply_to_id,
    )
    await unsavegif(event, sandy)
    await jmthonevent.delete()
    for files in (jmthongif, jmthonfile):
        if files and os.path.exists(files):
            os.remove(files)


@sbb_b.ar_cmd(pattern="تحويل الى (صوتي|بصمة)")
async def _(event):
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "𓆘𓆘- يجب عليك الرد على الميديا المراد تحويلها𓆘𓆘")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "𓆘𓆘- يجب عليك الرد على الميديا المراد تحويلها𓆘𓆘")
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "𓆘𓆘- جار التحويل انتظر قليلا ...𓆘𓆘")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await event.client.download_media(
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to download")
            ),
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(f"- تم تنزيل الملف : {downloaded_file_name}\nالوقت المستغرق: {ms} من الثواني")
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "بصمة":
            new_required_file_caption = f"voice_{str(round(time.time()))}.opus"
            new_required_file_name = (
                f"{Config.TMP_DOWNLOAD_DIRECTORY}/{new_required_file_caption}"
            )

            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name,
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "صوتي":
            new_required_file_caption = f"mp3_{str(round(time.time()))}.mp3"
            new_required_file_name = (
                f"{Config.TMP_DOWNLOAD_DIRECTORY}/{new_required_file_caption}"
            )

            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name,
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("𓆘𓆘- هذه الصيغة غير مدعومة𓆘𓆘")
            os.remove(downloaded_file_name)
            return
        process = await asyncio.create_subprocess_exec(
            𓆘command_to_run,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            force_document = False
            await event.client.send_file(
                entity=event.chat_id,
                file=new_required_file_name,
                allow_cache=False,
                silent=True,
                force_document=force_document,
                voice_note=voice_note,
                supports_streaming=supports_streaming,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(new_required_file_name)
            await event.delete()

