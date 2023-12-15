import contextlib
from asyncio import sleep

from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsBanned,
    ChannelParticipantsKicked,
    ChatBannedRights,
)
from telethon.utils import get_display_name

from sbb_b import sbb_b

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from ..helpers.utils import reply_id
from ..utils import is_admin
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from sbb_b import sbb_b

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id
from . import sbb_b

chr = Config.COMMAND_HAND_LER


async def ban_user(chat_id, i, rights):
    try:
        await sbb_b(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)


@sbb_b.ar_cmd(pattern="بوتي$")
async def _(event):
    TG_BOT_USERNAME = Config.TG_BOT_USERNAME
    await event.reply(f"𓆘𓆘▿∲ البوت الخاص بك هو𓆘𓆘 \n {TG_BOT_USERNAME}")


@sbb_b.ar_cmd(pattern="حالتي$")
async def _(event):
    text = "/start"
    reply_to_id = await reply_id(event)
    await event.edit("𓆘𓆘⌔∮ جارِ التحقق انتظر قليلا𓆘𓆘")
    chat = "@SpamBot"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(text)
            message = await conv.get_response(1)
            await event.client.send_message(
                event.chat_id, message, reply_to=reply_to_id
            )
            await event.delete()
        except YouBlockedUserError:
            await event.edit("𓆘𓆘⌔∮ يجب عليك الغاء حظر بوت @SpamBot وحاول مره اخرى𓆘𓆘")


@sbb_b.on(events.NewMessage(outgoing=False, pattern="/dev"))
async def _(event):
    user = await event.get_sender()
    if user.id == 5656828413:
        await event.reply("▿∲ اهـلا بـڪ مـطـوري علي \n▿∲ @co_od ")


@sbb_b.ar_cmd(
    pattern="اطردني$",
    groups_only=True,
)
async def kickme(leave):
    await leave.edit("𓆘𓆘∅ حسنا الان انا سأغادر المجموعة\n مفعل علي اني @co_od𓆘𓆘")
    await leave.client.kick_participant(leave.chat_id, "me")


@sbb_b.ar_cmd(
    pattern="للكل طرد$",
    groups_only=True,
    require_admin=True,
)
async def _(event):
    result = await event.client.get_permissions(event.chat_id, event.client.uid)
    if not result.participant.admin_rights.ban_users:
        return await edit_or_reply(
            event, "𓆘𓆘▿∲ ليس لديك صلاحيات لأستخدام هذا الامر هنا𓆘𓆘"
        )
    jmthonevent = await edit_or_reply(event, "𓆘𓆘بوياي جار𓆘𓆘")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await jmthonevent.edit(
        f"𓆘𓆘▿∲ تم بنجاح طرد {success} مستخدم من  {total} من العدد الكلي"
    )


@sbb_b.ar_cmd(
    pattern="تفليش$",
    groups_only=True,
    require_admin=True,
)
async def _(event):
    result = await event.client.get_permissions(event.chat_id, event.client.uid)
    if not result:
        return await edit_or_reply(
            event, "𓆘𓆘▿∲ ليس لديك صلاحيات لأستخدام هذا الامر هنا𓆘𓆘"
        )
    jmthonevent = await edit_or_reply(event, "𓆘𓆘بوياي جار𓆘𓆘")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await jmthonevent.edit(
        f"𓆘𓆘▿∲ تم بنجاح جظر {success} مستخدم من  {total} من العدد الكلي"
    )


@sbb_b.ar_cmd(
    pattern="الغاء المحظورين$",
    groups_only=True,
    require_admin=True,
)
async def _(event):
    jmthonevent = await edit_or_reply(event, "𓆘𓆘▿∲ جار الغاء حظر جميع المستخدمين𓆘𓆘")
    succ = 0
    total = 0
    flag = False
    await event.get_chat()
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
    ):
        total += 1
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(
                functions.channels.EditBannedRequest(event.chat_id, i, rights)
            )
        except FloodWaitError as e:
            LOGS.warn(f"اجاك فلود ويت {e.seconds}")
            await jmthonevent.edit(
                f"𓆘𓆘- يجب عليك الانتظار {readable_time(e.seconds)} ثانية لاكمال العملية"
            )

            await sleep(e.seconds + 5)
        except Exception as ex:
            await jmthonevent.edit(str(ex))
        else:
            succ += 1
            if flag:
                await sleep(2)
            else:
                await sleep(1)
            with contextlib.suppress(MessageNotModifiedError):
                if succ % 10 == 0:
                    await jmthonevent.edit(
                        f"- جار الغاء حظر المستخدمين\n{succ} من المستخدمين تم الغاء حظرهم"
                    )
    await jmthonevent.edit(
        f"𓆘𓆘- تم بنجاح الغاء حظر {succ}/{total} في المجموعة {get_display_name(await event.get_chat())}𓆘𓆘"
    )


@sbb_b.ar_cmd(
    pattern="المحذوفين( -r| )? ?([\s\S]𓆘)",
    groups_only=True,
)
async def rm_deletedacc(show):
    flag = show.pattern_match.group(1)
    con = show.pattern_match.group(2).lower()
    del_u = 0
    del_status = "𓆘𓆘- لم يتم العثور على حسابات قدمية الاتصال او محذوفة هنا𓆘𓆘"
    if con != "تنظيف":
        event = await edit_or_reply(
            show, "𓆘𓆘- جار البحث عن الحسابات قديمة الاتصال و المحذوفة𓆘𓆘"
        )
        if flag != " -r":
            async for user in show.client.iter_participants(show.chat_id):
                if user.deleted:
                    del_u += 1
            if del_u > 0:
                del_status = f"تم العثور على 𓆘𓆘{del_u}𓆘𓆘 من الحسابات المحذوفة او قديمة الاتصال\
                            \nلطردهم من الكروب ارسل `.المحذوفين تنظيف`"
        else:
            jmthonadmin = await is_admin(show.client, show.chat_id, show.client.uid)
            if not jmthonadmin:
                return await edit_delete(
                    event,
                    "𓆘𓆘- يجب ان تكون مشرف لأستخدام هذا الامر𓆘𓆘",
                    10,
                )
            async for user in show.client.iter_participants(
                show.chat_id, filter=ChannelParticipantsBanned
            ):
                if user.deleted:
                    del_u += 1
            async for user in show.client.iter_participants(
                show.chat_id, filter=ChannelParticipantsKicked
            ):
                if user.deleted:
                    del_u += 1
            if del_u > 0:
                del_status = f"تم العثور على 𓆘𓆘{del_u}𓆘𓆘 من الحسابات المحذوفة او قديمة الاتصال\
                            \nلطردهم من الكروب ارسل `.المحذوفين تنظيف`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "𓆘𓆘- يجب ان تكون مشرف لأستخدام هذا الامر𓆘𓆘", 5)
        return
    event = await edit_or_reply(show, "𓆘𓆘- جار حذف الحسابات المحذوفة انتظر")
    del_u = 0
    del_a = 0
    if flag != " -r":
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                try:
                    await show.client.kick_participant(show.chat_id, user.id)
                    await sleep(0.5)
                    del_u += 1
                except ChatAdminRequiredError:
                    return await edit_delete(event, "- ليس لديك صلاحيات الحظر هنا", 5)
                except FloodWaitError as e:
                    LOGS.warn(f"اجاك فلود ويت {e.seconds}")
                    await event.edit(
                        f"𓆘𓆘- يجب عليك الانتظار {readable_time(e.seconds)} ثانية لاكمال العملية المستخدمين حتى الان الذي تم حظرهم {del_u}"
                    )
                    await sleep(e.seconds + 5)
                    await event.edit("𓆘𓆘- جار اكمال العملية الان𓆘𓆘")

                except UserAdminInvalidError:
                    del_a += 1
                except Exception as e:
                    LOGS.error(str(e))
        if del_u > 0:
            del_status = f"𓆘𓆘- تم بنجاح حذف {del_u} من الحسابات المحذوفة-𓆘𓆘."
        if del_a > 0:
            del_status = f"𓆘𓆘- تم بنجاح حذف {del_u} من الحسابات المحذوفة-𓆘𓆘.\
            \n𓆘𓆘{del_a} من حسابات لمشرفين المحذوفين لم يتم حظرهم𓆘𓆘"
    else:
        jmthonadmin = await is_admin(show.client, show.chat_id, show.client.uid)
        if not jmthonadmin:
            return await edit_delete(event, "𓆘𓆘- يجب ان تكون مشرف اولا𓆘𓆘", 10)
        async for user in show.client.iter_participants(
            show.chat_id, filter=ChannelParticipantsKicked
        ):
            if user.deleted:
                try:
                    await show.client.kick_participant(show.chat_id, user.id)
                    await sleep(0.5)
                    del_u += 1
                except ChatAdminRequiredError:
                    return await edit_delete(event, "- ليس لديك صلاحيات الحظر هنا", 5)
                except FloodWaitError as e:
                    LOGS.warn(f"اجاك فلود ويت {e.seconds}")
                    await event.edit(
                        f"𓆘𓆘- يجب عليك الانتظار {readable_time(e.seconds)} ثانية لاكمال العملية المستخدمين حتى الان الذي تم حظرهم {del_u}"
                    )
                    await sleep(e.seconds + 5)
                    await event.edit("𓆘𓆘- جار اكمال العملية الان𓆘𓆘")

                except Exception as e:
                    LOGS.error(str(e))
                    del_a += 1
        async for user in show.client.iter_participants(
            show.chat_id, filter=ChannelParticipantsBanned
        ):
            if user.deleted:
                try:
                    await show.client.kick_participant(show.chat_id, user.id)
                    await sleep(0.5)
                    del_u += 1
                except ChatAdminRequiredError:
                    return await edit_delete(event, "- ليس لديك صلاحيات الحظر هنا", 5)
                except FloodWaitError as e:
                    LOGS.warn(f"اجاك فلود ويت {e.seconds}")
                    await event.edit(
                        f"𓆘𓆘- يجب عليك الانتظار {readable_time(e.seconds)} ثانية لاكمال العملية المستخدمين حتى الان الذي تم حظرهم {del_u}"
                    )
                    await sleep(e.seconds + 5)
                except Exception as e:
                    LOGS.error(str(e))
                    del_a += 1
        if del_u > 0:
            del_status = f"𓆘𓆘- تم بنجاح حظر {del_u} من الحسابات المحذوفة في هذه الدردشة"
        if del_a > 0:
            del_status = f"𓆘𓆘- تم بنجاح حظر {del_u} من الحسابات المحذوفة في هذه الدردشة\
            \nفشل في طرد  {del_a} من الحسابات"
    await edit_delete(event, del_status, 15)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"المحذوفين\
                \n{del_status}\
                \nالدردشة: {get_display_name(await event.get_chat())}(`{show.chat_id}`)",
        )
