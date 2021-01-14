import logging
import random
import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Bruh {round(client.latency * 1000)} ms')

@client.command()
async def jc(ctx):
    await ctx.send('Jorge chúpalo')

@client.command(aliases=['bola8', 'test'])
async def _8ball(ctx, *, question): # * is for taking multiple arguments as one
    responses =['En mi opinión, si',
                'Es cierto',
                'Es decididamente así',
                'Probablemente',
                'Buen pronóstico',
                'Todo apunta a que si',
                'Sin duda',
                'Si',
                'Si - definitivamente',
                'Debes confiar en ello',
                'Respuesta vaga, vuelve a intentarlo',
                'Pregunta en otro momento',
                'Será mejor que no te lo diga ahora',
                'No puedo predecirlo ahora',
                'Concéntrate y vuelve a preguntar',
                'Pueder ser',
                'No cuentes con ello',
                'Mi respuesta es no',
                'Mis fuentes me dicen que no',
                'Las perspectivas no son buenas',
                'Muy dudoso']
    if question.upper() == 'EL JORGE SE LA COME?':
        await ctx.send(f'{random.choice(responses[0:8])}')
    else:
        await ctx.send(f'{random.choice(responses)}')

client.run('NzY4MzA1NzIwNTMzMTg4NjA5.X4-idg.eMElndHW4CWibwYsJc6PMzKdUIc')



'''
import logging
import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged d in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('mati chupalo')

client.run('NzY4MzA1NzIwNTMzMTg4NjA5.X4-idg.eMElndHW4CWibwYsJc6PMzKdUIc')
'''

