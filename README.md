# YouTube Downloader

## Descrição

O YouTube Downloader é uma aplicação GUI simples desenvolvida em Python que permite aos usuários baixar o áudio de vídeos do YouTube.

## Pré-requisitos

- Python 3.12.4
- pip

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/bassanipedro/youtube-downloader.git
   cd youtube-downloader
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Execute o script:

   ```sh
   python main.py
   ```

2. Insira o link do vídeo do YouTube no campo de entrada e clique no botão de download para baixar o áudio.

## Gerar executável

Para gerar o executável, deverá usar o seguinte comando:

```sh
pyinstaller --onefile --windowed .\src\main.py
```

## Autor

- [Pedro Bassani](https://github.com/bassanipedro)
