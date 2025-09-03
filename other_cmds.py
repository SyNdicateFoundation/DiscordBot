import discord
from discord.ext import commands

class OtherCmds(commands.Cog):
    def __init__(self, cl):
        self.client = cl

    @commands.command()
    async def avatar(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author

        await ctx.send(embed=discord.Embed(
            title="Avatar Link",
            url=member.avatar.url,
            colour=0xf9cb11
        ).set_author(
            name=f"{member}",
            icon_url=member.avatar.url).set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar.url
        ).set_image(url=member.avatar.url))

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx: commands.Context):
        guild_roles = len(ctx.guild.roles)
        guild_categories = len(ctx.guild.categories)
        guild_members = len(ctx.guild.members)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        channels = text_channels + voice_channels

        serverinfo = (discord.Embed(colour=discord.Colour.blue()
                                    ).add_field(name="Server Name", value=f"{ctx.guild.name}"
                                                ).add_field(name="Server ID", value=f"{ctx.guild.id}"
                                                            ).add_field(name="Server Owner", value=f"{ctx.guild.owner}")
                      ).add_field(name="Boosts", value=f"{ctx.guild.premium_subscription_count}"
                                  ).add_field(name="Channels", value=f"{channels}"
                                              ).add_field(name="Roles", value=f"{guild_roles}"
                                                          ).add_field(name="Categories",
                                                                      value=f"{guild_categories} Categories"
                                                                      ).add_field(name="Members",
                                                                                  value=f"{guild_members}")

        if ctx.guild.icon:
            serverinfo.set_thumbnail(url=ctx.guild.icon.url)

        await ctx.send(embed=serverinfo)

    @commands.command()
    async def vote(self, ctx: commands.Context, *, message=None):
        await ctx.message.delete()

        if message is None:
            await ctx.send(f"no message to vote for.")
        else:
            s = discord.Embed(title=f"Vote By {ctx.author}", colour=discord.Colour.blue())
            s.add_field(name="Vote For :", value=f"{message}")

            if ctx.guild.icon:
                s.set_thumbnail(url=ctx.guild.icon.url)

            ss = await ctx.send(embed=s)

            await ss.add_reaction('\u2705')
            await ss.add_reaction('\u274c')

    @commands.command()
    async def send(self, ctx: commands.Context, *, message=None):
        await ctx.message.delete()

        if message is None:
            await ctx.send("No message to send.")
        elif ctx.author.guild_permissions.manage_channels:
            s = discord.Embed(title=f"A message From {ctx.guild.name}", colour=discord.Colour.blue()).add_field(
                name="Message :", value=message)

            if ctx.guild.icon:
                s.set_thumbnail(url=ctx.guild.icon.url)

            await ctx.send(embed=s)

    @commands.command()
    async def helpme(self, ctx, *, message=None):
        if message is None:
            await ctx.send(f"there is no message.")
        else:
            await ctx.send("Thank you for reporting this helpme.")

            channel = self.client.get_channel(1195763758962843738)
            s = discord.Embed(title=f"helpme by {ctx.author}", colour=discord.Colour.blue())
            s.add_field(name="Server", value=f"{ctx.guild.name}")
            s.add_field(name="helpme", value=f"{message}")

            if ctx.guild.icon:
                s.set_thumbnail(url=ctx.guild.icon.url)

            await channel.send(embed=s)

    @commands.command()
    async def suggest(self, ctx: commands.Context, *, message=None):
        if message is None:
            await ctx.send(f"there is no message.")
        else:
            await ctx.send("Thank you for giving a suggestion.")

            channel = self.client.get_channel(1195764301538000997)
            s = discord.Embed(title=f"suggest by {ctx.author}", colour=discord.Colour.blue())
            s.add_field(name="Server", value=f"{ctx.guild.name}")
            s.add_field(name="suggest", value=f"{message}")

            if ctx.guild.icon:
                s.set_thumbnail(url=ctx.guild.icon.url)

            ss = await channel.send(embed=s)

            await ss.add_reaction('\u2705')
            await ss.add_reaction('\u274c')

    @commands.command()
    async def bug(self, ctx, *, message=None):
        if message is None:
            await ctx.send(message="there is no message.")
        else:
            await ctx.send(message="Thank you for reporting this bug.")

            channel = self.client.get_channel(1195763719620272249)
            embed2 = discord.Embed(title=f"Bug reported by {ctx.author}", colour=discord.Colour.blue())
            embed2.add_field(name="Server", value=f"{ctx.guild.name}")
            embed2.add_field(name="Bug", value=f"{message}")

            if ctx.guild.icon:
                embed2.set_thumbnail(url=ctx.guild.icon.url)

            await channel.send(embed=embed2)