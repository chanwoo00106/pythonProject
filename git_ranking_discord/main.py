import commit
import discord
import datetime
import asyncio

token = 'token'
client = discord.Client()


complateDay = False

async def alarm():
    global complateDay
    user = client.get_channel('your channel id')

    while True:
        while not complateDay:
            now = datetime.datetime.now()
            if now.hour >= 19 and (now.minute == 0 or now.minute == 30):
                await user.send('커밋해!!!')
                await asyncio.sleep(60)
            elif not complateDay and now.minute == 0:
                await user.send('커밋해라!! 인간')
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(1)
        
        while complateDay:
            now = datetime.datetime.now()
            if now.hour == 0:
                complateDay = False
                await asyncio.sleep(1)
            else:
                await asyncio.sleep(1)


@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    client.loop.create_task(alarm())


@client.event
async def on_message(message):
    global complateDay
    if message.author.bot:
        return None
    
    if message.content.startswith('!커밋 완료') and message.author.id == 'your id' and not complateDay:
        complateDay = True
        channel = message.channel
        await channel.send('확인!')
        

    if message.content == 'git ranking':
        print('git ranking 준비중')
        channel = message.channel

        rankingDic = commit.ranking()
        j = 1
        say = ""
        for i in rankingDic:
            say = say + f"{j}. {i} : {rankingDic[i]} commit\n"
            j = j + 1
        embed = discord.Embed(title="1-2 Commit Ranking", description=say, color=0xdff9fb)
        await channel.send(embed=embed)

    if message.content.startswith('!git '):
        channel = message.channel
        print('!git 준비중')
        message.content = message.content.replace('!git ', '')
        try:
            commits = commit.commitNum(message.content)
            embed = discord.Embed(title=f'{message.content}님의 commit 수는 {commits}개 입니다', color=0xdff9fb)
            await channel.send(embed=embed)
        except AttributeError:
            await channel.send('없는 id 입니다.\n다시 검색해 주세요')

client.run(token)
