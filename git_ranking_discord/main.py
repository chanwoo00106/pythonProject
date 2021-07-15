import commit
import discord

token = 'discord토큰'
idList = ['git id list']
nameDic = {'name': 'class number'}
sayList = []


client = discord.Client()
a = commit.commitsNumber(idList)


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
        await channel.send('git ranking 준비중')
        commitList = a.main()
        
        for i in range(0, len(commitList)):
            max_value = max(commitList)
            
            sayList.append(f"{i + 1}. {nameDic[commitList.index(max_value) + 1]} : {max_value}개")
            commitList[commitList.index(max_value)] = -100
        
        say = f"""```{sayList[0]}
{sayList[1]}
{sayList[2]}
{sayList[3]}
{sayList[4]}```"""
        await channel.send(say)
        print('완료')
    
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
