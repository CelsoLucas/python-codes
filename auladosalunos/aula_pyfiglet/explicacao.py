import pyfiglet

text = "Hello World"
ascii_art_standard = pyfiglet.figlet_format(text, font="standard")
print(ascii_art_standard)

ascii_art_starwars = pyfiglet.figlet_format(text, font="starwars")
print(ascii_art_starwars)

ascii_art_starwars = pyfiglet.figlet_format(text, font="block")
print(ascii_art_starwars)

ascii_art_starwars = pyfiglet.figlet_format(text, font="script")
print(ascii_art_starwars)

ascii_art_starwars = pyfiglet.figlet_format(text, font="lean")
print(ascii_art_starwars)