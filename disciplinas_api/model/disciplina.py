# Exceção lançada quando se tenta associar um ID a uma entidade que já possui um.
class NaoTransienteException(Exception):
    pass

class AlunoJaInclusoException(Exception):
    pass

class Disciplina():
    
    def __init__(self, nome, professor_id):
        self.id = None
        self.nome = nome
        self.professor_id = professor_id
        self.alunos = []
    
    def associar_id(self, id):
        if self.id != None:
            raise NaoTransienteException
        self.id = id
            
    def incluir_aluno(self, aluno_id):
        if aluno_id in self.alunos:
            raise AlunoJaInclusoException
        self.alunos.append(aluno_id)

    def associar_alunos(self, alunos):
        for i in alunos:
            self.alunos.append(i)
    
    def remover_aluno(self, aluno_id):
        self.alunos.remove(aluno_id)
    
    def verificar_transiente(self):
        if self.id != None:
            return False
        return True
    
    def validar(self):
        if self.id != None and self.nome != None:
            return True
        return False
    
    def atualizar(self, dados):
        try:
            self.nome = dados['nome']
        except Exception as e:
            print('Problema ao atualizar disciplina')
            print(e)

    def __dict__(self):
        dicionario = dict()
        dicionario['id'] = self.id,
        dicionario['nome'] = self.nome,
        dicionario['professor_id'] = self.professor_id
        return dicionario

    @staticmethod
    def criar(dados):
        try:
            nome = dados['nome']
            professor = dados['professor_id']
            return Disciplina(nome=nome, professor_id=professor)
        except Exception as e:
            print('Problema ao criar a disciplina')
            print(e)
    
    @staticmethod    
    def criar_com_id(id, nome, professor_id):
        try:
            disciplina = Disciplina(nome=nome, professor_id=professor)
            disciplina.associar_id(id)
            return disciplina
        except Exception as e:
            print('Problema ao criar a disciplina e adicionar o id')
            print(e)
