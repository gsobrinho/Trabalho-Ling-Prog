
import pickle
def criaArquidvoDados():
    import pickle    
    aux = []
    with open('dados.pic', 'wb') as handle:
        pickle.dump(aux, handle, protocol=pickle.HIGHEST_PROTOCOL)
# c
def updados(pessoa ):
    import pickle    
    with open('dados.pic', 'rb') as handle:
        aux = pickle.load(handle)
    aux.append(pessoa)

    with open('dados.pic', 'wb') as handle:
        pickle.dump(aux, handle, protocol=pickle.HIGHEST_PROTOCOL)

def getDados():
    import pickle    
    with open('dados.pic', 'rb') as handle:
        aux = pickle.load(handle)
        return aux
