produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 150},
    {"nome": "Smartphone", "preco": 1800},
    {"nome": "Cadeira", "preco": 900},
    {"nome": "Monitor", "preco": 1200}
]

produtos_caros = [produto for produto in produtos if produto["preco"] > 1000]

print(produtos_caros)


