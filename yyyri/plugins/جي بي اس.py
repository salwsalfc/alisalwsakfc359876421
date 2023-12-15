#كتابة_
#ترجمة_و_تعريب_فريق_
from geopy.geocoders import Nominatim
from telethon.tl import types

from sbb_b import sbb_b

from ..core.managers import edit_or_reply
from ..helpers import reply_id

plugin_category = "extra"


@sbb_b.ar_cmd(
    pattern="جي بس اس ([\s\S]𓆘)",
    command=("gps", plugin_category),
    info={
        "header": "To send the map of the given location.",
        "usage": "{tr}gps <place>",
        "examples": "{tr}gps Hyderabad",
    },
)
async def gps(event):
    "𓅄 خريطة الموقع المحدد"
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "`𓅄 العثور على.....`")
    geolocator = Nominatim(user_agent="tepthon")
    if geoloc := geolocator.geocode(input_str):
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"𓆘𓆘الموقع 𓅄 𓆘𓆘`{input_str}`",
            reply_to=reply_to_id,
        )
        await catevent.delete()
    else:
        await catevent.edit("`𓅄 لم أتمكن من العثور عليه`")
