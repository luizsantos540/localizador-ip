import sqlite3
import requests


def inicializar_banco():
    conexao = sqlite3.connect("historico_ips.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            pais TEXT,
            estado TEXT,
            cidade TEXT,
            provedor TEXT
        )
    """
    )
    conexao.commit()
    conexao.close()


def salvar_no_banco(ip, pais, estado, cidade, provedor):
    conexao = sqlite3.connect("historico_ips.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO consultas (ip, pais, estado, cidade, provedor)
        VALUES (?, ?, ?, ?, ?)
    """,
        (ip, pais, estado, cidade, provedor),
    )
    conexao.commit()
    conexao.close()


def solicitar_ip():
    ip = input("Digite o endereço IP que deseja localizar (ou pressione Enter para o seu próprio IP): ")
    return ip


def localizar_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    resposta = requests.get(url)
    dados = resposta.json()

    if dados.get("status") == "success":
        ip_alvo = dados.get("query")
        pais = dados.get("country")
        estado = dados.get("regionName")
        cidade = dados.get("city")
        provedor = dados.get("isp")

        print("\n--- LOCALIZAÇÃO ENCONTRADA ---")
        print(f"IP analisado: {ip_alvo}")
        print(f"País:         {pais}")
        print(f"Estado:       {estado}")
        print(f"Cidade:       {cidade}")
        print(f"Provedor:     {provedor}")
        print("-" * 30)

        # Salva as informações organizadas diretamente no banco de dados
        salvar_no_banco(ip_alvo, pais, estado, cidade, provedor)
    else:
        print("\nNão foi possível localizar este endereço IP.")


# Fluxo principal do programa
inicializar_banco()
ip_usuario = solicitar_ip()
localizar_ip(ip_usuario)