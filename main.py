import random

import discord
from discord.ext import commands

import algorithms
import algorithms.bubble_sort
import algorithms.selection_sort
import algorithms.insertion_sort
import algorithms.merge_sort
import algorithms.utils

import io
import os
from dotenv import load_dotenv

# This is a sample Python script.
load_dotenv()
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

bot = commands.Bot(command_prefix="$")

algorithms_map = {
    "bubble": algorithms.bubble_sort.sort,
    "selection": algorithms.selection_sort.sort,
    "insertion": algorithms.insertion_sort.sort,
    "merge": algorithms.merge_sort.sort
}


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("Pong")


@bot.command()
async def sort(ctx: commands.Context, algorithm: str, length: int):
    if length > 64:
        await ctx.send("Too long for visualizer. Please open pull request if you want this.")
        return
    if length < 8:
        await ctx.send("Too short to sort.")
        return
    sort_algorithm = algorithms_map.get(algorithm)
    if not sort_algorithm:
        await ctx.send("Invalid or there is no such algorithm. You may consider sending PR.")
        return
    llist = list(range(1, length + 1))
    random.shuffle(llist)
    spec_sequence = sort_algorithm(llist)
    image_sequence = algorithms.utils.draw_queue(spec_sequence)
    with io.BytesIO() as image_binary:
        first_frame = image_sequence[0]
        first_frame.save(image_binary, 'GIF', save_all=True, append_images=image_sequence[1:], optimize=False,
                         duration=100)
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="sort.gif"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.run(os.getenv("DISCORD_TOKEN"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
