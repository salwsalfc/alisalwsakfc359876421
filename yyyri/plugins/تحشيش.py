import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from jmthon import sbb_b
from sbb_b.razan.resources.strings import 𓆘
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



﷽#
 


@sbb_b.on(admin_cmd(pattern="رفع مرتي(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"🚻 𓆘𓆘 𓅄 المستخدم => • 𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n ☑️ 𓆘𓆘𓅄 تم رفعها مرتك بواسطه  :𓆘𓆘{my_mention} 👰🏼‍♀️.\n𓆘𓆘𓅄 يلا حبيبي امشي نخلف بيبي 👶🏻🤤𓆘𓆘 ")

@sbb_b.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘▿∲ دا مبرمج السورس يعبيط𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅄 المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅄  تـم رفعـه جلب 🐶 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅄 خليه خله ينبح 😂𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓅽︙ المستخدم [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه تاج بواسطة :𓆘𓆘 {my_mention} 👑🔥")

@sbb_b.on(admin_cmd(pattern="رفع قرد(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓅽︙ المستخدم [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه قرد واعطائه موزة 🐒🍌 بواسطة :𓆘𓆘 {my_mention}")

@sbb_b.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه بكلـبك 🤍 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  انت حبي الابدي 😍𓆘𓆘")
    
    

@sbb_b.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه مطي 🐴 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  تعال حبي استلم  انه 𓆘𓆘")
    
#
 
 ﷽


@sbb_b.on(admin_cmd(pattern="رفع زوجي(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه زوجج بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  يلا حبيبي امشي نخلف 🤤🔞𓆘𓆘")
    

@sbb_b.on(admin_cmd(pattern="رفع زاحف(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفع المتهم زاحف اصلي بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  ها يلزاحف شوكت تبطل سوالفك حيوان 😂🐍𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع كحبة(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفع المتهم كحبة 👙 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  ها يلكحبة طوبز خلي انيجك/ج𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع فرخ(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه فرخ الكروب بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  لك الفرخ استر على خمستك ياهو اليجي يزورهاً 👉🏻👌🏻𓆘𓆘")

@sbb_b.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]𓆘)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 1260465030:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 1260465030:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"𓅽︙ ولك [{tag}](tg://user?id={user.id}) \n𓅽︙  هيو لتندك بسيادك لو بهاي 👞👈")

@sbb_b.on(admin_cmd(pattern="رفع حاته(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـها حاته الكروب 🤤😻 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  تعاي يعافيتي اريد حضن دافي 😽𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع هايشة(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه المتهم هايشة 🐄 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  ها يلهايشة خوش بيك حليب تعال احلبك 😂𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه صاك 🤤 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  تعال يلحلو انطيني بوسة من رگبتك 😻🤤𓆘𓆘")

@sbb_b.ar_cmd(
    pattern="مصه(?:\s|$)([\s\S]𓆘)",
    command=("مصه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 1260465030:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 1260465030:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"𓆘𓆘 ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀𓆘𓆘\n𓆘𓆘🚹 ¦ تعال مصه عزيزي 𓆘𓆘 [{tag}](tg://user?id={user.id})")

@sbb_b.on(admin_cmd(pattern="اسامه(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    await edit_or_reply(mention, f"اهلا بڪ مطوري أسـامة ♥ ")

@sbb_b.on(admin_cmd(pattern="رفع ايجة(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه ايچة 🤤 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  ها يلأيچة تطلعين درب بـ$25 👙𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع زبال(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعـه زبال الكروب 🧹 بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  تعال يلزبال اكنس الكروب لا أهينك 🗑😹𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع كواد(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعه كواد بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  تعال يكواد عرضك مطشر اصير حامي عرضك ؟😎𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع ديوث(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ المستخدم𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n𓆘𓆘𓅽︙  تـم رفعه ديوث الكروب بواسطة :𓆘𓆘 {my_mention} \n𓆘𓆘𓅽︙  تعال يلديوث جيب اختك خلي اتمتع وياها 🔞𓆘𓆘")

@sbb_b.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ الحلو𓆘𓆘 「[{jmthon}](tg://user?id={user.id})」 \n𓆘𓆘𓅽︙  تـم رفعه مميز بواسطة :𓆘𓆘 {my_mention}")

@sbb_b.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ الحلو𓆘𓆘 「[{jmthon}](tg://user?id={user.id})」 \n𓆘𓆘𓅽︙  تـم رفعه ادمن بواسطة :𓆘𓆘 {my_mention}")

@sbb_b.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ الحلو𓆘𓆘 「[{jmthon}](tg://user?id={user.id})」 \n𓆘𓆘𓅽︙  تـم رفعه منشئ بواسطة :𓆘𓆘 {my_mention}")

@sbb_b.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    jmthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙ الحلو𓆘𓆘 「[{jmthon}](tg://user?id={user.id})」 \n𓆘𓆘𓅽︙  تـم رفعه مالك الكروب بواسطة :𓆘𓆘 {my_mention}")

@sbb_b.on(admin_cmd(pattern="رفع مجنب(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f" 𓆘𓆘 𓅽︙  المستخدم => • 𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n ☑️ 𓆘𓆘𓅽︙  تم رفعه مجنب بواسطه  :𓆘𓆘{my_mention} .\n𓆘𓆘𓅽︙  كوم يلمجنب اسبح مو عيب تضرب جلغ 😹𓆘𓆘 ")

@sbb_b.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘 𓅽︙  المستخدم => • 𓆘𓆘 [{jmthon}](tg://user?id={user.id}) \n ☑️ 𓆘𓆘𓅽︙  تم رفعه وصخ الكروب 🤢 بواسطه  :𓆘𓆘{my_mention} .\n𓆘𓆘𓅽︙  لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 𓆘𓆘 ")

@sbb_b.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓅽︙ 𓆘𓆘 لقد تم زواجك/ج من : 𓆘𓆘[{jmthon}](tg://user?id={user.id}) 💍\n𓆘𓆘𓅽︙  الف الف مبروك الان يمكنك اخذ راحتك 𓆘𓆘 ")

@sbb_b.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]𓆘)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jmthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"𓆘𓆘𓅽︙  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :𓆘𓆘{my_mention} .\n𓆘𓆘𓅽︙  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق 𓆘𓆘 ")
ownersayed_id = 5656828413
@sbb_b.on(events.NewMessage(outgoing=False, pattern='منصب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersayed_id :
        order = await event.reply('يب منصب ✓')
ownersayed1_id = 5656828413
@sbb_b.on(events.NewMessage(outgoing=False, pattern='منو فخر العرب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersayed1_id :
        order = await event.reply('انته فخر العرب مح ❤️')
