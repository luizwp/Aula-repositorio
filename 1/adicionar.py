import repositorio
from repositorio import banco
# codigo - nome - categoria - preço
def adicionarProduto(nome, categoria, preco):
    repositorio.cod_atual += 1
    produto = {
        "codigo": repositorio.cod_atual,
        "nome": nome,
        "categoria": categoria,
        "preco": preco
    }
    banco.append(produto)
    print('Produto adicionado com sucesso!')