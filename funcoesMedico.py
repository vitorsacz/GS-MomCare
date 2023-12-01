
pacientes = {
    
    "Hellora Campelo": {
        "telefone": "11 998765432",
        "idade": "24",
        "semanas": "2", 
        "acompanhamento": "sim",
    },
}

agenda_consultas = {
    "Cardiologia": {
        "Dr. Vitor Santos": "01/12/2023",
        "Dr. Caio Santos": "05/12/2023",
        "Dr. Wagner Santos": "15/12/2023"
    },

    "Neurologia": {
        "Dra. Yasmim Cruz": "07/12/2023",
        "Dra. Sthefany Almeida": "22/12/2023",
    },

    "Dermatologia": {
        "Dra. Arthur Almeida": "02/12/2023",
        "Dra. Celia Santos": "13/12/2023",
    },

    "Obstetrícia": {
        "Dra. Gabriela Ribeiro": "06/12/2023",
        "Dr. Sidnei Bueno": "27/12/2023",
        "Dr. Lucca Matteoni": "23/12/2023",
    }
}

lista_medicos = {
    "Dr. Vitor Santos": "Cardiologia",
    "Dr. Caio Santos": "Cardiologia",
    "Dr. Wagner Santos": "Cardiologia",
    "Dra. Yasmim Cruz": "Neurologia",
    "Dra. Sthefany Almeida": "Neurologia",
    "Dra. Arthur Almeida": "Dermatologia",
    "Dra. Celia Santos": "Dermatologia",
    "Dra. Gabriela Ribeiro": "Obstetrícia",
    "Dr. Sidnei Bueno": "Obstetrícia",
    "Dr. Lucca Matteoni": "Obstetrícia",
}

pacientes_triagem ={
    "Hellora Campelo": {
        "queixa": "Dor abdominal",
        "alergias": "nenhuma",
        "urgencia": "urgente",
        "especialidade" : "obstetrícia"
    }
}


        



def triagem(pacientes_triagem, nome, queixa, alergias, urgencia, especialidade):

    inserir_triagem = {}
    inserir_triagem["queixa"] = queixa
    inserir_triagem["alergias"] = alergias
    inserir_triagem["urgencia"] =  urgencia
    inserir_triagem["especialidade"] = especialidade

    pacientes_triagem[nome] = inserir_triagem

    print("\n")
    print(f"Trigem de {nome}, realizada com sucesso")





def cadastrar_paciente(pacientes, nome, idade, telefone, semanas, acompanhamento):

    #CRIAR UM NOVA PACIENTE
    nova_paciente = {}
    nova_paciente ["idade"] = idade
    nova_paciente ["telefone"] = telefone
    nova_paciente ["semanas"] =  semanas
    nova_paciente ["acompanhamento"] = acompanhamento

    #INSERIR UMA NOVA PACIENTE
    pacientes[nome] = nova_paciente
    
    print("\n")
    print(f"Paciente {nome}, adicionada com sucesso!")




def listar_medicos(lista_medicos):

    print(50*"-")
    print("LISTA DE MÉDICOS")
    for nome, especialidade in lista_medicos.items():
        print("\n")
        print(f"Médico: {nome}")
        print(f"Especialidade: {especialidade}")
    print(50*"-")

def listar_dados_pacientes(pacientes):

    print(50*"-")
    print("PACIENTES")
    print(50*"-")

    for nome, dados in pacientes.items():
        print("\n")
        print(nome)
        for chave, valor in dados.items():
            print(f"{chave} - {valor}")  




print("\n")

def listar_triagem_pacientes(pacientes_triagem):

    print(50*"-")
    print("PACIENTES TRIADOS")
    print(50*"-")

    for nome, dados in pacientes_triagem.items():
        print("\n")
        print(nome)
        for chave, valor in dados.items():
            print(f"{chave} - {valor}")  




def listar_dias_disponiveis(agenda_consultas):
    for nome, dados in agenda_consultas.items():
        print("\n")
        print(nome)
        for chave, valor in dados.items():
            print(f"{chave} - {valor}") 

def menuMedico():
        
        while True: 
            print("\n")
            print("O QUE DESEJA REALIZAR?")
            print("\n")

            print("1- INSERIR NOVO PACIENTE")
            print("2- LISTA DE PACIENTES")
            print("3- REALIZAR TRIAGEM")
            print("4- LISTAR PACIENTES TRIADOS")
            print("5- SAIR")

            print("\n")
            user_op  = input("Informe sua opcão: ")

            if user_op == "1":
                print("\n")
                nome_paciente = input("Qual o nome da paciente? ")
                idade_paciente = input("Qual idade da paciente? ")
                tel_paciente = input("Qual o telefone da paciente? ")
                semanas_paciente = input("Quantas semanas de gestação?  ")
                acompanhamento_paciente = input("Possui acompanhamento médico prévio? ")
                
                cadastrar_paciente(pacientes, nome_paciente, idade_paciente, tel_paciente, semanas_paciente, acompanhamento_paciente)
                print("\n")

            elif user_op == "2":
                listar_dados_pacientes(pacientes)

            elif user_op == "3":
                

                nome_paciente = input("Informe o nome da paciente: ")
                queixa_paciente = input("Qual a queixa da paciente: ")
                alergias_paciente = input("A paciente possui alguma alergia? ")
                urgencia_paciente = input("Qual a urgencia paciente? ")
                especialidade_paciente = input("Qual a médico especialista é indicado para consultar a paciente?")

                triagem(pacientes_triagem, nome_paciente, queixa_paciente, alergias_paciente, urgencia_paciente, especialidade_paciente)

            elif user_op == "4":
                listar_triagem_pacientes(pacientes_triagem)
                
            


            elif user_op == "5":
                print("SAINDO...")
                break

            else:
                print("Insira uma opcao válida")
            