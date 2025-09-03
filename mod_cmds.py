import discord
from discord.ext import commands
from asyncio import sleep


class ModCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx: commands.Context, amount=1):
        await ctx.message.delete()

        if ctx.author.guild_permissions.kick_members:
            if amount > 300 or amount < 1:
                s = await ctx.send(
                    embed=discord.Embed(title=f"Faild!",
                                        description=f"Faild!\n"
                                                    f"reason : amount should be lower than 300 and higher than 1.\n"
                                                    f"x!help for commands .",
                                        color=0xFF0000)
                )

                await sleep(5)
                await s.delete()
                await sleep(5)

                return

            await ctx.send(embed=discord.Embed(title=f"doing your request...",
                                               description=f"doing your request...\n"
                                                           f"x!help for commands.",
                                               color=0x0B5394))

            await ctx.channel.purge(limit=amount + 1)

            s = await ctx.send(embed=discord.Embed(title=f"done", description=f"done!\n"
                                                                              f"deleted {amount} messages in "
                                                                              f"{ctx.channel.name} text channel.\n"
                                                                              f"x!help for commands.",
                                                   color=0x57ff36))

            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(
                embed=discord.Embed(title=f"access denied", description=f"your access denied !\n"
                                                                        f"reason : you dont have "
                                                                        f"**kick_members** permission .\n"
                                                                        f"x!help for commands .",
                                    color=0xFF0000)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)

    @clear.error
    async def clear_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                                   description=f"x!clear <amount> ",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        elif discord.errors.Forbidden:
            s = await ctx.send(embed=discord.Embed(title="no perm",
                                                   description=f"I dont have access to join that channel.",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)

    @commands.command()
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = "no reason"):
        await ctx.message.delete()

        if member.id == ctx.author.id:
            s = await ctx.send(
                embed=discord.Embed(title=f":|", description=f"Why you wanna kick yourself?\n"
                                                             f"x!help for commands",
                                    color=0x57ff36)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)

            return

        if ctx.author.guild_permissions.kick_members:
            s = await ctx.send(
                embed=discord.Embed(title=f"User Kicked", description=f"kicked : {member.display_name}\n"
                                                                      f"by : {ctx.author.display_name}\n"
                                                                      f"reason : {reason}",
                                    color=0x57ff36)
            )

            await member.kick(reason=reason)
            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(
                embed=discord.Embed(title=f"access denied", description=f"your access denied !\n"
                                                                        f"reason : you dont have "
                                                                        f"**kick_members** permission .\n"
                                                                        f"x!help for commands .",
                                    color=0xFF0000)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)

    @kick.error
    async def kick_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MemberNotFound):
            s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                                   description=f"x!kick @member ",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        elif isinstance(error, commands.MissingRequiredArgument):
            s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                                   description=f"x!kick @member ",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        elif discord.errors.Forbidden:
            s = await ctx.send(embed=discord.Embed(title="no perm",
                                                   description=f"I dont have ban access.",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)

    @commands.command()
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: str = "no reason"):
        await ctx.message.delete()

        if member.id == ctx.author.id:
            s = await ctx.send(
                embed=discord.Embed(title=f":|", description=f"Why you wanna ban yourself?\n"
                                                             f"x!help for commands",
                                    color=0x57ff36)
            )

            await sleep(5)
            await s.delete()
            await sleep(5)

            return

        if ctx.author.guild_permissions.ban_members:
            s = await ctx.send(embed=discord.Embed(title=f"User banned", description=f"banned : {member.display_name}\n"
                                                                                     f"by : {ctx.author.display_name}\n"
                                                                                     f"reason : {reason}",
                                                   color=0x57ff36)
                               )

            await member.ban(reason=reason)
            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(embed=discord.Embed(title=f"access denied", description=f"your access denied !\n"
                                                                                       f"reason : you dont have"
                                                                                       f"**ban_members** permission.\n"
                                                                                       f"x!help for commands .",
                                                   color=0xFF0000)
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)

    @ban.error
    async def ban_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MemberNotFound):
            s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                                   description=f"x!ban @member ",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        elif isinstance(error, commands.MissingRequiredArgument):
            s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                                   description=f"x!ban @member ",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)
        elif discord.errors.Forbidden:
            s = await ctx.send(embed=discord.Embed(title="no perm",
                                                   description=f"I dont have ban access.",
                                                   colour=discord.Colour.blue())
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)



    @commands.command()
    async def lock(self, ctx: commands.Context, channel: discord.TextChannel = None):
        await ctx.message.delete()

        try:
            if ctx.author.guild_permissions.manage_channels:
                channel = channel or ctx.channel
                overwrite = channel.overwrites_for(ctx.guild.default_role).send_messages = False

                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

                s = await ctx.send(embed=discord.Embed(title=f"Locked.", description=f"by {ctx.author.display_name}\n"
                                                                                     f"x!help for commands .",
                                                       color=0xFF0000)
                                   )

                await sleep(5)
                await s.delete()
                await sleep(5)
            else:
                s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                            f"reseon : you dont have "
                                                                                            f"**ban_members** "
                                                                                            f"permission .\n"
                                                                                            f"x!help for commands .",
                                                       color=0xFF0000)
                                   )

                await sleep(5)
                await s.delete()
                await sleep(5)

        except discord.errors.Forbidden:
            await ctx.send(embed=discord.Embed(title=f"No perm",
                                  description=f"I have no permission to manage channels\n"
                                              f"x!help for commands .", color=0xFF0000))

    @commands.command()
    async def unlock(self, ctx: commands.Context, channel: discord.TextChannel = None):
        await ctx.message.delete()

        try:
            if ctx.author.guild_permissions.manage_channels:
                channel = channel or ctx.channel
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = True

                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                await ctx.send(f"{channel.mention} unlocked!")
            else:
                s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                            f"reseon : you dont have "
                                                                                            f"**ban_members** "
                                                                                            f"permission .\n"
                                                                                            f"x!help for commands .",
                                                       color=0xFF0000)
                                   )

                await sleep(5)
                await s.delete()
                await sleep(5)
        except discord.errors.Forbidden:
            await ctx.send(embed=discord.Embed(title=f"I need access",
                                  description=f"I have no no permission to manage channels\n"
                                              f"x!help for commands .", color=0xFF0000))

    @commands.command()
    async def role(self, ctx: commands.Context, args, member: discord.Member, role: discord.Role):
        await ctx.message.delete()

        if not ctx.author.guild_permissions.manage_channels:
            s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                        f"reseon : you dont have "
                                                                                        f"**ban_members** permission "
                                                                                        f".\n"
                                                                                        f"x!help for commands .",
                                                   color=0xFF0000)
                               )

            await sleep(5)
            await s.delete()
            await sleep(5)

        args = args.lower()

        if args == 'add':
            if role == ctx.author.top_role:
                s = await ctx.send("his weanie is much bigger than yours is")

                await sleep(5)
                await s.delete()
                await sleep(5)

                return None

            if role in member.roles:
                s = await ctx.send("he got this in his basement, already")

                await sleep(5)
                await s.delete()
                await sleep(5)

                return None

            if role.position >= ctx.guild.me.top_role.position:
                s = await ctx.send(f"his weanie is much bigger than mine is")

                await sleep(5)
                await s.delete()
                await sleep(5)

                return None

            await member.add_roles(role)

            s = await ctx.send(f"I've added {member.mention} the role {role.mention}")

            await sleep(5)
            await s.delete()
            await sleep(5)

            return None

        elif args == 'remove':

            if role == ctx.author.top_role:
                return await ctx.send("his weanie is much bigger than yours is")

            if role not in member.roles:
                return await ctx.send("he got none of this in his basement, LeAvE hIm AlOnE")

            if role.position >= ctx.guild.me.top_role.position:
                return await ctx.send(f"his weanie is much bigger than mine is")

            await member.remove_roles(role)
            await ctx.send(f"I have removed {member.mention} the role {role.mention}")

        return None
