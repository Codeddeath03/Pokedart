import os
from flask import Flask, jsonify, request
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from discord_interactions import verify_key_decorator
import json
import pyrebase
from dotenv import load_dotenv
import ast
load_dotenv()
token = os.environ.get('token')
config = os.environ['config']
config = json.loads(config)
email = os.environ.get('email')
password = os.environ.get('password')
firebase= pyrebase.initialize_app(config)
db = firebase.database()

DISCORD_PUBLIC_KEY = os.environ.get("public_key")

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)


@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)


@verify_key_decorator(DISCORD_PUBLIC_KEY)
def interact(raw_request):
    if raw_request["type"] == 1:  # PING
        response_data = {"type": 1}  # PONG
    else:
        data = raw_request["data"]
        command_name = data["name"]
        #redirect function -admin check
        if command_name == "redirect":
            # Handle redirect command
            print(data["options"])
            channel_id = data["options"][0]["value"]  # Extract channel ID from options
            channel_name = data["resolved"]["channels"][str(channel_id)]['name']
            channeel = channel_id
            cid = ''.join( d for d in channeel if d.isdigit() )
            idd = int( cid )
            print(idd)
            channel1 = channel_id
            print(channel1)
            guild_id = data["guild_id"]
            print(guild_id)
            print("hohohoohohoh")
            checkkk = db.child( "servers" ).child("{}".format(guild_id)).get().val()
            print("is this true hahahah?",checkkk)
            if str(channel1) != "None":
                if str(checkkk) == "None":
                 print("booombaaam")
                 ok = "{}".format(idd)
                 db.child( "servers" ).child("{}".format(guild_id)).set(ok)
                 print( "ok" )
                 #await ctx.send( "{}'s spawn channel set to {}".format( ctx.message.guild.name, channel1 ) )
                 message_content = f"Spawn channel set to {channel_name}"
                else:
                    print("channel found")
                    spawnchannel = int(checkkk)
                    if spawnchannel == idd:
                        print("same channel")
                        ok1 = "{}".format(idd)
                        db.child( "servers" ).child("{}".format(guild_id)).set(ok1)
                        message_content = f"Spawn channel again set to {channel_name}"
                   # await ctx.send( "{}'s spawn channel again set to {}".format( ctx.message.guild.name, channel1 ) )
                    elif spawnchannel != idd:
                        print( "switching channel" )
                        ok1 = "{}".format(idd)
                        db.child( "servers" ).child( "{}".format( guild_id ) ).set( ok1 )
                        message_content = f"Spawn channel changed to {channel_name}"
                    #await ctx.send( "{}'s spawn channel changed to {}".format( ctx.message.guild.name, channel1 ) )
                        print(spawnchannel)
                response_data = {
                        "type": 4,
                        "data": {
                        "embeds": [
                        {
                            
                            "color": 15663191,  # Embed color (decimal value)
                            "fields": [
                            {"name": "", "value": message_content, "inline": True}
                            ],
                            
                        }
                        ]
                    },
                }        
        elif command_name == "balance":
            data = f"{raw_request}"
            data = ast.literal_eval(data)
            print(type(data))
            author=data['member']['user']['id']
            auth_name=data['member']['user']['global_name']
            if str(db.child( "users" ).child( "{}".format( author ) ).child( "credits" ).get().val()) == "None":
                db.child( "users" ).child( "{}".format( author ) ).child( "credits" ).set("0")
                response_data = {
                        "type": 4,
                        "data": {
                        "embeds": [
                        {
                            "title": f"**{auth_name}'s balance**",
                            "description": "You currently have 0 credits!",
                            "color": 15663191,  # Embed color (decimal value)
                            "thumbnail": {"url": "https://cdn.discordapp.com/attachments/703612469226242109/740210658112569435/money-bag_1f4b0.png"},  # Optional thumbnail
                    
                        }
                        ]
                    },
                }
            elif str(db.child( "users" ).child( "{}".format( author ) ).child( "credits" ).get().val()) != "None":
                earned = db.child( "users" ).child( "{}".format( author ) ).child( "credits" ).get().val()
                response_data = {
                        "type": 4,
                        "data": {
                        "embeds": [
                        {
                            "title": f"**{auth_name}'s balance**",
                            "description": f"You currently have {earned} credits!",
                            "color": 15663191,  # Embed color (decimal value)
                            "thumbnail": {"url": "https://cdn.discordapp.com/attachments/703612469226242109/740210658112569435/money-bag_1f4b0.png"},  # Optional thumbnail
                    
                        }
                        ]
                    },
                }

        elif command_name == "redeem":
            data = f"{raw_request}"
            data = ast.literal_eval(data)
            author=data['member']['user']['id']
            auth_name=data['member']['user']['global_name']
            if str(db.child( "users" ).child( "{}".format( author ) ).child( "redeems" ).get().val()) == "None":
                ar = { "redeems":"0"}
                db.child( "users" ).child( "{}".format( author ) ).child( "redeems" ).set(ar)
                response_data = {
                        "type": 4,
                        "data": {
                        "embeds": [
                        {
                            "title": f"**Your Redeems:0 💸**",
                            "description": f"***To obtain a redeem , You can get it through ``pdialy command``***",
                            "color": 15663191,  # Embed color (decimal value)
                            
                        }
                        ]
                    },
                }
            elif str(db.child( "users" ).child( "{}".format( author ) ).child( "redeems" ).get().val()) != "None":
                earned = db.child( "users" ).child( "{}".format(author) ).child( "redeems" ).get().val()
                response_data = {
                        "type": 4,
                        "data": {
                        "embeds": [
                        {
                            "title": f"**Your Redeems:{earned} 💸**",
                            "description": f"***To obtain a redeem , You can get it through ``pdaily command``***",
                            "color": 15663191,  # Embed color (decimal value)
                            
                        }
                        ]
                    },
                }
        elif command_name == "help":
            response_data = {
                        "type": 4,
                        "data": {
                        "embeds": [
                        {
                            "title": f"**Help**",
                            "color": 15663191,  # Embed color (decimal value)
                             "fields": 
                                    [
                                    {"name": "**Redirecting to a channel**", "value": "Use /redirect #channel ``User need to be an Admin``", "inline": True},
                                    {"name": "**pcatch**", "value": "Use pcatch pokemon-name to catch the pokemon", "inline": True},
                                    {"name": "**ppokemon**", "value": "Use ppokemon for listing your caught pokemons\nUse ppokemon --shiny for only listing shinies", "inline": True},
                                    {"name": "**pbalance**", "value": "**Use pbalance for knowing your owned credits**", "inline": True},
                                    {"name": "**pdaily**", "value": "**Use pdaily once every 24hrs to get your daily credits**", "inline": True},
                                    {"name": "**pinfo**", "value": "**Use pinfo for checking stats of your buddy pokemon/n use pinfo latest for checking the stats of recently caught pokemon**", "inline": True},
                                    {"name": "**pselect**", "value": "**Use pselect {pokemon_number} to set your buddy pokemon**", "inline": True},
                                    {"name": "**ppokedex**", "value": "**Use ppokedex poke_name to get to know more about that pokemon**", "inline": True},
                                    {"name": "**Trade**", "value": "**use ``ptrade @user`` to trade pokemons with other user**", "inline": True},
                                    
                                    ]
                            
                        }
                        ]
                    },
                }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)

""""title": "Embed Title",
                            "description": "Embed Description","""
""""thumbnail": {"url": "https://example.com/thumbnail.jpg"},  # Optional thumbnail
                            "image": {"url": "https://example.com/image.jpg"},  # Optional image
                            "footer": {"text": "Embed Footer"}  # Optional footer"""