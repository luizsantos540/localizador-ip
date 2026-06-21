import requests


def solicitar_ip():
    ip = input("Digite o endereço IP que deseja localizar (ou pressione Enter para o seu próprio IP): ")
    return ip


def localizar_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    resposta = requests.get(url)
    dados = resposta.json()

    if dados.get("status") == "success":
        print("\n--- LOCALIZAÇÃO ENCONTRADA ---")
        print(f"IP analisado: {dados.get('query')}")
        print(f"País:         {dados.get('country')}")
        print(f"Estado:       {dados.get('regionName')}")
        print(f"Cidade:       {dados.get('city')}")
        print(f"Provedor:     {dados.get('isp')}")
        print("-" * 30)
    else:
        print("\nNão foi possível localizar este endereço IP.")


ip_usuario = solicitar_ip()
localizar_ip(ip_usuario)