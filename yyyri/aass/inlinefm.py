import asyncio
import io
import os
import time
from pathlib import Path

from telethon import Button, types
from telethon.events import CallbackQuery
from telethon.utils import get_attributes

from sbb_b import sbb_b
from sbb_b.Config import Config
from sbb_b.core.decorators import check_owner
from sbb_b.helpers import humanbytes, progress
from sbb_b.helpers.utils import _jmthonutils

CC = []
PATH = []
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


# freaking selector
def add_s(msg, num: int):
    fmsg = ""
    msgs = msg.splitlines()
    leng = len(msgs)
    if num == 0:
        valv = leng - 1
        msgs[valv] = msgs[valv] + " ⭕️"
        for ff in msgs:
            fmsg += f"{ff}\n"
    elif num == leng:
        valv = 1
        msgs[valv] = msgs[valv] + " ⭕️"
        for ff in msgs:
            fmsg += f"{ff}\n"
    else:
        valv = num
        msgs[valv] = msgs[valv] + " ⭕️"
        for ff in msgs:
            fmsg += f"{ff}\n"
    buttons = [
        [
            Button.inline("D", data=f"fmrem_{msgs[valv]}|{valv}"),
            Button.inline("X", data=f"fmcut_{msgs[valv]}|{valv}"),
            Button.inline("C", data=f"fmcopy_{msgs[valv]}|{valv}"),
            Button.inline("V", data=f"fmpaste_{valv}"),
        ],
        [
            Button.inline("⬅️", data="fmback"),
            Button.inline("⬆️", data=f"fmup_{valv}"),
            Button.inline("⬇️", data=f"fmdown_{valv}"),
            Button.inline("➡️", data=f"fmforth_{msgs[valv]}"),
        ],
    ]
    return fmsg, buttons


def get_manager(path, num: int):
    if os.path.isdir(path):
        msg = "المجلدات والملفات `{}` :\n".format(path)
        lists = sorted(os.listdir(path))
        files = ""
        folders = ""
        for contents in sorted(lists):
            zpath = os.path.join(path, contents)
            if not os.path.isdir(zpath):
                size = os.stat(zpath).st_size
                if str(contents).endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += f"🎧`{contents}`\n"
                if str(contents).endswith((".opus")):
                    files += f"🎤`{contents}`\n"
                elif str(contents).endswith(
                    (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                ):
                    files += f"🎬`{contents}`\n"
                elif str(contents).endswith((".zip", ".tar", ".tar.gz", ".rar")):
                    files += f"📚`{contents}`\n"
                elif str(contents).endswith((".py")):
                    files += f"🐍`{contents}`\n"
                elif str(contents).endswith(
                    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")
                ):
                    files += f"🏞`{contents}`\n"
                else:
                    files += f"📔`{contents}`\n"
            else:
                folders += f"📂`{contents}`\n"
        msg = msg + folders + files if files or folders else f"{msg} مسار فارغ"
        PATH.clear()
        PATH.append(path)
        msgs = add_s(msg, int(num))
    else:
        size = os.stat(path).st_size
        msg = "المعلومات حول الملف :\n"
        if str(path).endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎧"
        if str(path).endswith((".opus")):
            mode = "🎤"
        elif str(path).endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎬"
        elif str(path).endswith((".zip", ".tar", ".tar.gz", ".rar")):
            mode = "📚"
        elif str(path).endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
            mode = "🏞"
        elif str(path).endswith((".py")):
            mode = "🐍"
        else:
            mode = "📔"
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"𓆘𓆘الموقع :𓆘𓆘 `{path}`\n"
        msg += f"𓆘𓆘الايقونة :𓆘𓆘 `{mode}`\n"
        msg += f"𓆘𓆘الحجم :𓆘𓆘 `{humanbytes(size)}`\n"
        msg += f"𓆘𓆘اخر تحديث للملف:𓆘𓆘 `{time2}`\n"
        msg += f"𓆘𓆘آخر وقت تم الوصول إليه:𓆘𓆘 `{time3}`"
        buttons = [
            [
                Button.inline("تسمية", data=f"fmrem_File|{num}"),
                Button.inline("ارسال", data="fmsend"),
                Button.inline("X", data=f"fmcut_File|{num}"),
                Button.inline("C", data=f"fmcopy_File{num}"),
            ],
            [
                Button.inline("⬅️", data="fmback"),
                Button.inline("⬆️", data="fmup_File"),
                Button.inline("⬇️", data="fmdown_File"),
                Button.inline("➡️", data="fmforth_File"),
            ],
        ]
        PATH.clear()
        PATH.append(path)
        msgs = (msg, buttons)
    return msgs


# رجوع
@sbb_b.tgbot.on(CallbackQuery(pattern="fmback"))
@check_owner
async def back(event):
    path = PATH[0]
    paths = path.split("/")
    if paths[-1] == "":
        paths.pop()
        paths.pop()
    else:
        paths.pop()
    npath = ""
    for ii in paths:
        npath += f"{ii}/"
    num = 1
    msg, buttons = get_manager(npath, num)
    await asyncio.sleep(1)
    await event.edit(msg, buttons=buttons)


# فوك
@sbb_b.tgbot.on(CallbackQuery(pattern="fmup_(.𓆘)"))
@check_owner
async def up(event):
    num = event.pattern_match.group(1).decode("UTF-8")
    if num == "File":
        await event.answer("هذا ملف يا غبي !", alert=True)
    else:
        num1 = int(num) - 1
        path = PATH[0]
        msg, buttons = get_manager(path, num1)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# تحت
@sbb_b.tgbot.on(CallbackQuery(pattern="fmdown_(.𓆘)"))
@check_owner
async def down(event):
    num = event.pattern_match.group(1).decode("UTF-8")
    if num == "File":
        await event.answer("هذا ملف يا غبي !", alert=True)
    else:
        path = PATH[0]
        num1 = int(num) + 1
        msg, buttons = get_manager(path, num1)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(pattern="fmforth_(.𓆘)"))
@check_owner
async def forth(event):
    npath = event.pattern_match.group(1).decode("UTF-8")
    if npath == "File":
        await event.answer("هذا ملف يا غبي !", alert=True)
    else:
        path = PATH[0]
        npath = npath[2:-4]
        rpath = f"{path}/{npath}"
        num = 1
        msg, buttons = get_manager(rpath, num)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# الحذف
@sbb_b.tgbot.on(CallbackQuery(pattern="fmrem_(.𓆘)"))
@check_owner
async def remove(event):
    fn, num = (event.pattern_match.group(1).decode("UTF-8")).split("|", 1)
    path = PATH[0]
    if fn == "File":
        paths = path.split("/")
        if paths[-1] == "":
            paths.pop()
            paths.pop()
        else:
            paths.pop()
        npath = ""
        for ii in paths:
            npath += f"{ii}/"
        rpath = path
    else:
        n_path = fn[2:-4]
        rpath = f"{path}/{n_path}"
        npath = path
    msg, buttons = get_manager(npath, num)
    await asyncio.sleep(1)
    await event.edit(msg, buttons=buttons)
    await _jmthonutils.runcmd(f"rm -rf '{rpath}'")
    await event.answer(f"{rpath} تم الحذف  بنجاح")


# الارسال
@sbb_b.tgbot.on(CallbackQuery(pattern="fmsend"))
@check_owner
async def send(event):
    path = PATH[0]
    startTime = time.time()
    attributes, mime_type = get_attributes(str(path))
    ul = io.open(Path(path), "rb")
    uploaded = await event.client.fast_upload_file(
        file=ul,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(
                d,
                t,
                event,
                startTime,
                "يتم الرفع",
                file_name=os.path.basename(Path(path)),
            )
        ),
    )
    ul.close()
    media = types.InputMediaUploadedDocument(
        file=uploaded,
        mime_type=mime_type,
        attributes=attributes,
        force_file=False,
        thumb=await event.client.upload_file(thumb_image_path)
        if thumb_image_path
        else None,
    )
    await event.edit("hi", file=media)


# الكص
@sbb_b.tgbot.on(CallbackQuery(pattern="fmcut_(.𓆘)"))
@check_owner
async def cut(event):
    f, n = (event.pattern_match.group(1).decode("UTF-8")).split("|", 1)
    if CC:
        return await event.answer(f"تم لصق {CC[1]} اولا")
    else:
        if f == "File":
            npath = PATH[0]
            paths = npath.split("/")
            if paths[-1] == "":
                paths.pop()
                paths.pop()
            else:
                paths.pop()
            path = ""
            for ii in paths:
                path += f"{ii}/"
            CC.append("cut")
            CC.append(npath)
            await event.answer(f"يتم تغيير مكان {npath} ...")
        else:
            path = PATH[0]
            npath = f[2:-4]
            rpath = f"{path}/{npath}"
            CC.append("cut")
            CC.append(rpath)
            await event.answer(f"يتم التغيير {rpath} ...")
        msg, buttons = get_manager(path, n)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# نسخ
@sbb_b.tgbot.on(CallbackQuery(pattern="fmcopy_(.𓆘)"))
@check_owner
async def copy(event):
    f, n = (event.pattern_match.group(1).decode("UTF-8")).split("|", 1)
    if CC:
        return await event.answer(f"لصق {CC[1]} اولا")
    else:
        if f == "File":
            npath = PATH[0]
            paths = npath.split("/")
            if paths[-1] == "":
                paths.pop()
                paths.pop()
            else:
                paths.pop()
            path = ""
            for ii in paths:
                path += f"{ii}/"
            CC.append("copy")
            CC.append(npath)
            await event.answer(f"يتم النسخ {path} ...")
        else:
            path = PATH[0]
            npath = f[2:-4]
            rpath = f"{path}/{npath}"
            CC.append("copy")
            CC.append(rpath)
            await event.answer(f"يتم النسخ {rpath} ...")
        msg, buttons = get_manager(path, n)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# PASTE
@sbb_b.tgbot.on(CallbackQuery(pattern="fmpaste_(.𓆘)"))
@check_owner
async def paste(event):
    n = event.pattern_match.group(1).decode("UTF-8")
    path = PATH[0]
    if CC:
        if CC[0] == "cut":
            cmd = f"mv '{CC[1]}' '{path}'"
        else:
            cmd = f"cp '{CC[1]}' '{path}'"
        await _jmthonutils.runcmd(cmd)
        msg, buttons = get_manager(path, n)
        await event.edit(msg, buttons=buttons)
        CC.clear
    else:
        await event.answer("لم تقوم بنسخ اي شي لعمل له لصق")
