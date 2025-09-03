import datetime
import discord
from discord.ext import commands
from asyncio import sleep


class BaseCommands(commands.Cog):
    def __init__(self, client, stt):
        self.client = client
        self.stt = stt

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(embed=discord.Embed(title=f"Help", description=f"> :nerd~1: Help\n"
                                                                      f"{ctx.author.name}\n"
                                                                      f"invite_link\n"
                                                                      f"clear\n"
                                                                      f"ping\n"
                                                                      f"kick\n"
                                                                      f"ban\n"
                                                                      f"moveall\n"
                                                                      f"avatar\n"
                                                                      f"stats\n"
                                                                      f"userinfo\n"
                                                                      f"serverinfo\n"
                                                                      f"uptime\n"
                                                                      f"suggest\n"
                                                                      f"helpme\n"
                                                                      f"lock\n"
                                                                      f"unlock\n"
                                                                      f"unban\n"
                                                                      f"mute\n"
                                                                      f"unmute\n"
                                                                      f"role\n"
                                                                      f"join\n"
                                                                      f"send\n"
                                                                      f"> Prefix -->  x!", color=0x0B5394))

    @commands.command()
    async def stats(self, ctx: commands.Context):
        await ctx.send(embed=
                       discord.Embed(title=f"Bot stats",
                                     description=f"servers : {len(self.client.guilds)}\n"
                                                 f"members : {len(ctx.guild.members)}\n"
                                                 f"ping : {round(self.client.latency * 1000)}\n"
                                                 f"real members : {round(len([m for m in ctx.guild.members if not m.bot]))}"
                                                 f"x!help for commands", color=0x0B5394)
                       )

    @commands.command()
    async def invite_link(self, ctx: commands.Context):
        await ctx.send("""https://discord.gg/BzY7hf2ACD""")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        try:
            s = await ctx.send(embed=discord.Embed(title=f"Ping", description=f"perfoming test ...\n"
                                                                              f"x!help for commands",
                                                   color=0x0B5394)
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)

            s = await ctx.send(
                embed=discord.Embed(title=f"Ping", description=f"test 1 : {round(self.client.latency * 1000)} ms\n"
                                                               f"test 2 : {round(self.client.latency * 1000)} ms\n"
                                                               f"test 3 : {round(self.client.latency * 1000)} ms\n"
                                                               f"x!help for commands",
                                    color=0x0B5394)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)

            s = await ctx.send(embed=discord.Embed(title=f"Ping", description=f"Done ?\n"
                                                                              f"x!help for commands",
                                                   color=0x57ff36)
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        except discord.errors.Forbidden:
            s = await ctx.send(embed=discord.Embed(title=f"Error",
                                                   description=f"please try later\n"
                                                               f"x!help for commands",
                                                   color=0x0B5394)

                               )
            await sleep(5)
            await s.delete()
            await sleep(5)

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        await ctx.send(embed=discord.Embed(title="Uptime",
                                           description=f"{datetime.datetime.now(datetime.UTC) - self.stt}",
                                           color=discord.Colour.blue()))

    @commands.command()
    async def server_list(self, ctx: commands.Context):
        if ctx.author.id == 1042894447815430229:
            s = await ctx.send(embed=discord.Embed(title=f"server list",
                                                   description=f"```\n{"\n".join(f"{x}" for x in self.client.guilds)}\n```\n"
                                                                                     f"x!help for commands",
                                                   color=0x57ff36)
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(
                embed=discord.Embed(title=f"Only dev can use this.", description=f"this is only owner command .\n"
                                                                                 f"x!help for commands", color=0x57ff36)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)