from asyncio import sleep

from googletrans import LANGUAGES, Translator

from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply
from . import deEmojify


async def getTranslate(text, 𓆘𓆘kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, 𓆘𓆘kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result


@sbb_b.ar_cmd(pattern="ترجمة ([\s\S]𓆘)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ar"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        return await edit_delete(
            event, "`.ترجمة + كود الترجمه` بالرد على رساله", time=5
        )
    text = deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"𓆘𓆘تم الترجمه من  {LANGUAGES[translated.src].title()} الى {LANGUAGES[lan].title()}𓆘𓆘\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, f"𓆘𓆘خطأ:𓆘𓆘\n`{exc}`", time=5)
