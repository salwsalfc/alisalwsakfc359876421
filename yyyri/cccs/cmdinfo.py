from typing import Dict, List, Union

from ..Config import Config
from ..helpers.utils.extdl import install_pip
from . import CMD_INFO, GRP_INFO, PLG_INFO
from .managers import edit_delete

try:
    from urlextract import URLExtract
except ModuleNotFoundError:
    install_pip("urlextract")
    from urlextract import URLExtract


extractor = URLExtract()
cmdprefix = Config.COMMAND_HAND_LER

hemojis = {
    "admin": "👮‍♂️",
    "bot": "🤖",
    "fun": "🎨",
    "misc": "🧩",
    "tools": "🧰",
    "utils": "🗂",
    "extra": "➕",
    "useless": "⚰️",
}


def get_data(about, ktype):
    data = about[ktype]
    urls = extractor.find_urls(data)
    if len(urls) > 0:
        return data
    return data.capitalize()


def _format_about(
    about: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
) -> str:  # sourcery no-metrics  # sourcery skip: low-code-quality
    if not isinstance(about, dict):
        return about
    tmp_chelp = ""
    if "header" in about and isinstance(about["header"], str):
        tmp_chelp += f"__{about['header'].title()}__"
        del about["header"]
    if "description" in about and isinstance(about["description"], str):
        tmp_chelp += (
            "\n\n✘  𓆘𓆘Description :𓆘𓆘\n" f"__{get_data(about , 'description')}__"
        )
        del about["description"]
    if "flags" in about:
        tmp_chelp += "\n\n✘  𓆘𓆘Available Flags :𓆘𓆘"
        if isinstance(about["flags"], dict):
            for f_n, f_d in about["flags"].items():
                tmp_chelp += f"\n    ▫ `{f_n}` : __{f_d.lower()}__"
        else:
            tmp_chelp += f"\n    {about['flags']}"
        del about["flags"]
    if "options" in about:
        tmp_chelp += "\n\n✘  𓆘𓆘Available Options :𓆘𓆘"
        if isinstance(about["options"], dict):
            for o_n, o_d in about["options"].items():
                tmp_chelp += f"\n    ▫ `{o_n}` : __{o_d.lower()}__"
        else:
            tmp_chelp += f"\n    __{about['options']}__"
        del about["options"]
    if "types" in about:
        tmp_chelp += "\n\n✘  𓆘𓆘Supported Types :𓆘𓆘"
        if isinstance(about["types"], list):
            for _opt in about["types"]:
                tmp_chelp += f"\n    `{_opt}` ,"
        else:
            tmp_chelp += f"\n    __{about['types']}__"
        del about["types"]
    if "usage" in about:
        tmp_chelp += "\n\n✘  𓆘𓆘Usage :𓆘𓆘"
        if isinstance(about["usage"], list):
            for ex_ in about["usage"]:
                tmp_chelp += f"\n    `{ex_}`"
        else:
            tmp_chelp += f"\n    `{about['usage']}`"
        del about["usage"]
    if "examples" in about:
        tmp_chelp += "\n\n✘  𓆘𓆘Examples :𓆘𓆘"
        if isinstance(about["examples"], list):
            for ex_ in about["examples"]:
                tmp_chelp += f"\n    `{ex_}`"
        else:
            tmp_chelp += f"\n    `{about['examples']}`"
        del about["examples"]
    if "others" in about:
        tmp_chelp += f"\n\n✘  𓆘𓆘Others :𓆘𓆘\n__{get_data(about , 'others')}__"
        del about["others"]
    if about:
        for t_n, t_d in about.items():
            tmp_chelp += f"\n\n✘  𓆘𓆘{t_n.title()} :𓆘𓆘\n"
            if isinstance(t_d, dict):
                for o_n, o_d in t_d.items():
                    tmp_chelp += f"    ▫ `{o_n}` : __{get_data(t_d , o_n)}__\n"
            elif isinstance(t_d, list):
                for _opt in t_d:
                    tmp_chelp += f"    `{_opt}` ,"
                tmp_chelp += "\n"
            else:
                tmp_chelp += f"__{get_data(about ,t_n)}__"
                tmp_chelp += "\n"
    return tmp_chelp.replace("{tr}", Config.COMMAND_HAND_LER)


def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None


async def cmdinfo(input_str, event, plugin=False):
    if input_str[0] == cmdprefix:
        input_str = input_str[1:]
    try:
        about = CMD_INFO[input_str]
    except KeyError:
        if plugin:
            await edit_delete(
                event,
                f"𓆘𓆘There is no plugin or command as 𓆘𓆘`{input_str}`𓆘𓆘 in your bot.𓆘𓆘",
            )
            return None
        await edit_delete(
            event, f"𓆘𓆘There is no command as 𓆘𓆘`{input_str}`𓆘𓆘 in your bot.𓆘𓆘"
        )
        return None
    except Exception as e:
        await edit_delete(event, f"𓆘𓆘Error𓆘𓆘\n`{e}`")
        return None
    outstr = f"𓆘𓆘Command :𓆘𓆘 `{cmdprefix}{input_str}`\n"
    plugin = get_key(input_str)
    if plugin is not None:
        outstr += f"𓆘𓆘Plugin :𓆘𓆘 `{plugin}`\n"
        category = getkey(plugin)
        if category is not None:
            outstr += f"𓆘𓆘Category :𓆘𓆘 `{category}`\n\n"
    outstr += f"𓆘𓆘✘  Intro :𓆘𓆘\n{about[0]}"
    return outstr


async def plugininfo(input_str, event, flag):
    try:
        cmds = PLG_INFO[input_str]
    except KeyError:
        outstr = await cmdinfo(input_str, event, plugin=True)
        return outstr
    except Exception as e:
        await edit_delete(event, f"𓆘𓆘Error𓆘𓆘\n`{e}`")
        return None
    if len(cmds) == 1 and (flag is None or (flag and flag != "-p")):
        outstr = await cmdinfo(cmds[0], event, plugin=False)
        return outstr
    outstr = f"𓆘𓆘Plugin : 𓆘𓆘`{input_str}`\n"
    outstr += f"𓆘𓆘Commands Available :𓆘𓆘 `{len(cmds)}`\n"
    category = getkey(input_str)
    if category is not None:
        outstr += f"𓆘𓆘Category :𓆘𓆘 `{category}`\n\n"
    for cmd in sorted(cmds):
        outstr += f"•  𓆘𓆘cmd :𓆘𓆘 `{cmdprefix}{cmd}`\n"
        try:
            outstr += f"•  𓆘𓆘info :𓆘𓆘 `{CMD_INFO[cmd][1]}`\n\n"
        except IndexError:
            outstr += "•  𓆘𓆘info :𓆘𓆘 `None`\n\n"
    outstr += f"𓆘𓆘👩‍💻 Usage : 𓆘𓆘 `{cmdprefix}help <command name>`\
        \n𓆘𓆘Note : 𓆘𓆘If command name is same as plugin name then use this `{cmdprefix}help -c <command name>`."
    return outstr


async def grpinfo():
    outstr = "𓆘𓆘Plugins in Catuserbot are:𓆘𓆘\n\n"
    outstr += f"𓆘𓆘👩‍💻 Usage : 𓆘𓆘 `{cmdprefix}help <plugin name>`\n\n"
    category = ["admin", "bot", "fun", "misc", "tools", "utils", "extra"]
    if Config.BADCAT:
        category.append("useless")
    for cat in category:
        plugins = GRP_INFO[cat]
        outstr += f"𓆘𓆘{hemojis[cat]} {cat.title()} 𓆘𓆘({len(plugins)})\n"
        for plugin in plugins:
            outstr += f"`{plugin}`  "
        outstr += "\n\n"
    return outstr


async def cmdlist():
    outstr = "𓆘𓆘Total list of Commands in your Catuserbot are :𓆘𓆘\n\n"
    category = ["admin", "bot", "fun", "misc", "tools", "utils", "extra"]
    if Config.BADCAT:
        category.append("useless")
    for cat in category:
        plugins = GRP_INFO[cat]
        outstr += f"𓆘𓆘{hemojis[cat]} {cat.title()} 𓆘𓆘 - {len(plugins)}\n\n"
        for plugin in plugins:
            cmds = PLG_INFO[plugin]
            outstr += f"• 𓆘𓆘{plugin.title()} has {len(cmds)} commands𓆘𓆘\n"
            for cmd in sorted(cmds):
                outstr += f"  - `{cmdprefix}{cmd}`\n"
            outstr += "\n"
    outstr += f"𓆘𓆘👩‍💻 Usage : 𓆘𓆘 `{cmdprefix}help -c <command name>`"
    return outstr
