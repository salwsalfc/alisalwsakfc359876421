import asyncio
import io
import os
import time
import zipfile
from datetime import datetime
from pathlib import Path
from tarfile import is_tarfile
from tarfile import open as tar_open

from telethon import types
from telethon.utils import get_extension

from ..Config import Config
from . import edit_delete, edit_or_reply, progress, sbb_b

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


def zipdir(dirName):
    filePaths = []
    for root, directories, files in os.walk(dirName):
        for filename in files:
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)
    return filePaths


@sbb_b.ar_cmd(pattern="زايب(?:\s|$)([\s\S]𓆘)")
async def zip_file(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(event, "- يجب عليك كتابة مسار الملف لجعله بصيغة zip")
    start = datetime.now()
    if not os.path.exists(Path(input_str)):
        return await edit_or_reply(
            event,
            f"- المسار المكتوب غير صحيح `{input_str}` تأكد من المسار",
        )
    if os.path.isfile(Path(input_str)):
        return await edit_delete(event, "𓆘𓆘- لم يتم تنفيذ العملية بعد𓆘𓆘")
    mone = await edit_or_reply(
        event, "𓆘𓆘- جار تحويل الملف الى الصيغة المطلوبة انتظر قليلا𓆘𓆘"
    )
    filePaths = zipdir(input_str)
    filepath = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY, os.path.basename(Path(input_str))
    )
    zip_file = zipfile.ZipFile(f"{filepath}.zip", "w")
    with zip_file:
        for file in filePaths:
            zip_file.write(file)
    end = datetime.now()
    ms = (end - start).seconds
    await mone.edit(
        f"𓆘𓆘- تم تحويل صيغة الملف في المسار`{input_str}` الى صيغة zip في المسار`{filepath}.zip` في {ms} من الثواني𓆘𓆘"
    )


@sbb_b.ar_cmd(pattern="تار(?:\s|$)([\s\S]𓆘)")
async def tar_file(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(event, "- يجب عليك كتابة مسار الملف لجعله بصيغة tar")
    if not os.path.exists(Path(input_str)):
        return await edit_or_reply(
            event,
            f"- المسار المكتوب غير صحيح `{input_str}` تأكد من المسار",
        )
    if os.path.isfile(Path(input_str)):
        return await edit_delete(event, "𓆘𓆘- لم يتم تنفيذ العملية بعد𓆘𓆘")
    mone = await edit_or_reply(
        event, "𓆘𓆘- جار تحويل الملف الى الصيغة المطلوبة انتظر قليلا𓆘𓆘"
    )
    start = datetime.now()
    filePaths = zipdir(input_str)
    filepath = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY, os.path.basename(Path(input_str))
    )
    destination = f"{filepath}.tar.gz"
    zip_file = tar_open(destination, "w:gz")
    with zip_file:
        for file in filePaths:
            zip_file.add(file)
    end = datetime.now()
    ms = (end - start).seconds
    await mone.edit(
        f"𓆘𓆘- تم صنع ملف للمسار: {input_str} في الصيغة المطلوبة في المسار𓆘𓆘 `{destination}` في {ms} من الثواني"
    )


@sbb_b.ar_cmd(pattern="ان زايب(?:\s|$)([\s\S]𓆘)")
async def zip_file(event):
    if input_str := event.pattern_match.group(1):
        path = Path(input_str)
        if os.path.exists(path):
            start = datetime.now()
            if not zipfile.is_zipfile(path):
                return await edit_delete(
                    event, f"- المسار التالي {path} ليس بصيغة zip لفك ضغطه"
                )

            mone = await edit_or_reply(event, "𓆘𓆘- جار فك الضغط انتظر قليلا𓆘𓆘")
            destination = os.path.join(
                Config.TMP_DOWNLOAD_DIRECTORY,
                os.path.splitext(os.path.basename(path))[0],
            )
            with zipfile.ZipFile(path, "r") as zip_ref:
                zip_ref.extractall(destination)
            end = datetime.now()
            ms = (end - start).seconds
            await mone.edit(
                f"- تم فك الضفط والحفظ في المسار {destination}` \n𓆘𓆘 الوقت المستغرزق :𓆘𓆘 `{ms}` من الثواني"
            )
        else:
            await edit_delete(
                event, f"𓆘𓆘- لم يتم العثور على المسار𓆘𓆘 `{input_str}`", 10
            )
    elif event.reply_to_msg_id:
        start = datetime.now()
        reply = await event.get_reply_message()
        ext = get_extension(reply.document)
        if ext != ".zip":
            return await edit_delete(
                event,
                "𓆘𓆘- يبدو ان الملف الذي قمت بالرد عليه ليس بصيغة zip𓆘𓆘",
            )
        mone = await edit_or_reply(event, "𓆘𓆘- جار فك الضغط انتظر قليلا𓆘𓆘")
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                filename = attr.file_name
        filename = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, filename)
        c_time = time.time()
        try:
            dl = io.FileIO(filename, "a")
            await event.client.fast_download_file(
                location=reply.document,
                out=dl,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
            dl.close()
        except Exception as e:
            return await edit_delete(mone, f"𓆘𓆘خطأ:𓆘𓆘\n__{e}__")
        await mone.edit("𓆘𓆘- تم تحميل الملفات التي تم فك صغطها𓆘𓆘")
        destination = os.path.join(
            Config.TMP_DOWNLOAD_DIRECTORY,
            os.path.splitext(os.path.basename(filename))[0],
        )
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(destination)
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(
            f"𓆘𓆘- تم فك الضغط والحفظ في المسار `{destination}` \n𓆘𓆘الوقت المستغرق :𓆘𓆘 `{ms}` من الثواني"
        )
        os.remove(filename)
    else:
        await edit_delete(
            mone,
            "𓆘𓆘- يجب عليك الرد على ملف بصيغة zip او كتابة مسار الملف",
        )


@sbb_b.ar_cmd(pattern="ان تار(?:\s|$)([\s\S]𓆘)")
async def untar_file(event):
    if input_str := event.pattern_match.group(1):
        path = Path(input_str)
        if os.path.exists(path):
            start = datetime.now()
            if not is_tarfile(path):
                return await edit_delete(
                    event, f"𓆘𓆘- المسار المعطى: {path} ليس بصيغة tar ليتم فكه𓆘𓆘"
                )

            mone = await edit_or_reply(event, "𓆘𓆘- جار فك ضغط الفولدر الملعطى𓆘𓆘")
            destination = os.path.join(
                Config.TMP_DOWNLOAD_DIRECTORY, (os.path.basename(path).split("."))[0]
            )
            if not os.path.exists(destination):
                os.mkdir(destination)
            file = tar_open(path)
            # extracting file
            file.extractall(destination)
            file.close()
            end = datetime.now()
            ms = (end - start).seconds
            await mone.edit(
                f"𓆘𓆘الوقت المستغرق :𓆘𓆘 `{ms}` من الثواني\
                \nجار فك المسار التالي:`{input_str}` وحفظه الى `{destination}`"
            )
        else:
            await edit_delete(
                event, f"𓆘𓆘- لم اتمكن من العثور على المسار `{input_str}`", 10
            )
    elif event.reply_to_msg_id:
        start = datetime.now()
        reply = await event.get_reply_message()
        mone = await edit_or_reply(event, "𓆘𓆘- جار فك الضغط  انتظر قليلا𓆘𓆘")
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                filename = attr.file_name
        filename = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, filename)
        c_time = time.time()
        try:
            dl = io.FileIO(filename, "a")
            await event.client.fast_download_file(
                location=reply.document,
                out=dl,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
            dl.close()
        except Exception as e:
            return await edit_delete(mone, f"𓆘𓆘Error:𓆘𓆘\n__{e}__")
        if not is_tarfile(filename):
            return await edit_delete(
                mone, "𓆘𓆘- يبدو ان الملف الذي تم عمل له رد ليس بصيغة tar"
            )
        await mone.edit("𓆘𓆘- تم بنجاح حفظ الملفات التي تم فك ضغطها𓆘𓆘")
        destination = os.path.join(
            Config.TMP_DOWNLOAD_DIRECTORY, (os.path.basename(filename).split("."))[0]
        )

        if not os.path.exists(destination):
            os.mkdir(destination)
        file = tar_open(filename)
        # استخراج الملفات
        file.extractall(destination)
        file.close()
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(
            f"𓆘𓆘الوقت المستغرق :𓆘𓆘 `{ms}` من الثواني\
                \n𓆘𓆘- تم فك الضغط وحفظ الملفات في المسار𓆘𓆘 `{destination}`"
        )
        os.remove(filename)
    else:
        await edit_delete(
            mone,
            "𓆘𓆘- يجب عليك الرد على ملف بصيغة tar او كتابة مسار الملف",
        )
