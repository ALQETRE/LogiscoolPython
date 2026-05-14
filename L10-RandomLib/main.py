import emoji, art, pyjokes

print(emoji.emojize("Hello :hear-no-evil_monkey:"))
print()

print(emoji.demojize("Ahoj 🥶 text"))


art.tprint("Hello", font= "rnd-xlarge")

print(art.art("random"))

print(pyjokes.get_joke(category= "chuck"))

import freegames.snake