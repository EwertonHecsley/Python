import json

def load_games_from_json(file_path:str):
    with open(file_path, "r") as file:  #Desta forma abstrai-se o uso do file.close()
        game = json.load(file)
    return game

video_game = load_games_from_json('leitura_tests/data/jogos.json')

for game in video_game['jogos']:
    print(game['titulo'])
    print(game['plataforma'])
    
   