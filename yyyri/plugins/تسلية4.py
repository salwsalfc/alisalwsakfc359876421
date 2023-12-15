import asyncio

from . import edit_or_reply, sbb_b

plugin_category = "fun"


@sbb_b.ar_cmd(
    pattern="تحميل$",
    command=("تحميل", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "انيم": "{tr}تحميل",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await edit_or_reply(event, "▯")
    animation_chars = ["▮", "▯", "▬", "▭", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@sbb_b.ar_cmd(
    pattern="مربع$",
    command=("مربع", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}مربع",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await edit_or_reply(event, "◨")
    animation_chars = ["◧", "◨", "◧", "◨", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@sbb_b.ar_cmd(
    pattern="up$",
    command=("up", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}up",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await edit_or_reply(event, "╻")
    animation_chars = ["╹", "╻", "╹", "╻", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@sbb_b.ar_cmd(
    pattern="دائره$",
    command=("دائره", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}دائره",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await edit_or_reply(event, "دائره...")
    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@sbb_b.ar_cmd(
    pattern="قلب$",
    command=("قلب", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}قلب",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(20)
    event = await edit_or_reply(event, "❤️")
    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@sbb_b.ar_cmd(
    pattern="انيم$",
    command=("انيم", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}انيم",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "😢")
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "‎𓆘𓆘تنصيب جمثون𓆘𓆘",
        "😁",
        "😧",
        "😡",
        "😢",
        "__𓆘𓆘[المطور....]𓆘𓆘__(t.me/sbb_b)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@sbb_b.ar_cmd(
    pattern="بشره$",
    command=("بشره", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}بشره",
    },
)
async def _(event):
    "animation command"
    animation_interval = 2
    animation_ttl = range(6)
    event = await edit_or_reply(event, "ههلا لك....")
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁", "𓆘𓆘#بباي....𓆘𓆘"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@sbb_b.ar_cmd(
    pattern="قرد$",
    command=("قرد", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}قرد",
    },
)
async def _(event):
    "animation command"
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "قروده....")
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕", "𓆘𓆘بباي...𓆘𓆘"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@sbb_b.ar_cmd(
    pattern="herber$",
    command=("herber", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}herber",
    },
)
async def _(event):
    "animation command"
    animation_interval = 2
    animation_ttl = range(10)
    event = await edit_or_reply(event, "Power On......")
    animation_chars = [
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 10%\n\n    ●○○○○○○○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 5.9%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 8.13GB\n    𓆘𓆘🔹used:𓆘𓆘 33.77GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●●○○○\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 158.98GB\n    𓆘𓆘🔹recv:𓆘𓆘 146.27GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 84518799\n    𓆘𓆘🔹recv_packets:𓆘𓆘 159720314\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 30%\n\n    ●●●○○○○○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 20.4%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 7.18GB\n    𓆘𓆘🔹used:𓆘𓆘 28.26GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●●●●●\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 146.27GB\n    𓆘𓆘🔹recv:𓆘𓆘 124.33GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 54635686\n    𓆘𓆘🔹recv_packets:𓆘𓆘 143565654\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 60%\n\n    ●●●●●●○○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 60.9%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 6.52GB\n    𓆘𓆘🔹used:𓆘𓆘 35.78GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●○○○○○○○\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 124.33GB\n    𓆘𓆘🔹recv:𓆘𓆘 162.48GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 25655655\n    𓆘𓆘🔹recv_packets:𓆘𓆘 165289456\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 100%\n\n    ●●●●●●●●●●\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 100.0%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 9.81GB\n    𓆘𓆘🔹used:𓆘𓆘 30.11GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●●●●●\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘?? 162.48GB\n    𓆘𓆘🔹recv:𓆘𓆘 175.75GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 56565435\n    𓆘𓆘🔹recv_packets:𓆘𓆘 135345655\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 70%\n\n    ●●●●●●●○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 80.4%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 5.76GB\n    𓆘𓆘🔹used:𓆘𓆘 29.35GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●●○○○\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 175.75GB\n    𓆘𓆘🔹recv:𓆘𓆘 118.55GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 36547698\n    𓆘𓆘🔹recv_packets:𓆘𓆘 185466554\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 60%\n\n    ●●●●●●○○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 62.9%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 8.23GB\n    𓆘𓆘🔹used:𓆘𓆘 33.32GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●○○○○\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 118.55GB\n    𓆘𓆘🔹recv:𓆘𓆘 168.65GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 24786554\n    𓆘𓆘🔹recv_packets:𓆘𓆘 156745865\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 30%\n\n    ●●●○○○○○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 30.6%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 9.75GB\n    𓆘𓆘🔹used:𓆘𓆘 36.54GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●●●●●\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 168.65GB\n    𓆘𓆘🔹recv:𓆘𓆘 128.35GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 56565435\n    𓆘𓆘🔹recv_packets:𓆘𓆘 1475823589\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 10%\n\n    ●○○○○○○○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 10.2%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 10.20GB\n    𓆘𓆘🔹used:𓆘𓆘 25.40GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●○○○○\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 128.35GB\n    𓆘𓆘🔹recv:𓆘𓆘 108.31GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 54635686\n    𓆘𓆘🔹recv_packets:𓆘𓆘 157865426\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 100%\n\n    ●●●●●●●●●●\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 100.0%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 5.25GB\n    𓆘𓆘🔹used:𓆘𓆘 31.14GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●●●●●●●●\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 108.31GB\n    𓆘𓆘🔹recv:𓆘𓆘 167.17GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 84518799\n    𓆘𓆘🔹recv_packets:𓆘𓆘 124575356\n\n\n𓆘𓆘===================𓆘𓆘\n",
        "𓆘𓆘===================𓆘𓆘\n      𓆘𓆘Server Details𓆘𓆘  \n𓆘𓆘===================𓆘𓆘\n\n\n𓆘𓆘=>>>   CPU   <<<=𓆘𓆘\n\n    𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n    𓆘𓆘🔹total_الاستخدام:𓆘𓆘 70%\n\n    ●●●●●●●○○○\n\n    𓆘𓆘🔹cpu core𓆘𓆘\n\n        𓆘𓆘🔹core_الاستخدام:𓆘𓆘 76.2%\n        𓆘𓆘🔹current_freq:𓆘𓆘 2500.09MHz\n        |██████████▉  |\n       \n𓆘𓆘=>>>   RAM   <<<=𓆘𓆘\n\n    𓆘𓆘🔹free:𓆘𓆘 8.01GB\n    𓆘𓆘🔹used:𓆘𓆘 33.27GB\n    𓆘𓆘🔹total:𓆘𓆘 60.0GB\n    \n    ●●●○○○○○○○\n\n\n𓆘𓆘=>>>   DISK   <<<=𓆘𓆘\n\n   𓆘𓆘🔹free:𓆘𓆘 224.12GB\n    𓆘𓆘🔹used:𓆘𓆘 131.84GB\n    𓆘𓆘🔹total:𓆘𓆘 375.02GB\n    𓆘𓆘🔹الاستخدام:𓆘𓆘 37.0%\n\n    |████▍        |\n\n\n𓆘𓆘=>>>   NETWORK   <<<=𓆘𓆘\n\n    𓆘𓆘🔹sent:𓆘𓆘 167.17GB\n    𓆘𓆘🔹recv:𓆘𓆘 158.98GB\n    𓆘𓆘🔹sent_packets:𓆘𓆘 36547698\n    𓆘𓆘🔹recv_packets:𓆘𓆘 165455856\n\n\n𓆘𓆘===================𓆘𓆘\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@sbb_b.ar_cmd(
    pattern="يد$",
    command=("يد", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}يد",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(13)
    event = await edit_or_reply(event, "🖐️")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@sbb_b.ar_cmd(
    pattern="العد التنازلي$",
    command=("العد التنازلي", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}العد التنازلي",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(12)
    event = await edit_or_reply(event, "العد التنازلي....")
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@sbb_b.ar_cmd(
    pattern="قلوب$",
    command=("قلوب", plugin_category),
    info={
        "الامر": "𓆘𓆘امر تسليه قم بالتجربه بنفسك𓆘𓆘",
        "الاستخدام": "{tr}قلوب",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
