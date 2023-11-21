from repositorio import banco
from adicionar import adicionarProduto

def listarProdutos():
    print('---- LISTA DE PRODUTOS ----')
    for produto in banco:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")
        print('-'*50)

if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perifericos', 135.00)
    adicionarProduto('Monitor Philco', 'Monitores', 750.00)
    listarProdutos()