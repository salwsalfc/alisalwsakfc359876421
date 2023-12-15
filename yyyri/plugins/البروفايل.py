import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from sbb_b import sbb_b

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply

LOGS = logging.getLogger(__name__)


INVALID_MEDIA = "⌔∮ امتداد الصورة غير صالح."
PP_CHANGED = "⌔∮ تم تغيير صورة الملف الشخصي بنجاح."
PP_TOO_SMOL = "⌔∮ هذه الصورة صغيرة جدًا ، استخدم صورة أكبر."
PP_ERROR = "⌔∮ حدث فشل أثناء معالجة الصورة."
BIO_SUCCESS = "⌔∮ تم تغيير البايو بنجاح."
NAME_OK = "⌔∮ تم تغيير اسمك بنجاح."
USERNAME_SUCCESS = "⌔∮ تم تغيير اسم المستخدم الخاص بك بنجاح."
USERNAME_TAKEN = "⌔∮ أسم المستخدم مأخوذ مسبقا."


@sbb_b.ar_cmd(pattern="وضع بايو ([\s\S]𓆘)")
async def _(event):
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "𓆘𓆘- تم بنجاح تغيير البايو او النبذة𓆘𓆘")
    except Exception as e:
        await edit_or_reply(event, f"𓆘𓆘خطأ:𓆘𓆘\n`{e}`")


@sbb_b.ar_cmd(pattern="وضع اسم ([\s\S]𓆘)")
async def _(event):
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split(";", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await edit_delete(event, "𓆘𓆘- تم بنجاح تغيير الاسم𓆘𓆘")
    except Exception as e:
        await edit_or_reply(event, f"𓆘𓆘خطأ:𓆘𓆘\n`{e}`")


@sbb_b.ar_cmd(pattern="وضع صورة$")
async def _(event):
    reply_message = await event.get_reply_message()
    jmthonevent = await edit_or_reply(
        event, "𓆘𓆘- جار تحميل الصورة الى قاعدة البيانات انتظر قليلا𓆘𓆘"
    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY
        )
    except Exception as e:
        await jmthonevent.edit(str(e))
    else:
        if photo:
            await jmthonevent.edit("𓆘𓆘- جار الرفع على اتلجرام انتظر قليلا𓆘𓆘")
            if photo.endswith((".mp4", ".MP4")):
                size = os.stat(photo).st_size
                if size > 2097152:
                    await jmthonevent.edit("𓆘𓆘- يجب ان يكون الحجم اقل من 2 ميغا𓆘𓆘")
                    os.remove(photo)
                    return
                jmthonpic = None
                jmthonvideo = await event.client.upload_file(photo)
            else:
                jmthonpic = await event.client.upload_file(photo)
                jmthonvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(
                        file=jmthonpic, video=jmthonvideo, video_start_ts=0.01
                    )
                )
            except Exception as e:
                await jmthonevent.edit(f"𓆘𓆘خطا:𓆘𓆘\n`{e}`")
            else:
                await edit_or_reply(jmthonevent, "𓆘𓆘- تم بنجاح تحديث صورة الحساب𓆘𓆘")
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))


@sbb_b.ar_cmd(pattern="وضع يوزر ([\s\S]𓆘)")
async def update_username(event):
    newusername = event.pattern_match.group(1)
    try:
        await event.client(UpdateUsernameRequest(newusername))
        await edit_delete(event, USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await edit_or_reply(event, USERNAME_TAKEN)
    except Exception as e:
        await edit_or_reply(event, f"𓆘𓆘خطا:𓆘𓆘\n`{e}`")


@sbb_b.ar_cmd(pattern="حسابي$")
async def count(event):
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    jmthonevent = await edit_or_reply(event, "𓆘𓆘- جار التعداد انتظر قليلا𓆘𓆘")
    dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            LOGS.info(d)

    result += f"المعرف:\t𓆘𓆘{u}𓆘𓆘\n"
    result += f"الكروب:\t𓆘𓆘{g}𓆘𓆘\n"
    result += f"المجموعة الخارقة:\t𓆘𓆘{c}𓆘𓆘\n"
    result += f"القنوات:\t𓆘𓆘{bc}𓆘𓆘\n"
    result += f"البوتات:\t𓆘𓆘{b}𓆘𓆘"

    await jmthonevent.edit(result)


@sbb_b.ar_cmd(pattern="ازالة الصورة ?([\s\S]𓆘)")
async def remove_profilepic(delpfp):
    group = delpfp.text[8:]
    if group == "جميعها":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.sender_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [
        InputPhoto(
            id=sep.id,
            access_hash=sep.access_hash,
            file_reference=sep.file_reference,
        )
        for sep in pfplist.photos
    ]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await edit_delete(delpfp, f"𓆘𓆘- تم بنجاح حذف {len(input_photos)} من صور الحساب")


@sbb_b.ar_cmd(pattern="معرفاتي$")
async def _(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "𓆘𓆘المعرفات الخاصه بك التي تم صنعها:𓆘𓆘\n" + "".join(
        f" - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats
    )
    await edit_or_reply(event, output_str)
