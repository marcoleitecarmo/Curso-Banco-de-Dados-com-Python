import sqlite3

conexao = sqlite3.connect('basedados.db')  # criando banco de dados.
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#               'nome TEXT,'
#               'peso REAL'
#               ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Luiz Otavio", 80.0)')
# conexao.commit()3

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', # Alterar dados.
#               {'nome': 'Fernanda Lima', 'id': 2})

# cursor.execute('DELETE FROM clientes WHERE id=:id',  # Excluir dados
#               {'id': 4})


conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    codigo, nome, peso = linha

    print(codigo, nome, peso)


cursor.close()
conexao.close()
