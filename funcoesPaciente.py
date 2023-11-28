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
    for nome, dados in pacientes.items():
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



def menuPaciente():
        
        while True: 
            print("O QUE DESEJA REALIZAR?")

            print("1- CADASTRE-SE")
            print("2- CONHECER MÉDICOS DISPONÍVEIS")
            print("3- DIAS DISPONÍVEIS PARA CONSULTA")
            print("4- SAIR")

            user_op  = input("Informe sua opcão: ")

            if user_op == "1":
                nome = input("Informe seu nome: ")
                idade = input("Informe a sua idade: ")
                tel = input("Informe seu telefone")
                semanas = input("Quantas semanas você possue de gestação? ")
                acompanhamento = input("Já realiza acompanhamento médico prévio?")
                
                cadastrar_paciente(pacientes, nome, idade, tel, semanas, acompanhamento)

            elif user_op == "2":
                listar_medicos(lista_medicos)

            elif user_op == "3":
                listar_dias_disponiveis(pacientes)
            
            elif user_op == "4":
                print("SAINDO...")
                break
