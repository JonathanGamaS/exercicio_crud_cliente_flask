from app.__init__ import app, post_cliente, put_cliente, delete_cliente, update_password
import unittest


class TestHomeView(unittest.TestCase):

    def setUp(self):
        app_test = app.test_client()
        self.response_get_clientes = app_test.get('/clientes')
        self.post_cliente = post_cliente
        self.put_cliente = put_cliente
        self.delete_cliente = delete_cliente
        self.update_password = update_password

    def test_get_clientes(self):
        self.assertEqual(200, self.response_get_clientes.status_code)

    def test_post_cadastro(self):
        nome = "Arthur"
        email = "arthur@email.com"
        senha = "123Ar"
        self.post_cliente(nome, email, senha)

    def test_put_cliente(self):
        id = 2
        nome = 'Teste'
        email = 'teste@email.com'
        self.put_cliente(id, nome, email)

    def test_delete_cliente(self):
        id = 2
        self.delete_cliente(id)

    def test_alteracao_senha(self):
        id = 1
        senha = 'novasenhaforte'
        self.update_password(id, senha)
