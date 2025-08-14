import streamlit as st
import webbrowser

# --- CONFIGURAÇÃO INICIAL DA PÁGINA ---
st.set_page_config(
    page_title="z1p0l0ck@portfolio:~$",
    page_icon="🟢",
    layout="centered" # Voltamos para 'centered' para melhor foco no conteúdo
)

# --- FUNÇÃO PARA CARREGAR O ARQUIVO CSS EXTERNO ---
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Arquivo de estilo '{file_name}' não encontrado.")

load_css('style.css')

# O código da animação Matrix foi REMOVIDO daqui.

# --- DEFINIÇÃO DAS ABAS (NAVEGAÇÃO) ---
tab1, tab2, tab3 = st.tabs(["./inicio.sh", "ls -a projetos", "send-mail"])

with tab1:
    # Aplicando a classe 'glitch-effect' e o atributo 'data-text'
    command_text = "z1p0l0ck@localhost:~$ ./apresentar-servicos.sh"
    st.markdown(f"<h3 class='glitch-effect' data-text='{command_text}'>{command_text}</h3>", unsafe_allow_html=True)
    
    # Aplicando a classe 'typing-effect'
    st.markdown("<h1 class='typing-effect' style='color:#00FF00; font-family:monospace;'>Vamos Construir Juntos.</h1>", unsafe_allow_html=True)
    
    st.write("Crio soluções web ultraleves e seguras, desenvolvidas inteiramente em ambiente Linux (Termux). Performance máxima, burocracia zero.")
    st.write("---")
    
    command_text_2 = "$ mostrar --filosofia"
    st.markdown(f"<h3 class='glitch-effect' data-text='{command_text_2}'>{command_text_2}</h3>", unsafe_allow_html=True)
    
    st.markdown("#### > AGILIDADE")
    st.write("Prototipação e implementação rápidas, ideal para projetos de site único, landing pages e APIs.")
    st.markdown("#### > VERSATILIDADE")
    st.write("Do backend com Python ao frontend interativo com Streamlit, tudo direto do Termux.")
    st.markdown("#### > PROTEÇÃO")
    st.write("Desenvolvimento focado em segurança, minimizando superfícies de ataque.")
    st.markdown("#### > CUSTO-BENEFÍCIO")
    st.write("Soluções viáveis e de baixo custo, eliminando gastos com infraestruturas complexas.")

with tab2:
    command_text_3 = "z1p0l0ck@localhost:~/projetos$ ls -la"
    st.markdown(f"<h3 class='glitch-effect' data-text='{command_text_3}'>{command_text_3}</h3>", unsafe_allow_html=True)
    
    
    st.markdown("#### [ Projeto Alpha ] - Bot de Análise de Cripto")
    st.write(
        "Um bot para Telegram construído em Python que monitora o mercado de criptomoedas em tempo real, "
        "utilizando APIs da Binance e notificando sobre oportunidades de compra/venda."
    )
    
    link_alpha = "https://github.com/SEU_USUARIO/SEU_PROJETO_1"
    st.markdown(f'<div class="button-link"><a href="{link_alpha}" target="_blank">ver_codigo_fonte_alpha</a></div>', unsafe_allow_html=True)
    st.write("---")


    st.markdown("#### [ Projeto Beta ] - Dashboard Interativo")
    st.write(
        "Dashboard de vendas criado com Streamlit e Pandas. Permite a visualização de dados de forma "
        "interativa, com filtros dinâmicos e gráficos gerados na hora. Hospedado diretamente do Termux."
    )
    
    link_beta = "https://github.com/zuckalez0-oss/dashboard-vendas"
    st.markdown(f'<div class="button-link"><a href="{link_beta}" target="_blank">ver_codigo_fonte_dashboard</a></div>', unsafe_allow_html=True)
    st.write("---")
    
with tab3:
    command_text_4 = "z1p0l0ck@localhost:~$ mail -s 'Nova Oportunidade'"
    st.markdown(f"<h3 class='glitch-effect' data-text='{command_text_4}'>{command_text_4}</h3>", unsafe_allow_html=True)
    
    st.write("Payload de contato. Preencha os campos abaixo para iniciar uma conexão direta.")
    contact_form = """
    <form action="https://formsubmit.co/matheus.z1p0l0ck@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Assinatura (seu nome)" required>
        <input type="email" name="email" placeholder="Endereço de resposta (seu email)" required>
        <textarea name="message" placeholder="Corpo da mensagem..." required></textarea>
        <button type="submit">--send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

# --- RODAPÉ ---
st.write("---")
footer_text = "[ established_connection ]"
st.markdown(f"<h3 style='text-align: center; font-family:monospace;' class='glitch-effect' data-text='{footer_text}'>{footer_text}</h3>", unsafe_allow_html=True)

social_icons_html = """
<div class="social-icons">
    <a href="https://www.linkedin.com/in/matheus-ribeiro-bbb894237?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank" title="LinkedIn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
    <a href="https://wa.me/17996261525" target="_blank" title="WhatsApp"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.894 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.451-4.437-9.887-9.888-9.888-5.451 0-9.887 4.436-9.888 9.888.001 2.228.651 4.315 1.919 6.066l-1.442 5.254 5.378-1.401z"/></svg></a>
    <a href="https://www.instagram.com/z1p0l0ck/?utm_source=qr&r=nametag" target="_blank" title="Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.85s-.011 3.584-.069 4.85c-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07s-3.584-.012-4.85-.07c-3.252-.148-4.771-1.691-4.919-4.919-.058-1.265-.069-1.645-.069-4.85s.011-3.584.069-4.85c.149-3.225 1.664-4.771 4.919-4.919 1.266-.057 1.644-.069 4.85-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948s.014 3.667.072 4.947c.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072s3.667-.014 4.947-.072c4.358-.2 6.78-2.618 6.98-6.98.059-1.281.073-1.689.073-4.948s-.014-3.667-.072-4.947c-.2-4.358-2.618-6.78-6.98-6.98-1.281-.059-1.689-.072-4.948-.072zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4s1.791-4 4-4 4 1.79 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44 1.441-.645 1.441-1.44-.645-1.44-1.441-1.44z"/></svg></a>
    <a href="https://github.com/zuckalez0-oss" target="_blank" title="GitHub"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.91 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>
"""
st.markdown(social_icons_html, unsafe_allow_html=True)
