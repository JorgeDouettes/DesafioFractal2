import time

import pytest
from helper import Testador

@pytest.fixture
def testador():
    teste = Testador()
    yield teste
    teste.driver.quit()


class Test_geral:

    def test_criar_modulo_com_sucesso(self, testador):
        teste = testador

        # Login
        teste.abrir_pag('https://playful-torrone-162c28.netlify.app/')
        teste.clicar('//*[@id="app"]/div[1]/section/a')
        teste.inserir_texto('//*[@id="app"]/div[1]/form/div/div[1]/div/input', 'qualityassurance@bertoni.com.br')
        teste.inserir_texto('//*[@id="app"]/div[1]/form/div/div[2]/div/input', 'versar123')
        teste.clicar('//*[@id="app"]/div[1]/form/button')

        # Criar módulo
        teste.clicar('//*[@id="app"]/div[1]/div/main/div[2]/div[1]/button')
        teste.inserir_texto('//*[@id="app"]/div[1]/div/main/div[2]/div/div[2]/div/form/div/div[1]/div/input',
                            'Tests_Jorge_1_aut')
        teste.clicar('//*[@id="mui-component-select-grade_id"]')
        teste.clicar('//*[@id="menu-grade_id"]/div[3]/ul/li[1]')
        teste.inserir_texto('//*[@id="app"]/div[1]/div/main/div[2]/div/div[2]/div/form/div/div[3]/div/textarea',
                            'Teste_Jorge_1_aut2')
        teste.clicar(
            '//*[@id="app"]/div[1]/div/main/div[2]/div/div[2]/div/form/div/div[5]/ul/li[1]/div/div/div[2]/button')
        teste.clicar('//*[@id="app"]/div[1]/div/main/div[2]/div/div[2]/div/form/div/div[7]/button[2]')
        teste.clicar('//*[@id="app"]/div[1]/div/main/div[2]/div/div[2]/div/form/div/div[3]/button[2]')
        teste.clicar('//*[@id="app"]/div[1]/div/main/div[2]/div/div[2]/div/form/div/div[2]/button[2]')

        # Buscar módulo
        teste.inserir_texto('//*[@id="app"]/div[1]/div/header/div/div/div[1]/div/div/input', 'Tests_Jorge_1_aut')
        teste.clicar('//*[@id="app"]/div[1]/div/header/div/div/div[1]/div/button')

        # Validação final
        assert teste.texto_esta_na_tabela('Tests_Jorge_1_aut')
