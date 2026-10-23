from .models import ConfiguracaoLoja


def configuracao_loja(request):
    config = ConfiguracaoLoja.objects.first()
    if not config:
        config = ConfiguracaoLoja.objects.create(
            nome_loja="Da Fran pra Você ☕",
            slogan="Canecas personalizadas feitas à mão, com amor e história",
            whatsapp="5517999999999",
            instagram="@dafranpravoce",
            aviso_topo="Envio para todo o Brasil 🇧🇷 • Feito à mão com carinho • Garantia contra quebra 📦",
            garantia_texto="Garantia da Fran: se chegar quebrada, eu mando outra imediatamente. Sem burocracia."
        )
    return {
        'config': config,
    }
