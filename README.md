# Organizador de Arquivos

Aplicativo desktop para organizar automaticamente arquivos de uma pasta em subpastas por categoria (Imagens, PDFs, Vídeos, etc.).

## Funcionalidades

- Interface gráfica moderna com tema escuro
- Barra de progresso em tempo real
- Log de todos os arquivos movidos
- Evita sobrescrever arquivos com nomes duplicados

## Como usar

### Rodando pelo Python

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/organizador-de-arquivos.git
   cd organizador-de-arquivos
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute:
   ```bash
   python main.py
   ```

## Categorias suportadas

| Categoria | Extensões |
|---|---|
| Imagens | .png, .jpg, .jpeg, .gif, .webp, .bmp |
| PDF | .pdf |
| Word | .docx |
| Planilhas | .xlsx |
| PowerPoint | .pptx |
| Músicas | .mp3, .wav, .flac, .aac |
| Vídeos | .mp4, .mkv, .avi, .mov |
| Compactados | .rar, .zip, .7z, .tar, .gz |
| Texto | .txt |

## Tecnologias

- Python 3
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
