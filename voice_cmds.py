import discord
from discord.ext import commands
from asyncio import sleep


class VoiceCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['move'])
    async def moveall(self, ctx: commands.Context):
        await ctx.message.delete()

        if not ctx.author.guild_permissions.move_members:
            s = await ctx.send(
                embed=discord.Embed(title=f"Faild!", description=f"Join a voice first or check your perms.\n",
                                    color=0x57ff36)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)
            return
        try:
            if ctx.author.voice is not None:
                moved_members = []

                for voice_channel in ctx.guild.voice_channels:

                    for member in voice_channel.members:
                        await member.move_to(ctx.author.voice.channel)
                        moved_members.append(member)
                s = await ctx.send(
                    embed=discord.Embed(title=f"Users moved", description=f"channel : {ctx.author.voice.channel}\n"
                                                                          f"by : {ctx.author.display_name}\n",
                                        color=0x57ff36)
                )

                await sleep(5)
                await s.delete()
                await sleep(5)
            else:
                s = await ctx.send(
                    embed=discord.Embed(title=f"Faild!", description=f"Join a voice first or check your perms.\n",
                                        color=0x57ff36)
                )

                await sleep(5)
                await s.delete()
                await sleep(5)
        except discord.errors.Forbidden:
            s = await ctx.send(
                embed=discord.Embed(title=f"No perm", description=f"I don't have **move members** perm\n",
                                    color=0x57ff36)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)

    @commands.command()
    async def join(self, ctx: commands.Context):
        await ctx.message.delete()

        if ctx.author.voice:
            s = await ctx.send(embed=discord.Embed(title=f"connected", description=f"voice connected\n"
                                                                                   f"x!help for commands .",
                                                   color=0xFF0000
                                                   ))

            await s.add_reaction('\u2705')
            await s.add_reaction('\u274c')
            await ctx.author.voice.channel.connect()
        else:
            s = await ctx.send(
                embed=discord.Embed(title=f"you arent in a voice", description=f"join a voice for connect\n"
                                                                               f"x!help for commands .",
                                    color=0xFF0000))

            await s.add_reaction('\u2705')
            await s.add_reaction('\u274c')

    @commands.command()
    async def leave(self, ctx: commands.Context):
        await ctx.message.delete()

        s = await ctx.send(embed=discord.Embed(title=f"disconnected", description=f"leaved\n"
                                                                                  f"x!help for commands .",
                                               color=0xFF0000))

        await ctx.voice_client.disconnect(force=True)
        await s.add_reaction('\u2705')
        await s.add_reaction('\u274c')
