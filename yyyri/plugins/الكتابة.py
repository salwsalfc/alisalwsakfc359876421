from sbb_b import sbb_b


@sbb_b.ar_cmd(pattern="تغميق(?: |$)(.𓆘)")
async def _(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("𓆘", "𓆘")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"𓆘𓆘{the_real_message}𓆘𓆘")
    else:
        await event.edit("𓆘𓆘⌔∮ يجب عليك الرد على الرساله𓆘𓆘")


@sbb_b.ar_cmd(pattern="نسخ(?: |$)(.𓆘)")
async def _(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("𓆘", "𓆘")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"`{the_real_message}`")
    else:
        await event.edit("𓆘𓆘⌔∮ يجب عليك الرد على الرساله𓆘𓆘")


@sbb_b.ar_cmd(pattern="مائل(?: |$)(.𓆘)")
async def _(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("𓆘", "𓆘")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"__{the_real_message}__")
    else:
        await event.edit("𓆘𓆘⌔∮ يجب عليك الرد على الرساله𓆘𓆘")
