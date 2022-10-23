import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='mc152030',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()

#    with conecta() as conexao:
#        with conexao.cursor() as cursor:
#            sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
#                '(%s, %s, %s, %s)'  
#            cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#            conexao.commit()

#    with conecta() as conexao:
#        with conexao.cursor() as cursor:
#            sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
#                '(%s, %s, %s, %s)'  
#            dados = [
#                ('Muriel', 'Figueredo', 19, 75), ('Ana', 'Clara', 21, 59), 
#                ('Renato', 'Russo', 37, '94'), ('Olivio', 'Leite', 78, 92),
#                ('Flavio', 'Silva', 42, 104), ('Fernanda', 'Lima', 27, 67),
#                ('Silvio', 'Brito', 58, 87), ('Fabio', 'Fernandes', 84, 78),
#            ]      
#            cursor.executemany(sql, dados)
#            conexao.commit()


#    with conecta() as conexao:
#        with conexao.cursor() as cursor:
#            sql = 'DELETE FROM clientes WHERE id= %s'
#            cursor.execute(sql, (6,))
#            conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Joana', 5))
        conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)



