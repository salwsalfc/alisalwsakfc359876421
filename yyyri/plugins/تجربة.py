import io
import sys
import traceback

from ..helpers.utils import _format
from . import 𓆘


@sbb_b.ar_cmd(pattern="امر التجربة")
async def hi(event):
    await edit_or_reply(
        event,
        "𓆘𓆘[𓏺 𓆋 ســـورس آلَفــــرآعـــنه 𓆋 ˼](t.me/wasit_go)\n⎈━━━⊶𐂡•علاوي•𐂡⊷━━━⎈𓆘𓆘\n\n الامر: `.تجربة` + كود برمجي\n- يقوم بتشغيل الكود و أظهار النتيجة",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="تجربة(?:\s|$)([\s\S]𓆘)")
async def _(event):
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await edit_delete(event, "𓆘𓆘▿∲ يجب عليك كتابة الكود مع الامر اولا𓆘𓆘")
    cmd = (
        cmd.replace("sendmessage", "send_message")
        .replace("sendfile", "send_file")
        .replace("editmessage", "edit_message")
    )
    jmthon = await edit_or_reply(event, "𓆘𓆘▿∲ جار التشغيل أنتظر قليلًا𓆘𓆘")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = (
        f"𓆘𓆘•  الكود : 𓆘𓆘\n```{cmd}``` \n\n𓆘𓆘•  النتيجة : 𓆘𓆘\n```{evaluation}``` \n"
    )
    await edit_or_reply(
        jmthon,
        text=final_output,
        aslink=True,
        linktext=f"𓆘𓆘•  الكود : 𓆘𓆘\n```{cmd}``` \n\n𓆘𓆘•  النتيجة : 𓆘𓆘\n",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"𓆘𓆘▿∲ تم بنجاح تشغيل وتجربة امر {cmd}𓆘𓆘."
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        (
            "async def __aexec(message, event , reply, client, p, chat): "
            + "".join(f"\n {l}" for l in code.split("\n"))
        )
    )

    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )
