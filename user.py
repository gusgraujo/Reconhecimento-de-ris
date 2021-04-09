



class Usuario ():
    def __init__(self,id,nome,idade,data,caminho):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.data = data 
        self.caminho = caminho



    def getName(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getData(self):
        return self.data
    def getCaminho(self):
        return self.idade
    def getId(self):
        return self.id



def cadastrar(listaDados,nome,idade,data,caminho):
        #Pegar ultimo ID
        ultimo = listaDados[len(listaDados)]
        newId = ultimo.id + 1

        novoUsuario = Usuario(newId,nome,idade,data,caminho)
        #Cadastra novo usuario
        listaDados.apppend(novoUsuario)

        return listaDados


def removerUser(listaDados,usuario):
    listaDados.remove(usuario)
    return listaDados