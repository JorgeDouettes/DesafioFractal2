# Testes Automatizados com Selenium e Pytest

Este projeto realiza testes automatizados de interface para um sistema web usando **Selenium WebDriver** com o navegador **Chrome**, em conjunto com o framework de testes **Pytest**. Ele simula o comportamento do usuário para realizar login, criar módulos, temas e verificar funcionalidades da interface.

---

## 📁 Estrutura dos Arquivos

- `main.py` — Arquivo principal de testes com `pytest`
- `helper.py` — Classe `Testador` que encapsula funções auxiliares reutilizáveis com Selenium

---

## ▶️ Como Executar

1. Instale as dependências:

```bash
pip install selenium pytest
```

2. Execute os testes:

```bash
pytest main.py
```

---

## 📦 helper.py — Classe Testador

A classe `Testador` abstrai operações com Selenium:

### `__init__(self)`
Inicializa uma instância do `webdriver.Chrome()`.

---

### `abrir_pag(url)`
Abre a URL fornecida no navegador.

---

### `clicar(xpath)`
Clica em um elemento identificado pelo XPATH. Aguarda até que ele esteja clicável (timeout de 10 segundos).

---

### `encontrar(xpath)`
Retorna o elemento visível encontrado pelo XPATH (aguarda até 10 segundos). Retorna `None` se não for encontrado.

---

### `inserir_texto(xpath, texto)`
Localiza o campo com o `xpath`, limpa qualquer conteúdo anterior e insere o texto fornecido.

---

### `texto_esta_na_tabela(texto_esperado)`
Procura por um texto específico dentro de uma `<tbody>` com a classe `"MuiTableBody-root"`. Retorna `True` se o texto for encontrado em alguma linha da tabela.

---



## 🧪 main.py — Casos de Teste

### `test_criar_modulo_com_sucesso`
- Abre a página principal
- Realiza login
- Cria um novo módulo com nome e descrição
- Realiza busca do módulo
- Valida se o nome está presente na tabela



## ✅ Requisitos

- Python 3.7+
- Google Chrome instalado
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com a versão do Chrome

---

