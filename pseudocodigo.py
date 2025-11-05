Algoritmo: Clínica Vida+

var
    nome, cpf : caractere
    fila : fila de pacientes
    atendimento : registro {nome, cpf}

inicio

    escreva("Digite o nome do paciente: ")
    leia(nome)
    escreva("Digite o CPF do paciente: ")
    leia(cpf)
    enfileira(fila, (nome, cpf))

    escreva("Digite o nome do paciente: ")
    leia(nome)
    escreva("Digite o CPF do paciente: ")
    leia(cpf)
    enfileira(fila, (nome, cpf))

    escreva("Digite o nome do paciente: ")
    leia(nome)
    escreva("Digite o CPF do paciente: ")
    leia(cpf)
    enfileira(fila, (nome, cpf))

    atendimento <- desenfileira(fila)

    escreva("Atendendo paciente: ", atendimento.nome, ", CPF: ", atendimento.cpf)

    escreva("Ainda na fila:")
    escreva(fila)

fimalgoritmo
