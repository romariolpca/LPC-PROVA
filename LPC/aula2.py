class Endereco (self,logradouro,estado):
    logradouro = None
    estado = ''

    def __init__(self,logradouro= ''):
        self.logradouro = logradouro
        self.estado = estado

# ************************************************************

class Projeto (self):
    nome
    numIdentificacao

# ************************************************************

class Tarefa (self):
    
    def __init__(self,descricao= '',dataInicio='',dataFim='',prioridade=''):
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.prioridade = prioridade

            '''Agregação de Projeto '''
            
self.numIdentificacao = Projeto (numIdentificacao)
self.idPessoa = Pessoa(56)

    def criarTarefa(object):


    def executarTarefa(object):

    def statusTarefa (object):
# ************************************************************

    
class Pessoa ():
     

#Construtor
    def __init__(self,idPessoa = 0, nome = '' ,data_nascimento = '',idade = 0, raca = '',sexo = ''):
        self.idPessoa = idPessoa
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idade = idade
        self.raca = raca
        self.sexo = sexo
        self.endereco = Endereco ('rua 1','TO')



    def __str__(self):
        return self.nome


# ************************************************************
#Herda caracteristicas de Pessoa

class PessoaFisica (Pessoa):

#Construtor
    def __init__(self,cpf = '',nome = '',data_nascimento= ''):
        Pessoa.__init__(self,nome,data_nascimento)
        self.cpf = cpf

    def __str__ (self):
        return u'{} - {}'.format (self.cpf, self.nome)

    def executa ():


# ************************************************************

#Herda caracteristicas de Pessoa

class PessoaJuridica (Pessoa):

#Construtor
    def __init__ (self, CNPJ = '' , nome='', data_nascimento=''):
        Pessoa.__init__(self,nome,idade)
        self.CNPJ = CNPJ


    def solicita ():
        


    






    
