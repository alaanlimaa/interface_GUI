def cadastro_dados_bd():
    import mysql.connector
    connect = mysql.connector.connect(host='localhost', user='root', password='28101565', database='gui_interface_dados')