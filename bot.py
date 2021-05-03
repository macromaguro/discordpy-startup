import discord

client = discord.Client()

@client.event
async def on_ready():

@client.event
async def on_message(message):
    if message.author.bot:
        return
    GLOBAL_CH_NAME = "ポケモンチャット" # グローバルチャットのチャンネル名
    GLOBAL_WEBHOOK_NAME = "人狼online" # グローバルチャットのWebhook名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する
        await message.delete()

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        for channel in global_channels:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)

            if webhook is None:
                # そのチャンネルに hoge-webhook というWebhookは無かったので無視
                continue
            await webhook.send(content=message.content,
                username=message.author.name,
                avatar_url=message.author.avatar_url_as(format="png
client.run("ODM4NjQzOTQwMjkwNDYxNzI2.YI-GCA.-UyqX6GoSk9P9TmZ7czrWQHsyxM")
