from use_cases.buscar_por_cod import buscarPorCodigo
from repositorio import banco
from adicionar import adicionarProduto

def deletarProduto(codigo: int) -> None:
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto deletado com sucesso!')
    else:
        print('Produto não encontrado!')

if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perifericos', 135.00)
    adicionarProduto('Monitor Philco', 'Monitores', 750.00)
    deletarProduto(1)
    deletarProduto(99)
    print(banco)