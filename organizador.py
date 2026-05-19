import os
import shutil
from categorias import CATEGORIAS


def organizar_arquivos(pasta, atualizar_progresso=None, log_callback=None):

    estatisticas = {}

    arquivos = os.listdir(pasta)

    # Filtra apenas arquivos
    arquivos = [
        arquivo for arquivo in arquivos
        if os.path.isfile(os.path.join(pasta, arquivo))
    ]

    total_arquivos = len(arquivos)
    arquivos_processados = 0

    # Evita erro se pasta estiver vazia
    if total_arquivos == 0:
        print("Nenhum arquivo encontrado.")
        if log_callback:
            log_callback("Nenhum arquivo encontrado.")
        return

    for arquivo in arquivos:

        caminho_arquivo = os.path.join(pasta, arquivo)

        _, ext = os.path.splitext(arquivo)
        extensao = ext.lower()

        categoria = "Outros"

        # Verifica categorias
        for nome_categoria, extensoes in CATEGORIAS.items():

            if extensao in extensoes:
                categoria = nome_categoria
                break

        # Cria pasta da categoria
        pasta_categoria = os.path.join(pasta, categoria)

        os.makedirs(pasta_categoria, exist_ok=True)

        # Caminho destino
        destino = os.path.join(pasta_categoria, arquivo)

        # Evita nomes duplicados
        contador = 1
        nome_sem_ext, extensao_arquivo = os.path.splitext(arquivo)

        while os.path.exists(destino):

            novo_nome = (
                f"{nome_sem_ext}_{contador}"
                f"{extensao_arquivo}"
            )

            destino = os.path.join(
                pasta_categoria,
                novo_nome
            )

            contador += 1

        # Move arquivo
        shutil.move(caminho_arquivo, destino)

        # Estatísticas
        estatisticas[categoria] = estatisticas.get(categoria, 0) + 1

        mensagem = f"{arquivo}  →  {categoria}/"
        print(mensagem)

        if log_callback:
            log_callback(mensagem)

        # Atualiza progresso
        arquivos_processados += 1

        if atualizar_progresso:

            progresso = (
                arquivos_processados /
                total_arquivos
            )

            atualizar_progresso(progresso)

    # Resumo final
    resumo = "\n===== RESUMO ====="
    print(resumo)
    if log_callback:
        log_callback(resumo)

    for categoria, quantidade in estatisticas.items():

        linha = f"  {categoria}: {quantidade} arquivo(s)"
        print(linha)

        if log_callback:
            log_callback(linha)