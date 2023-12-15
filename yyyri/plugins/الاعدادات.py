import os
from asyncio.exceptions import CancelledError
from time import sleep

from sbb_b import sbb_b

from ..core.logger import logging
from ..core.managers import edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP

LOGS = logging.getLogger(__name__)


@sbb_b.ar_cmd(
    pattern="اعادة تشغيل$",
    disable_errors=True,
)
async def _(event):
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#اعادة_التشغيل \n" "تم اعادة تشغيل البوت"
        )
    sandy = await edit_or_reply(
        event,
        "𓆘𓆘𓅽 جارِ اعادة تشغيل السورس\nارسل𓆘𓆘 `.فحص` 𓆘𓆘او𓆘𓆘 `.الاوامر` 𓆘𓆘للتحقق مما إذ كان البوت شغال ، يستغرق الأمر في الواقع 1-2 دقيقة لإعادة التشغيل𓆘𓆘",
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS.error(e)
    try:
        await sbb_b.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)


@sbb_b.ar_cmd(pattern="أيقاف السورس$")
async def _(event):
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#ايقاف_التشغيل \n" "تم ايقاف تشغيل السورس"
        )
    await edit_or_reply(
        event, "𓆘𓆘⌔∮ جارِ إيقاف تشغيل السورس الآن ... شغِّلني يدويًا لاحقًا𓆘𓆘"
    )
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        os._exit(143)


@sbb_b.ar_cmd(pattern="أيقاف مؤقت( [0-9]+)?$")
async def _(event):
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(
            event, "⌔∮ استخدام الامر؛  `.أيقاف مؤقت` <وقت بالثواني>"
        )
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "𓅽 لقد وضعت السورس في وضع السكون لمدة " + str(counter) + " ثواني",
        )
    event = await edit_or_reply(
        event, f"𓆘𓆘⌔∮ حسنا تم ايقاف البوت لمده {counter} ثواني𓆘𓆘"
    )
    sleep(counter)
    await event.edit("𓆘𓆘⪼ اهلا الان اشتغل بشكل طبيعي𓆘𓆘")


@sbb_b.ar_cmd(pattern="الاشعارات (تشغيل|ايقاف)$")
async def set_pmlog(event):
    input_str = event.pattern_match.group(1)
    if input_str == "ايقاف":
        if gvarstatus("restartupdate") is None:
            return await edit_delete(event, "𓆘𓆘⌔∮ تم تعطيل التحديثات بالفعل 𓆰️𓆘𓆘")
        delgvar("restartupdate")
        return await edit_or_reply(event, "𓆘𓆘⌔∮ تم تعطيل التحديثات بنجاح 𓆰𓆘𓆘")
    if gvarstatus("restartupdate") is None:
        addgvar("restartupdate", "turn-oned")
        return await edit_or_reply(event, "𓆘𓆘⌔∮ تم تشغيل التحديثات بنجاح 𓆰𓆘𓆘")
    await edit_delete(event, "𓆘𓆘⌔∮ تم تشغيل التحديثات بالفعل 𓆰️𓆘𓆘")
