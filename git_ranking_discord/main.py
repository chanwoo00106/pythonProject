import commit
import discord
import datetime
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.environ.get('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")


@client.event
async def on_message(message):
    global complateDay
    if message.author.bot:
        return None

    if message.content.startswith('!git ') or message.content.startswith('!햣 '):
        channel = message.channel
        print('!git 준비중')
        message.content = message.content.replace(
            '!git ', '').replace('!햣 ', '')
        try:
            commits = commit.commitNum(message.content)
            embed = discord.Embed(
                title=f'{message.content}님의 commit 수는 {commits[0]}개 입니다', color=0xdff9fb)
            await channel.send(embed=embed)
            await channel.send(commits[1])
        except TypeError:
            await channel.send('없는 id 입니다.\n다시 검색해 주세요')

client.run(TOKEN)
