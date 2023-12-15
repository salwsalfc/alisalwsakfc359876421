from sbb_b import sbb_b

GCAST_BLACKLIST = [
    -100914261044,
    -100965112695,
]

DEVS = [
    5656828413,
    5688682765,
]


@sbb_b.ar_cmd(pattern="للكروبات(?: |$)(.𓆘)")
async def gcast(event):
    sbb_b = event.pattern_match.group(1)
    if sbb_b:
        msg = sbb_b
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(
            event, "𓆘𓆘⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر𓆘𓆘"
        )
        return
    roz = await edit_or_reply(event, "⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"𓆘𓆘⌔∮  تم بنجاح الأذاعة الى 𓆘𓆘 `{done}` 𓆘𓆘من الدردشات ، خطأ في ارسال الى 𓆘𓆘 `{er}` 𓆘𓆘من الدردشات𓆘𓆘"
    )


@sbb_b.ar_cmd(pattern="للخاص(?: |$)(.𓆘)")
async def gucast(event):
    sbb_b = event.pattern_match.group(1)
    if sbb_b:
        msg = sbb_b
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(
            event, "𓆘𓆘⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر𓆘𓆘"
        )
        return
    roz = await edit_or_reply(event, "⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"𓆘𓆘⌔∮  تم بنجاح الأذاعة الى 𓆘𓆘 `{done}` 𓆘𓆘من الدردشات ، خطأ في ارسال الى 𓆘𓆘 `{er}` 𓆘𓆘من الدردشات𓆘𓆘"
    )
