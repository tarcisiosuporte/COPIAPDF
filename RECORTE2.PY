import os
import shutil
import PyPDF2

# Nome do PDF que você está procurando
pdf_name = "teste.pdf"

# Pasta onde você quer procurar o PDF
pasta_origem = "D:\PYTHON\LEITURA PDF"

# Setor específico para verificar
setor_especifico = "setor1"

# Pasta onde você quer RECORTAR o PDF
pasta_destino = "D:\PYTHON\LEITURA PDF"

# Navegue pela pasta para encontrar o PDF pelo nome
for pasta_raiz, pastas, arquivos in os.walk(pasta_origem):
    if pdf_name in arquivos:
        # Verifique se o PDF pertence ao setor específico
        if setor_especifico in pasta_raiz:
            # Copie o PDF para a pasta do setor designado
            shutil.copy(os.path.join(pasta_raiz, pdf_name), pasta_destino)
            print(f"O PDF {pdf_name} foi copiado para a pasta do setor {setor_especifico}")
            break
