from json import dumps, loads, dump, load


with open("text.txt", mode= "w", encoding= "utf8") as fd:
    fd.write("Ahoj\nhello\ntohle je textový soubor\n")
    fd.write("Ahoj\nhello\ntohle je textový soubor\n")


with open("text.txt", mode= "r", encoding= "utf8") as fd:
    print(fd.read(2))
    print(fd.read(2))

with open("cvic.txt", mode= "w", encoding= "utf8") as fd:
    fd.write("#-----\n-#----\n--#---\n---#--\n----#-\n-----#")




def make_diagonal(width, main_char, diagonal_char):
    with open("cvic.txt", mode= "w", encoding= "utf8") as fd:
        for i in range(width):
            fd.write((main_char * i) + diagonal_char + ((width-1-i) * main_char) + "\n")

make_diagonal(10, "--", "##")



# "--" * 2 == "----"

# "-"*3 == "---"
# main_char * 3 == "---"

# "--" + "#" + "---" == "--#---"


my_dict = {
    "alice": 1,
    "bob": 20,
    "clara": 3
}

new_dict = {}

# with open("data.json", mode= "r") as fd:
#     data_str = fd.read()
#     new_dict = loads(data_str)

# print(new_dict)

# with open("data.json", mode= "w") as fd:
#     data_str = dumps(my_dict)
#     fd.write(data_str)

# with open("data.json", mode= "r") as fd:
#     new_dict = load(fd)

# print(new_dict)

# with open("data.json", mode= "w") as fd:
#     dump(my_dict, fd)



def load_hs():
    high_score = 0
    with open("game_data.json", mode= "r") as fd:
        data = load(fd)
        high_score = data["high_score"]
    return high_score

def save_hs(high_score):
    with open("game_data.json", mode= "w") as fd:
        data = {
            "high_score": high_score
        }
        dump(data, fd)



high_score = load_hs()
high_score += 1

print(high_score)

save_hs(high_score)



with open("data.json", mode= "r") as fd:
    data = load(fd)
    make_diagonal(data["width"], data["main_char"], data["dia_char"])