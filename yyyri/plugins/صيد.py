# by: t.me/Dar4k  ~ t.me/R0R77

import asyncio
import random

import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent

from sbb_b import sbb_b

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,𓆘/𓆘;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "ثلاثيات":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "سداسيات":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        # random.shuffle(f)
        username = "".join(f)
        username = username + "bot"

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)

        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعيات":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        return "error"
    return username


@sbb_b.ar_cmd(pattern="الصيد")
async def _(event):
    await event.edit(
        """
أوامر الصيد الخاصة بسورس جمثون : 

ٴ— — — — — — — — — —

النوع :(  سداسي حرفين/ ثلاثيات/ سداسيات/ بوتات/ خماسي حرفين/خماسي /سباعيات )

الامر:  `.صيد` + النوع
- يقوم بصيد معرفات عشوائية حسب النوع

الامر:  `تثبيت` + معرف
𓆘 وظيفة الامر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه

ٴ— — — — — — — — — —
الامر:   `.حالة الصيد`
• لمعرفة عدد المحاولات للصيد

الامر:  `.حالة التثبيت`
• لمعرفة عدد المحاولات للصيد

@FTTUTY  - channle userbot 

"""
    )


@sbb_b.ar_cmd(pattern="صيد (.𓆘)")
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء الصيد في @{ch} .")
    except:
        try:
            ch = await sbb_b(
                functions.channels.CreateChannelRequest(
                    title="SEMO HUNTER - صيد سيمو",
                    about="This channel to hunt username by - @FTTUTY ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"𓆘𓆘- تم تفعيل الصيد بنجاح الان𓆘𓆘")
        except Exception as e:
            await sbb_b.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ𓆘𓆘-  : {str(e)}𓆘𓆘"
            )
    isclaim.clear()
    isclaim.append("on")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("𓆘𓆘- يرجى وضع النوع بشكل صحيح𓆘𓆘.")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await sbb_b(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n- By : @DEV_SAMIR - @FTTUTY !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await sbb_b.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند𓆘𓆘-  ({e.seconds}) ثانية .𓆘𓆘",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند𓆘𓆘-  ({e.seconds}) ثانية .𓆘𓆘",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await sbb_b.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
    await event.client.send_message(event.chat_id, "𓆘𓆘- تم بنجاح الانتهاء من الصيد𓆘𓆘")


@sbb_b.ar_cmd(pattern="تثبيت (.𓆘)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في𓆘𓆘-  @{ch} .𓆘𓆘")
    except:
        try:
            ch = await sbb_b(
                functions.channels.CreateChannelRequest(
                    title="SEMO HUNTER - صيد سيمو",
                    about="This channel to hunt username by - @FTTUTY ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"𓆘𓆘- تم بنجاح بدأ التثبيت𓆘𓆘")
        except Exception as e:
            await sbb_b.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    for i in range(1000000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await sbb_b(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n- By : @DEV_SAMIR - @FTTUTT0 !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف 𓆘𓆘-  @{username} غير صالح . 𓆘𓆘"
                )
                break
            except telethon.errors.FloodError as e:
                await sbb_b.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await sbb_b.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1

        await asyncio.sleep(1.3)
    isclaim.clear()
    isclaim.append("off")
    await sbb_b.send_message(event.chat_id, "𓆘𓆘- تم الانتهاء من التثبيت بنجاح𓆘𓆘")


@sbb_b.ar_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"𓆘𓆘- الصيد وصل لـ({trys[0]}) 𓆘𓆘من المحاولات")
    elif "off" in isclaim:
        await event.edit("𓆘𓆘- الصيد بالاصل لا يعمل .𓆘𓆘")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@sbb_b.ar_cmd(pattern="حالة التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"𓆘𓆘- التثبيت وصل لـ({trys2[0]}) من المحاولات𓆘𓆘")
    elif "off" in isauto:
        await event.edit("𓆘𓆘- التثبيت بالاصل لا يعمل .𓆘𓆘")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
