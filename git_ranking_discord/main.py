import commit
import discord

token = 'token'
client = discord.Client()


@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('git ranking'):
        print('git ranking 준비중')
        channel = message.channel

        rankingDic = commit.ranking()
        say = "```\n"
        for i in rankingDic:
            say = say + f"{i} : {rankingDic[i]} commit\n"
        say = say + "```"
        await channel.send(say)

    if message.content.startswith('!git '):
        channel = message.channel
        print('!git 준비중')
        message.content = message.content.replace('!git ', '')
        try:
            commits = commit.commitNum(message.content)
            await channel.send(f'{message.content}님의 commit 수는 {commits}개 입니다')
        except AttributeError:
            await channel.send('없는 id 입니다.\n다시 검색해 주세요')


client.run(token)
