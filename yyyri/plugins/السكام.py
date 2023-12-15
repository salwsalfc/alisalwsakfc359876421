import asyncio

from sbb_b import sbb_b


@sbb_b.ar_cmd(pattern="وهمي كتابه(?: |$)(.𓆘)")
async def _(event):
    roz = event.pattern_match.group(1)
    if not (roz or roz.isdigit()):
        roz = 100
    else:
        try:
            roz = int(roz)
        except BaseException:
            try:
                roz = await event.ban_time(roz)
            except BaseException:
                return await event.edit("𓆘𓆘- عليك كتابة الامر بشكل صحيح𓆘𓆘")
    await event.edit(f"𓆘𓆘- تم بدء وضع الكتابه الوهمي ل {roz} من الثوانـي𓆘𓆘")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(roz)


@sbb_b.ar_cmd(pattern="وهمي صوت(?: |$)(.𓆘)")
async def _(event):
    roz = event.pattern_match.group(1)
    if not (roz or roz.isdigit()):
        roz = 100
    else:
        try:
            roz = int(roz)
        except BaseException:
            try:
                roz = await event.ban_time(roz)
            except BaseException:
                return await event.edit("𓆘𓆘- عليك كتابة الامر بشكل صحيح𓆘𓆘")
    await event.edit(f"𓆘𓆘- تم بدء وضع ارسال تسجيل الصوت الوهمي ل {roz} من الثوانـي𓆘𓆘")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(roz)


@sbb_b.ar_cmd(pattern="وهمي فيديو(?: |$)(.𓆘)")
async def _(event):
    roz = event.pattern_match.group(1)
    if not (roz or roz.isdigit()):
        roz = 100
    else:
        try:
            roz = int(roz)
        except BaseException:
            try:
                roz = await event.ban_time(roz)
            except BaseException:
                return await event.edit("𓆘𓆘- عليك كتابة الامر بشكل صحيح𓆘𓆘")
    await event.edit(f"𓆘𓆘- تم بدء وضع ارسال الفيديو الوهمي ل {roz} من الثوانـي𓆘𓆘")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(roz)


@sbb_b.ar_cmd(pattern="وهمي لعبه(?: |$)(.𓆘)")
async def _(event):
    roz = event.pattern_match.group(1)
    if not (roz or roz.isdigit()):
        roz = 100
    else:
        try:
            roz = int(roz)
        except BaseException:
            try:
                roz = await event.ban_time(roz)
            except BaseException:
                return await event.edit("𓆘𓆘- عليك كتابة الامر بشكل صحيح𓆘𓆘")
    await event.edit(f"𓆘𓆘- تم بدء وضع اللعب الوهمي ل {roz} من الثوانـي𓆘𓆘")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(roz)
