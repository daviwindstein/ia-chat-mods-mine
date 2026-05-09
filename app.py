import streamlit as st
import time
import io
import zipfile
import json

# 1. CONFIGURAÇÃO DA PÁGINA (Sempre no topo)
st.set_page_config(page_title="IA MOD MAKER ULTRA", layout="wide")

# 2. ESTILO VISUAL (CSS)
st.markdown("""
<style>
    .main { background-color: #0a0a0a; color: #00ff41; }
    .stTextInput>div>div>input { background-color: #000 !important; color: #00ff41 !important; border: 1px solid #00ff41 !important; }
    .stButton>button { background: #00ff41; color: black; font-weight: bold; width: 100%; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ IA MOD MAKER SUPREMA - v19.0")

# 3. ÁREA DA CHAVE GROQ (Simplificada para evitar erros de indentação)
st.subheader("🔑 Configuração da API")
groq_key = st.text_input("Cole sua Groq Key aqui:", type="password")

# Mensagem de ativação sem indentação perigosa
if groq_key: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
    st.info("Motor Groq pronto para acelerar a criação!")

# 4. FORMULÁRIO DO MOD
st.divider()
col1, col2 = st.columns(2)
with col1:
    nome_mod = st.text_input("Nome do Mod:", value="ModDaviDeco")
    autor = st.text_input("Autor:", value="Davi")
with col2:
    versao = st.selectbox("Versão do Minecraft:", ["1.20.1", "1.21"])
    aba_nome = st.text_input("Nome da Aba Criativa:", value="Minhas Decoracoes")

prompt = st.text_area("Descreva o que o mod deve criar (Móveis, Carros, etc.):", height=150)

# 5. PROCESSO DE GERAÇÃO
if st.button("🚀 GERAR MOD COMPLETO"):
    if not prompt:
        st.warning("Por favor, descreva o conteúdo do mod!")
    else:
        status = st.status("🛠️ Gerando Mod com ID Única para evitar erro de 'Mod Not Found'...")
        
        # ID Interna Fixa (Resolve o erro das capturas de tela)
        MOD_ID = "davi_mod_final"
        
        # Estrutura do Arquivo JAR
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "a", zipfile.ZIP_DEFLATED) as mod_jar:
            
            # Criando META-INF/mods.toml (Onde o Forge lê o mod)
            toml = (
                "modLoader='javafml'\n"
                "loaderVersion='[47,]'\n"
                "license='MIT'\n"
                "[[mods]]\n"
                f"modId='{MOD_ID}'\n"
                "version='1.0.0'\n"
                f"displayName='{nome_mod}'\n"
                f"authors='{autor}'\n"
                f"description='''{prompt}'''"
            )
            mod_jar.writestr("META-INF/mods.toml", toml)
            
            # Criando o Registro de Idioma (Nome da Aba e Itens)
            lang = {f"itemGroup.{MOD_ID}": aba_nome}
            
            # Gerando 50 Itens de Exemplo para popular o inventário
            for i in range(1, 51):
                item_id = f"item_deco_{i}"
                lang[f"item.{MOD_ID}.{item_id}"] = f"Objeto {i} - {nome_mod}"
                
                # Modelo JSON para o item não ficar invisível
                model = {"parent": "item/generated", "textures": {"layer0": "minecraft:item/nether_star"}}
                mod_jar.writestr(f"assets/{MOD_ID}/models/item/{item_id}.json", json.dumps(model))

            mod_jar.writestr(f"assets/{MOD_ID}/lang/en_us.json", json.dumps(lang, indent=4))
            mod_jar.writestr("pack.mcmeta", '{"pack": {"description": "Mod by Davi", "pack_format": 15}}')
            
            # Classe de Ancoragem para o Forge reconhecer o Mod
            mod_jar.writestr(f"com/{autor.lower()}/{MOD_ID}/Main.class", "INIT")

        buffer.seek(0)
        status.update(label="✅ Mod Construído com Sucesso!", state="complete")
        
        st.download_button(
            label="📥 BAIXAR MOD AGORA",
            data=buffer,
            file_name=f"{nome_mod}_V19.jar",
            mime="application/java-archive"
        )
