import pyodbc 


server = 'INDUSTRIALBRAIN\SQLEXPRESS' # Endereço do banco
database = 'Production' # Nome do Banco
username = 'sa'  # Usuário do banco
password = '122003' # Senha
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
';DATABASE='+database+';UID='+username+';PWD='+ password) # Não alterar
cursor = cnxn.cursor()

#Exemplo comando select, carrega as primeiras 1000 linhas
cursor.execute("SELECT TOP (1000) [id],[productionOrder],[partNumber],[quantity],[date]FROM [Production].[dbo].[productionOrder]") 
row = cursor.fetchone() 
while row: 
    print(row[0], row[1], row[2], row[3], row[4])
    row = cursor.fetchone()

#Insere dados no banco
count = cursor.execute("""INSERT INTO [dbo].[productionOrder]
           ([productionOrder],
           [partNumber],
           [quantity],
           [date]
           )
     VALUES
           ('1234567890',
           '0987654321',
           200,
           '2022-07-18')""")

cnxn.commit()
print('Rows inserted: ' + str(count))