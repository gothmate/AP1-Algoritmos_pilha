class Queue {
    constructor() {
        this.elements = []
    }
    
    isEmpty() {
        /* Verifica se a Fila está vazia */
        return this.elements.length == 0
    }
    peek() {
        /* Acessa o primeiro elemento da Fila sem modificá-lo */
        return !this.isEmpty() ? this.elements[0] : undefined
    }
    numeroElementos() {
        /* Verifica o tamanho da fila */
        return this.elements.length
    }
    enqueue (e) {
        /* Adiciona um elemento ao fim da Fila */
        this.elements.push(e)
    }
    dequeue (e) {
        /* Retira o primeiro elemento da Fila */
        return this.elements.shift()
    }

    insereAteIesima(pos, e) {
        let qte = this.numeroElementos()
        
        if(qte == (pos-1)) {
            this.enqueue(e)
        }
        else if(qte < pos) {
            while(qte < pos) {
                this.enqueue(e)
                qte = this.numeroElementos()
            }
        }
        else if(qte >= pos) {
            while(qte >= pos) {
                this.dequeue()
                qte = this.numeroElementos()
            }
            this.enqueue(e)
        }
        return this
    }

    removeDaIesima(pos) {
        let qte = this.numeroElementos()

        if(qte < pos) {
            return "Essa posição não está ocupada"
        }
        else if(qte == pos) {
            return this.dequeue()
        } else {
            while(qte >= pos) {
                this.dequeue()
                qte = this.numeroElementos()
            }
            return this
        }
    }

}


// ----------------------------------------------------------------

//EXEMPLOS DE USO

// Definindo uma fila com 5 elementos armazenada em um vetor
let q = new Queue()
for(let i = 1; i < 6; i++) {
    q.enqueue(i)
}
console.log('Definindo uma fila com 5 elementos armazenada em um vetor:', q)

// a. Inserir um elemento(enqueue)
q.enqueue(6)
console.log('Inserir um elemento:', q)

// b. Remover um elemento(dequeue)
q.dequeue()
console.log('Remover um elemento:', q);

// Retornar o número de elementos da Fila
console.log('Número de elementos da Fila:', q.numeroElementos())

// Inserir um elemento na i-ésima posição da fila

q.insereAteIesima(3, 8)
console.log('Inserir um elemento na 3ª posição:', q)

q.insereAteIesima(7, 10)
console.log('Inserir um elemento até a 7ª posição:', q)

// remove até a i-ésima posição
q.removeDaIesima(5)
console.log('Removendo até a 5ª posição: ', q)
console.log("Tentando remover da 7ª posição: ", q.removeDaIesima(7))
