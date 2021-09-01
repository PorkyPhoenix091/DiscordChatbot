import discord
import os
from neuralintents import GenericAssistant

client = discord.Client()
#importing the secret
my_token = os.environ['token']

client.run(my_token)
