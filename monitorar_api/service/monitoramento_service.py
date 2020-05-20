from monitorar.model import monitoramento as m

def listar_mudancas():
    return [monitoramento.__dict__ for monitoramento in dao_listar()]



