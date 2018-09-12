import psycopg2
#pip install psycopg2-binary

class ConexaoBanco:

    def __init__(self):
        self.conexao = self.iniciarConexao()
        self.criarTabelas()

    def iniciarConexao(self):
        try:
            conexao = psycopg2.connect("host=localhost dbname=exemplo user=postgres password=secret")
            return conexao
        except:
            print("Falha ao conectar com o banco ")

    def criarTabelas(self):
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pessoa
                             (id int PRIMARY KEY, nome text, idade int)''')
        self.conexao.commit()

    def persistir(self):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO pessoa VALUES (2,'Diego',30)")
        self.conexao.commit()

    def encerrarConexao(self):
        self.conexao.close()

    def ler(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM pessoa WHERE id=%s', ('2',))
        print(cursor.fetchone())

conexaoBanco = ConexaoBanco()
conexaoBanco.persistir()
conexaoBanco.ler()
conexaoBanco.encerrarConexao()


