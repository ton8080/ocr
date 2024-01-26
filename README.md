# OCR Web App

Este é um aplicativo web simples que utiliza OCR (Reconhecimento Óptico de Caracteres) para extrair texto de imagens em arquivos PDF. Construído com o framework Flask em Python, o aplicativo utiliza a biblioteca Tesseract para realizar o OCR.

## Pré-requisitos
Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/).

## Instalação de dependências
1. Instale as dependências necessárias usando o seguinte comando:

```bash
pip install -r requirements.txt
```

2. Baixe e instale o Tesseract OCR de acordo com a arquitetura do seu sistema:
   - Para Windows 32 bits, baixe e instale a versão [Tesseract OCR 32 bits](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-5.3.3.20231005.exe).
   - Para Windows 64 bits, baixe e instale a versão [Tesseract OCR 64 bits](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe).
  
3. Adicione o caminho do executável do Tesseract ao seu ambiente. No arquivo `ocr_processor.py`, certifique-se de apontar o `pytesseract.pytesseract.tesseract_cmd` para o caminho correto. Por exemplo:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

## Executando o aplicativo
Para iniciar o aplicativo, execute o seguinte comando no terminal:

```bash
python web_interface.py
```

## Como usar
1. Acesse a página inicial.
2. Selecione um arquivo PDF.
3. Insira o número da página que você deseja processar.
4. Clique no botão "Processar".
5. O texto extraído será exibido na página.

Lembre-se de que este é um aplicativo de exemplo e pode ser expandido para incluir mais recursos, como processamento em lote, uma interface de usuário mais sofisticada, entre outros.

## Autores
- Washington (@ton8080)




