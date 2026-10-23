from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import urllib.parse
from .models import (
    ConfiguracaoLoja,
    Produto,
    Depoimento,
    PassoProcesso,
    PassoComoPedir,
    FAQ,
    ItemGaleria
)


def index(request):
    config = ConfiguracaoLoja.objects.first()
    produtos = Produto.objects.filter(ativo=True).order_by('ordem', 'id')
    depoimentos = Depoimento.objects.filter(ativo=True).order_by('ordem', 'id')
    passos_processo = PassoProcesso.objects.filter(ativo=True).order_by('ordem', 'numero')
    passos_pedido = PassoComoPedir.objects.filter(ativo=True).order_by('numero')
    faqs = FAQ.objects.filter(ativo=True).order_by('ordem', 'id')
    galeria = ItemGaleria.objects.filter(ativo=True).order_by('ordem', 'id')

    context = {
        'config': config,
        'produtos': produtos,
        'depoimentos': depoimentos,
        'passos_processo': passos_processo,
        'passos_pedido': passos_pedido,
        'faqs': faqs,
        'galeria': galeria,
    }
    return render(request, 'index.html', context)


def gerar_link_whatsapp(request):
    """
    Endpoint para calcular e gerar link dinâmico de pedido via WhatsApp
    a partir do Simulador de Caneca Interativo.
    """
    modelo = request.GET.get('modelo', 'Caneca Personalizada')
    cor = request.GET.get('cor', 'Branca Clássica')
    texto_personalizado = request.GET.get('texto', '').strip()
    observacao = request.GET.get('obs', '').strip()

    config = ConfiguracaoLoja.objects.first()
    whatsapp_num = config.whatsapp if config else "5517999999999"

    msg_lines = [
        f"Olá, Fran! Quero pedir uma caneca personalizada feita com carinho 💖",
        f"• Modelo: {modelo}",
        f"• Cor interna/alça: {cor}",
    ]
    if texto_personalizado:
        msg_lines.append(f"• Frase/Nome desejado: \"{texto_personalizado}\"")
    if observacao:
        msg_lines.append(f"• Detalhes adicionais: {observacao}")

    msg_lines.append("\nPoderia me enviar a prévia da arte?")

    full_msg = "\n".join(msg_lines)
    wa_url = f"https://wa.me/{whatsapp_num}?text={urllib.parse.quote(full_msg)}"

    return JsonResponse({'whatsapp_url': wa_url, 'mensagem': full_msg})
