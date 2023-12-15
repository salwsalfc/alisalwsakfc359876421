import random

from razan.strings.fun import 𓆘
from sbb_b import sbb_b
from sbb_b.core.managers import edit_or_reply
from sbb_b.helpers import get_user_from_event

from . import 𓆘


@sbb_b.ar_cmd(pattern="رفع بكلبي(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بڪلبك 🖤 "
    )


@sbb_b.ar_cmd(pattern="رفع زوجي(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجج روحوا خلفوا 🤤😂",
    )


@sbb_b.ar_cmd(pattern="رفع مطي(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه مطي هـنا "
    )


@sbb_b.ar_cmd(pattern="رفع مرتي(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 673936943:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
    )


@sbb_b.ar_cmd(pattern="رفع كلب(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه جلب خليه خله ينبح 😂🐶",
    )


@sbb_b.ar_cmd(pattern="كت(?: |$)(.𓆘)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"𓆘𓆘- {reza}𓆘𓆘")


@sbb_b.ar_cmd(pattern="هينه(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@sbb_b.ar_cmd(pattern="نسبة الحب(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الانوثة(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور زلمة وعلى راسك𓆘𓆘")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور زلمة وعلى راسك𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور زلمة وعلى راسك𓆘𓆘")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الغباء(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@sbb_b.ar_cmd(pattern="رفع تاج(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه تاج 👑🔥"
    )


@sbb_b.ar_cmd(pattern="رفع قرد(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور 𓆘𓆘")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘- لكك دي هذا المطور𓆘𓆘")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@sbb_b.ar_cmd(pattern="اوصف(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@sbb_b.ar_cmd(pattern="شغله(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@sbb_b.ar_cmd(pattern="نسبة الرجولة(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘100%𓆘𓆘")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"𓆘𓆘100%𓆘𓆘")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"𓆘𓆘100%𓆘𓆘")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="رفع حيوان(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه حيوان 🐏"
    )


@sbb_b.ar_cmd(pattern="رفع بزون(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بزون 🐈"
    )


@sbb_b.ar_cmd(pattern="رفع زاحف(?: |$)(.𓆘)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🐍💞"
    )


@sbb_b.on(admin_cmd(pattern="نزوج(?:\s|$)([\s\S]𓆘)"))
async def rzfun(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘⌔∮ عذرا هذا مطور السورس𓆘𓆘")
    await edit_or_reply(mention, f"𓆘𓆘نزوج وماتباوع على غيري 🥺💞 ܰ𓆘𓆘")


@sbb_b.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]𓆘)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"𓆘𓆘⌔∮ عذرا هذا مطور السورس𓆘𓆘")
    await edit_or_reply(mention, f"𓆘𓆘طالق طالق بالعشرة 😹😭💕 ܰ𓆘𓆘")
