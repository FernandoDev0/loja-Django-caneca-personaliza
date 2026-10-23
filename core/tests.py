from django.test import TestCase, Client
from django.urls import reverse
from core.models import Produto, ConfiguracaoLoja


class LojaCanecasTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.config = ConfiguracaoLoja.objects.create(
            nome_loja="Da Fran pra Você ☕",
            slogan="Canecas artesanais feitas à mão com amor",
            whatsapp="5517999999999"
        )
        self.produto = Produto.objects.create(
            nome="Caneca com Foto",
            slug="caneca-com-foto",
            preco=39.90,
            descricao_curta="Sua foto favorita estampada.",
            imagem_fallback="images/canecas_trio.webp",
            ordem=1
        )

    def test_homepage_loads_successfully(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Da Fran pra Você")
        self.assertContains(response, "Garantia da Fran")

    def test_whatsapp_link_endpoint(self):
        response = self.client.get(
            reverse('core:gerar_link_whatsapp'),
            {'modelo': 'Caneca Mágica', 'cor': 'Preta', 'texto': 'Super Pai'}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('whatsapp_url', data)
        self.assertIn('wa.me/5517999999999', data['whatsapp_url'])
