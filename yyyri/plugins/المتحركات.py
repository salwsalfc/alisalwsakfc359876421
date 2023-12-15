import random

import requests

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import reply_id, unsavegif
from . import sbb_b


@sbb_b.ar_cmd(pattern="متحركات(?:\s|$)([\s\S]𓆘)")
async def some(event):
    inpt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not inpt:
        await edit_delete(event, "𓆘𓆘- يجب كتابة عنوان للبحث وارسال المتحركات اليك𓆘𓆘")
    count = 1
    if ";" in inpt:
        inpt, count = inpt.split(";")
    if int(count) < 0 and int(count) > 20:
        await edit_delete(
            event, "𓆘𓆘- يجب عليك كتابة عدد المتحركات من عدد يبدأ من 1 الى 20"
        )
    jmthonevent = await edit_or_reply(event, "- جار ارسال المتحركات انتظر قليلا")
    res = requests.get("https://giphy.com/")
    res = res.text.split("GIPHY_FE_WEB_API_KEY =")[1].split("\n")[0]
    api_key = res[2:-1]
    r = requests.get(
        f"https://api.giphy.com/v1/gifs/search?q={inpt}&api_key={api_key}&limit=50"
    ).json()
    list_id = [r["data"][i]["id"] for i in range(len(r["data"]))]
    rlist = random.sample(list_id, int(count))
    for items in rlist:
        nood = await event.client.send_file(
            event.chat_id,
            f"https://media.giphy.com/media/{items}/giphy.gif",
            reply_to=reply_to_id,
        )
        await unsavegif(event, nood)
    await jmthonevent.delete()
