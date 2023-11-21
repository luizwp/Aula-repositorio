from use_cases.buscar_por_cod import buscarPorCodigo


def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
    else:
        print('Produto não encontrado!')

