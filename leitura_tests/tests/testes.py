from src.games_report import get_all_consoles

def test_get_all_consoles():
    data = [
        {
            "nome": "PlayStation 5",
            "fabricante": "Sony",
            "ano_lancamento": 2020
        },
        {
            "nome": "Xbox Series X",
            "fabricante": "Microsoft",
            "ano_lancamento": 2020
        },
        {
            "nome": "Nintendo Switch",
            "fabricante": "Nintendo",
            "ano_lancamento": 2017
        },
        {
            "nome": "PC",
            "fabricante": "Diversos",
            "ano_lancamento": 2015
        }
    ]
    consoles = get_all_consoles(data)
    assert consoles == ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PC"]
