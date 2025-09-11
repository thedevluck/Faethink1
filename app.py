import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🎓", layout="wide")

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

# -------- CHATBOT --------
if menu == "Chatbot":
    st.markdown("## 👋 Bem-vindo ao FaeThink!")
    st.write("Seu assistente especializado em FAETEC. Manda ver 😁!")

    # Botão para abrir o chat estilo WhatsApp
    if "abrir_chat" not in st.session_state:
        st.session_state.abrir_chat = False

    if not st.session_state.abrir_chat:
        if st.button("💬 Abrir Chat"):
            st.session_state.abrir_chat = True
    else:
        st.markdown("### 💬 Chat")

        base_conhecimento = [
    {
        "keywords": ["estágio", "estágios", "vaga de estágio"],
        "resposta": "A Faetec possui convênios com empresas e instituições para fornecer estágios aos alunos de cursos técnicos e de qualificação, gerenciados pelo DIVEST."
    },
    {
        "keywords": ["como me inscrevo", "inscrição estágio", "cadastrar estágio"],
        "resposta": "Os alunos podem se inscrever via portal de estágio da Faetec ou diretamente no DIVEST (Setor de Estágio)."
    },
    {
        "keywords": ["estágio obrigatório", "obrigatoriedade do estágio"],
        "resposta": "Depende do curso. Nos cursos técnicos, o estágio é obrigatório para a conclusão, com acompanhamento do DIVEST."
    },
    {
        "keywords": ["carga horária do estágio", "horas de estágio"],
        "resposta": "A carga horária varia conforme o curso, geralmente entre 400 e 600 horas."
    },
    {
        "keywords": ["bolsa estágio", "estágio remunerado"],
        "resposta": "Sim, alguns estágios oferecem bolsa auxílio, enquanto outros não são remunerados."
    },
    {
        "keywords": ["estágio saúde", "enfermagem estágio"],
        "resposta": "Cursos como Técnico em Enfermagem possuem estágio obrigatório em hospitais e clínicas parceiras."
    },
    {
        "keywords": ["escolher empresa", "empresa do estágio"],
        "resposta": "A escolha depende das vagas disponíveis nas empresas conveniadas com a Faetec."
    },
    {
        "keywords": ["acompanhamento estágio", "supervisor estágio"],
        "resposta": "Sim, há supervisores que acompanham o desempenho do aluno durante o estágio."
    },
    {
        "keywords": ["estágio fora do RJ", "estágio em outro estado"],
        "resposta": "Sim, desde que a empresa possua convênio com a Faetec."
    },
    {
        "keywords": ["estágio informática", "estágio redes de computadores"],
        "resposta": "Sim, cursos de Informática e Redes de Computadores possuem oportunidades em empresas de tecnologia."
    },
    {
        "keywords": ["como me inscrever", "inscrição", "fazer inscrição"],
        "resposta": "As inscrições são realizadas exclusivamente pelo site oficial da Faetec: www.faetec.rj.gov.br/inscricoes."
    },
    {
        "keywords": ["inscrição presencial", "fazer inscrição na escola"],
        "resposta": "Não é possível fazer inscrição presencial. O processo é apenas online, conforme os editais."
    },
    {
        "keywords": ["pagar inscrição", "taxa inscrição"],
        "resposta": "Sim. No processo seletivo 2025.2 a taxa foi de R$ 20,00."
    },
    {
        "keywords": ["idade mínima", "qual idade para inscrição"],
        "resposta": "Depende do curso. Para cursos técnicos é necessário ter concluído o Ensino Fundamental. Para cursos de qualificação, a idade mínima é 16 anos."
    },
    {
        "keywords": ["estrangeiro pode", "inscrição estrangeiro"],
        "resposta": "Sim, desde que possua documentos oficiais válidos no Brasil, como CPF e RG."
    },
    {
        "keywords": ["quantas vagas", "número de vagas"],
        "resposta": "No processo seletivo 2025.1 foram oferecidas 9.022 vagas, sendo mais de 7 mil para cursos técnicos."
    },
    {
        "keywords": ["posso escolher mais de um curso", "vários cursos"],
        "resposta": "Não. O candidato deve optar por apenas um curso por inscrição."
    },
    {
        "keywords": ["cotas", "reserva de vagas"],
        "resposta": "Sim. A Faetec reserva vagas para candidatos com deficiência, filhos de servidores, entre outros critérios do edital."
    },
    {
        "keywords": ["perdi o prazo", "inscrição fora do prazo"],
        "resposta": "É necessário aguardar o próximo processo seletivo. A Faetec não aceita inscrições fora do período."
    },
    {
        "keywords": ["alterar dados", "corrigir inscrição"],
        "resposta": "Durante o período de inscrição é possível corrigir informações no sistema online. Após o encerramento não há alterações."
    },
    {
        "keywords": ["quais cursos", "cursos oferecidos", "cursos disponíveis"],
        "resposta": "A Faetec oferece cursos de Qualificação Profissional, Técnicos de Nível Médio e de Formação Inicial e Continuada, como Administração, Informática, Enfermagem, Segurança do Trabalho e Logística."
    },
    {
        "keywords": ["curso online", "curso a distância", "ead"],
        "resposta": "Alguns cursos possuem atividades a distância, mas a maioria é presencial."
    },
    {
        "keywords": ["curso de idiomas", "curso de inglês", "curso de espanhol"],
        "resposta": "Sim. Em algumas unidades há cursos de línguas, como Inglês e Espanhol."
    },
    {
        "keywords": ["curso de eletricista", "curso elétrica"],
        "resposta": "Sim. A Faetec oferece cursos como Eletricista Instalador e relacionados à área elétrica."
    },
    {
        "keywords": ["curso de gastronomia", "cozinha", "confeitaria", "panificação"],
        "resposta": "Sim. Em algumas unidades há cursos de Auxiliar de Cozinha, Confeitaria e Panificação."
    },
    {
        "keywords": ["curso técnico de administração", "técnico em administração"],
        "resposta": "Sim. O curso Técnico em Administração é ofertado em algumas unidades."
    },
    {
        "keywords": ["curso técnico de logística", "técnico em logística"],
        "resposta": "Sim. Algumas unidades oferecem o curso Técnico em Logística."
    },
    {
        "keywords": ["curso de redes", "redes de computadores"],
        "resposta": "Sim. A Faetec oferece o curso Técnico em Redes de Computadores em determinadas unidades."
    },
    {
        "keywords": ["cursos mais procurados", "curso popular"],
        "resposta": "Os cursos mais procurados costumam ser Técnico em Enfermagem, Informática, Administração e Eletricista."
    },
    {
        "keywords": ["atualiza cursos", "novos cursos", "mudança de cursos"],
        "resposta": "Sim. A Faetec revisa periodicamente sua oferta de cursos de acordo com a demanda de mercado."
    },
    {
        "keywords": ["documentos matrícula", "quais documentos", "documentos necessários"],
        "resposta": "Para matrícula, são exigidos: certidão de nascimento ou casamento, RG, CPF, fotos 3x4, título de eleitor (maiores de 18 anos), certificado de reservista (homens), diploma ou certificado do Ensino Médio e histórico escolar."
    },
    {
        "keywords": ["usar CNH", "CNH no lugar do RG"],
        "resposta": "Sim. A CNH pode ser usada como documento oficial de identificação."
    },
    {
        "keywords": ["preciso de título de eleitor", "documento título eleitor"],
        "resposta": "Não é obrigatório para matrícula, mas necessário para fins eleitorais, caso tenha mais de 18 anos."
    },
    {
        "keywords": ["documentos digitais", "aceita digital", "gov.br"],
        "resposta": "Sim. Documentos digitais oficiais, como os disponíveis no aplicativo gov.br, são aceitos."
    },
    {
        "keywords": ["certidão nascimento serve", "matrícula com certidão"],
        "resposta": "A certidão de nascimento pode ser aceita, mas é preferível apresentar o RG."
    },
    {
        "keywords": ["enviar documentos por e-mail", "mandar por e-mail"],
        "resposta": "Não. Os documentos devem ser apresentados presencialmente no ato da matrícula."
    },
    {
        "keywords": ["vacina obrigatória", "comprovante de vacinação"],
        "resposta": "Alguns cursos da área de saúde podem exigir comprovação de vacinação."
    },
    {
        "keywords": ["comprovante escolaridade original", "preciso original"],
        "resposta": "Sim. É necessário apresentar o comprovante original de escolaridade para conferência."
    },
    {
        "keywords": ["menor de idade matrícula", "responsável matrícula"],
        "resposta": "Sim. Menores de 18 anos devem estar acompanhados por responsável legal."
    },
    {
        "keywords": ["cópias autenticadas", "aceita cópia autenticada"],
        "resposta": "Em geral, a Faetec exige documentos originais, mas cópias autenticadas podem ser aceitas em alguns casos."
    },
     {
        "keywords": ["resultado", "onde ver resultado", "consultar resultado"],
        "resposta": "O resultado do processo seletivo está disponível no site oficial da Faetec, na seção de resultados: www.faetec.rj.gov.br."
    },
    {
        "keywords": ["aviso por e-mail", "recebo e-mail resultado"],
        "resposta": "Sim. Geralmente é enviado um e-mail avisando sobre a aprovação, mas é importante conferir no site."
    },
    {
        "keywords": ["não fui chamado", "segunda chamada", "lista de espera"],
        "resposta": "Se você não for chamado na primeira chamada, ainda pode ser convocado em chamadas subsequentes conforme as vagas."
    },
    {
        "keywords": ["lista de espera", "posição na lista"],
        "resposta": "Os candidatos em lista de espera são chamados conforme a disponibilidade de vagas remanescentes. O edital explica como consultar sua posição."
    },
    {
        "keywords": ["resultado simultâneo", "unidades resultado"],
        "resposta": "Sim. O resultado é publicado ao mesmo tempo em todas as unidades no portal oficial."
    },
    {
        "keywords": ["prazo matrícula", "até quando matricular"],
        "resposta": "O prazo para efetuar matrícula é informado no edital e deve ser rigorosamente cumprido."
    },
    {
        "keywords": ["perder a vaga", "não compareci matrícula"],
        "resposta": "Sim. Quem não comparece perde o direito à vaga."
    },
    {
        "keywords": ["segunda chamada", "convocação extra"],
        "resposta": "Caso sobrem vagas, haverá segunda chamada para aprovados."
    },
    {
        "keywords": ["como saber lista de espera", "estou na lista de espera"],
        "resposta": "O edital informa como consultar a posição na lista de espera pelo sistema da Faetec."
    },
    {
        "keywords": ["recorrer resultado", "recurso resultado"],
        "resposta": "Sim. É possível recorrer dentro do prazo e critérios estabelecidos no edital."
    },
    {
        "keywords": ["documentos matrícula", "quais documentos", "preciso levar"],
        "resposta": "São exigidos: certidão de nascimento ou casamento, RG, CPF, comprovante de residência, título de eleitor (maiores de 18 anos), certificado de reservista (homens), diploma ou certificado do Ensino Médio e histórico escolar."
    },
    {
        "keywords": ["matrícula online", "fazer matrícula pela internet"],
        "resposta": "Não. A matrícula deve ser feita presencialmente na unidade onde o candidato foi aprovado."
    },
    {
        "keywords": ["prazo matrícula", "até quando fazer matrícula"],
        "resposta": "O prazo é estabelecido no edital de cada processo seletivo e deve ser rigorosamente cumprido."
    },
    {
        "keywords": ["não compareci matrícula", "perder matrícula"],
        "resposta": "Quem não comparece à matrícula perde a vaga, que é repassada ao próximo da lista de espera."
    },
    {
        "keywords": ["transferir matrícula", "mudar de unidade"],
        "resposta": "Não é possível transferir a matrícula entre unidades da Faetec."
    },
    {
        "keywords": ["pagar matrícula", "taxa matrícula"],
        "resposta": "Não. A matrícula é gratuita."
    },
    {
        "keywords": ["mais de um curso", "matrícula em dois cursos"],
        "resposta": "Sim, desde que os horários não coincidam. Caso contrário, será necessário optar por apenas um curso."
    },
    {
        "keywords": ["matrícula em curso iniciado", "curso já começou"],
        "resposta": "Em geral, a matrícula ocorre no início do semestre letivo. Exceções dependem da disponibilidade de vagas e autorização da instituição."
    },
    {
        "keywords": ["informações matrícula", "onde ver matrícula"],
        "resposta": "As informações sobre matrícula estão disponíveis no site oficial da Faetec e na página da COSEAC/UFF."
    },
    {
        "keywords": ["documentos digitais matrícula", "aceita digital"],
        "resposta": "Sim, desde que sejam documentos oficiais digitais aceitos pela instituição."
    },
    {
        "keywords": ["cursos técnicos", "quais cursos técnicos", "técnico disponível"],
        "resposta": "A Faetec oferece cursos técnicos em áreas como Administração, Informática, Enfermagem, Segurança do Trabalho, Logística, Eletrotécnica, Análises Clínicas, Design Gráfico, Música e Turismo."
    },
    {
        "keywords": ["curso técnico acessível", "deficiente", "pessoa com deficiência"],
        "resposta": "Sim. A Faetec oferece cursos técnicos com adaptações para garantir inclusão de pessoas com deficiência."
    },
    {
        "keywords": ["curso noturno", "técnico à noite"],
        "resposta": "Sim. Algumas unidades oferecem cursos técnicos no período noturno."
    },
    {
        "keywords": ["curso subsequente", "já concluiu ensino médio"],
        "resposta": "Sim. Existem cursos subsequentes destinados a quem já concluiu o Ensino Médio."
    },
    {
        "keywords": ["vagas cursos técnicos", "disponibilidade de vagas"],
        "resposta": "A disponibilidade de vagas é informada no edital do processo seletivo."
    },
    {
        "keywords": ["unidades cursos técnicos", "onde tem cursos técnicos"],
        "resposta": "Algumas unidades que oferecem cursos técnicos são: ETE Oscar Tenório, ETE Juscelino Kubitschek, ETE Ferreira Viana, ETE República e ETE Henrique Lage."
    },
    {
        "keywords": ["estágio curso técnico", "estágio durante curso técnico"],
        "resposta": "Sim. A Faetec possui parcerias com empresas que oferecem estágio prático durante os cursos técnicos."
    },
    {
        "keywords": ["duração curso técnico", "quanto tempo dura técnico"],
        "resposta": "A duração varia de acordo com o curso, geralmente entre 1 a 2 anos."
    },
    {
        "keywords": ["transferência curso técnico", "mudar curso técnico"],
        "resposta": "Não é possível transferir entre cursos técnicos. Para mudar de curso, é necessário participar de novo processo seletivo."
    },
    {
        "keywords": ["certificação curso técnico", "diploma técnico", "certificado técnico"],
        "resposta": "Sim. Os cursos técnicos oferecem certificado reconhecido pelo MEC."
    },
    {
        "keywords": ["curso técnico saúde", "técnico enfermagem", "técnico análises clínicas"],
        "resposta": "Sim. A Faetec oferece cursos técnicos na área de saúde, como Técnico em Enfermagem e Técnico em Análises Clínicas."
    },
    {
        "keywords": ["curso técnico música", "técnico em música"],
        "resposta": "Sim. É possível estudar música em unidades como Henrique Lage e Marechal Hermes."
    },
    {
        "keywords": ["curso técnico informática", "técnico em informática", "técnico em redes"],
        "resposta": "Sim. A Faetec oferece Técnico em Informática e Técnico em Redes de Computadores."
    },
    {
        "keywords": ["curso técnico administração", "técnico em administração", "recursos humanos"],
        "resposta": "Sim. Há cursos como Técnico em Administração e Técnico em Recursos Humanos."
    },
    {
        "keywords": ["curso técnico turismo", "guia de turismo", "hospedagem"],
        "resposta": "Sim. A Faetec oferece Técnico em Guia de Turismo e Técnico em Hospedagem."
    },
    {
        "keywords": ["curso técnico logística", "técnico em logística", "transporte"],
        "resposta": "Sim. Há cursos técnicos como Logística e Transporte."
    },
    {
        "keywords": ["curso técnico design gráfico", "produção multimídia"],
        "resposta": "Sim. A Faetec oferece Técnico em Design Gráfico e Produção Multimídia."
    },
    {
        "keywords": ["curso técnico teatro", "artes cênicas", "produção teatral"],
        "resposta": "Sim. Há cursos técnicos em Artes Cênicas e Produção Teatral."
    },
    {
        "keywords": ["curso técnico gastronomia", "técnico cozinha", "técnico confeitaria"],
        "resposta": "Sim. A Faetec oferece Técnico em Cozinha e Técnico em Confeitaria."
    },
    {
        "keywords": ["curso técnico moda", "produção de moda", "modelagem do vestuário"],
        "resposta": "Sim. Existem cursos como Técnico em Produção de Moda e Modelagem do Vestuário."
    },
    {
        "keywords": ["curso técnico mecânica", "manutenção automotiva"],
        "resposta": "Sim. A Faetec oferece Técnico em Mecânica e Técnico em Manutenção Automotiva."
    },
    {
        "keywords": ["curso técnico eletrônica", "automação industrial"],
        "resposta": "Sim. Há cursos técnicos em Eletrônica e Automação Industrial."
    },
    {
        "keywords": ["curso técnico telecomunicações", "redes comunicação"],
        "resposta": "Sim. A Faetec oferece Técnico em Redes de Comunicação e Sistemas de Telecomunicações."
    },
    {
        "keywords": ["curso técnico segurança do trabalho", "curso técnico meio ambiente"],
        "resposta": "Sim. Há cursos como Técnico em Segurança do Trabalho e Técnico em Meio Ambiente."
    },
    {
        "keywords": ["curso técnico logística portuária", "operações portuárias"],
        "resposta": "Sim. A Faetec oferece Técnico em Logística Portuária e Operações Portuárias."
    },
    {
        "keywords": ["curso técnico transporte", "técnico em transporte rodoviário"],
        "resposta": "Sim. Há cursos como Técnico em Transporte e Transporte Rodoviário."
    },
    {
        "keywords": ["curso técnico gestão empresarial", "gestão de negócios"],
        "resposta": "Sim. A Faetec oferece Técnico em Gestão Empresarial e Gestão de Negócios."
    },
    {
        "keywords": ["curso técnico recursos humanos", "gestão de pessoas"],
        "resposta": "Sim. Existem cursos técnicos em Recursos Humanos e Gestão de Pessoas."
    },
    {
        "keywords": ["curso técnico logística internacional", "comércio exterior"],
        "resposta": "Sim. A Faetec oferece Técnico em Logística Internacional e Comércio Exterior."
    },
    {
        "keywords": ["curso técnico transporte ferroviário", "operações ferroviárias"],
        "resposta": "Sim. Há cursos como Técnico em Transporte Ferroviário e Operações Ferroviárias."
    },
    {
        "keywords": ["curso técnico transporte aéreo", "operações aéreas"],
        "resposta": "Sim. A Faetec oferece Técnico em Transporte Aéreo e Operações Aéreas."
    },
    {
        "keywords": ["curso técnico transporte marítimo", "operações marítimas"],
        "resposta": "Sim. Há cursos como Técnico em Transporte Marítimo e Operações Marítimas."
    },
    {
        "keywords": ["curso técnico transporte fluvial", "operações fluviais"],
        "resposta": "Sim. A Faetec oferece Técnico em Transporte Fluvial e Operações Fluviais."
    },
    {
        "keywords": ["curso técnico transporte rodoviário internacional", "operações rodoviárias internacionais"],
        "resposta": "Sim. Há cursos como Técnico em Transporte Rodoviário Internacional e Operações Rodoviárias Internacionais."
    },
    {
        "keywords": ["pré-requisitos cursos técnicos", "quem pode fazer técnico"],
        "resposta": "Para cursos subsequentes é necessário ter concluído o Ensino Médio. Para concomitante externa, é preciso estar matriculado no 2º ano do Ensino Médio."
    },
    {
        "keywords": ["inscrição cursos técnicos", "como se inscrever técnico"],
        "resposta": "As inscrições para cursos técnicos são realizadas online pelo site oficial: www.faetec.rj.gov.br."
    },
    {
        "keywords": ["quais unidades", "unidades faetec", "escolas faetec"],
        "resposta": "A Faetec possui diversas unidades distribuídas pelo estado do Rio de Janeiro, incluindo escolas técnicas, ISEPs, CVTs e unidades de qualificação profissional."
    },
    {
        "keywords": ["quantas unidades", "número de unidades"],
        "resposta": "A Faetec conta com mais de 120 unidades em todo o estado do Rio de Janeiro."
    },
    {
        "keywords": ["diretorias regionais", "divisão por regiões"],
        "resposta": "As unidades da Faetec estão organizadas em Diretorias Regionais que fazem a gestão administrativa e pedagógica de acordo com cada região."
    },
    {
        "keywords": ["qual a sede", "onde fica a sede da faetec"],
        "resposta": "A sede administrativa da Faetec está localizada no Rio de Janeiro, na Rua Clarimundo de Melo, 847 – Quintino Bocaiúva."
    },
    {
        "keywords": ["responsável unidade", "quem administra a unidade"],
        "resposta": "Cada unidade da Faetec possui direção própria, subordinada às Diretorias Regionais e à presidência da instituição."
    },
    {
        "keywords": ["contato unidade", "telefone unidade", "como falar com a unidade"],
        "resposta": "Os contatos de cada unidade (telefone, e-mail, endereço) estão disponíveis no site oficial da Faetec: www.faetec.rj.gov.br."
    },
    {
        "keywords": ["transferência de unidade", "mudar de unidade"],
        "resposta": "Não é permitido transferir matrícula entre unidades. O aluno deve participar de novo processo seletivo."
    },
    {
        "keywords": ["pré-requisitos técnico", "quem pode fazer técnico", "requisitos curso técnico"],
        "resposta": "Para cursos técnicos subsequentes é necessário ter concluído o Ensino Médio. Já para concomitante externa, é preciso estar matriculado no 2º ano do Ensino Médio."
    },
    {
        "keywords": ["como se inscrever técnico", "inscrição curso técnico", "fazer inscrição técnico"],
        "resposta": "As inscrições para os cursos técnicos da Faetec são realizadas online pelo site oficial: www.faetec.rj.gov.br."
    },
]


        if "conversa" not in st.session_state:
            st.session_state.conversa = []

        pergunta_usuario = st.text_input("Digite sua mensagem:")

        if st.button("Enviar"):
            if pergunta_usuario:
                pergunta_lower = pergunta_usuario.lower()
                resposta_bot = "Desculpe, não entendi sua pergunta 😅"

                for item in base_conhecimento:
                    if any(k in pergunta_lower for k in item["keywords"]):
                        resposta_bot = item["resposta"]
                        break

                st.session_state.conversa.append(("Você 😁", pergunta_usuario))
                st.session_state.conversa.append(("FaeThink 🤖", resposta_bot))

        # Links das fotos de perfil
        foto_usuario = "https://i.imgur.com/5FAZMMX.png"  # 👉 troque pelo link da foto do usuário
        foto_bot = "https://i.imgur.com/zg6qpgy.png"      # 👉 troque pelo link da foto do bot

        # Exibe o histórico no estilo WhatsApp fofinho com foto de perfil
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

        if st.button("⬅️ Voltar"):
            st.session_state.abrir_chat = False
            st.session_state.conversa = []

# -------- SOBRE O PROJETO --------
elif menu == "Sobre o Projeto":
    st.markdown("## 🎓 Bem vindo ao FaeThink")

    col1, col2 = st.columns([2, 1])  # texto ocupa mais espaço, imagem menos

    with col1:  # Texto à esquerda
        st.write("""
        A plataforma criada para te ajudar e responder suas duvidas sobre a escola.

        No Faethink, você encontra tudo o que precisa para além de responder suas duvidas, também socializar.

        Nosso objetivo é facilitar a vida dos estudantes com tecnologia acessível 🚀.
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