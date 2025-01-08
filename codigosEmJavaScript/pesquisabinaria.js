function pesquisaBinaria(lista, item) {
    let baixo = 0; //declarando variável
    let alto = lista.length - 1; //subtraindo para entrar na contagem Buckets

    while (baixo <= alto) { //estrutura de repetição
        let meio = Math.floor((baixo + alto) / 2); //função par arredondar para o inteiro mais próximo
        let chute = lista[meio]; 

        console.log('meio/posição:', meio); //imprimindo posições que o algoritmo está

        if (chute === item) { // estrutura de decisão
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

const minhaLista = [1, 3, 5, 7, 9]; // arry
console.log("Resultado da pesquisa: ", pesquisaBinaria(minhaLista, 7));
console.log("Resultado da pesquisa: ", pesquisaBinaria(minhaLista, -1));
