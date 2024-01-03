import json

def load_games_from_json(file_path:str):
    with open(file_path, "r") as file:  #Desta forma abstrai-se o uso do file.close()
        game = json.load(file)
    return game

if __name__ == "__main__":
    video_game = load_games_from_json('leitura_tests/data/jogos.json')

print(video_game['consoles'])
    

def get_all_consoles(list):
    consoles = set()
    for console in list:
        consoles.add(console['nome'])
    return consoles

print(get_all_consoles(video_game['consoles']))    

   