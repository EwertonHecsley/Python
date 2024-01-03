import json

def load_games_from_json(file_path:str):
    file = open(file_path, "r")
    game = json.load(file)
    file.close()
    return game

video_game = load_games_from_json('leitura_tests/data/jogos.json')

for game in video_game['jogos']:
    print(game['titulo'])
    print(game['plataforma'])
    
   