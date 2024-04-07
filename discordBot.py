import asyncio
import discord
from discord import Embed
from discord.ui import View, Button
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True 
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('CHANNEL_ID'))

class yes_no(View):
    def __init__(self, channel):
        super().__init__(timeout=None)
        self.channel = channel
        self.value = None

    async def disableAll(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    @discord.ui.button(label="Save", style=discord.ButtonStyle.green, custom_id="save-button")
    async def callback_1(self, interaction, button):
        await interaction.response.edit_message(view=self)
        self.value = 1
        self.stop()

    @discord.ui.button(label="Run", style=discord.ButtonStyle.green, custom_id="run-button")
    async def callback_2(self, interaction, button):
        await interaction.response.edit_message(view=self)
        self.value = 2
        self.stop()

    @discord.ui.button(label="Kill", style=discord.ButtonStyle.red, custom_id="kill-button")
    async def callback_3(self, interaction, button):
        await interaction.response.edit_message(view=self)
        self.value = 3
        self.stop()

    @discord.ui.button(label="RKill", style=discord.ButtonStyle.red, custom_id="rkill-button")
    async def callback_4(self, interaction, button):
        await interaction.response.edit_message(view=self)
        self.value = 4
        self.stop()

async def getResponse():
    channel = bot.get_channel(CHANNEL)

    file = discord.File("test.gif")
    e = Embed(title="Potential Tint Found")
    e.set_image(url="attachment://test.gif")

    view = yes_no(channel)
    await channel.send(file = file, embed=e, content="", view=view)

    await view.wait()

    # await channel.send(f"your response = {view.Value}")

    return view.value
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

async def main():
    bot_task = asyncio.create_task(bot.start(TOKEN))

    await asyncio.sleep(5)

    result = await getResponse()

    print(result)

    while(True):
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())