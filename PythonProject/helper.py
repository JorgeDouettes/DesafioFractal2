from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testador:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def abrir_pag(self, url):
        self.driver.get(url)

    def clicar(self, xpath):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            elemento.click()
        except:
            print(f"[ERRO] Elemento com XPATH '{xpath}' não foi clicável em até 10 segundos.")

    def encontrar(self, xpath):
        try:

            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
        except:
            print(f"[ERRO] Elemento com XPATH '{xpath}' não foi encontrado em até 10 segundos.")
            return None

    def inserir_texto(self, xpath, texto):
        inserir = self.encontrar(xpath)
        if inserir:
            inserir.clear()
            inserir.send_keys(texto)
        else:
            print(f"[ERRO] Não foi possível inserir texto no elemento '{xpath}'")

    def texto_esta_na_tabela(self, texto_esperado):
        try:
            tbody = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//tbody[@class="MuiTableBody-root"]'))
            )

            linhas = tbody.find_elements(By.TAG_NAME, "tr")


            for linha in linhas:
                if texto_esperado in linha.text:
                    print(f"[OK] Texto encontrado: '{texto_esperado}'")
                    return True

            print(f"[INFO] Texto '{texto_esperado}' **não** encontrado na tabela.")
            return False

        except Exception as e:
            print(f"[ERRO] Erro ao procurar o texto na tabela: {e}")
            return False

    def clicar_texto_em_xpath(self, xpath_container, texto_esperado, timeout=10):
        try:
            # Espera até o container estar presente
            container = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath_container))
            )

            # Busca todos os elementos filhos do container
            itens = container.find_elements(By.XPATH, ".//*")

            for item in itens:
                if texto_esperado.strip().lower() in item.text.strip().lower():
                    item.click()
                    print(f"Texto '{texto_esperado}' encontrado e clicado.")
                    return True

            print(f"Texto '{texto_esperado}' não foi encontrado dentro do container.")
            return False

        except Exception as e:
            print(f"Erro ao tentar clicar no texto '{texto_esperado}': {e}")
            return False
