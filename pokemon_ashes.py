from pprint import pprint
import discord
from discord.ext import commands
from discord import app_commands
import os
import random
import json
import pyrebase
import asyncio
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os 

load_dotenv()

token = os.environ['token']
config = os.environ['config']
config = json.loads(config)
email = os.environ.get('email')
password = os.environ.get('password')
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()



number = [5,15,11,26,30]
ar = []
wait = [5]
owner = ["407914192105111563"]
client = commands.Bot(command_prefix='p',intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence( status=discord.Status.do_not_disturb,activity=discord.Game('Just a simple botto') )
#    await client.tree.sync()
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_guild=True)
async def redirect(ctx,channeel):
    print(channeel)
    cid = ''.join( d for d in channeel if d.isdigit() )
    idd = int( cid )
    print(idd)
    channel1 = client.get_channel(idd)
    print(channel1)
    guild_id = ctx.message.guild.id
    print(guild_id)
    checkkk = db.child( "servers" ).child("{}".format(guild_id)).get().val()
    print(checkkk)
    if str(channel1) != "None":
     if str(checkkk) == "None":
        ok = "{}".format(idd)
        db.child( "servers" ).child("{}".format(guild_id)).set(ok)
        print( "ok" )
        await ctx.send( "{}'s spawn channel set to {}".format( ctx.message.guild.name, channel1 ) )
     else:
        print("channel found")
        spawnchannel = int(checkkk)
        if spawnchannel == idd:
            print( "same channel" )
            ok1 = "{}".format(idd)
            db.child( "servers" ).child("{}".format(guild_id)).set(ok1)
            await ctx.send( "{}'s spawn channel again set to {}".format( ctx.message.guild.name, channel1 ) )
        elif spawnchannel != idd:
            print( "switching channel" )
            ok1 = "{}".format(idd)
            db.child( "servers" ).child( "{}".format( guild_id ) ).set( ok1 )
            await ctx.send( "{}'s spawn channel changed to {}".format( ctx.message.guild.name, channel1 ) )
        print(spawnchannel)

    elif str(channel1) == "None":
        embed = discord.Embed( title="Invalid CHANNEL Provided, note:channel id doesnt work.", description="Please use predirect #channel",
                               color=0xff00f6 )
        await ctx.send( embed=embed )

@redirect.error
async def redirect_error(ctx, error):
    if isinstance( error, commands.CommandInvokeError ):
        embed = discord.Embed( title="No SUCH CHANNEL FOUND", description="Please use predirect #channel", color=0xff00f6 )
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed( title="You can't use that command, you are missing permissions", description="",
                               color=0xff00f6 )
        await ctx.send( embed=embed )
    if isinstance(error,commands.MissingRequiredArgument):
        embed = discord.Embed( title="Please use predirect #channel", description="no channel provided",
                               color=0xff00f6 )
        await ctx.send( embed=embed )



@client.event
@commands.guild_only()
async def on_message(message):
    check = db.child( "spawns" ).child( "{}".format( message.channel.id ) ).get()
    gcheck = db.child( "servers" ).child( "{}".format( message.channel.guild.id ) ).get()
    if message.author != client.user and message.author.bot != True and str(message.channel.type) == "text" :
        ar.append(message.guild.id)
        lenth = len(ar)
        if lenth == wait[0]:
          gid = str(ar[-1])
          checkkk = db.child( "servers" ).child("{}".format(gid)).get()
          print("valuieeee",checkkk.val())
          if str(checkkk.val()) == "None":
                channel1 = message.channel
                print(message.channel)
                print("spawning in the channel itself")
          elif str(checkkk.val()) != "None":
                channe = int(checkkk.val())
                channel1 = client.get_channel(channe)
                print("name",channel1)

          chand = channel1
          wait.clear()
          wait1 = random.choice(number)
          wait.append(wait1)
          if str(channel1.id) == "754286362869497957":
              chances = ["0", "0", "0", "0", "0", "0","0", "0", "0", "0", "1"]
              print("popo")
          elif str(channel1.id) == "722805070445412385":
              chances = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","1"]
              print( "popo" )
          else:
           chances = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                     "1"]
          shiny_chance = random.choice( chances )
          ar.clear()
          pokemonnn = random.randint(0,809)
          pokemond = pokemonnn
          with open("mons.json", "r", encoding='utf8') as f:
                mons = json.load(f)
                mon1 = mons[pokemond-1]
                name = mon1["name"]["english"]
                name1 = mon1["name"]["french"]
                jap = mon1["name"]["japanese"][0]
                jap1 = mon1["name"]["japanese"][1]
                chin = mon1["name"]["chinese"]
                germ = mon1["name"]["german"]
                if "fun" in mon1["name"]:
                    another = mon1["name"]["fun"]
                elif "fun" not in mon1["name"]:
                    another = name
          print(pokemond)
          print(name.lower())
          if shiny_chance == "0":
                    embed = discord.Embed( title="**A wild pokemon appeared!**",
                                           description="Guess the pokémon аnd type pcatch <pokémon> to cаtch it!",
                                           color=0xC27C0E )
                    if pokemond < 10:
                        file = discord.File(
                            r"mon\poke_capture_000{}_000_mf_n_00000000_f_n.png".format(pokemond ),
                           # C:\Users\Homie\Documents\BOTS\pokemon_bot\mon\poke_capture_0050_000_mf_n_00000000_f_n.png
                            filename="image.png" )
                    elif pokemond > 9 and pokemond < 100:
                        file = discord.File(
                            r"mon\poke_capture_00{}_000_mf_n_00000000_f_n.png".format(pokemond ),
                            filename="image.png" )
                    elif pokemond > 99:
                        
                        file = discord.File(
                            r"mon\poke_capture_0{}_000_mf_n_00000000_f_n.png".format( pokemond ),
                            filename="image.png" )
                    embed.set_image( url="attachment://image.png" )
                    await asyncio.sleep(2)
                    spawn = await channel1.send( file=file, embed=embed )
                    arrary = {"{}".format(channel1.id): {"name": "{}".format( name ),
                                                      "id": "{}".format( pokemond ),
                                                      "shiny": "false"}}
                    db.child( "spawns" ).update( arrary )
          elif shiny_chance == "1":
                    embed = discord.Embed( title="**A wild pokemon appeared!**",
                                           description="Guess the pokémon аnd type pcatch <pokémon> to cаtch it!",
                                           color=0xC27C0E )
                    if pokemond < 10:
                        file = discord.File(
                            r"{}mon\poke_capture_000{}_000_mf_n_00000000_f_r.png".format( pokemond ),
                            filename="image.png" )
                    elif pokemond > 9 and pokemond < 100:
                        file = discord.File(
                            r"{}mon\poke_capture_00{}_000_mf_n_00000000_f_r.png".format( pokemond ),
                            filename="image.png" )
                    elif pokemond > 99:
                        file = discord.File(
                            r"{}mon\poke_capture_0{}_000_mf_n_00000000_f_r.png".format( pokemond ),
                            filename="image.png" )
                    embed.set_image( url="attachment://image.png" )
                    await asyncio.sleep( 2 )
                    await channel1.send( file=file, embed=embed )
                    arrary = {"{}".format(channel1.id): {"name": "{}".format( name ),
                                                      "id": "{}".format( pokemond ),
                                                      "shiny": "true"}}
                    db.child( "spawns" ).update( arrary )
    await client.process_commands(message)



@client.command()
async def spawn(ctx):
    if ctx.message.author.id == 407048494868856856:
       await ctx.send("Command is removed and deathy also can't use this")

@client.command(aliases=['Pokémon','pokémon'])
async def pokemon(ctx,stats):
    if stats == "--shiny":
     checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
     if checkkk.val() == None:
        await ctx.send( "Do pstart to start you pokemon journey " )
     else:
        all_users = db.child( "users" ).child( "{}".format(ctx.message.author.id) ).child( "pokemons" ).get()
        result = []
        k = 0
        for user in all_users.each():
            dict = user.val()
            if "true" in dict["shiny"]:
                    k = k + 1
                    mon_name = dict["name"]
                    mon_number = dict["number"]
                    mon_iv = dict["IV"]
                    mon_level = dict["level"]
                    array = {
                        "name": "**✨{}**|Level:{}|Number:{}|IV:{}".format( mon_name, mon_level, mon_number,
                                                                            mon_iv ),
                        "number":"{}".format(k)
                    }
                    result.append( array )
        print( len( result ) )
        divide = len( result ) / 20
        stri = str( divide )
        print( divide )
        if type( divide ) == int or stri.endswith( ".0" ):
            divide = int( divide )
        elif type( divide ) == float:
            divide = divide + 1
        print( divide )
        i = 0
        lists = []
        while i < int( divide ):
            lists.append( [] )
            i += 1

        z = 0
        length = len( result )
        print( length )
        len1 = int( length )
        while length > 0:
            if length > 20:
                lists[z].append( result[:20] )
                del result[:20]
            elif length <= 20:
                lists[z].append( result )
            length = length - 20
            z += 1

        ress = lists[0][0]
        print( ress )
        resultant = "\n ".join( x["name"] for x in ress )
        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                               color=0x2ECC71 )
        if len1 <= 20:
         embed.set_footer(text="Showing {}-{} out of {} pokémon matching this search.".format(1,len1, len1 ) )
        elif len1 >20:
            embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format( 1,20, len1 ) )
        sent = await ctx.send( embed=embed )
        await sent.add_reaction( "<:left:725668526869708881>" )
        await sent.add_reaction( "<:right:725668611615621133>" )
        if len1<=20:
            return
        elif len1 > 20:
         c = 0
         def check(reaction, user):
            return user == ctx.message.author and str( reaction.emoji ) == '<:right:725668611615621133>' or str(reaction.emoji ) == '<:left:725668526869708881>'

         while True:
            try:
                reaction, user = await client.wait_for( 'reaction_add', timeout=120.0, check=check )
            except asyncio.TimeoutError:
                return
            if str( reaction.emoji ) == '<:right:725668611615621133>':
                try:
                    c = c + 1
                    ress = lists[c][0]
                    resultant = "\n ".join( x["name"] for x in ress )
                    embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                           color=0x2ECC71 )
                    embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(lists[c][0][0]["number"], lists[c][0][-1]["number"],len1) )
                    await sent.edit( embed=embed )
                    await sent.add_reaction( "<:left:725668526869708881>" )
                    await sent.add_reaction( "<:right:725668611615621133>" )
                    print( lists[c][0] )
                    print( c )
                except:
                    c = 0
                    ress = lists[c][0]
                    resultant = "\n ".join( x["name"] for x in ress )
                    embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                           color=0x2ECC71 )
                    embed.set_footer(
                        text="Showing {}-{} out of {} pokémon matching this search.".format(
                            lists[c][0][0]["number"], lists[c][0][-1]["number"],
                            len1 ) )
                    await sent.edit( embed=embed )
                    await sent.add_reaction( "<:left:725668526869708881>" )
                    await sent.add_reaction( "<:right:725668611615621133>" )
                    print( lists[c][0] )
                    print( c )
            elif str( reaction.emoji ) == '<:left:725668526869708881>':
                try:
                    c = c - 1
                    ress = lists[c][0]
                    resultant = "\n ".join( x["name"] for x in ress )

                    embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                           color=0x2ECC71 )
                    embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(
                        lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                    await sent.edit( embed=embed )
                    await sent.add_reaction( "<:left:725668526869708881>" )
                    await sent.add_reaction( "<:right:725668611615621133>" )
                    c = c - 1
                    print( lists[c][0] )
                    print( c )
                except:
                    c = len( lists ) - 1
                    ress = lists[c][0]
                    resultant = "\n ".join( x["name"] for x in ress )
                    embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                           color=0x2ECC71 )
                    embed.set_footer(
                        text="Showing {}-{} out of {} pokémon matching this search.".format(
                            lists[c][0][0]["number"], lists[c][0][-1]["number"],
                            len1 ) )
                    await sent.edit( embed=embed )
                    await sent.add_reaction( "<:left:725668526869708881>" )
                    await sent.add_reaction( "<:right:725668611615621133>" )
                    print( lists[c][0] )
                    print( c )
    elif stats != "--shiny":
        mon = stats
        with open( "mons.json", "r", encoding="utf8" ) as f:
            mons = json.load( f )
            length = len( mons )
        for i in range( length ):
            if "{}".format( mon.lower() ) in mons[i]["name"]["english"].lower() or "{}".format( mon.lower() ) in mons[i]["name"]["german"].lower() or \
                    "{}".format( mon.lower() ) in mons[i]["name"]["japanese"][1].lower() or "{}".format( mon.lower() ) in mons[i]["name"]["japanese"][0].lower() or "{}".format( mon.lower() ) in mons[i]["name"]["french"].lower() or \
                "{}".format( mon.lower() ) in mons[i]["name"]["chinese"].lower():
                res = mons[i]["type"]
                eng = mons[i]["name"]["english"]
                jap = mons[i]["name"]["japanese"][0]
                jap1 = mons[i]["name"]["japanese"][1]
                chin= mons[i]["name"]["chinese"]
                germ = mons[i]["name"]["german"]
                stats = mons[i]["base"]
                id = mons[i]["id"]
                if mons[i]["name"]["french"] !="":
                    fren = mons[i]["name"]["french"]
                bool = "true"
                break
            elif "{}".format( mon.lower() ) not in mons[i]["name"]["english"].lower() or "{}".format( mon.lower() ) in mons[i]["name"]["german"].lower() or \
                    "{}".format( mon.lower() ) in mons[i]["name"]["japanese"][1].lower() or "{}".format( mon.lower() ) in mons[i]["name"]["japanese"][0].lower() or "{}".format( mon.lower() ) in mons[i]["name"]["french"].lower() or \
                "{}".format( mon.lower() ) in mons[i]["name"]["chinese"].lower():
                bool = "false"
        print(bool)
        if bool == "true":
            k=0
            result = []
            all_users = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
            for user in all_users.each():
                dict = user.val()
                if str(dict["name"].lower()) == "{}".format(mon.lower()):
                    k = k+1
                    if "true" in dict["shiny"]:
                        mon_name = dict["name"]
                        mon_number = dict["number"]
                        mon_iv = dict["IV"]
                        mon_level = dict["level"]
                        array = {
                            "name": "**✨{}**|Level:{}|Number:{}|IV:{}".format( mon_name, mon_level, mon_number,
                                                                               mon_iv ),
                            "number": "{}".format(k),

                        }
                        result.append( array )
                    elif "false" in dict["shiny"]:
                        mon_name = dict["name"]
                        mon_number = dict["number"]
                        mon_iv = dict["IV"]
                        mon_level = dict["level"]
                        array = {
                            "name": "**{}**|Level:{}|Number:{}|IV:{}".format( mon_name, mon_level, mon_number,
                                                                              mon_iv ),
                            "number": "{}".format(k)
                        }
                        result.append( array )
            if len(result) == 0:
                embed = discord.Embed( title="You don't have any of {}".format(mon),
                                               description="",
                                               color=0xeee657 )
                await ctx.send( embed=embed )
            elif len(result) != 0:
                print( len( result ) )
                divide = len( result ) / 20
                stri = str( divide )
                print( divide )
                if type( divide ) == int or stri.endswith( ".0" ):
                    divide = int( divide )
                elif type( divide ) == float:
                    divide = divide + 1

                print( divide )
                i = 0
                lists = []
                while i < int( divide ):
                    lists.append( [] )
                    i += 1

                z = 0
                length = len( result )
                print( length )
                len1 = int( length )
                while length > 0:
                    if length > 20:
                        lists[z].append( result[:20] )
                        del result[:20]
                    elif length <= 20:
                        lists[z].append( result )
                    length = length - 20
                    z += 1

                ress = lists[0][0]
                print( ress )
                resultant = "\n ".join( x["name"] for x in ress )

                embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                       color=0x2ECC71 )
                embed.set_footer(
                    text="Showing {}-{} out of {} pokémon matching this search.".format(
                        lists[0][0][0]["number"],
                        lists[0][0][-1]["number"],
                        len1 ) )

                sent = await ctx.send( embed=embed )
                await sent.add_reaction( "<:left:725668526869708881>" )
                await sent.add_reaction( "<:right:725668611615621133>" )
                c = 0

                def check(reaction, user):
                    return user == ctx.message.author and str(
                        reaction.emoji ) == '<:right:725668611615621133>' or str(
                        reaction.emoji ) == '<:left:725668526869708881>'

                while True:
                    try:
                        reaction, user = await client.wait_for( 'reaction_add', timeout=120.0, check=check )
                    except asyncio.TimeoutError:
                        return
                    if str( reaction.emoji ) == '<:right:725668611615621133>':
                        try:
                            c = c + 1
                            ress = lists[c][0]
                            resultant = "\n ".join( x["name"] for x in ress )
                            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                                   color=0x2ECC71 )
                            embed.set_footer(
                                text="Showing {}-{} out of {} pokémon matching this search.".format(
                                    lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                            await sent.edit( embed=embed )
                            await sent.add_reaction( "<:left:725668526869708881>" )
                            await sent.add_reaction( "<:right:725668611615621133>" )
                            print( lists[c][0] )
                            print( c )

                        except:
                            c = 0
                            ress = lists[c][0]
                            resultant = "\n ".join( x["name"] for x in ress )
                            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                                   color=0x2ECC71 )
                            embed.set_footer(
                                text="Showing {}-{} out of {} pokémon matching this search.".format(
                                    lists[c][0][0]["number"], lists[c][0][-1]["number"],
                                    len1 ) )
                            await sent.edit( embed=embed )
                            await sent.add_reaction( "<:left:725668526869708881>" )
                            await sent.add_reaction( "<:right:725668611615621133>" )
                            print( lists[c][0] )
                            print( c )
                    elif str( reaction.emoji ) == '<:left:725668526869708881>':
                        try:
                            c = c - 1
                            ress = lists[c][0]
                            resultant = "\n ".join( x["name"] for x in ress )

                            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                                   color=0x2ECC71 )
                            embed.set_footer(
                                text="Showing {}-{} out of {} pokémon matching this search.".format(
                                    lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                            await sent.edit( embed=embed )
                            await sent.add_reaction( "<:left:725668526869708881>" )
                            await sent.add_reaction( "<:right:725668611615621133>" )
                            c = c - 1
                            print( lists[c][0] )
                            print( c )
                        except:
                            c = len( lists ) - 1
                            ress = lists[c][0]
                            resultant = "\n ".join( x["name"] for x in ress )
                            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                                   color=0x2ECC71 )
                            embed.set_footer(
                                text="Showing {}-{} out of {} pokémon matching this search.".format(
                                    lists[c][0][0]["number"], lists[c][0][-1]["number"],
                                    len1 ) )
                            await sent.edit( embed=embed )
                            await sent.add_reaction( "<:left:725668526869708881>" )
                            await sent.add_reaction( "<:right:725668611615621133>" )
                            print( lists[c][0] )
                            print( c )

        elif bool == "false":
            embed = discord.Embed( title="Invalid pokemon name",
                                   description="",
                                   color=0xeee657 )
            await ctx.send( embed=embed )

@client.command()
async def donate(ctx):
    embed = discord.Embed( title="**Donation**", description="**{***Not yet implemented***},but you can free feel to donate to @chelly#0001**",
                           color=0xeee657 )
    await ctx.send( embed=embed )

@client.command(aliases=['bal'])
async def balance(ctx):
    if str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).get().val()) == "None":
           db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).set("0")
           embed = discord.Embed( title="**{}'s balance**".format(ctx.message.author.name),
                                  description="You currently have 0 credits!",
                                  color=0xeee657 )
           embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/703612469226242109/740210658112569435/money-bag_1f4b0.png")
           await ctx.send( embed=embed )
    elif str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).get().val()) != "None":
           earned = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).get().val()
           embed = discord.Embed( title="**{}'s balance**".format( ctx.message.author.name ),
                                  description="You currently have {}!".format(earned),
                                  color=0xeee657 )
           embed.set_thumbnail( url="https://cdn.discordapp.com/attachments/703612469226242109/740210658112569435/money-bag_1f4b0.png")
           await ctx.send( embed=embed )
@client.command()
async def redeem(ctx):
    if str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).get().val()) == "None":
           ar = { "redeems":"0"}
           db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).set(ar)
           embed = discord.Embed( title="**Your Redeems:0 💸**",
                                  description="***To obtain a redeem , You can get it through ``pdialy command``.\nor can donate 0.5$ to @chelly#0001 or @Ash#0666 or @MrShawnRogers#6969***",
                                  color=0xeee657 )
           await ctx.send( embed=embed )
    elif str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).get().val()) != "None":
           earned = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).get().val()
           embed = discord.Embed( title="**Your Redeems:{}💸**".format(earned),
                                  description="***To obtain a redeem , You can get it through ``pdialy command``.\nor can donate 0.5$ to @chelly#0001 or @Ash#0666 or @MrShawnRogers#6969***",
                                  color=0xeee657 )
           await ctx.send( embed=embed )

@client.command()
@commands.cooldown( 1,86400, commands.BucketType.user )
async def daily(ctx):
    print("wjh")
    rewards = ["100 credits","100 credits","100 credits","100 credits","100 credits",
               "250 credits","250 credits","250 credits","250 credits",
               "350 credits","350 credits","350 credits",
               "1 redeem"]
    reward = str(random.choices(rewards)[0])
    print(reward)
    if reward.endswith("credits"):
       print("rewag")
       reward =int(reward.replace('credits', ''))
       if  str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).get().val()) == "None":
           ar = "{}".format(reward)
           db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child("credits").set(ar)
           embed = discord.Embed( title="**Here's your daily rewards**",
                                  description="You recieved {}!".format( reward ),
                                  color=0xeee657 )
           await ctx.send( embed=embed )
       elif  str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).get()) != "None":
           earned = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).get().val()
           credits = int(earned.replace('credits', ''))
           credits = credits + reward
           ar = "{} credits".format(credits)
           db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "credits" ).set( ar )
           embed = discord.Embed( title="**Here's your daily rewards**",
                                  description="You recieved {}!".format(reward),
                                  color=0xeee657 )
           await ctx.send( embed=embed )
    elif reward.endswith("redeem"):
        reward = int( reward.replace( 'redeem', '' ) )
        if str( db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).get() ) == "None":
            ar =  "{}".format( reward )
            db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child("redeems").set( ar )
            embed = discord.Embed( title="**Here's your daily rewards**",
                                   description="You recieved {} 💸!".format( reward ),
                                   color=0xeee657 )
            await ctx.send( embed=embed )
        elif str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).get() ) != "None":
            earned = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "redeems" ).get().val()
            credits = int( earned.replace( 'redeem', '' ) )
            credits = credits + reward
            ar = "{}".format( credits )
            db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child("redeems").set( ar )
            embed = discord.Embed( title="**Here's your daily rewards**",
                                   description="You recieved {} 💸!".format( reward ),
                                   color=0xeee657 )
            await ctx.send( embed=embed )
@daily.error
async def daily_error(ctx,error):
    if isinstance( error, commands.CommandOnCooldown ):
        error = str(error)
        stopwords = ['you', 'are', 'on', 'cooldown.', 'try', 'again', 'in','s']
        querywords = error.split()
        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join( resultwords )
        result = result.split()
        stopwords = ["s"]
        resultwords = [word for word in result if word.lower() not in stopwords]
        result = ' '.join( resultwords )
        print(result)
        def GetTime(sec):
            sec = float(sec)
            sec = round( sec, 0 )
            sec = timedelta( seconds=int( sec ) )
            d = datetime( 1, 1, 1 ) + sec
            print( "DAYS:HOURS:MIN:SEC" )
            print( "%d:%d:%d:%d" % (d.day - 1, d.hour, d.minute, d.second) )
            return d.day - 1, d.hour, d.minute, d.second
        yo = GetTime(result[:-1])
        if str(yo[0]) == "0" and str(yo[1]) == "0":
                embed = discord.Embed( title="You can try again in **{}min: {}secs**".format(yo[2], yo[3]), description="", color=0xff00f6 )
                await ctx.send( embed=embed )
        elif str(yo[0]) == "0" and str(yo[1]) != "0":
            embed = discord.Embed( title="You can try again in **{}hour {}mins**".format( yo[1], yo[2] ),description="", color=0xff00f6 )
            await ctx.send( embed=embed )
        elif str(yo[0]) == "1":
         embed = discord.Embed( title="You can try again in **{} day**".format(yo[0]), description="", color=0xff00f6 )
         await ctx.send( embed=embed )
        elif str(yo[0]) == "0" and str(yo[1]) == "0":
            embed = discord.Embed( title="You can try again in **{}mins**".format(yo[2] ),description="", color=0xff00f6 )
            await ctx.send( embed=embed )
        elif str(yo[0]) == "0" and str(yo[1]) == "0" and str(yo[2]) == "0":
            embed = discord.Embed( title="You can try again in **{}secs**".format(yo[3] ),description="", color=0xff00f6 )
            await ctx.send( embed=embed )



@client.command()
async def help(ctx):
    embed = discord.Embed( title="**Help**",
                           description="",
                           color=0xeee657 )
    embed.add_field( name="**Redirecting to a channel**", value="Use predirect #channel ``User need to be an Admin``", inline=False )
    embed.add_field( name="**Market&shop&redeem features**", value="**This features are not yet implemented**", inline=False )
    embed.add_field( name="**Upcoming features**", value="``Trade``:can trade infinte no. of mon to any user \n``Leveling``:it would be implemented after evolutions is supported.", inline=False )
    embed.add_field( name="**Invite Link**", value="``Use pinvite to get the invite link for the bot``", inline=False )
    await ctx.send( embed=embed )

'''
@client.command()
async def invite(ctx):
    link = 'https://discordapp.com/oauth2/authorize?client_id=671706523541569546&scope=bot'
    embed = discord.Embed( title="**InviteLink**",
                           description="[Link]({})".format(link),
                           color=0xeee657 )

    # give users a link to invite thsi bot to their server
    await ctx.send(embed=embed)


'''
@client.command()
async def catch(ctx,*,mon):
    guild = ctx.message.guild.id
    channel = ctx.message.channel.id
    check = db.child( "spawns" ).child("{}".format(channel)).get()
    dict = check.val()
    gcheck = db.child( "servers" ).child("{}".format(guild)).get()
    if str(check.val()) != "None":
     idd = list(dict.items())
     id = int(idd[0][1])
     shiny = str(idd[2][1])
     with open( "mons.json", "r", encoding='utf8' ) as f:
        mons = json.load( f )
        mon1 = mons[id-1]
        name = mon1["name"]["english"]
        name1 = mon1["name"]["french"]
        jap = mon1["name"]["japanese"][0]
        jap1 = mon1["name"]["japanese"][1]
        chin = mon1["name"]["chinese"]
        germ = mon1["name"]["german"]
        if "fun" in mon1["name"]:
            another = mon1["name"]["fun"]
        elif "fun" not in mon1["name"]:
            another = name
     print(name)
     print("user mon",mon)
     checkkk = db.child( "users" ).child( "{}".format(ctx.message.author.id ) ).get()
     if checkkk.val() == None:
         await ctx.send( "Do pstart to start you pokemon journey " )
     elif  checkkk.val() !=None:
      if str(mon.lower()) == "{}".format(name.lower()) or str(mon.lower()) == '{}'.format(name1.lower() ) or \
                    str(mon.lower()) == '{}'.format( another.lower())  or str(mon.lower()) == '{}'.format( name ) \
                    or str(mon.lower()) == '{}'.format( name1 )  or str(mon.lower()) == '{}'.format( another ) or \
                    str(mon.lower()) == '{}'.format(jap) or str(mon.lower()) == '{}'.format(jap.lower()) or \
                    str(mon.lower()) == '{}'.format(chin) or str(mon.lower()) == '{}'.format(chin.lower()) or \
                    str(mon.lower()) == '{}'.format(germ) or str(mon.lower()) =='{}'.format(germ.lower())  or\
                    str(mon.lower()) == '{}'.format( jap1) or str(mon.lower()) == '{}'.format( jap1.lower()):
         level = random.randint(1,20)
         if shiny == "false":
             db.child( "spawns" ).child( "{}".format( channel ) ).remove()
             await ctx.send("Congratulations {}! You caught a level {} {}!".format(ctx.message.author.mention, level,
                                                                         name))
             result = []
             result_no = []
             hp_stats = random.randint( 0, 10 )
             Attack_stats = random.randint( 0, 10 )
             Defense_stats = random.randint( 0, 10 )
             sp_attack_stats = random.randint( 0, 10 )
             spdef_stats = random.randint( 0, 10 )
             speed_stats = random.randint( 0, 10 )
             overall_iv = hp_stats + Attack_stats + Defense_stats + sp_attack_stats + spdef_stats + speed_stats / 50 * 100
             user1 = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
             print( user1.val() )
             lat = len( user1.val() )
             print( lat )
             pokemonr = {"name": "{}".format( name ),
                         "level": "{}".format( level ),
                         "hp": "{}/10".format( hp_stats ),
                         "attack": "{}/10".format( Attack_stats ),
                         "defense": "{}/10".format( Defense_stats ),
                         "sp atk": "{}/10".format( sp_attack_stats ),
                         "sp def": "{}/10".format( spdef_stats ),
                         "speed": "{}/10".format( speed_stats ),
                         "IV": "{}%".format( overall_iv ),
                         "shiny": "false",
                         "number": "{}".format( lat + 1 ),
                         "selected": "no",
                         "id": "{}".format(id)
                         }

             db.child( "users" ).child( "{}".format(ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( lat ) ).set(pokemonr)
         elif shiny == "true":
             db.child( "spawns" ).child( "{}".format( channel ) ).remove()
             await ctx.send(
                 "Congratulations {}! You caught a level {} ✨{}!".format(ctx.message.author.mention, level,
                                                                          name ) )
             result = []
             result_no = []
             hp_stats = random.randint( 0, 10 )
             Attack_stats = random.randint( 0, 10 )
             Defense_stats = random.randint( 0, 10 )
             sp_attack_stats = random.randint( 0, 10 )
             spdef_stats = random.randint( 0, 10 )
             speed_stats = random.randint( 0, 10 )
             overall_iv = hp_stats + Attack_stats + Defense_stats + sp_attack_stats + spdef_stats + speed_stats / 50 * 100
             user1 = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
             print( user1.val() )
             lat = len( user1.val() )
             print( lat )
             pokemonr = {"name": "{}".format( name ),
                         "level": "{}".format( level ),
                         "hp": "{}/10".format( hp_stats ),
                         "attack": "{}/10".format( Attack_stats ),
                         "defense": "{}/10".format( Defense_stats ),
                         "sp atk": "{}/10".format( sp_attack_stats ),
                         "sp def": "{}/10".format( spdef_stats ),
                         "speed": "{}/10".format( speed_stats ),
                         "IV": "{}%".format( overall_iv ),
                         "shiny": "true",
                         "number": "{}".format( lat + 1 ),
                         "selected": "no",
                         "id": "{}".format(id)
                         }
             db.child( "users" ).child( "{}".format(ctx.message.author.id ) ).child( "pokemons" ).child(
                 "{}".format( lat ) ).set( pokemonr )
      elif str( mon.lower() )!= "{}".format( name.lower() ) or str( mon.lower() ) != '{}'.format( name1.lower() ) or \
             str( mon.lower() ) != '{}'.format( another.lower() ) or str( mon.lower() ) != '{}'.format( name ) \
             or str( mon.lower() ) != '{}'.format( name1 ) or str( mon.lower() ) != '{}'.format( another ) or \
             str( mon.lower() ) != '{}'.format( jap ) or str( mon.lower() ) != '{}'.format( jap.lower() ) or \
             str( mon.lower() ) != '{}'.format( chin ) or str( mon.lower() ) != '{}'.format( chin.lower() ) or \
             str( mon.lower() ) != '{}'.format( germ ) or str( mon.lower() ) != '{}'.format( germ.lower() ) or \
             str( mon.lower() ) != '{}'.format( jap1 ) or str( mon.lower() ) != '{}'.format( jap1.lower() ):
         await ctx.send("This is the wrong pokémon!")
    elif str(check.val()) == "None" and str(gcheck.val()) == "{}".format(channel):
         await ctx.send("There are no wild spawns in the channel.")


@pokemon.error
async def pokemon_error(ctx,error):
    if isinstance( error, commands.MissingRequiredArgument ):
        checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
        if checkkk.val() == None:
            await ctx.send( "Do pstart to start you pokemon journey " )
        else:
            all_users = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
            result = []
            for user in all_users.each():
                dict = user.val()
                if "true" in dict["shiny"]:
                    mon_name = dict["name"]
                    mon_number = dict["number"]
                    mon_iv = dict["IV"]
                    mon_level = dict["level"]
                    array = {
                        "name": "**✨{}**|Level:{}|Number:{}|IV:{}".format( mon_name, mon_level, mon_number,
                                                                           mon_iv ),
                        "number": "{}".format( mon_number )
                    }
                    result.append( array )
                elif "false" in dict["shiny"]:
                    mon_name = dict["name"]
                    mon_number = dict["number"]
                    mon_iv = dict["IV"]
                    mon_level = dict["level"]
                    array = {
                        "name": "**{}**|Level:{}|Number:{}|IV:{}".format( mon_name, mon_level, mon_number,
                                                                          mon_iv ),
                        "number": "{}".format( mon_number )
                    }
                    result.append( array )

            print( len( result ) )
            divide = len( result ) / 20
            stri = str( divide )
            print( divide )
            if type( divide ) == int or stri.endswith( ".0" ):
                divide = int( divide )
            elif type( divide ) == float:
                divide = divide + 1

            print( divide )
            i = 0
            lists = []
            while i < int( divide ):
                lists.append( [] )
                i += 1

            z = 0
            length = len( result )
            print( length )
            len1 = int( length )
            while length > 0:
                if length > 20:
                    lists[z].append( result[:20] )
                    del result[:20]
                elif length <= 20:
                    lists[z].append( result )
                length = length - 20
                z += 1

            ress = lists[0][0]
            print( ress )
            resultant = "\n ".join( x["name"] for x in ress )

            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                   color=0x2ECC71 )
            embed.set_footer(
                text="Showing {}-{} out of {} pokémon matching this search.".format( lists[0][0][0]["number"],
                                                                                     lists[0][0][-1]["number"], len1 ) )

            sent = await ctx.send( embed=embed )
            await sent.add_reaction( "<:left:725668526869708881>" )
            await sent.add_reaction( "<:right:725668611615621133>" )
            c = 0

            def check(reaction, user):
                return user == ctx.message.author and str( reaction.emoji ) == '<:right:725668611615621133>' or str(
                    reaction.emoji ) == '<:left:725668526869708881>'

            while True:
                try:
                    reaction, user = await client.wait_for( 'reaction_add', timeout=120.0, check=check )
                except asyncio.TimeoutError:
                    return
                if str( reaction.emoji ) == '<:right:725668611615621133>':
                    try:
                        c = c + 1
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )
                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(
                            lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )
                        print( lists[c][0] )
                        print( c )

                    except:
                        c = 0
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )
                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer(
                            text="Showing {}-{} out of {} pokémon matching this search.".format(
                                lists[c][0][0]["number"], lists[c][0][-1]["number"],
                                len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )
                        print( lists[c][0] )
                        print( c )
                elif str( reaction.emoji ) == '<:left:725668526869708881>':
                    try:
                        c = c - 1
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )

                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(
                            lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )
                        c = c - 1
                        print( lists[c][0] )
                        print( c )
                    except:
                        c = len( lists ) - 1
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )
                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer(
                            text="Showing {}-{} out of {} pokémon matching this search.".format(
                                lists[c][0][0]["number"], lists[c][0][-1]["number"],
                                len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )
                        print( lists[c][0] )
                        print( c )

@client.command()
async def trade(ctx,member:discord.Member):
    if member == ctx.message.author:
        await ctx.send("You cant trade with yourself")
    elif member != ctx.message.author:
     await ctx.send("{} has invited you for a trade, do paccept to accept {}".format(ctx.message.author.mention,member.mention))
     channel = ctx.message.channel
     def check(m):
      return (m.channel == ctx.message.channel) and (m.author is not m.author.bot) and (m.author == member) and (
            'paccept' in m.content.lower())

     msg = await client.wait_for( 'message', check=check )
     h = msg.content.lower()
     embed = discord.Embed( title="Trading Centre", description="**Trade between {} and {}**".format( ctx.message.author.name,member.name),
                           color=0xeee657 )
     embed.add_field(name="**{} is offering**".format(ctx.message.author.name), value="```|```", inline=False)
     embed.add_field(name="**{} is offering**".format(member.name), value="```|```", inline=False)
     send = await channel.send( embed=embed )
     await ctx.send("Use padd <number> <number>..... of the pokemon you wanna trade , and pdeny to cancel the trade.")
     list11 = []
     list11_items = []
     list22 = []
     list22_items = []
     ctx_trader = []
     trader2 = []
     def solve(lis):
         for x in lis:
             try:
                 float( x )
                 return True
             except:
                 return False
     while True:
        def check(m):
            return (m.channel == ctx.message.channel) and (m.author is not m.author.bot) and (m.author == member) or (m.author == ctx.message.author)  and (m.content.startswith("padd" )) or ('pconfirm' in m.content)
        msg = await client.wait_for( 'message', check=check )
        h = msg.content.lower()
        if h.startswith("padd"):
         if msg.author == ctx.message.author:
            trade = msg.content.lower()
            querywords = trade.split()
            stopwords = ['shiny', 'padd']
            resultwords = [word for word in querywords if word.lower() not in stopwords and word.lower() not in list11]
            ok = [x for x in resultwords if solve(x)]
            result = ' '.join(ok)
            if result == "":
                await ctx.send("please enter only pokemon numbers only or Dont repeat the pokemon number")
            elif result != "":
             words = result.split()
             for i in words:
                 if i not in list11:
                    list11.append(i)
                 elif i in list11 :
                     continue
             i = 0
             ctx_trader.clear()
             while i < len(list11):

                check = db.child( "users" ).child( "{}".format(ctx.message.author.id) ).child( "pokemons").child("{}".format(int(list11[i])-1)).get()

                if str(check.val()) == "None":
                    list11.remove("{}".format(list11[i]))
                    i = i
                elif str(check.val()) != "None":
                    items = list(check.val().items())
                    if str(items[8][1]) != "yes":
                     ctx_trader.append("|Level {} {}".format(items[5][1],items[6][1]))
                    i =i+1
             i = 0
             listo = ' \n'.join( mon for mon in ctx_trader)
             list1 = ' \n'.join( mon for mon in trader2)
             new_embed = discord.Embed(title="Trading Centre", description="**Trade between {} and {}**".format( ctx.message.author.name, member.name ),
                                       color=0xeee657 )
             new_embed.add_field(name="**{} is offering**".format( ctx.message.author.name ), value="```{}```".format(' \n'.join(mon for mon in ctx_trader)),
                                 inline=False)
             new_embed.add_field(name="**{} is offering**".format( member.name ), value="```{}```".format(' \n'.join( mon for mon in trader2)), inline=False)

             await send.edit(embed=new_embed)
         elif msg.author == member:
            trade = msg.content.lower()
            querywords = trade.split()
            stopwords = ['shiny', 'padd']
            resultwords1 = [word for word in querywords if word.lower() not in stopwords and word.lower() not in list22]
            ok = [x for x in resultwords1 if solve( x )]
            result1 = ' '.join(ok)
            if result1 == "":
                await ctx.send("please enter only pokemon numbers only")
            elif result1 != "":
             words = result1.split()
             for i in words:
                 if i not in list22:
                     list22.append(i)
                 elif i in list22 :
                     continue
             i = 0
             trader2.clear()
             while i < len( list22):
                 check = db.child( "users" ).child( "{}".format(member.id ) ).child( "pokemons" ).child("{}".format(int(list22[i])-1)).get()
                 if str( check.val() ) == "None":
                     list22.remove("{}".format(list22[i]))
                     i = i
                 elif str( check.val() ) != "None":
                     items = list( check.val().items() )
                     if str( items[8][1] ) != "yes":
                      trader2.append("|Level {} {}".format(items[5][1], items[6][1]))
                     i = i + 1
             i = 0
             listo = ' \n'.join( mon for mon in ctx_trader )
             list1 = ' \n'.join( mon for mon in trader2)

             new_embed = discord.Embed( title="Trading Centre",
                                       description="**Trade between {} and {}**".format(ctx.message.author.name, member.name), color=0xeee657)

             new_embed.add_field( name="**{} is offering**".format( ctx.message.author.name ),
                                 value="```{}```".format(' \n'.join( mon for mon in ctx_trader )),
                                 inline=False )
             new_embed.add_field( name="**{} is offering**".format( member.name ), value="```{}```".format(' \n'.join( mon for mon in trader2)), inline=False )

             await send.edit(embed=new_embed)
        elif h == "pconfirm" and msg.author == ctx.message.author:
            new_embed = discord.Embed( title="Trading Centre",
                                       description="**Trade between {} and {}**".format( ctx.message.author.name,
                                                                                         member.name ), color=0xeee657 )

            new_embed.add_field( name="**{} is offering** ✅".format( ctx.message.author.name ),
                                 value="```{}```".format(' \n'.join( mon for mon in ctx_trader)),
                                 inline=False )
            new_embed.add_field( name="**{} is offering**".format( member.name ), value="```{}```".format(' \n'.join( mon for mon in trader2 )),
                                 inline=False )
            await send.edit(embed=new_embed)
            while True:
             def check(m):
                return (m.channel == ctx.message.channel) and (m.author is not m.author.bot) and (
                            m.author == member) and ('pconfirm' in m.content) or (m.content.startswith("padd"))
             msg = await client.wait_for( 'message', check=check )
             h = msg.content.lower()
             if h.startswith( "padd" ):
                print( member.id )
                trade = msg.content.lower()
                querywords = trade.split()
                stopwords = ['shiny', 'padd']
                resultwords1 = [word for word in querywords if word.lower() not in stopwords and word.lower() not in list22]
                ok = [x for x in resultwords1 if solve( x )]
                result1 = ' '.join( ok )
                if result1 == "":
                    await ctx.send( "please enter only pokemon numbers only" )
                elif result1 != "":
                    m = 0
                    words = result1.split()
                    for i in words:
                        if i not in list22:
                            list22.append( i )
                        elif i in list22:
                            continue
                    i = 0
                    while i < len( list22 ):
                        check = db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).child(
                            "{}".format( int( list22[i] ) - 1 ) ).get()

                        if str( check.val() ) == "None":
                            list22.remove( "{}".format( list22[i] ) )
                            i = i
                        elif str( check.val() ) != "None":
                            items = list( check.val().items() )
                            if str( items[8][1] ) != "yes":
                             trader2.append( "|Level {} {}".format( items[5][1], items[6][1] ) )
                            i = i + 1

                    listo = ' \n'.join( mon for mon in ctx_trader )
                    list1 = ' \n'.join( mon for mon in trader2 )
                    new_embed = discord.Embed( title="Trading Centre",
                                               description="**Trade between {} and {}**".format(
                                                   ctx.message.author.name, member.name ), color=0xeee657 )

                    new_embed.add_field( name="**{} is offering ✅**".format( ctx.message.author.name ),
                                         value="```{}```".format( listo ),
                                         inline=False )
                    new_embed.add_field( name="**{} is offering**".format( member.name ),
                                         value="```{}```".format( list1 ), inline=False )

                    await send.edit( embed=new_embed )
             elif h == "pconfirm" and msg.author == member:
                new_embed = discord.Embed( title="Trading Centre",
                                           description="**Trade between {} and {}**".format( ctx.message.author.name,
                                                                                             member.name ),
                                           color=0xeee657 )

                new_embed.add_field( name="**{} is offering** ✅".format( ctx.message.author.name ),
                                     value="```{}```".format( ' \n'.join( mon for mon in ctx_trader ) ),
                                     inline=False )
                new_embed.add_field( name="**{} is offering** ✅".format( member.name ),
                                     value="```{}```".format( ' \n'.join( mon for mon in trader2 ) ),
                                     inline=False )
                await send.edit( embed=new_embed )
                break
            bool = "true"
            break
        elif h == "pconfirm" and msg.author == member:
            new_embed = discord.Embed( title="Trading Centre",
                                       description="**Trade between {} and {}**".format( ctx.message.author.name,member.name ), color=0xeee657 )
            new_embed.add_field( name="**{} is offering**".format( ctx.message.author.name ),value="```{}```".format(' \n'.join( mon for mon in ctx_trader )), inline=False )
            new_embed.add_field( name="**{} is offering** ✅".format( member.name ), value="```{}```".format(' \n'.join( mon for mon in trader2)), inline=False )
            await send.edit(embed=new_embed)
            while True :
             def check(m):
                return (m.channel == ctx.message.channel) and (m.author is not m.author.bot) and (m.author == ctx.message.author) and ('pconfirm' in m.content) or (m.content.startswith("padd"))
             msg = await client.wait_for( 'message', check=check )
             h = msg.content.lower()
             if h.startswith( "padd" ):
                trade = msg.content.lower()
                querywords = trade.split()
                stopwords = ['shiny', '!add']
                resultwords = [word for word in querywords if word.lower() not in stopwords and word.lower() not in list11]
                ok = [x for x in resultwords if solve( x )]
                result = ' '.join( ok )
                if result == "":
                    await ctx.send( "please enter only pokemon numbers only" )
                elif result != "":
                    words = result.split()
                    for i in words:
                        if i not in list11:
                            list11.append( i )
                        elif i in list11 :
                            continue
                    i = 0
                    while i < len( list11 ):
                        check = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child(
                            "pokemons" ).child(
                            "{}".format( int( list11[i] ) - 1 ) ).get()
                        if str( check.val() ) == "None":
                            list11.remove( "{}".format( list11[i] ) )
                            i = i
                        elif str( check.val() ) != "None":
                            items = list( check.val().items() )
                            if str( items[8][1] ) != "yes":
                             ctx_trader.append( "|Level {} {}".format( items[5][1], items[6][1] ) )
                            i = i + 1

                    listo = ' \n'.join( mon for mon in ctx_trader )
                    list1 = ' \n'.join( mon for mon in trader2 )
                    new_embed = discord.Embed( title="Trading Centre",
                                               description="**Trade between {} and {}**".format(
                                                   ctx.message.author.name,
                                                   member.name ),
                                               color=0xeee657 )
                    new_embed.add_field( name="**{} is offering** ".format( ctx.message.author.name ),
                                         value="```{}```".format( listo ),
                                         inline=False )
                    new_embed.add_field( name="**{} is offering** ✅".format( member.name ),
                                         value="```{}```".format( list1 ),
                                         inline=False )

                    await send.edit( embed=new_embed )
             elif h == "pconfirm" and msg.author == ctx.message.author:
                new_embed = discord.Embed( title="Trading Centre",
                                           description="**Trade between {} and {}**".format( ctx.message.author.name,
                                                                                             member.name ),
                                           color=0xeee657 )

                new_embed.add_field( name="**{} is offering** ✅".format( ctx.message.author.name ),
                                     value="```{}```".format( ' \n'.join( mon for mon in ctx_trader ) ),
                                     inline=False )
                new_embed.add_field( name="**{} is offering** ✅".format( member.name ),
                                     value="```{}```".format( ' \n'.join( mon for mon in trader2 ) ),
                                     inline=False )
                await send.edit( embed=new_embed )
                break
            bool = "true"
            break

        elif h.startswith("pcancel"):
            bool = "false"
            await ctx.send("**Trade is being cancelled**")
            break

     if bool == "true":
         if list11 != "" and list22 != "" :
          await ctx.send("<a:load:729332167691337839> Processing <a:process:729332112511205387>")

          user1 = db.child( "users" ).child( "{}".format(ctx.message.author.id) ).child( "pokemons" ).get()
          listtrader = user1.val()

          #####################GETTING DATA FOR BOTH USERS#############################
          #####################                           #############################

          # getting items
          k = 0
          while k < len( list11 ):
              list11_items.append( listtrader[int( list11[k] ) - 1] )
              k = k + 1

          p = 0
          # removing from database
          while p < len( list11_items ):
              listtrader.remove( list11_items[p] )
              p = p + 1

          # sorting database
          o = 0
          m = 1
          while o < len( listtrader ):
              listtrader[o]["number"] = m
              o = o + 1
              m = m + 1


          #######################      trader2      ############################

          user2 = db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).get()
          listacceptor = user2.val()

          # getting items
          k = 0
          while k < len( list22 ):
              list22_items.append( listacceptor[int( list22[k] ) - 1] )
              k = k + 1


          p = 0
          # removing from database
          while p < len( list22_items ):
              listacceptor.remove( list22_items[p] )
              p = p + 1

          # sorting database
          o = 0
          m = 1
          while o < len( listacceptor ):
              listacceptor[o]["number"] = m
              o = o + 1
              m = m + 1


          ###################################transferring mons##########################################
          ##############################################################################################

          # TRADER1

          l = 0
          while l < len( list22_items ):
              list22_items[l]["number"] = len( listtrader ) + 1
              listtrader.append( list22_items[l] )
              l = l + 1

          db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).set( listtrader )
          # TRADER2

          g = 0
          while g < len( list11_items ):
              list11_items[g]["number"] = len( listacceptor ) + 1
              listacceptor.append( list11_items[g] )
              g = g + 1
          db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).set( listacceptor )
          await ctx.send( "Trade has been confirmed" )

         elif list11 == "" and list22 != "":
             await ctx.send( "<a:load:729332167691337839> Processing <a:process:729332112511205387>" )

             #####################GETTING DATA FOR BOTH USERS#############################
             #####################                           #############################

             # getting items

             #trader1
             user1 = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
             listtrader = user1.val()
             '''
             k = 0
             while k < len( list11 ):
                 list11_items.append(listtrader[int( list11[k] ) - 1] )
                 k = k + 1

             p = 0
             # removing from database
             while p < len( list11_items ):
                 listtrader.remove( list11_items[p] )
                 p = p + 1

             # sorting database
             o = 0
             m = 1
             while o < len( listtrader ):
                 listtrader[o]["number"] = m
                 o = o + 1
                 m = m + 1

             print( len( listtrader ) )
             '''
             #######################      trader2      ############################

             user2 = db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).get()
             listacceptor = user2.val()

             # getting items
             k = 0
             while k < len( list22 ):
                 list22_items.append( listacceptor[int( list22[k] ) - 1] )
                 k = k + 1

             p = 0
             # removing from database
             while p < len( list22_items ):
                 listacceptor.remove( list22_items[p] )
                 p = p + 1

             # sorting database
             o = 0
             m = 1
             while o < len( listacceptor ):
                 listacceptor[o]["number"] = m
                 o = o + 1
                 m = m + 1


             ###################################transferring mons##########################################
             ##############################################################################################

             # TRADER1
             l = 0
             while l < len( list22_items ):
                 list22_items[l]["number"] = len( listtrader ) + 1
                 listtrader.append( list22_items[l] )
                 l = l + 1

             db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).set( listtrader )

             '''
             # TRADER2

             g = 0
             while g < len( list11_items ):
                 list11_items[g]["number"] = len( listacceptor ) + 1
                 listacceptor.append( list11_items[g] )
                 g = g + 1
             db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).set( listacceptor )
             await ctx.send( "Trade has been confirmed" )
             print( list11 )
             print( list22 )
            '''
         elif list11 != ""and list22 == "":
             await ctx.send( "<a:load:729332167691337839> Processing <a:process:729332112511205387>" )

             #####################GETTING DATA FOR BOTH USERS#############################
             #####################                           #############################

             # getting items

             #trader1
             user1 = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
             listtrader = user1.val()

             k = 0
             while k < len( list11 ):
                 list11_items.append(listtrader[int( list11[k] ) - 1] )
                 k = k + 1

             p = 0
             # removing from database
             while p < len( list11_items ):
                 listtrader.remove( list11_items[p] )
                 p = p + 1

             # sorting database
             o = 0
             m = 1
             while o < len( listtrader ):
                 listtrader[o]["number"] = m
                 o = o + 1
                 m = m + 1


             #######################      trader2      ############################

             user2 = db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).get()
             listacceptor = user2.val()
             '''
             # getting items
             k = 0
             while k < len( list22 ):
                 list22_items.append( listacceptor[int( list22[k] ) - 1] )
                 k = k + 1

             p = 0
             # removing from database
             while p < len( list22_items ):
                 listacceptor.remove( list22_items[p] )
                 p = p + 1

             # sorting database
             o = 0
             m = 1
             while o < len( listacceptor ):
                 listacceptor[o]["number"] = m
                 o = o + 1
                 m = m + 1

             print( len( listacceptor ) )
             '''
             ###################################transferring mons##########################################
             ##############################################################################################
             '''
             # TRADER1
             l = 0
             while l < len( list22_items ):
                 list22_items[l]["number"] = len( listtrader ) + 1
                 listtrader.append( list22_items[l] )
                 l = l + 1
             print( listtrader )

             db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).set( listtrader )
             
             '''
             # TRADER2

             g = 0
             while g < len( list11_items ):
                 list11_items[g]["number"] = len( listacceptor ) + 1
                 listacceptor.append( list11_items[g] )
                 g = g + 1
             db.child( "users" ).child( "{}".format( member.id ) ).child( "pokemons" ).set( listacceptor )
             await ctx.send( "Trade has been confirmed" )
         elif list11 == "" and list22 == "":
             await ctx.send("Nothing got traded :)")


@client.command()
async def shiny(ctx):
    checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
    if checkkk.val() == None:
        await ctx.send( "Do pstart to start you pokemon journey " )
    else:
        all_users = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
        result = []
        k = 0
        for user in all_users.each():
            dict = user.val()
            if "true" in dict["shiny"]:
                k = k + 1
                mon_name = dict["name"]
                mon_number = dict["number"]
                mon_iv = dict["IV"]
                mon_level = dict["level"]
                array = {
                    "name": "**✨{}**|Level:{}|Number:{}|IV:{}".format( mon_name, mon_level, mon_number,
                                                                       mon_iv ),
                    "number": "{}".format( k )
                }
                result.append( array )

        divide = len( result ) / 20
        stri = str( divide )

        if type( divide ) == int or stri.endswith( ".0" ):
            divide = int( divide )
        elif type( divide ) == float:
            divide = divide + 1

        i = 0
        lists = []
        while i < int( divide ):
            lists.append( [] )
            i += 1

        z = 0
        length = len( result )

        len1 = int( length )
        while length > 0:
            if length > 20:
                lists[z].append( result[:20] )
                del result[:20]
            elif length <= 20:
                lists[z].append( result )
            length = length - 20
            z += 1

        ress = lists[0][0]

        resultant = "\n ".join( x["name"] for x in ress )
        if resultant == "":
            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                   color=0x2ECC71 )
        elif resultant != "":
            embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                               color=0x2ECC71 )

        if len1 <= 20:
            embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format( 1, len1, len1 ) )
        elif len1 > 20:
            embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format( 1, 20, len1 ) )
        sent = await ctx.send( embed=embed )
        await sent.add_reaction( "<:left:725668526869708881>" )
        await sent.add_reaction( "<:right:725668611615621133>" )
        if len1 <= 20:
            return
        elif len1 > 20:
            c = 0

            def check(reaction, user):
                return user == ctx.message.author and str( reaction.emoji ) == '<:right:725668611615621133>' or str(
                    reaction.emoji ) == '<:left:725668526869708881>'

            while True:
                try:
                    reaction, user = await client.wait_for( 'reaction_add', timeout=120.0, check=check )
                except asyncio.TimeoutError:
                    return
                if str( reaction.emoji ) == '<:right:725668611615621133>':
                    try:
                        c = c + 1
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )
                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ), color=0x2ECC71 )
                        embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )

                    except:
                        c = 0
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )
                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(lists[c][0][0]["number"], lists[c][0][-1]["number"],len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )

                elif str( reaction.emoji ) == '<:left:725668526869708881>':
                    try:
                        c = c - 1
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )

                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer( text="Showing {}-{} out of {} pokémon matching this search.".format(
                            lists[c][0][0]["number"], lists[c][0][-1]["number"], len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )
                        c = c - 1

                    except:
                        c = len( lists ) - 1
                        ress = lists[c][0]
                        resultant = "\n ".join( x["name"] for x in ress )
                        embed = discord.Embed( title="**Pokemon**", description="{}".format( resultant ),
                                               color=0x2ECC71 )
                        embed.set_footer(
                            text="Showing {}-{} out of {} pokémon matching this search.".format(
                                lists[c][0][0]["number"], lists[c][0][-1]["number"],
                                len1 ) )
                        await sent.edit( embed=embed )
                        await sent.add_reaction( "<:left:725668526869708881>" )
                        await sent.add_reaction( "<:right:725668611615621133>" )



@client.command()
async def start(ctx):
            chances = ["0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                       "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                       "0", "0", "0", "0", "0", "0", "0", "0"]
            shiny_chance = random.choice( chances )
            pokemonnn = random.randint( 0,890)
            pokemond = int(pokemonnn)
            with open( "mons.json", "r", encoding='utf8' ) as f:
                mons = json.load( f )
                mon1 = mons[pokemond-1]
                name = mon1["name"]["english"]
                level = random.randint(1,20)
                if shiny_chance == "0":
                    checkkk = db.child( "users" ).child( "{}".format(ctx.message.author.id ) ).get()
                    if checkkk.val() == None:
                                await ctx.send("Randomly giving you a pokemon for start.")
                                await ctx.message.channel.send(
                                    "Congratulations {}! You got a level {} {}!".format(ctx.message.author.mention,
                                                                                         level,
                                                                                         name))
                                hp_stats = random.randint( 0, 10 )
                                Attack_stats = random.randint( 0, 10 )
                                Defense_stats = random.randint( 0, 10 )
                                sp_attack_stats = random.randint( 0, 10 )
                                spdef_stats = random.randint( 0, 10 )
                                speed_stats = random.randint( 0, 10 )
                                overall_iv = hp_stats + Attack_stats + Defense_stats + sp_attack_stats + spdef_stats + speed_stats / 50 * 100
                                pokemonr = {"name": "{}".format( name ),
                                            "level": "{}".format( level ), "hp": "{}/10".format( hp_stats ),
                                            "attack": "{}/10".format( Attack_stats ),
                                            "defense": "{}/10".format( Defense_stats ),
                                            "sp atk": "{}/10".format( sp_attack_stats ),
                                            "sp def": "{}/10".format( spdef_stats ),
                                            "speed": "{}/10".format( speed_stats ), "IV": "{}%".format( overall_iv ),
                                            "shiny": "false",
                                            "number": "1",
                                            "selected":"yes",
                                        "id":"{}".format(pokemond)
                                            }
                                db.child("users").child("{}".format( ctx.message.author.id ) ).child("pokemons").child("{}".format(0)).set(pokemonr)
                                db.child("users").child("{}".format(ctx.message.author.id)).child("selected").set("0")
                    else:
                        embed = discord.Embed( title="**You have already started your journey , do ppokemon to see your pokemons.**",
                                               description="", color=0xff00f6 )
                        await ctx.send( embed=embed )
                elif shiny_chance == "1":
                   checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
                   if checkkk.val() == None:
                    await ctx.send( "Randomly giving you a pokemon for start." )
                    await ctx.message.channel.send(
                        "Congratulations {}! You got  a level {} ✨{}!".format( ctx.author.mention, level,
                                                                                        name ) )
                    hp_stats = random.randint( 0, 10 )
                    Attack_stats = random.randint( 0, 10 )
                    Defense_stats = random.randint( 0, 10 )
                    sp_attack_stats = random.randint( 0, 10 )
                    spdef_stats = random.randint( 0, 10 )
                    speed_stats = random.randint( 0, 10 )
                    overall_iv = hp_stats + Attack_stats + Defense_stats + sp_attack_stats + spdef_stats + speed_stats / 50 * 100
                    pokemonr = {"name": "{}".format( name ),
                                "level": "{}".format( level ), "hp": "{}/10".format( hp_stats ),
                                "attack": "{}/10".format( Attack_stats ),
                                "defense": "{}/10".format( Defense_stats ),
                                "sp atk": "{}/10".format( sp_attack_stats ),
                                "sp def": "{}/10".format( spdef_stats ),
                                "speed": "{}/10".format( speed_stats ), "IV": "{}%".format( overall_iv ),
                                "shiny": "true",
                                "number": "1",
                                "selected":"yes",
                                "id":"{}".format(pokemond)

                                }
                    db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child(
                        "{}".format( 0 ) ).set( pokemonr )
                    db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "selected" ).set( "0" )
                   else:
                    embed = discord.Embed(
                    title="**You have already started your journey , do ppokemon to see your pokemons.**",
                    description="", color=0xff00f6 )
                    await ctx.send( embed=embed )


@client.command()
@commands.guild_only()
async def info(ctx,*,stat):
    try:
        stat = int(stat)
        checkkk = db.child( "users" ).child("{}".format(ctx.message.author.id)).get()
        if checkkk.val() == None:
            await ctx.send( "Do pstart to start you pokemon journey " )
        else:
            lat_info1 = db.child( "users" ).child( "{}".format(ctx.message.author.id)).child( "pokemons" ).child("{}".format(stat- 1 ) ).get()
            check = lat_info1.val()

            items = list( check.items() )

            p_name = items[6][1]
            p_level = items[5][1]
            p_hp = items[3][1]
            p_atak = items[1][1]
            p_def = items[2][1]
            p_spatk = items[10][1]
            p_spdef = items[11][1]
            p_speed = items[12][1]
            p_iv = items[0][1]
            p_image = items[4][1]
            image = int(p_image)
            if "true" in items[9][1]:
                    if image < 10:
                        file = discord.File(
                            r"mon\poke_capture_000{}_000_mf_n_00000000_f_r.png".format(image ), filename="image.png" )
                    elif image > 9 and image < 100:
                        file = discord.File(
                            r"mon\poke_capture_00{}_000_mf_n_00000000_f_r.png".format(image ), filename="image.png" )
                    elif image > 99:
                        file = discord.File(
                            r"mon\poke_capture_0{}_000_mf_n_00000000_f_r.png".format(image ), filename="image.png" )
                    embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                           color=0xeee657 )
                    embed.add_field( name="**Level {} {}**".format( p_level, p_name ),
                                     value="**HP**:{}\n**Attack**:{}\n**Defense**:{}\n**Sp.Atk**:{}\n**Sp.Def**:{}\n**Speed**:{}\n**IV**:{}".format(
                                         p_hp, p_atak, p_def, p_spatk, p_spdef, p_speed, p_iv ), inline=False )

                    embed.set_image( url="attachment://image.png" )
                    await ctx.message.channel.send( file=file, embed=embed )
            elif "false" in items[9][1]:
                    if image < 10:
                        file = discord.File(
                            r"mon\poke_capture_000{}_000_mf_n_00000000_f_n.png".format(image ), filename="image.png" )
                    elif image > 9 and image < 100:
                        file = discord.File(
                            r"mon\poke_capture_00{}_000_mf_n_00000000_f_n.png".format(image ), filename="image.png" )
                    elif image > 99:
                        file = discord.File(
                            r"mon\poke_capture_0{}_000_mf_n_00000000_f_n.png".format(image ), filename="image.png" )
                    embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                           color=0xeee657 )
                    embed.add_field( name="**Level {} {}**".format( p_level, p_name ),
                                     value="**HP**:{}\n**Attack**:{}\n**Defense**:{}\n**Sp.Atk**:{}\n**Sp.Def**:{}\n**Speed**:{}\n**IV**:{}".format(
                                         p_hp, p_atak, p_def, p_spatk, p_spdef, p_speed, p_iv ), inline=False )

                    embed.set_image( url="attachment://image.png" )
                    await ctx.message.channel.send( file=file, embed=embed )
    except :
        stat = str(stat)
        if stat == "latest":
            checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
            if checkkk.val() == None:
                await ctx.send( "Do pstart to start you pokemon journey " )
            else:
                stat1 = len(db.child("users").child("{}".format(ctx.message.author.id)).child("pokemons").get().val())
                lat_info1 = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format(stat1-1)).get()
                check = lat_info1.val()

                items = list( check.items() )

                p_name = items[6][1]
                p_level = items[5][1]
                p_hp = items[3][1]
                p_atak = items[1][1]
                p_def = items[2][1]
                p_spatk = items[10][1]
                p_spdef = items[11][1]
                p_speed = items[12][1]
                p_iv = items[0][1]
                p_image = items[4][1]
                image = int( p_image )
                if "true" in items[9][1]:
                    if image < 10:
                        file = discord.File(
                            r"mon\poke_capture_000{}_000_mf_n_00000000_f_r.png".format( cwd,
                                                                                           image ),
                            filename="image.png" )
                    elif image > 9 and image < 100:
                        file = discord.File(
                            r"mon\poke_capture_00{}_000_mf_n_00000000_f_r.png".format( cwd,
                                                                                          image ),
                            filename="image.png" )
                    elif image > 99:
                        file = discord.File(
                            r"mon\poke_capture_0{}_000_mf_n_00000000_f_r.png".format( cwd,
                                                                                         image ), filename="image.png" )
                    embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                           color=0xeee657 )
                    embed.add_field( name="**Level {} ✨{}**".format( p_level, p_name ),
                                     value="**HP**:{}\n**Attack**:{}\n**Defense**:{}\n**Sp.Atk**:{}\n**Sp.Def**:{}\n**Speed**:{}\n**IV**:{}".format(
                                         p_hp, p_atak, p_def, p_spatk, p_spdef, p_speed, p_iv ), inline=False )

                    embed.set_image( url="attachment://image.png" )
                    await ctx.message.channel.send( file=file, embed=embed )
                elif "false" in items[9][1]:
                    if image < 10:
                        file = discord.File(
                            r"mon\poke_capture_000{}_000_mf_n_00000000_f_n.png".format( image ),
                            filename="image.png" )
                    elif image > 9 and image < 100:
                        file = discord.File(
                            r"mon\poke_capture_00{}_000_mf_n_00000000_f_n.png".format( image ),
                            filename="image.png" )
                    elif image > 99:
                        file = discord.File(
                            r"mon\poke_capture_0{}_000_mf_n_00000000_f_n.png".format(image ), filename="image.png" )
                    embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                           color=0xeee657 )
                    embed.add_field( name="**Level {} {}**".format( p_level, p_name ),
                                     value="**HP**:{}\n**Attack**:{}\n**Defense**:{}\n**Sp.Atk**:{}\n**Sp.Def**:{}\n**Speed**:{}\n**IV**:{}".format(
                                         p_hp, p_atak, p_def, p_spatk, p_spdef, p_speed, p_iv ), inline=False )

                    embed.set_image( url="attachment://image.png" )
                    await ctx.message.channel.send( file=file, embed=embed )

@client.command()
async def select(ctx,*,num:int):
    try:
        num = int(num)
        num1 = num-1
        checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
        if checkkk.val() == None:
            await ctx.send( "Do pstart to start you pokemon journey " )
        else:
            all_users = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
            if str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).get().val()) == "None":
                await ctx.send( "The given number to select pokemon is invalid :(" )
            elif str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).get().val()) != "None":
             for user in all_users.each():
                dict = user.val()
                if dict["selected"] == "yes":
                    nm = dict["number"]
                    n = int( nm )
                    db.child( "users" ).child( "{}".format(ctx.message.author.id) ).child( "pokemons" ).child("{}".format( n - 1 ) ).update( {"selected": "no"} )
                    print( "found :{}".format( user.key() ) )
             db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).update( {"selected": "yes"} )
             level = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format(num1)).child("level").get().val()
             name = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).child( "name" ).get().val()
             await ctx.send("You Selected your level {} {}.N°{}".format(level,name,num))
             db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "selected" ).set("{}".format(n))
    except:
        pass

        
'''
@client.command()
async def release(ctx,*,num:int):
    try:
        num = int(num)
        num1 = num-1
        checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
        if checkkk.val() == None:
            await ctx.send( "Do pstart to start you pokemon journey " )
        else:
            all_users = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).get()
            if str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).get().val()) == "None":
                await ctx.send( "The given number to select pokemon is invalid :(" )
            elif str(db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).get().val()) != "None":
                #list_pokemon = list()
             for user in all_users.each():
                dict = user.val()
                if dict["selected"] == "yes":
                    nm = dict["number"]
                    n = int( nm )
                    db.child( "users" ).child( "{}".format(ctx.message.author.id) ).child( "pokemons" ).child("{}".format( n - 1 ) ).update( {"selected": "no"} )
                    print( "found :{}".format( user.key() ) )
             db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).update( {"selected": "yes"} )
             level = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format(num1)).child("level").get().val()
             name = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "pokemons" ).child("{}".format( num1 ) ).child( "name" ).get().val()
             await ctx.send("You Selected your level {} {}.N°{}".format(level,name,num))
             db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).child( "selected" ).set("{}".format(n))
    except:
        pass
'''
@info.error
async def info_error(ctx, error):
    if isinstance( error, commands.MissingRequiredArgument):
        checkkk = db.child( "users" ).child( "{}".format( ctx.message.author.id ) ).get()
        if checkkk.val() == None:
            await ctx.send( "Do pstart to start you pokemon journey " )
        else:
            all_users = db.child( "users" ).child( "{}".format(ctx.message.author.id) ).child( "pokemons" ).get()
            for user in all_users.each():
                dict = user.val()
                if dict["selected"] == "yes":
                    nm = dict["number"]
                    n = int( nm )
                    print( "found :{}".format( user.key() ) )
                    p_name = dict["name"]
                    p_level = dict["level"]
                    p_hp = dict["hp"]
                    p_atak = dict["attack"]
                    p_def = dict["defense"]
                    p_spatk = dict["sp atk"]
                    p_spdef = dict["sp def"]
                    p_speed = dict["speed"]
                    p_iv = dict["IV"]
                    p_image = dict["id"]
                    image = int( p_image )
                    if "true" in dict["shiny"]:
                        if image < 10:
                            file = discord.File(
                                r"mon\poke_capture_000{}_000_mf_n_00000000_f_r.png".format( 
                                                                                               image ),
                                filename="image.png" )
                        elif image > 9 and image < 100:
                            file = discord.File(
                                r"mon\poke_capture_00{}_000_mf_n_00000000_f_r.png".format( 
                                                                                              image ),
                                filename="image.png" )
                        elif image > 99:
                            file = discord.File(
                                r"mon\poke_capture_0{}_000_mf_n_00000000_f_r.png".format( 
                                                                                             image ),
                                filename="image.png" )
                        embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                               color=0xeee657 )
                        embed.add_field( name="**Level {} {}**".format( p_level, p_name ),
                                         value="**HP**:{}\n**Attack**:{}\n**Defense**:{}\n**Sp.Atk**:{}\n**Sp.Def**:{}\n**Speed**:{}\n**IV**:{}".format(
                                             p_hp, p_atak, p_def, p_spatk, p_spdef, p_speed, p_iv ), inline=False )

                        embed.set_image( url="attachment://image.png" )
                        await ctx.send( file=file, embed=embed )
                    elif "false" in dict["shiny"]:
                        if image < 10:
                            file = discord.File(
                                r"mon\poke_capture_000{}_000_mf_n_00000000_f_n.png".format( 
                                                                                               image ),filename="image.png" )
                        elif image > 9 and image < 100:
                            file = discord.File(
                                r"mon\poke_capture_00{}_000_mf_n_00000000_f_n.png".format(  image ),filename="image.png" )
                        elif image > 99:
                            file = discord.File(
                                r"mon\poke_capture_0{}_000_mf_n_00000000_f_n.png".format( 
                                                                                             image ),filename="image.png" )
                        embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                               color=0xeee657 )
                        embed.add_field( name="**Level {} {}**".format( p_level, p_name ),
                                         value="**HP**:{}\n**Attack**:{}\n**Defense**:{}\n**Sp.Atk**:{}\n**Sp.Def**:{}\n**Speed**:{}\n**IV**:{}".format(
                                             p_hp, p_atak, p_def, p_spatk, p_spdef, p_speed, p_iv ), inline=False )

                        embed.set_image( url="attachment://image.png" )
                        await ctx.send( file=file, embed=embed )
                    break



@client.command(aliases=['dex'])
async def pokedex(ctx,*,mon):
    if not mon.startswith("shiny"):
        with open( "mons.json", "r", encoding="utf8" ) as f:
            mons = json.load( f )
            length = len( mons )
        for i in range( length ):
            if "{}".format( mon.lower() ) == mons[i]["name"]["english"].lower() or "{}".format( mon.lower() ) ==  mons[i]["name"]["german"].lower() or \
                    "{}".format( mon.lower() ) ==  mons[i]["name"]["japanese"][1].lower() or "{}".format( mon.lower() ) == mons[i]["name"]["japanese"][0].lower() or "{}".format( mon.lower() ) == mons[i]["name"]["french"].lower() or \
                "{}".format( mon.lower() ) ==  mons[i]["name"]["chinese"].lower():
                res = mons[i]["type"]
                eng = mons[i]["name"]["english"]
                jap = mons[i]["name"]["japanese"][0]
                jap1 = mons[i]["name"]["japanese"][1]
                chin= mons[i]["name"]["chinese"]
                germ = mons[i]["name"]["german"]
                stats = mons[i]["base"]
                id = mons[i]["id"]
                if mons[i]["name"]["french"] != "":
                    fren = mons[i]["name"]["french"]
                bool = "true"
                break
            elif "{}".format( mon.lower() )!= mons[i]["name"]["english"].lower() or "{}".format( mon.lower() ) != mons[i]["name"]["german"].lower() or \
                    "{}".format( mon.lower() ) != mons[i]["name"]["japanese"][1].lower() or "{}".format( mon.lower() ) != mons[i]["name"]["japanese"][0].lower() or "{}".format( mon.lower() ) != mons[i]["name"]["french"].lower() or \
                "{}".format( mon.lower() ) != mons[i]["name"]["chinese"].lower():
                bool = "false"
        print(bool)
        if bool == "true":
            if id < 10:
                file = discord.File(
                    r"mon\poke_capture_000{}_000_mf_n_00000000_f_n.png".format(
                                                                                   id ), filename="image.png" )
            elif id > 9 and id < 100:
                file = discord.File(
                    r"mon\poke_capture_00{}_000_mf_n_00000000_f_n.png".format(
                                                                                  id ), filename="image.png" )
            elif id > 99:
                file = discord.File(
                    r"mon\poke_capture_0{}_000_mf_n_00000000_f_n.png".format(
                                                                                 id ), filename="image.png" )
            embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                   color=0xeee657 )
            embed.add_field(name="**#{}-{}**".format(id,eng),value="Evolutions are not supported yet", inline=False)
            embed.add_field(name="**Alternative names**",value="Japnese:{},{}\nChinese:{}\nFrench:{}\nGerman:{}".format(jap,jap1,chin,fren,germ),inline=False)
            embed.add_field(name="**Base Stats**",value="{}".format(stats),inline=False)
            embed.add_field(name="**Types**",value="{}".format(res),inline=False)
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=file, embed=embed)
        elif bool == "false":
            await ctx.send("Pokemon not found, **Gen8 mons are not implemented yet**")
    elif mon.startswith("shiny"):
        querywords = mon.split()
        stopwords = ['shiny']
        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join( resultwords )
        mon = result
        with open( "mons.json", "r", encoding="utf8" ) as f:
            mons = json.load( f )
            length = len( mons )
        for i in range( length ):
            if "{}".format( mon.lower() ) == mons[i]["name"]["english"].lower() or "{}".format( mon.lower() ) == \
                    mons[i]["name"]["german"].lower() or \
                    "{}".format( mon.lower() ) == mons[i]["name"]["japanese"][1].lower() or "{}".format(
                mon.lower() ) == mons[i]["name"]["japanese"][0].lower() or "{}".format( mon.lower() ) == \
                    mons[i]["name"]["french"].lower() or \
                    "{}".format( mon.lower() ) == mons[i]["name"]["chinese"].lower():
                res = mons[i]["type"]
                eng = mons[i]["name"]["english"]
                jap = mons[i]["name"]["japanese"][0]
                jap1 = mons[i]["name"]["japanese"][1]
                chin= mons[i]["name"]["chinese"]
                germ = mons[i]["name"]["german"]
                stats = mons[i]["base"]
                id = mons[i]["id"]
                if mons[i]["name"]["french"] != "":
                    fren = mons[i]["name"]["french"]
                bool = "true"
                break
            elif "{}".format( mon.lower() ) != mons[i]["name"]["english"].lower() or "{}".format( mon.lower() ) != mons[i]["name"]["german"].lower() or \
                    "{}".format( mon.lower() ) != mons[i]["name"]["japanese"][1].lower() or "{}".format( mon.lower() ) != mons[i]["name"]["japanese"][0].lower() or "{}".format( mon.lower() ) != mons[i]["name"]["french"].lower() or \
                "{}".format( mon.lower() ) !=  mons[i]["name"]["chinese"].lower():
                bool = "false"
        print(bool)
        if bool == "true":
            if id < 10:
                file = discord.File(
                    r"mon\poke_capture_000{}_000_mf_n_00000000_f_r.png".format(
                                                                                   id ), filename="image.png" )
            elif id > 9 and id < 100:
                file = discord.File(
                    r"mon\poke_capture_00{}_000_mf_n_00000000_f_r.png".format(
                                                                                  id ), filename="image.png" )
            elif id > 99:
                file = discord.File(
                    r"mon\poke_capture_0{}_000_mf_n_00000000_f_r.png".format(
                                                                                 id ), filename="image.png" )
            embed = discord.Embed( title="**<:choduoak:745318454986276895> Professor Oak**", description="",
                                   color=0xeee657 )
            embed.add_field(name="**✨#{}-{}**".format(id,eng),value="Evolutions are not supported yet", inline=False)
            embed.add_field(name="**Alternative names**",value="Japnese:{},{}\nChinese:{}\nFrench:{}\nGerman:{}".format(jap,jap1,chin,fren,germ),inline=False)
            embed.add_field(name="**Base Stats**",value="{}".format(stats),inline=False)
            embed.add_field(name="**Types**",value="{}".format(res),inline=False)
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=file, embed=embed)
        elif bool == "false":
            await ctx.send("Pokemon not found, **Gen8 mons are not implemented yet**")


client.run(token)