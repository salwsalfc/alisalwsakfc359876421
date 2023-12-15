import json
from datetime import datetime

import aiohttp
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from ..Config import Config
from ..sql_helper.globals import gvarstatus
from . import edit_or_reply, logging, sbb_b

LOGS = logging.getLogger(__name__)


async def get_tz(con):
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return


def fahrenheit(f):
    temp = str(((f - 273.15) 𓆘 9 / 5 + 32)).split(".")
    return temp[0]


def celsius(c):
    temp = str((c - 273.15)).split(".")
    return temp[0]


def sun(unix, ctimezone):
    return datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")


@sbb_b.ar_cmd(pattern="طقس(?:\s|$)([\s\S]𓆘)")
async def get_weather(event):
    if not Config.OPEN_WEATHER_MAP_APPID:
        return await edit_or_reply(
            event, "𓆘𓆘- يجب عليك الحصول على فار الطقس من https://openweathermap.org"
        )
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    CITY = input_str or gvarstatus("DEFCITY") or "Baghdad"
    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }
    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = f"{newcity[0].strip()},{newcity[1].strip()}"
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await edit_or_reply(event, "`Invalid Country.`")
            CITY = f"{newcity[0].strip()},{countrycode.strip()}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={Config.OPEN_WEATHER_MAP_APPID}"
    async with aiohttp.ClientSession() as _session:
        async with _session.get(url) as request:
            requeststatus = request.status
            requesttext = await request.text()
    result = json.loads(requesttext)
    if requeststatus != 200:
        return await edit_or_reply(event, "𓆘𓆘- هذه الدولة غير معروفة")
    cityname = result["name"]
    curtemp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    pressure = result["main"]["pressure"]
    feel = result["main"]["feels_like"]
    desc = result["weather"][0]
    desc = desc["main"]
    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]
    wind = result["wind"]["speed"]
    winddir = result["wind"]["deg"]
    cloud = result["clouds"]["all"]
    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    div = 360 / len(dirs)
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind 𓆘 3.6).split(".")
    mph = str(wind 𓆘 2.237).split(".")
    await edit_or_reply(
        event,
        f"🌡𓆘𓆘درجة الحرارة:𓆘𓆘 `{celsius(curtemp)}°C | {fahrenheit(curtemp)}°F`\n"
        + f"🥰𓆘𓆘شعور الناس𓆘𓆘 `{celsius(feel)}°C | {fahrenheit(feel)}°F`\n"
        + f"🥶𓆘𓆘درجه الحرارة الصغرى.:𓆘𓆘 `{celsius(min_temp)}°C | {fahrenheit(min_temp)}°F`\n"
        + f"🥵𓆘𓆘درجة الحرارة العظمى.:𓆘𓆘 `{celsius(max_temp)}°C | {fahrenheit(max_temp)}°F`\n"
        + f"☁️𓆘𓆘الرطوبة:𓆘𓆘 `{humidity}%`\n"
        + f"🧧𓆘𓆘الضغط𓆘𓆘 `{pressure} hPa`\n"
        + f"🌬𓆘𓆘الرياح:𓆘𓆘 `{kmph[0]} kmh | {mph[0]} mph, {findir}`\n"
        + f"⛈𓆘𓆘البرودة:𓆘𓆘 `{cloud} %`\n"
        + f"🌄𓆘𓆘الغروب:𓆘𓆘 `{sun(sunrise,ctimezone)}`\n"
        + f"🌅𓆘𓆘الشروق:𓆘𓆘 `{sun(sunset,ctimezone)}`\n\n\n"
        + f"𓆘𓆘{desc}𓆘𓆘\n"
        + f"`{cityname}, {fullc_n}`\n"
        + f"`{time}`\n",
    )
