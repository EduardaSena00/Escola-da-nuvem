import re
import statistics
import os # Para criar um arquivo de log de exemplo

def analisar_log_treinamento(nome_arquivo):
    """
    Lê um arquivo de log de treinamento, extrai os tempos de execução
    e calcula a média e o desvio padrão.

    Args:
        nome_arquivo (str): O caminho para o arquivo de log.
    """
    tempos_execucao = []
    # Expressão regular para encontrar "Tempo de execução: XX.XXs"
    # O grupo de captura 1 `([0-9.]+?)` pega o número decimal
    padrao_tempo = re.compile(r"Tempo de execução: ([0-9.]+?)s")

    try:
        # Abrimos o arquivo de log para leitura, garantindo que ele seja fechado
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            # Iteramos linha por linha no arquivo
            for linha in f:
                # Tentamos encontrar o padrão do tempo de execução em cada linha
                match = padrao_tempo.search(linha)
                if match:
                    try:
                        # Extraímos o valor numérico e o convertemos para float
                        tempo = float(match.group(1))
                        tempos_execucao.append(tempo)
                    except ValueError:
                        print(f"Aviso: Não foi possível converter '{match.group(1)}' para número na linha: {linha.strip()}")

        # Verificamos se encontramos algum tempo de execução
        if tempos_execucao:
            media = statistics.mean(tempos_execucao)
            # O desvio padrão só pode ser calculado se houver mais de um ponto de dado
            desvio_padrao = statistics.stdev(tempos_execucao) if len(tempos_execucao) > 1 else 0.0

            print(f"\n--- Análise do Log: {nome_arquivo} ---")
            print(f"Tempos de execução encontrados: {tempos_execucao}")
            print(f"Média do tempo de execução: {media:.2f} segundos")
            print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
        else:
            print(f"Nenhum 'Tempo de execução' encontrado no arquivo '{nome_arquivo}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Por favor, verifique o caminho.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a análise do log: {e}")

if __name__ == "__main__":
    # --- Parte para criar um arquivo de log de exemplo para teste ---
    log_exemplo_nome = 'log_treinamento.txt'
    conteudo_log_exemplo = """
    [INFO] Epoch 1 - Tempo de execução: 12.34s
    [DEBUG] Carregando dados complexos...
    [INFO] Epoch 2 - Tempo de execução: 15.00s
    [WARNING] Perda muito alta. Ajustando parâmetros.
    [INFO] Epoch 3 - Tempo de execução: 13.50s
    [INFO] Epoch 4 - Tempo de execução: 14.80s
    [ERROR] Erro durante o treinamento: dados corrompidos
    [INFO] Epoch 5 - Tempo de execução: 12.90s
    [DEBUG] Salvando modelo...
    [INFO] Epoch 6 - Tempo de execução: 16.10s
    [INFO] Epoch 7 - Tempo de execução: 13.20s
    [INFO] Fim do treinamento.
    """
    
    # Escreve o conteúdo de exemplo no arquivo
    with open(log_exemplo_nome, 'w', encoding='utf-8') as f:
        f.write(conteudo_log_exemplo)
    
    print(f"Arquivo '{log_exemplo_nome}' criado com dados de exemplo para teste.")
    # --- Fim da parte de criação do arquivo de log de exemplo ---

    # Chama a função principal para analisar o log
    analisar_log_treinamento(log_exemplo_nome)