import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='au.')
@bot.event
async def on_ready():
    print('we have logged in as{0.user}'.format(bot))

@bot.command()
async def newGame(ctx,*args):
    global currentGameMsg
    emojis = ["🥼","🏈","🐜",":flag_eu:",":blue_circle:",":crocodile:",":green_circle:",":yellow_heart:",":orange_heart:",":purple_heart:",":heart:",":ballet_shoes:"]
    print(args)
    msg = ''
    if len(args)>0:
        msg = 'Room code is ' +args[0]+'\n'
    msg+='React with your Color Dipshits'
    currentGameMsg = await ctx.send(msg)
    for x in emojis:
        await currentGameMsg.add_reaction(x)
    #await currentGameMsg.add_reaction("<:YellowCircle:758723895057449011>")

@bot.command()
async def changePrefix(ctx, *args):
    if len(args) == 0:
        await ctx.send("requires argument to change prefix")
        return
    bot.command_prefix = args[0]


bot.run('NzU4MzI1MjExMTc0NjY2MzEx.X2tTYw.dQpq5IkRzmyB4c918EOLeLeNhOY')

#blue
#green
#purple
#orange
#white
#black
#magenta
#lime
#yellow
#brown
#cyan
#red