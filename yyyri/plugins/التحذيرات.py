import html

from sbb_b import sbb_b

from ..core.managers import edit_or_reply
from ..sql_helper import warns_sql as sql


@sbb_b.ar_cmd(pattern="تحذير(?:\s|$)([\s\S]𓆘)")
async def _(event):
    warn_reason = event.pattern_match.group(1)
    if not warn_reason:
        warn_reason = "⪼ لا يوجد سبب ، 🗒"
    reply_message = await event.get_reply_message()
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(
        reply_message.sender_id, event.chat_id, warn_reason
    )
    if num_warns >= limit:
        sql.reset_warns(reply_message.sender_id, event.chat_id)
        if soft_warn:
            logger.info("TODO: طرد المستخدم")
            reply = "𓆘𓆘▸┊بسبب تخطي التحذيرات الـ {} ، يجب طرد المستخدم! 🚷𓆘𓆘".format(
                limit, reply_message.sender_id
            )
        else:
            logger.info("TODO: حظر المستخدم")
            reply = "𓆘𓆘▸┊بسبب تخطي التحذيرات الـ {} ، يجب حظر المستخدم! ⛔️𓆘𓆘".format(
                limit, reply_message.sender_id
            )
    else:
        reply = "𓆘𓆘▸┊[ المستخدم 👤](tg://user?id={}) 𓆘𓆘لديه {}/{} تحذيرات ، احذر!𓆘𓆘𓆘𓆘".format(
            reply_message.sender_id, num_warns, limit
        )
        if warn_reason:
            reply += "\n𓆘𓆘▸┊سبب التحذير الأخير 𓆘𓆘\n{}".format(html.escape(warn_reason))
    await edit_or_reply(event, reply)


@sbb_b.ar_cmd(pattern="التحذيرات")
async def _(event):
    reply_message = await event.get_reply_message()
    if not reply_message:
        return await edit_delete(
            event, "𓆘𓆘▸┊قم بالرد ع المستخدم للحصول ع تحذيراته . ☻𓆘𓆘"
        )
    result = sql.get_warns(reply_message.sender_id, event.chat_id)
    if not result or result[0] == 0:
        return await edit_or_reply(event, "__▸┊هذا المستخدم ليس لديه أي تحذير! ツ__")
    num_warns, reasons = result
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    if not reasons:
        return await edit_or_reply(
            event,
            "𓆘𓆘▸┊[ المستخدم 👤](tg://user?id={}) 𓆘𓆘لديه {}/{} تحذيرات ، لكن لا توجد اسباب !𓆘𓆘".format(
                num_warns, limit
            ),
        )

    text = "𓆘𓆘▸┊[ المستخدم 👤](tg://user?id={}) 𓆘𓆘لديه {}/{} تحذيرات ، للأسباب : ↶𓆘𓆘".format(
        num_warns, limit
    )

    text = "𓆘𓆘▸┊ المستخدم لديه {}/{} تحذيرات ، للأسباب : ↶:".format(num_warns, limit)
    text += "\r\n"
    text += reasons
    await event.edit(text)


@sbb_b.ar_cmd(pattern="حذف التحذيرات(?: |$)(.𓆘)")
async def _(event):
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.sender_id, event.chat_id)
    await edit_or_reply(event, "𓆘𓆘▸┊تم إعادة ضبط التحذيرات!𓆘𓆘")
