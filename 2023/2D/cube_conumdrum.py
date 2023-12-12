from rich import print

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


class Color:
    name: str
    count: int


class ColorSet:
    colors: list[Color]


class Game:
    game_name: int
    color_sets: list[ColorSet]


lines = test_input.splitlines()


def make_games(lines):
    games = []
    for index_g, line in enumerate(lines):
        game = Game()
        game.game_name = line.split(":")[0]
        color_sets = line.split(":")[1].split(";")
        # print("sets = ", len(color_sets))
        # print("sets = ", color_sets)
        # print(index_g, game.game_name)
        # loop through color_sets and print the index and the set
        for index_cs, color_set in enumerate(color_sets):
            # print(index_g, color_set)
            # loop through the color_set and print the index and the color
            for index_c, color in enumerate(color_set.split(",")):
                # print(index_g, color)
                color_name = color.split()[1]
                color_count = color.split()[0]
                # print(color_count, color_name)
                # print the sum of each color_count if the color_name is the same and the index is the same
                # print(index_g, color_name, color_count)
                # append index_g, color_name, color_count to games
                games.append(
                    {
                        "game_name": {game.game_name[-1]: {color_name: color_count}},
                    }
                )
    return games


games = make_games(lines)
print(games)
# color_dict_names = {
#     "red": 0,
#     "blue": 0,
#     "green": 0,
# }
# game dict that will be a count of the colors but the count of the games is unknown and the count of the colors is unknown


# write a function that takes a list of of dictionaries and adds the values of color_name if the index_g is the same
# def sum_colors(games):
#     games_dict = {}
#     # loop through games
#     for game in games:
#         # loop through game
#         for game_name in game:
#             # if game[game_name].key is in color_dict_names add the value of the key to the value of the key in color_dict_names. do this for each game
#             if game[game_name].keys() in color_dict_names.keys():
#                 color_dict_names[game[game_name].keys()] += game[game_name].values()
#             # else add the key to color_dict_names and set the value to the value of the key in game
#             else:
#                 color_dict_names[game[game_name].keys()] = game[game_name].values()
#     print(color_dict_names)
#     print(games_dict)


def sum_colors(games):
    color_dict_names = {"red": 0, "blue": 0, "green": 0}
    games_dict = {}
    # loop through games
    for game in games:
        # loop through game
        for color_dict in game.values():
            # loop through the color_dict and if the game[game_name] key is in color_dict_names print the key and the value
            # print(color_dict)
            for color_name, color_count in color_dict.items():
    #             if color_name in color_dict_names.keys():
    #                 color_dict_names[color_name] += int(color_count)
    #             else:
    #                 color_dict_names[color_name] = int(color_count)
    # print(color_dict_names)


sum_colors(games)
