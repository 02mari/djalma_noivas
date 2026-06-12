import csv

print("=== INICIANDO PIPELINE DE DADOS: DJALMA NOIVAS ===")

# 1. EXTRAÇÃO (Simulação dos dados brutos que chegam da loja)
# Criando uma lista de dados fictícios com personagens de Tapas & Beijos
dados_alugueis = [
    ["ID_Aluguel", "Noiva", "Modelo_Vestido", "Valor_Aluguel", "Status_Pagamento"],
    ["1", "Sueli", "Sereia Imperial", "1500.00", "Confirmado"],
    ["2", "Fátima", "Tomara que Caia Clássico", "1800.00", "Confirmado"],
    ["3", "Dona Jô", "Princesa de Seda", "2200.00", "Cancelado"],
    ["4", "Flavinha", "Sereia com Renda", "2000.00", "Confirmado"],
    ["5", "Norma", "Vintage Boho", "1400.00", "Cancelado"],
    ["6", "Bia", "Evasê Moderno", "1300.00", "Confirmado"]
]

# Salvando a lista acima num arquivo CSV bruto para simular a origem dos dados
with open("alugueis_brutos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerows(dados_alugueis)

print("[INFO] Arquivo 'alugueis_brutos.csv' gerado com sucesso.")


# 2. TRANSFORMAÇÃO (Limpeza dos dados e cálculos lógicos)
registros_limpos = []
faturamento_total = 0.0

# Lendo o arquivo bruto para processar as informações
with open("alugueis_brutos.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor) # Salva e pula a linha de títulos (cabeçalho)
    
    # Adiciona a linha de títulos à nossa lista limpa
    registros_limpos.append(cabecalho)
    
    # Varre linha por linha do relatório
    for linha in leitor:
        id_aluguel, noiva, vestido, valor, status = linha
        valor_float = float(valor)
        
        # Regra de Negócio: Se o casamento foi cancelado, ignoramos no faturamento
        if status == "Confirmado":
            registros_limpos.append(linha)
            faturamento_total += valor_float

print("[INFO] Transformação concluída. Linhas nulas ou canceladas removidas.")


# 3. CARGA (Salvar o resultado final organizado em um novo arquivo)
with open("relatorio_faturamento_final.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerows(registros_limpos)

print("[INFO] Novo relatório 'relatorio_faturamento_final.csv' exportado.")

print("\n================ COMPUTAÇÃO CONCLUÍDA ================")
print(f"Faturamento Total Confirmado (Djalma Noivas): R$ {faturamento_total:.2f}")
print("======================================================")