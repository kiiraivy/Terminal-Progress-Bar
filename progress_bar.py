import math
import colorama

def progress_bar(progress, total, bar_length=30, color=colorama.Fore.LIGHTCYAN_EX):
    percent = 100 * (progress / float(total))
    filled_length = int(bar_length * progress // total)
    bar = '■' * filled_length + '-' * (bar_length - filled_length)
    print(color + f'\r|{bar}| {percent:.2f}%', end ='\r')

total = int(input('What is your word count goal?'))
progress = int(input('What is your current word count?'))

progress_bar(progress,total)
print()