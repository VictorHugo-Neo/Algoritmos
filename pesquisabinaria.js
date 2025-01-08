function pesquisaBinaria(lista, item) {
    let baixo = 0;
    let alto = lista.length - 1;

    while (baixo <= alto) {
        let meio = Math.floor((baixo + alto) / 2);
        let chute = lista[meio];

        console.log('meio:', meio);

        if (chute === item) {
            return meio;
        }
        if (chute > item) {
            alto = meio - 1;
        } else {
            baixo = meio + 1;
        }
    }
    return null;
}

const minhaLista = [1, 3, 5, 7, 9];
console.log("Resultado da pesquisa: ", pesquisaBinaria(minhaLista, 3));
console.log("Resultado da pesquisa: ", pesquisaBinaria(minhaLista, -1));
