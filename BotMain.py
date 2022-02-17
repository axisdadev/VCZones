import string
import hikari
import lightbulb
bot = lightbulb.BotApp(token='OTQzMDM2NDA3NDQwNjMzOTA2.YgtNGA.rw4SFS7h6WjMpbhq6QJV1ZJhjaY',
default_enabled_guilds=(908087465380814868))

@bot.listen(hikari.StartedEvent)
async def on_start(event):
    activityVar = hikari.Activity(name="For VcZone Requests", type=hikari.ActivityType.WATCHING)
    await bot.update_presence(status="dnd",activity=activityVar)
    print("Bot Has Started Up!")


@bot.command
@lightbulb.option("clientid","Users Client ID",type=string)
@lightbulb.option("channelid","Voice Call ChannelID",type=string)
@lightbulb.command("addtovc","Moves User To Voice Call")
@lightbulb.implements(lightbulb.SlashCommand)


async def vc_command(ctx):
    await bot.rest.edit_member(int(908087465380814868), int(ctx.options.clientid), voice_channel=int(ctx.options.channelid))
    await ctx.respond("Sucessfully Connected User, To VC!")

    


bot.run()
