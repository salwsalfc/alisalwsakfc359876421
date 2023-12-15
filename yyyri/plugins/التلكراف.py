import os
import random
import string
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from telethon.utils import get_display_name
from urlextract import URLExtract

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_or_reply
from . import BOTLOG, BOTLOG_CHATID, sbb_b

LOGS = logging.getLogger(__name__)


extractor = URLExtract()
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@sbb_b.ar_cmd(pattern="(ت(ل)?ك(راف)?) ?(m|t|ميديا|نص)(?:\s|$)([\s\S]𓆘)")
async def _(event):
    sbb_bevent = await edit_or_reply(event, "𓆘𓆘 ⌔∮ جار انشاء رابط تلكراف𓆘𓆘")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f" ⌔∮ انشاء حساب تلكراف جديد {auth_url} لهذه الجلسة. \n𓆘𓆘لا تعطي هذا الرابط لاي احد, حتى لو قالو انهم من شركة التلكرام!𓆘𓆘",
        )
    optional_title = event.pattern_match.group(5)
    if not event.reply_to_msg_id:
        return await sbb_bevent.edit(
            "𓆘𓆘 ⌔∮ قم بالرد على هذه الرسالة للحصول على رابط تلكراف فورا𓆘𓆘",
        )

    start = datetime.now()
    r_message = await event.get_reply_message()
    input_str = (event.pattern_match.group(4)).strip()
    if input_str in ["ميديا", "m"]:
        downloaded_file_name = await event.client.download_media(
            r_message, Config.TEMP_DIR
        )
        await sbb_bevent.edit(f"𓆘𓆘⌔∮ تم التحميل الى {downloaded_file_name}𓆘𓆘")
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await sbb_bevent.edit(f"𓆘𓆘 ⌔∮ خطأ : 𓆘𓆘\n𓆘𓆘{exc}𓆘𓆘")
            os.remove(downloaded_file_name)
        else:
            end = datetime.now()
            ms = (end - start).seconds
            os.remove(downloaded_file_name)
            await sbb_bevent.edit(
                f"𓆘𓆘 ⌔∮ الرابط : 𓆘𓆘[إضغط هنا](https://telegra.ph{media_urls[0]})\
                    \n𓆘𓆘 ⌔∮ الوقت المأخوذ : {ms} ثانية.𓆘𓆘",
                link_preview=True,
            )
    elif input_str in ["نص", "t"]:
        user_object = await event.client.get_entity(r_message.sender_id)
        title_of_page = get_display_name(user_object)
        if optional_title:
            title_of_page = optional_title
        page_content = r_message.message
        if r_message.media:
            if page_content != "":
                title_of_page = page_content
            downloaded_file_name = await event.client.download_media(
                r_message, Config.TEMP_DIR
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            for m in m_list:
                page_content += m.decode("UTF-8") + "\n"
            os.remove(downloaded_file_name)
        page_content = page_content.replace("\n", "<br>")
        try:
            response = telegraph.create_page(title_of_page, html_content=page_content)
        except Exception as e:
            LOGS.info(e)
            title_of_page = "".join(
                random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
                for _ in range(16)
            )
            response = telegraph.create_page(title_of_page, html_content=page_content)
        end = datetime.now()
        ms = (end - start).seconds
        sbb_b = f"https://telegra.ph/{response['path']}"
        await sbb_bevent.edit(
            f"𓆘𓆘الرابط𓆘𓆘:  [اضغط هنا]({sbb_b})\
                 \n𓆘𓆘الوقت المستغرق𓆘𓆘 : {ms} 𓆘𓆘ثواني𓆘𓆘",
            link_preview=True,
        )
