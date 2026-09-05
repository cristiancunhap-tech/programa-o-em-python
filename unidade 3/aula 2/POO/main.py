class Carro:
    def __init__(self, cor, ano, modelo):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo


carro = Carro("Prata", "2025", "hilux")



class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha


usuario_correto = "Cristian"
senha_correta = "1234"

usuario = input("Digite o seu usuario: ")
senha = input("Digite a sua senha: ")

login = Login(usuario, senha)

if login.usuario == usuario_correto and login.senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Login falhou!")

