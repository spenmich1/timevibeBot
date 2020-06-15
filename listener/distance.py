import discord
from discord.ext import commands
from discord.utils import get
import arrow as ar
import datetime as dt
from dotenv import load_dotenv
import settings
import time
import sys
import asyncio

from master import get_prefix
bot = commands.Bot(command_prefix=get_prefix)
token = settings.TOKEN
botColor = 0x176BD3

month = ["months", "month", "mo", "mos"]
week = ["weeks", "week", "wk", "wks"]
day = ["days", "day", "dy", "dys"]
hour = ["hours", "hour", "hr", "hrs"]
min = ["minutes", "minute", "min", "mins"]

# difference algorithm
def difference(self, initial: str, method: str):
    now = ar.utcnow()
    difference = initial - now
    inFormat = method.lower()
    difference = difference.days
    if inFormat in ["years", "year", "yr", "yrs"]:
        differenceQ = (divmod(difference, 365))
        if differenceQ[0] == 1:
            year = "year"
        else:
            year = "years"
        differenceQ2 = (divmod(differenceQ[1], 30))
        if differenceQ2[0] == 1:
            month = "month"
        else: 
            month = "months"
        differenceQ3 = (divmod(differenceQ2[1], 7))
        if differenceQ3[0] == 1:
            week = "week"
        else: 
            week = "weeks"
        if differenceQ3[1] == 1:
            day = "day"
        else:
            day = "days"
        string = "Time until: {0}: \n{1} {2}, {3} {4}, {5} {6}, and {7} {8}".format(initial.format("MMMM DD, YYYY"), str(differenceQ[0]), year, str(differenceQ2[0]), month,str(differenceQ3[0]) , week, str(differenceQ3[1], day))
        return string, initial.format("MMMM DD, YYYY:")
    elif inFormat in ["months", "month", "mo", "mos"]:
        differenceQ = (divmod(difference, 30))
        differenceQ2 = (divmod(differenceQ[1], 7))
        if differenceQ[0] == 1:
            month = "month"
        else: 
            month = "months"
        differenceQ3 = (divmod(differenceQ2[1], 7))
        if differenceQ2[0] == 1:
            week = "week"
        else: 
            week = "weeks"
        if differenceQ2[1] == 1:
            day = "day"
        else:
            day = "days"
        string = "Time until: {0}: \n{1} {2}, {3} {4}, {5} {6}".format(initial.format("MMMM DD, YYYY"), str(differenceQ[0]), month, str(differenceQ2[0]), week, str(differenceQ2[1]), day)
        return string, initial.format("MMMM DD, YYYY:")
    elif inFormat in ["weeks", "week", "wk", "wks"]:
        differenceQ = (divmod(difference, 7))
        if differenceQ[0] == 1:
            week = "week"
        else: 
            week = "weeks"
        if differenceQ[1] == 1:
            day = "day"
        else:
            day = "days"
        string = "Time until" + initial.format("MMMM DD, YYYY: \n") + str(differenceQ[0]) + " weeks and " + str(differenceQ[1]) + " days."
        string = "Time until: {0}: \n{1} {2}, {3} {4}".format(initial.format("MMMM DD, YYYY"), str(differenceQ[0]), week, str(differenceQ[1]), day)
        return string, initial.format("MMMM DD, YYYY:")
    elif inFormat in ["days", "day", "dy", "dys"]:
        differenceQ = (divmod(difference, 1))
        string = "Time until: "+ initial.format("MMMM DD, YYYY: \n") + str(differenceQ[0]) + " days."
        return string, initial.format("MMMM DD, YYYY:")
    else: 
        print("error")
    
class DistanceListener(commands.Cog):
    #difference command
    @bot.command()
    async def dis(self, ctx, arg1:str, arg2:str):
        now = ar.utcnow()
        try:
            startDateParsed = ar.get(arg1, 'DD/MM/YYYY')
        except ar.ParserError:
            print("error")
        string, date = difference(self, startDateParsed, arg2)
        embed = discord.Embed(title="Days until: {0}".format(date), colour=discord.Colour(botColor))
        embed.add_field(name="⏰", value=string)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(DistanceListener(client))
    print('DistanceListener is Loaded') 