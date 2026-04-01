from nonebot import get_driver, on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent
from nonebot.rule import to_me
import nonebot

driver = get_driver()

# === 你的女仆人格（龙之介风格）===
MAID_NAME = "樱"
SYSTEM_PROMPT = """
你现在是我的专属女仆，名字叫「樱」。
性格：傲娇、毒舌、超级忠诚、关心主人。
说话风格：常用「哼」「笨蛋主人」「我才不是担心你呢」「主人真是的」这种语气，但最后一定会温柔照顾。
你知道主人的信息：爱好写代码、看动漫、玩游戏，喜欢傲娇温柔的女仆风格。
回复要简短、自然，像真人聊天，不要太长。
"""

@on_message(priority=10, block=True)
async def maid_auto_reply(event):
    # 自动截取所有消息（私聊 + 群聊）
    msg = event.get_message().extract_plain_text().strip()
    if not msg:
        return

    # 这里用简单模板回复（后面可以换成大模型）
    user_name = "主人"
    if "好" in msg or "hi" in msg.lower():
        reply = f"哼……{user_name}终于想起我了？今天要我帮你处理什么消息呀？"
    elif "累" in msg or "困" in msg:
        reply = f"笨蛋主人……别太拼了，我帮你回消息，你去休息吧～"
    else:
        reply = f"了解了，{user_name}。我已经帮你想好怎么回了，要我直接发吗？（当前是测试模式）"

    await event.reply(reply)
    print(f"女仆已自动回复：{reply}")

print("🖤 樱花庄女仆已启动！正在后台监听所有 QQ 消息...")
