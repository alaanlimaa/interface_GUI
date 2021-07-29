import mysql.connector

connect = mysql.connector.connect(host='localhost', user='root', password='28101565', database='gui_interface_dados')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
    cursor = connect.cursor()
    arquivo = open('dados.txt', 'r')
    lines = arquivo.readlines()
    for line in lines:
        cursor.execute(f'insert into clientescadastro (nome, sobrenome, usuario, contato, senha) '
                       f'values {line}')
        connect.commit()
    arquivo.close()
connect.close()
if connect.is_closed():
    print(f'\033[1;32mDados adcionados com sucesso no banco de dados MySQL versão {connect.get_server_info()}!\033[m')
