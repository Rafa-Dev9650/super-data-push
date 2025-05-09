import requests
cep = input("Digite o CEP que deseja puxar: ")
cep = cep

def showDataCep(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
    if response.status_code == 200:
        try:
            data = response.json()
            if 'erro' not in data:
                print(f"query: {data['cep']}")
                print(f"logradouro: {data['logradouro']}")
                print(f"complemento: {data['complemento']}")
                print(f"unidade: {data['unidade']}")
                print(f"bairro: {data['bairro']}")
                print(f"localidade: {data['localidade']}")
                print(f"uf: {data['uf']}")
                print(f"estado: {data['estado']}")
                print(f"regiao: {data['regiao']}")
                print(f"ibge: {data['ibge']}")
                print(f"gia: {data['gia']}")
                print(f"ddd: {data['ddd']}")
                print(f"siafi: {data['siafi']}")
                
        except requests.exceptions.JSONDecodeError:
            print(f"Houve um erro ao puxar os dados, verifique se o cep realmente existe.")

# verifica se o usuário inserriu apenas números
if not cep.isdigit():
    print("Você deve inserir apenas números inteiros.")
else:
    if len(cep) == 8:
        showDataCep(cep)
    else:
        print("O cep digitado deve ter 8 digitos.")
        exit()
    