import streamlit as st
import unicodedata
import re

st.set_page_config(page_title="FaeThink", page_icon="🎓", layout="wide")
def normalizar_texto(texto: str) -> str:
    """
    Remove acentos, coloca tudo em minúsculas e tira caracteres especiais
    """
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # remove caracteres que não sejam letras, números ou espaços
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Estilos
st.markdown(
    """
    <style>
    .balao-usuario {
        background: linear-gradient(135deg, #6EC1E4, #4A90E2); 
        color: #fff; 
        font-weight: bold; 
        padding: 12px 16px; 
        border-radius: 20px 20px 0 20px; 
        margin: 6px 0; 
        display: inline-block; 
        max-width: 70%; 
        box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
    }
    .balao-bot {
        background: linear-gradient(135deg, #FFFFFF, #E0EAFD); 
        color: #333; 
        font-weight: bold; 
        padding: 12px 16px; 
        border-radius: 20px 20px 20px 0; 
        margin: 6px 0; 
        display: inline-block; 
        max-width: 70%; 
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .titulo-gradient {
        text-align: center;
        background: linear-gradient(90deg, #4A90E2, #6EC1E4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
    }
    .subtitulo {
        text-align: center;
        font-size: 18px;
        color: #333;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6EC1E4, #4A90E2);
        color: white;
        font-weight: bold;
        border-radius: 25px;
        padding: 10px 20px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .card {
        background: #f9f9ff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .chat-linha {
        display: flex;
        align-items: flex-end;
        margin: 8px 0;
        clear: both;
    }
    .chat-linha.usuario {
        justify-content: flex-end;
    }
    .chat-linha.bot {
        justify-content: flex-start;
    }
    .chat-linha img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin: 0 8px;
        object-fit: cover;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown("<h1 class='titulo-gradient'>FaeThink</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Seu assistente escolar da FAETEC com muito carinho 💙✨</p>", unsafe_allow_html=True)

# Sidebar menu
menu = st.sidebar.radio("📌 Navegação", ["Chatbot", "Sobre o Projeto", "Projetos da Escola"])

base_conhecimento = [
    {
        "keywords": ["estagio", "estagios", "vaga"],
        "resposta": "A Faetec possui convênios com empresas e instituições para fornecer estágios aos alunos de cursos técnicos e de qualificação, gerenciados pela DIVEST."
    },
    {
        "keywords": ["inscrever", "inscricao", "cadastrar"],
        "resposta": "Os alunos podem se inscrever via portal de estágio da Faetec ou diretamente na DIVEST (Setor de Estágio)."
    },
    {
        "keywords": ["obrigatorio", "obrigatoriedade"],
        "resposta": "Depende do curso. Nos cursos técnicos, o estágio é obrigatório para a conclusão, com acompanhamento da DIVEST."
    },
    {
        "keywords": ["carga", "horas", "horario"],
        "resposta": "A carga horária varia conforme o curso, geralmente entre 400 e 600 horas."
    },
    {
        "keywords": ["bolsa", "remunerado", "auxílio"],
        "resposta": "Sim, alguns estágios oferecem bolsa auxílio, enquanto outros não são remunerados."
    },
    {
        "keywords": ["saude", "enfermagem", "hospital", "clinica"],
        "resposta": "Cursos como Técnico em Enfermagem possuem estágio obrigatório em hospitais e clínicas parceiras."
    },
    {
        "keywords": ["empresa", "vagas", "escolher"],
        "resposta": "A escolha depende das vagas disponíveis nas empresas conveniadas com a Faetec."
    },
    {
        "keywords": ["acompanhamento", "supervisor", "desempenho"],
        "resposta": "Sim, há supervisores que acompanham o desempenho do aluno durante o estágio."
    },
    {
        "keywords": ["fora", "outro", "estado", "externo"],
        "resposta": "Sim, desde que a empresa possua convênio com a Faetec."
    },
    {
        "keywords": ["informática", "redes", "computadores", "tecnologia"],
        "resposta": "Sim, cursos de Informática e Redes de Computadores possuem oportunidades em empresas de tecnologia."
    },
    {
        "keywords": ["inscrever", "inscricao", "cadastrar"],
        "resposta": "As inscrições são realizadas exclusivamente pelo site oficial da Faetec: www.faetec.rj.gov.br/inscricoes."
    },
    {
        "keywords": ["presencial", "na escola", "presencial"],
        "resposta": "Não é possível fazer inscrição presencial. O processo é apenas online, conforme os editais."
    },
    {
        "keywords": ["pagar", "taxa", "inscricao"],
        "resposta": "Sim. No processo seletivo 2025.2 a taxa foi de R$ 20,00."
    },
    {
        "keywords": ["idade", "faixa etaria", "minima"],
        "resposta": "Depende do curso. Para cursos técnicos é necessário ter concluído o Ensino Fundamental. Para cursos de qualificação, a idade mínima é 16 anos."
    },
    {
        "keywords": ["estrangeiro", "imigrante", "documentos"],
        "resposta": "Sim, desde que possua documentos oficiais válidos no Brasil, como CPF e RG."
    },
    {
        "keywords": ["vagas", "número", "ofertas"],
        "resposta": "No processo seletivo 2025.1 foram oferecidas 9.022 vagas, sendo mais de 7 mil para cursos técnicos."
    },
    {
        "keywords": ["curso", "vários", "escolher"],
        "resposta": "Não. O candidato deve optar por apenas um curso por inscrição."
    },
    {
        "keywords": ["cotas", "reservas", "vagas especiais"],
        "resposta": "Sim. A Faetec reserva vagas para candidatos com deficiência, filhos de servidores, entre outros critérios do edital."
    },
    {
        "keywords": ["perdi", "fui", "fora", "prazo"],
        "resposta": "É necessário aguardar o próximo processo seletivo. A Faetec não aceita inscrições fora do período."
    },
    {
        "keywords": ["alterar", "corrigir", "atualizar"],
        "resposta": "Durante o período de inscrição é possível corrigir informações no sistema online. Após o encerramento não há alterações."
    },
    {
        "keywords": ["quais", "curso", "disponíveis", "oferecidos"],
        "resposta": "A Faetec oferece cursos de Qualificação Profissional, Técnicos de Nível Médio e de Formação Inicial e Continuada, como Administração, Informática, Enfermagem, Segurança do Trabalho e Logística."
    },
    {
        "keywords": ["online", "distancia", "ead"],
        "resposta": "Alguns cursos possuem atividades a distância, mas a maioria é presencial."
    },
    {
        "keywords": ["idiomas", "ingles", "espanhol"],
        "resposta": "Sim. Em algumas unidades há cursos de línguas, como Inglês e Espanhol."
    },
    {
        "keywords": ["eletricista", "eletrica"],
        "resposta": "Sim. A Faetec oferece cursos como Eletricista Instalador e relacionados à área elétrica."
    },
    {
        "keywords": ["gastronomia", "cozinha", "confeitaria", "panificacao"],
        "resposta": "Sim. Em algumas unidades há cursos de Auxiliar de Cozinha, Confeitaria e Panificação."
    },
    {
        "keywords": ["administracao", "técnico", "administração"],
        "resposta": "Sim. O curso Técnico em Administração é ofertado em algumas unidades."
    },
    {
        "keywords": ["logistica", "técnico", "logistica"],
        "resposta": "Sim. Algumas unidades oferecem o curso Técnico em Logística."
    },
    {
        "keywords": ["redes", "computadores", "tecnologia"],
        "resposta": "Sim. A Faetec oferece o curso Técnico em Redes de Computadores em determinadas unidades."
    },
    {
        "keywords": ["mais procurados", "populares", "curso"],
        "resposta": "Os cursos mais procurados costumam ser Técnico em Enfermagem, Informática, Administração e Eletricista."
    },
    {
        "keywords": ["atualiza", "novos", "mudança"],
        "resposta": "Sim. A Faetec revisa periodicamente sua oferta de cursos de acordo com a demanda de mercado."
    },
    {
        "keywords": ["documentos", "matricula", "necessarios", "requisitos"],
        "resposta": "Para matrícula, são exigidos: certidão de nascimento ou casamento, RG, CPF, fotos 3x4, título de eleitor (maiores de 18 anos), certificado de reservista (homens), diploma ou certificado do Ensino Médio e histórico escolar."
    },
    {
        "keywords": ["cnh", "carteira de motorista"],
        "resposta": "Sim. A CNH pode ser usada como documento oficial de identificação."
    },
    {
        "keywords": ["título de eleitor", "eleitor"],
        "resposta": "Não é obrigatório para matrícula, mas necessário para fins eleitorais, caso tenha mais de 18 anos."
    },
    {
        "keywords": ["digital", "gov.br", "online"],
        "resposta": "Sim. Documentos digitais oficiais, como os disponíveis no aplicativo gov.br, são aceitos."
    },
    {
        "keywords": ["certidao nascimento", "documento"],
        "resposta": "A certidão de nascimento pode ser aceita, mas é preferível apresentar o RG."
    },
    {
        "keywords": ["enviar", "por email", "digitalizar"],
        "resposta": "Não. Os documentos devem ser apresentados presencialmente no ato da matrícula."
    },
    {
        "keywords": ["vacina", "comprovante", "saúde"],
        "resposta": "Alguns cursos da área de saúde podem exigir comprovação de vacinação."
    },
    {
        "keywords": ["comprovante escolaridade", "original", "certificado"],
        "resposta": "Sim. É necessário apresentar o comprovante original de escolaridade para conferência."
    },
    {
        "keywords": ["menor", "menores", "responsável"],
        "resposta": "Sim. Menores de 18 anos devem estar acompanhados por responsável legal."
    },
    {
        "keywords": ["copias", "autenticadas", "cópia autenticada"],
        "resposta": "Em geral, a Faetec exige documentos originais, mas cópias autenticadas podem ser aceitas em alguns casos."
    },
    {
        "keywords": ["resultado", "resultado", "consulta", "ver"],
        "resposta": "O resultado do processo seletivo está disponível no site oficial da Faetec, na seção de resultados: www.faetec.rj.gov.br."
    },
    {
        "keywords": ["aviso", "email", "resultado"],
        "resposta": "Sim. Geralmente é enviado um e-mail avisando sobre a aprovação, mas é importante conferir no site."
    },
    {
        "keywords": ["não chamado", "segunda chamada", "lista de espera"],
        "resposta": "Se você não for chamado na primeira chamada, ainda pode ser convocado em chamadas subsequentes conforme as vagas."
    },
    {
        "keywords": ["lista de espera", "posicao", "aguardar"],
        "resposta": "Os candidatos em lista de espera são chamados conforme a disponibilidade de vagas remanescentes. O edital explica como consultar sua posição."
    },
    {
        "keywords": ["resultado", "publicado", "unidades"],
        "resposta": "Sim. O resultado é publicado ao mesmo tempo em todas as unidades no portal oficial."
    },
    {
        "keywords": ["prazo", "matricula", "validade"],
        "resposta": "O prazo para efetuar matrícula é informado no edital e deve ser rigorosamente cumprido."
    },
    {
        "keywords": ["perder", "não comparecer", "matricula"],
        "resposta": "Sim. Quem não comparece perde a vaga."
    },
    {
        "keywords": ["segunda chamada", "convocacao"],
        "resposta": "Caso sobrem vagas, haverá segunda chamada para aprovados."
    },
    {
        "keywords": ["como saber", "lista de espera", "posicao"],
        "resposta": "O edital informa como consultar a posição na lista de espera pelo sistema da Faetec."
    },
    {
        "keywords": ["recorrer", "recurso", "resultado"],
        "resposta": "Sim. É possível recorrer dentro do prazo e critérios estabelecidos no edital."
    },
    {
        "keywords": ["documentos", "matricula", "quais", "necessarios"],
        "resposta": "São exigidos: certidão de nascimento ou casamento, RG, CPF, comprovante de residência, título de eleitor (maiores de 18 anos), certificado de reservista (homens), diploma ou certificado do Ensino Médio e histórico escolar."
    },
    {
        "keywords": ["online", "matricula", "pela internet"],
        "resposta": "Não. A matrícula deve ser feita presencialmente na unidade onde o candidato foi aprovado."
    },
    {
        "keywords": ["prazo", "fim", "fazer matricula"],
        "resposta": "O prazo é estabelecido no edital de cada processo seletivo e deve ser rigorosamente cumprido."
    },
    {
        "keywords": ["não compareci", "perdi", "matricula"],
        "resposta": "Quem não comparece à matrícula perde a vaga, que é repassada ao próximo da lista de espera."
    },
    {
        "keywords": ["transferir", "mudar", "unidade"],
        "resposta": "Não é possível transferir matrícula entre unidades da Faetec."
    },
    {
        "keywords": ["pagar", "taxa", "matricula"],
        "resposta": "Não. A matrícula é gratuita."
    },
    {
        "keywords": ["mais de um", "matricula em dois", "cursos"],
        "resposta": "Sim, desde que os horários não coincidam. Caso contrário, será necessário optar por apenas um curso."
    },
    {
        "keywords": ["curso iniciado", "curso ja começou", "matricula"],
        "resposta": "Em geral, a matrícula ocorre no início do semestre letivo. Exceções dependem da disponibilidade de vagas e autorização da instituição."
    },
    {
        "keywords": ["informacoes", "matricula", "detalhes"],
        "resposta": "As informações sobre matrícula estão disponíveis no site oficial da Faetec e na página da COSEAC/UFF."
    },
    {
        "keywords": ["documentos digitais", "aceitos", "online"],
        "resposta": "Sim, desde que sejam documentos oficiais digitais aceitos pela instituição."
    },
    {
        "keywords": ["cursos técnicos", "quais cursos", "técnico"],
        "resposta": "A Faetec oferece cursos técnicos em áreas como Administração, Informática, Enfermagem, Segurança do Trabalho, Logística, Eletrotécnica, Análises Clínicas, Design Gráfico, Música e Turismo."
    },
    {
        "keywords": ["deficiente", "pessoa com deficiência", "acessibilidade"],
        "resposta": "Sim. A Faetec oferece cursos técnicos com adaptações para garantir inclusão de pessoas com deficiência."
    },
    {
        "keywords": ["noturno", "periodo"],
        "resposta": "Sim. Algumas unidades oferecem cursos técnicos no período noturno."
    },
    {
        "keywords": ["subsequente", "já concluiu", "ensino medio"],
        "resposta": "Sim. Existem cursos subsequentes destinados a quem já concluiu o Ensino Médio."
    },
    {
        "keywords": ["vagas", "disponibilidade", "curso"],
        "resposta": "A disponibilidade de vagas é informada no edital do processo seletivo."
    },
    {
        "keywords": ["unidades", "locais", "escolas"],
        "resposta": "Algumas unidades que oferecem cursos técnicos são: ETE Oscar Tenório, ETE Juscelino Kubitschek, ETE Ferreira Viana, ETE República e ETE Henrique Lage."
    },
    {
        "keywords": ["estagio", "curso", "duracao", "pratica"],
        "resposta": "Sim. A Faetec possui parcerias com empresas que oferecem estágio prático durante os cursos técnicos."
    },
    {
        "keywords": ["duracao", "tempo", "curso"],
        "resposta": "A duração varia de acordo com o curso, geralmente entre 1 a 2 anos."
    },
    {
        "keywords": ["transferir", "mudar", "curso"],
        "resposta": "Não é possível transferir entre cursos técnicos. Para mudar de curso, é necessário participar de novo processo seletivo."
    },
    {
        "keywords": ["certificacao", "diploma", "certificado"],
        "resposta": "Sim. Os cursos técnicos oferecem certificado reconhecido pelo MEC."
    },
    {
        "keywords": ["saude", "enfermagem", "analises", "clinicas"],
        "resposta": "Sim. A Faetec oferece cursos técnicos na área de saúde, como Técnico em Enfermagem e Técnico em Análises Clínicas."
    },
    {
        "keywords": ["musica", "tecnico", "curso"],
        "resposta": "Sim. É possível estudar música em unidades como Henrique Lage e Marechal Hermes."
    },
    {
        "keywords": ["informatica", "redes", "tecnico"],
        "resposta": "Sim. A Faetec oferece Técnico em Informática e Técnico em Redes de Computadores."
    },
    {
        "keywords": ["administracao", "recursos humanos", "gestao"],
        "resposta": "Sim. Há cursos como Técnico em Administração e Técnico em Recursos Humanos."
    },
    {
        "keywords": ["turismo", "guia", "hospedagem"],
        "resposta": "Sim. A Faetec oferece Técnico em Guia de Turismo e Técnico em Hospedagem."
    },
    {
        "keywords": ["logistica", "transporte"],
        "resposta": "Sim. Há cursos técnicos como Logística e Transporte."
    },
    {
        "keywords": ["design", "grafico", "multimidia"],
        "resposta": "Sim. A Faetec oferece Técnico em Design Gráfico e Produção Multimídia."
    },
    {
        "keywords": ["teatro", "artes", "cênicas"],
        "resposta": "Sim. Há cursos técnicos em Artes Cênicas e Produção Teatral."
    },
    {
        "keywords": ["gastronomia", "cozinha", "confeitaria", "padaria"],
        "resposta": "Sim. A Faetec oferece Técnico em Cozinha e Técnico em Confeitaria."
    },
    {
        "keywords": ["moda", "vestuário", "modelagem"],
        "resposta": "Sim. Existem cursos como Técnico em Produção de Moda e Modelagem do Vestuário."
    },
    {
        "keywords": ["mecanica", "automotiva", "manutenção"],
        "resposta": "Sim. A Faetec oferece Técnico em Mecânica e Técnico em Manutenção Automotiva."
    },
    {
        "keywords": ["eletronica", "automacao"],
        "resposta": "Sim. Há cursos técnicos em Eletrônica e Automação Industrial."
    },
    {
        "keywords": ["telecom", "redes", "sistemas"],
        "resposta": "Sim. A Faetec oferece Técnico em Redes de Comunicação e Sistemas de Telecomunicações."
    },
    {
        "keywords": ["segurança", "meio ambiente", "tst"],
        "resposta": "Sim. Há cursos como Técnico em Segurança do Trabalho e Técnico em Meio Ambiente."
    },
    {
        "keywords": ["logistica", "porto", "operacoes"],
        "resposta": "Sim. A Faetec oferece Técnico em Logística Portuária e Operações Portuárias."
    },
    {
        "keywords": ["transporte", "rodoviario", "aereo", "maritimo", "fluvial"],
        "resposta": "Sim. Há cursos como Técnico em Transporte Rodoviário, Aéreo, Marítimo e Fluvial."
    },
    {
        "keywords": ["pre-requisitos", "quem pode fazer", "requisitos"],
        "resposta": "Para cursos subsequentes é necessário ter concluído o Ensino Médio. Para concomitante externo, é preciso estar matriculado no 2º ano do Ensino Médio."
    },
    {
        "keywords": ["inscricao", "se inscrever", "como fazer"],
        "resposta": "As inscrições para cursos técnicos são realizadas online pelo site oficial: www.faetec.rj.gov.br."
    },
    {
        "keywords": ["unidades", "escolas", "locais"],
        "resposta": "A Faetec possui diversas unidades distribuídas pelo estado do Rio de Janeiro, incluindo escolas técnicas, ISEPs, CVTs e unidades de qualificação profissional."
    },
    {
        "keywords": ["quantas unidades", "numero de unidades"],
        "resposta": "A Faetec conta com mais de 120 unidades em todo o estado do Rio de Janeiro."
    },
    {
        "keywords": ["diretoria", "regional", "gestao"],
        "resposta": "As unidades da Faetec estão organizadas em Diretorias Regionais que fazem a gestão administrativa e pedagógica de acordo com cada região."
    },
    {
        "keywords": ["sede", "localizacao"],
        "resposta": "A sede administrativa da Faetec está localizada no Rio de Janeiro, na Rua Clarimundo de Melo, 847 – Quintino Bocaiúva."
    },
    {
        "keywords": ["responsavel", "administra", "diretoria"],
        "resposta": "Cada unidade da Faetec possui direção própria, subordinada às Diretorias Regionais e à presidência da instituição."
    },
    {
        "keywords": ["contato", "telefone", "email"],
        "resposta": "Os contatos de cada unidade (telefone, e-mail, endereço) estão disponíveis no site oficial da Faetec: www.faetec.rj.gov.br."
    },
    {
        "keywords": ["transferencia", "mudar", "unidade"],
        "resposta": "Não é permitido transferir matrícula entre unidades. O aluno deve participar de novo processo seletivo."
    },
    {
        "keywords": ["entrego", "documento"],
        "resposta": "Você entrega (ou apresenta, se for documento externo) junto à Secretaria Acadêmica da FAETEC / ETER República. Em geral, esse setor é responsável por registrar formalmente boletins, documentos escolares, notas e demais registros acadêmicos."
    },
    {
        "keywords": ["solicito", "antigo"],
        "resposta": "Faça uma solicitação formal à Secretaria Acadêmica, informando: seu nome completo, matrícula, curso/turma e o período do boletim que você não recebeu. Pode ser necessário preencher um requerimento (presencial ou digital) e aguardar o prazo interno para emissão."
    },
    {
        "keywords": ["onde", "pego"],
        "resposta": "Faça uma solicitação formal à Secretaria Acadêmica, informando: seu nome completo, matrícula, curso/turma e o período do boletim que você não recebeu. Pode ser necessário preencher um requerimento (presencial ou digital) e aguardar o prazo interno para emissão."
    },
    {
        "keywords": ["perdi", "comprovante", "matricula"],
        "resposta": "Com a Secretaria Acadêmica. Este setor pode emitir uma segunda via do comprovante de matrícula ou fornecer uma declaração oficial confirmando sua matrícula, mediante apresentação de documentos de identificação."
    },
    {
        "keywords": ["segunda via", "documentos", "historico", "certificado", "declaracao"],
        "resposta": "Para documentos como histórico escolar, declarações, certificados ou comprovantes, você deve: dirigir-se à Secretaria Acadêmica; preencher requerimento ou formulário específico; apresentar identificação pessoal; verificar se há taxa de emissão; aguardar o prazo estabelecido pela FAETEC (declarações em até 3 dias úteis, certificados em até 7 dias e histórico em até 30 dias úteis)."
    },
    {
        "keywords": ["problemas", "notas", "erro", "lancamento"],
        "resposta": "Proceda inicialmente com o professor responsável pela disciplina. Se não houver correção ou resposta satisfatória, leve ao Coordenador de Curso ou à Coordenação Pedagógica para formalizar a reclamação."
    },
    {
        "keywords": ["erro", "frequencia", "faltas", "incorreta"],
        "resposta": "Primeiramente com o professor que faz a chamada da turma. Se ainda assim o erro persistir, leve à Coordenação de Curso e/ou à Secretaria para averiguação. Traga provas ou registros se possível."
    },
    {
        "keywords": ["regularizar", "faltas", "justificadas", "atestado"],
        "resposta": "Você deve apresentar justificativa formal com documentação (atestado médico ou justificativa legal). A justificativa deve ser protocolada na Secretaria Acadêmica ou setor indicado, respeitando o prazo definido no regulamento."
    },
    {
        "keywords": ["datas", "provas", "trabalhos", "quando"],
        "resposta": "Datas são divulgadas em sala pelos professores, no plano de ensino, no calendário acadêmico da unidade, no site/portal da FAETEC ou em murais físicos."
    },
    {
        "keywords": ["perdi", "prova", "falta", "segunda chamada"],
        "resposta": "Com o professor da disciplina primeiro. Em seguida, se necessário, com a Coordenação de Curso para verificar possibilidade de reposição ou segunda chamada, conforme regulamento interno."
    },
    {
        "keywords": ["reagendar", "prova", "avaliacao", "segunda"],
        "resposta": "Necessita-se de motivo justificado (problemas de saúde, imprevistos sérios, etc.) e documentação comprobatória. Solicitação formal deve ser feita à Secretaria ou Coordenação dentro dos prazos determinados."
    },
    {
        "keywords": ["revisar", "ver", "prova", "nota"],
        "resposta": "Normalmente com o professor da disciplina. Se houver canal institucional para revisão formal, será via Coordenador ou Direção."
    },
    {
        "keywords": ["erro", "correcao", "nota", "prova"],
        "resposta": "Converse primeiro com o professor apresentando gabarito ou critérios. Se não resolver, leve à Coordenação do Curso ou Direção para revisão oficial."
    },
    {
        "keywords": ["avaliacoes", "externas", "certificacao", "provas"],
        "resposta": "A Coordenação de Curso ou setor responsável divulgará editais, comunicados ou instruções no site da FAETEC, na unidade, por e-mail institucional ou em murais."
    },
    {
        "keywords": ["prova", "substitutiva", "convocacao", "regra"],
        "resposta": "As normas constam no regimento interno. A convocação é feita pela Secretaria ou Coordenação por meio de edital ou aviso oficial com datas e requisitos."
    },
    {
        "keywords": ["mudanca", "horario", "aula", "alteracao"],
        "resposta": "Mudanças de horário são comunicadas pela Coordenação do Curso ou Direção, via murais, site, portal, e-mails institucionais ou avisos em sala."
    },
    {
        "keywords": ["substituicao", "professor", "troca", "aula"],
        "resposta": "A Coordenação de Curso ou Direção Pedagógica é responsável por comunicar substituição de professor, repassando o aviso à turma."
    },
    {
        "keywords": ["duvida", "conteudo", "professor", "orientacao"],
        "resposta": "Com o professor da disciplina. Se persistirem dúvidas, pode-se procurar a Coordenação de Curso ou monitores, se houver."
    },
    {
        "keywords": ["confirmar", "conteudo", "aula", "plano"],
        "resposta": "Verifique o plano de ensino da disciplina, cronograma, materiais do professor ou registros em plataformas institucionais."
    },
    {
        "keywords": ["avisos", "eventos", "gincanas", "feiras", "programacoes"],
        "resposta": "Avisos são publicados em murais, site/portal da unidade, redes sociais oficiais e comunicados internos."
    },
    {
        "keywords": ["atividades", "extracurriculares", "culturais", "esportivas"],
        "resposta": "A coordenação de Extensão anuncia editais ou convocações. O aluno deve preencher formulários ou inscrição conforme normas e prazos."
    },
    {
        "keywords": ["acidente", "aula", "pratica", "leve"],
        "resposta": "Primeiro com o professor responsável pela aula. Depois, o incidente deve ser comunicado formalmente à Coordenação ou Direção da unidade."
    },
    {
        "keywords": ["problema", "colega", "professor", "conflito"],
        "resposta": "Utilize canais formais: Coordenação de Curso, Direção Pedagógica, Orientação Educacional ou Ouvidoria. Protocolize o relato por escrito se possível."
    },
    {
        "keywords": ["comunicados", "avisos", "escola"],
        "resposta": "No site oficial da FAETEC / ETER, no portal do aluno, em murais físicos, e-mails institucionais ou avisos da Direção/Coordenação."
    },
    {
        "keywords": ["mudanca", "calendario", "escolar", "alteracao"],
        "resposta": "Mudanças de calendário são divulgadas oficialmente pela FAETEC em comunicados no site, murais ou portal da unidade."
    },
    {
        "keywords": ["cancelamento", "aula", "evento"],
        "resposta": "A Direção ou Coordenação emite comunicados oficiais, também por e-mail institucional, sistema interno ou murais."
    },
    {
        "keywords": ["nao", "não", "comunicado", "aviso"],
        "resposta": "Verifique se seus contatos estão atualizados na Secretaria. Consulte site, mural e canais oficiais. Caso persista, solicite reemissão ou confirmação na Secretaria."
    },
    {
        "keywords": ["estagio", "pratica", "profissional", "escolar"],
        "resposta": "Procure o setor de Estágios ou Prática Profissional da unidade. Caso não haja setor visível, vá à Coordenação de Curso ou Direção Pedagógica."
    },
    {
        "keywords": ["ola", "oi", "eae"],
        "resposta": "Opa amigão, no que posso te ajudar?"
    },
    {
        "keywords": ["bom", "dia"],
        "resposta": "Bom diaa! No que posso te ajudar?"
    },
    {
        "keywords": ["boa", "tarde"],
        "resposta": "Boa tarde! No que posso te ajudar?"
    },
    {
        "keywords": ["boa", "noite"],
        "resposta": "Boa noite! No que posso te ajudar?"
    }
]
for item in base_conhecimento:
    item['keywords'] = [normalizar_texto(k) for k in item.get('keywords', [])]
# -------- CHATBOT --------
if menu == "Chatbot":
    st.markdown("## 👋 Bem-vindo ao FaeThink!")
    st.write("Seu assistente especializado em FAETEC. Manda ver 😁!")
    # Inicializar o estado se não existir
    if "abrir_chat" not in st.session_state:
        st.session_state.abrir_chat = False
    if "conversa" not in st.session_state:
        st.session_state.conversa = []
    # Botão para abrir/fechar chat
    if st.session_state.abrir_chat:
        if st.button("⬅️ Fechar Chat"):
            st.session_state.abrir_chat = False
            st.session_state.conversa = []
    else:
        if st.button("💬 Abrir Chat"):
            st.session_state.abrir_chat = True
    # Mostrar chat se aberto
    if st.session_state.abrir_chat:
        st.markdown("### 💬 Chat")
        pergunta_usuario = st.text_input("Digite sua mensagem:")
        if st.button("Enviar"):
            if pergunta_usuario:
                pergunta_normalizada = normalizar_texto(pergunta_usuario)
                resposta_bot = "Desculpe, não entendi sua pergunta 😅"
                for item in base_conhecimento:
                    if any(k in pergunta_normalizada for k in item["keywords"]):
                        resposta_bot = item["resposta"]
                        break
                st.session_state.conversa.append(("Você 😁", pergunta_usuario))
                st.session_state.conversa.append(("FaeThink 🤖", resposta_bot))
        # Links das fotos de perfil
        foto_usuario = "https://i.imgur.com/5FAZMMX.png"
        foto_bot = "https://i.imgur.com/zg6qpgy.png"
        # Exibe o histórico
        for usuario, mensagem in st.session_state.conversa:
            if "Você" in usuario:
                st.markdown(
                    f"""
                    <div class='chat-linha usuario'>
                        <div class='balao-usuario'>{mensagem}</div>
                        <img src='{foto_usuario}' alt='Você'>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div class='chat-linha bot'>
                        <img src='{foto_bot}' alt='Bot'>
                        <div class='balao-bot'>{mensagem}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
# -------- SOBRE O PROJETO --------
elif menu == "Sobre o Projeto":
    st.markdown("## 🎓 Bem vindo ao FaeThink")

    col1, col2 = st.columns([2, 1])  # texto ocupa mais espaço, imagem menos

    with col1:  # Texto à esquerda
        st.write("""
        O FaeThink é uma ferramenta digital desenvolvida para oferecer suporte aos estudantes da instituição. Sua principal finalidade é responder dúvidas relacionadas ao campus e disponibilizar informações relevantes para o cotidiano escolar.

Além de esclarecer questões, o FaeThink também apresenta os projetos em andamento na escola, permitindo que a comunidade acadêmica acompanhe, participe e conheça melhor as iniciativas promovidas pela instituição. Trata-se de um recurso que contribui para ampliar a transparência e o acesso às informações.

Nosso compromisso é facilitar a comunicação entre a escola e seus estudantes por meio da tecnologia. 🚀 Com o FaeThink, garantimos um canal confiável e acessível para consulta, interação e acompanhamento das atividades do campus.
        """)

    with col2:  # Imagem à direita
        st.image("https://i.imgur.com/fTew3xy.png", width=350)

# -------- PROJETOS DA ESCOLA --------
elif menu == "Projetos da Escola":
    st.markdown("## 📢 Projetos da Escola")
    st.write("Aqui estão alguns projetos em andamento na nossa escola:")

    # Projeto 1
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/N2DeKr9.png", width=200)
    with col2:
        st.markdown("### Jornal A Voz do Republica 📰")
        st.markdown("[📸 Instagram](https://www.instagram.com/avoz_republica/)")

    st.divider()

    # Projeto 2
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/PAHqMhJ.png", width=200)
    with col2:
        st.markdown("### Projeto Multiplicadores 🎭")
        st.markdown("[📸 Instagram](https://www.instagram.com/alunomultiplicador/)")
        
    st.divider()

    # Projeto 3
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/VR8il50.jpeg", width=200)
    with col2:
        st.markdown("### NÚCLEO DE ENSINO DE LINGUAS 🌍")
        st.markdown("[📸 Instagram](https://www.instagram.com/nel_ete_republica/)")
                
    st.divider()

    # Projeto 4
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/VuIxG81.png", width=200)
    with col2:
        st.markdown("### Projeto Vida ✝")
        st.markdown("[📸 Instagram](https://www.instagram.com/projetovidafaetec/)")
                
    st.divider()

    # Projeto 5
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/lVtd1Yy.png", width=200)
    with col2:
        st.markdown("### Gremio Vivaz 💫")
        st.markdown("[📸 Instagram](https://www.instagram.com/gremio.vivaz/)")