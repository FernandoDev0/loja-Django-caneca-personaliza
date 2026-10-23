from django.core.management.base import BaseCommand
from core.models import (
    ConfiguracaoLoja,
    Produto,
    Depoimento,
    PassoProcesso,
    PassoComoPedir,
    FAQ,
    ItemGaleria
)


class Command(BaseCommand):
    help = "Popula o banco de dados com os dados iniciais refinados da loja de canecas"

    def handle(self, *args, **options):
        self.stdout.write("Configurando a loja...")

        config, _ = ConfiguracaoLoja.objects.get_or_create(id=1)
        config.nome_loja = "Da Fran pra Você ☕"
        config.slogan = "Canecas personalizadas feitas à mão, com amor e história"
        config.whatsapp = "5517999999999"
        config.instagram = "@dafranpravoce"
        config.aviso_topo = "Envio para todo o Brasil 🇧🇷 • Feito à mão com carinho • Garantia contra quebra 📦"
        config.garantia_texto = "Garantia da Fran: se chegar quebrada, eu mando outra imediatamente. Sem burocracia."
        config.tempo_producao = "Até 3 dias úteis após aprovação da arte"
        config.banner_cta_titulo = "Bora criar a sua caneca dos sonhos? 💖"
        config.banner_cta_subtitulo = "Me chama no WhatsApp que a gente cria juntas uma arte exclusiva que vai arrancar lágrimas de emoção!"
        config.sobre_fran = "Oi, eu sou a Fran! E eu transformo um simples café num presente inesquecível. Cada caneca é estampada à mão no meu ateliê, cuidando de cada tom e detalhe como se fosse pra mim."
        config.save()

        # Produtos
        self.stdout.write("Criando produtos...")
        produtos_data = [
            {
                "nome": "Caneca com Foto",
                "slug": "caneca-com-foto",
                "tag_destaque": "A mais pedida 💕",
                "preco": 39.90,
                "preco_antigo": 49.90,
                "descricao_curta": "Sua foto favorita estampada com qualidade fotográfica de altíssima definição. O presente certeiro pra emocionar quem você ama.",
                "descricao_completa": "Caneca em cerâmica de alta qualidade com acabamento brilhante. As cores não desbotam e o brilho é duradouro. Enviamos prévia para você aprovar antes de estampar.",
                "imagem_fallback": "images/canecas_trio.webp",
                "foco_imagem": "22% center",
                "ordem": 1,
                "caracteristicas": "Cerâmica resinada Premium AAA+\nCapacidade 325ml padrão barista\nPode ir ao micro-ondas e lava-louças\nImpressão fotográfica 100% nítida\nCaixa kraft acolchoada para presente",
            },
            {
                "nome": "Caneca com Nome ou Frase",
                "slug": "caneca-nome-frase",
                "tag_destaque": "Do seu jeito ✨",
                "preco": 34.90,
                "preco_antigo": 44.90,
                "descricao_curta": "Seu nome em tipografia elegante ou aquela frase bem humorada que só a sua turma entende. Do seu jeitinho único!",
                "descricao_completa": "Escolha entre dezenas de fontes caligráficas, cores da alça e adicione detalhes especiais. Uma peça autoral cheia de personalidade.",
                "imagem_fallback": "images/canecas_trio.webp",
                "foco_imagem": "50% center",
                "ordem": 2,
                "caracteristicas": "Cerâmica branca ultra brilhante\nAcabamento impecável sem rebarbas\nFonte e cor à sua escolha\nEmbalagem perfumada para presente\nEnvio rápido e seguro",
            },
            {
                "nome": "Kit Casal / Família (2 Canecas)",
                "slug": "kit-casal-familia",
                "tag_destaque": "Presente perfeito 🎁",
                "preco": 69.90,
                "preco_antigo": 89.90,
                "descricao_curta": "Par combinando com artes que se completam pra presentear quem você ama — ou pra deixar a mesa do café da manhã muito mais charmosa.",
                "descricao_completa": "Dois modelos harmonizados: perfeitos para casais, mãe e filha, melhores amigos ou parceiros de trabalho. Embalagem dupla especial inclusa.",
                "imagem_fallback": "images/canecas_trio.webp",
                "foco_imagem": "78% center",
                "ordem": 3,
                "caracteristicas": "Kit com 2 canecas combinando\nArtes que se conectam lado a lado\nDupla camada de resina protetora\nCaixa de presente dupla de luxo\nFrete compartilhado super econômico",
            },
            {
                "nome": "Caneca Mágica Termossensível",
                "slug": "caneca-magica-termossensivel",
                "tag_destaque": "Efeito Surpresa 🔥",
                "preco": 49.90,
                "preco_antigo": 59.90,
                "descricao_curta": "Preta fosca enquanto fria. Ao colocar café ou chá quente, sua foto e mensagem mágica se revelam instantaneamente na frente dos olhos!",
                "descricao_completa": "A favorita para pedidos de casamento, anúncio de gravidez, aniversários e presentes surpresa. Efeito visual impactante que nunca perde a graça.",
                "imagem_fallback": "images/canecas_trio.webp",
                "foco_imagem": "center",
                "ordem": 4,
                "caracteristicas": "Efeito térmico instantâneo e reversível\nAcabamento preto fosco acetinado\nRevelação fotográfica em alta definição\nIdeal para anúncios surpresa e datas comemorativas\nAcompanha cartão dedicatória artesanal",
            },
        ]

        for p_data in produtos_data:
            Produto.objects.update_or_create(slug=p_data["slug"], defaults=p_data)

        # Passos Processo (Ateliê)
        self.stdout.write("Criando etapas do ateliê...")
        PassoProcesso.objects.all().delete()
        processos_data = [
            (1, "Bom dia com café ☕", "Acordo cedo e respondo vocês no WhatsApp com uma xícara quentinha do lado — adoro começar o dia conversando com quem vai emocionar alguém especial.", "coffee"),
            (2, "A arte nasce juntinhas ✨", "Crio a arte sob medida com você — envio as prévias virtuais, ajusto cada detalhe, troco fotos e nada vai pra prensa sem a sua aprovação total.", "sparkles"),
            (3, "Impressão e prensa artesanal 🔥", "Imprimo em papel especial de alta gramatura e prenso cada caneca uma a uma no ateliê, calibrando temperatura e tempo para cores vivas e eternas.", "printer"),
            (4, "Embalagem de presente com carinho 🎁", "Embalo como se fosse presente (porque quase sempre é!), com proteção acolchoada anti-impacto, laço de cetim e cartão perfumado.", "gift"),
            (5, "Envio seguro com rastreamento 📦", "Despacho com seguro total e código de rastreamento. Fico ansiosa acompanhando até você me mandar foto comemorando o momento do recebimento!", "truck"),
        ]
        for num, tit, desc, ico in processos_data:
            PassoProcesso.objects.create(numero=num, titulo=tit, descricao=desc, icone=ico, ordem=num)

        # Como Pedir
        self.stdout.write("Criando passos de pedido...")
        PassoComoPedir.objects.all().delete()
        pedir_data = [
            (1, "Me chama no WhatsApp", "É só clicar em qualquer botão verdinho aqui na página. Eu mesma vou te responder com carinho, sem robôs chatos!", "message-circle"),
            (2, "A gente cria a arte juntas", "Você me envia a foto, frase ou tema, e eu monto a prévia visual realista para você ver como sua caneca vai ficar.", "palette"),
            (3, "Você aprova, eu produzo", "Nada vai pra prensa sem o seu 'Tá perfeita!'. Depois da sua confirmação, produzo no ateliê em até 3 dias úteis.", "check-circle"),
            (4, "Prontinha pra presentear", "Sua caneca chega super protegida em uma embalagem linda, pronta para emocionar quem você ama — ou alegrar seu dia!", "heart"),
        ]
        for num, tit, desc, ico in pedir_data:
            PassoComoPedir.objects.create(numero=num, titulo=tit, descricao=desc, icone=ico, ordem=num)

        # Depoimentos
        self.stdout.write("Criando depoimentos...")
        Depoimento.objects.all().delete()
        depoimentos_data = [
            ("Larissa R.", "Caneca com Foto", "São Paulo - SP", "Dei de presente pra minha mãe com uma foto nossa de infância e ela chorou de alegria! A imagem ficou tão nítida que parece trabalho de gráfica de luxo. Super recomendo a Fran!", 5),
            ("Diego M.", "Caneca com Nome", "Campinas - SP", "Pedi na segunda e na quinta já estava na minha casa, incrivelmente bem embalada. A estampa tem uma qualidade absurda, já lavei várias vezes e continua brilhando como nova.", 5),
            ("Patrícia L.", "Caneca com Frase", "Curitiba - PR", "O atendimento da Fran é um encanto! Ela me mandou três opções de fontes, ajustou tudo que pedi com muita paciência e só produziu quando eu amei de verdade.", 5),
            ("Thiago S.", "Kit Casal", "Belo Horizonte - MG", "Comprei o kit casal pra presentear minha esposa no nosso aniversário. Chegou antes do prazo e virou a nossa caneca oficial do café da manhã. Ela ficou apaixonada!", 5),
        ]
        for i, (nome, prod, cid, txt, est) in enumerate(depoimentos_data):
            Depoimento.objects.create(
                cliente_nome=nome,
                produto_comprado=prod,
                cidade=cid,
                texto=txt,
                estrelas=est,
                ordem=i + 1
            )

        # Galeria
        self.stdout.write("Criando itens da galeria...")
        ItemGaleria.objects.all().delete()
        galeria_data = [
            ("Momento Café Especial", "Cliente sorrindo com sua caneca de foto na cozinha ☕", "images/cliente_cozinha.webp", 1),
            ("Café a Dois", "Casal segurando suas canecas combinando com muito amor 💕", "images/cliente_casal.webp", 2),
            ("No Ateliê da Fran", "Fran embalando cada pedido artesanal com proteção reforçada 🎁", "images/fran_atelie.webp", 3),
            ("Feita com Afeto", "Fran sorrindo com uma caneca personalizada recém-saída da prensa 🥰", "images/fran_hero.webp", 4),
        ]
        for tit, leg, img, ord in galeria_data:
            ItemGaleria.objects.create(titulo=tit, legenda=leg, imagem_fallback=img, ordem=ord)

        # FAQ
        self.stdout.write("Criando perguntas frequentes...")
        FAQ.objects.all().delete()
        faq_data = [
            (
                "Quanto tempo demora pra ficar pronta?",
                "Depois que você aprova a prévia digital da arte, eu produzo no ateliê em até 3 dias úteis. O prazo de entrega da transportadora ou Correios depende do seu CEP, mas te envio o código de rastreio para acompanhar tudo em tempo real!",
                1
            ),
            (
                "A estampa sai na lava-louças ou no micro-ondas?",
                "Não sai! Nossas canecas são de cerâmica resinada classe AAA com sublimação térmica profissional de alta temperatura. A estampa fica fundida na cerâmica. Elas podem ir ao micro-ondas e lava-louças tranquilamente. Dica de ateliê: lavar com o lado macio da esponja conserva o brilho de fábrica por muitos anos!",
                2
            ),
            (
                "Vocês entregam para onde? É seguro contra quebra?",
                "Enviamos com total segurança para qualquer cidade do Brasil! Nossas canecas recebem embalagem de tripla proteção: plástico bolha reforçado, berço anti-impacto e caixa reforçada. E você conta com a Garantia da Fran: se por ventura o transporte quebrar, eu envio outra nova sem burocracia!",
                3
            ),
            (
                "Posso mandar mais de uma foto ou juntar foto com frase?",
                "Com certeza! Podemos colocar foto de um lado e frase do outro, ou fazer uma colagem harmônica com até 3 fotos. Nós criamos a composição juntas no WhatsApp e você confere tudo antes de produzir.",
                4
            ),
            (
                "Quais são as formas de pagamento aceitas?",
                "Aceitamos Pix (com aprovação e início imediato), cartão de crédito em até 12x e transferência bancária. A gente combina com toda tranquilidade e segurança direto pelo WhatsApp.",
                5
            ),
        ]
        for q, a, ord in faq_data:
            FAQ.objects.create(pergunta=q, resposta=a, ordem=ord)

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso com dados da Fran!"))
