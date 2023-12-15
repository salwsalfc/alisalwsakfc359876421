import os
from pathlib import Path

from ..Config import Config
from ..core import CMD_INFO, PLG_INFO
from ..utils import load_module, remove_plugin
from . import CMD_HELP, CMD_LIST, SUDO_LIST, edit_delete, edit_or_reply, sbb_b

DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


def plug_checker(plugin):
    plug_path = f"./sbb_b/plugins/{plugin}.py"
    if not os.path.exists(plug_path):
        plug_path = f"./xtraplugins/{plugin}.py"
    return plug_path


@sbb_b.ar_cmd(pattern="تنصيب$")
async def install(event):
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "sbb_b/plugins/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_delete(
                    event,
                    f"𓆘𓆘▿∲ تم بنجاح تثبيت الملف: `{os.path.basename(downloaded_file_name)}`",
                    10,
                )
            else:
                os.remove(downloaded_file_name)
                await edit_delete(
                    event, "𓆘𓆘▿∲ عذرا اسم هذا الملف بالاصل موجود في السورس𓆘𓆘", 10
                )
        except Exception as e:
            await edit_delete(event, f"𓆘𓆘خطأ:𓆘𓆘\n`{e}`", 10)
            os.remove(downloaded_file_name)


@sbb_b.ar_cmd(pattern="الغاء تنصيب ([\s\S]𓆘)")
async def unload(event):
    shortname = event.pattern_match.group(1)
    path = plug_checker(shortname)
    if not os.path.exists(path):
        return await edit_delete(
            event, f"اسم الملف الذي كتبته غير صحيح لا يوجد المسار : {path}"
        )
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"{shortname} تم بنجاح الغاء تثبيته")
    except Exception as e:
        await edit_or_reply(event, f"تم بنجاح تثبيت الملف : {shortname}\n{e}")
    if shortname in PLG_INFO:
        for cmd in PLG_INFO[shortname]:
            CMD_INFO.pop(cmd)
        PLG_INFO.pop(shortname)
