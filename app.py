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
st.markdown("<h1 class='titulo-gradient'>FaeThink 🎓</h1>", unsafe_allow_html=True)
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
            {"keywords": ["estágio", "trabalho"], "resposta": "Você pode procurar estágio no setor de carreiras da escola, na sala ***."},
            {"keywords": ["boletim", "notas"], "resposta": "O boletim pode ser pego na secretaria após cada trimestre."},
            {"keywords": ["horário", "aulas"], "resposta": "O horário completo das aulas está disponível no mural da escola."},
            {"keywords": ["secretaria", "contato"], "resposta": "Você pode falar com a secretaria pessoalmente, assim que entrar na escola à esquerda."}
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
    st.markdown("## ℹ️ Sobre o FaeThink")
    st.write("""
    O **FaeThink 🎓** é um projeto criado para ajudar alunos da Faetec 
    a encontrarem informações rápidas sobre:
    - Estágios
    - Boletim
    - Horários
    - Secretaria

    Nosso objetivo é facilitar a vida dos estudantes com tecnologia acessível 🚀.
    """)

# -------- PROJETOS DA ESCOLA --------
elif menu == "Projetos da Escola":
    st.markdown("## 📢 Projetos da Escola")
    st.write("Aqui estão alguns projetos em andamento na nossa escola:")

    # Projeto 1
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/N2DeKr9.png", width=200)
    with col2:
        st.markdown("### Jornal A Voz do Republica 🤖")
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