import streamlit as st
import io
import zipfile
import json

st.set_page_config(page_title="IA COM AUTO-INSTALAÇÃO", layout="wide")

# Interface Neon
st.markdown("""
<style>
    .main { background-color: #000; color: #00ff41; font-family: 'Consolas', monospace; }
    .stButton>button { 
        background: #00ff41; color: black; font-weight: bold;
        border-radius: 20px; height: 80px; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 IA GERADORA + PONTE AUTOMÁTICA")

comando = st.text_area("O que a IA deve fazer?", "Crie um mod de ferramentas de Esmeralda")

if st.button("🚀 GERAR E ENVIAR PARA O SENTINELA"):
    # Geração do ZIP/JAR
    MOD_ID = "mod_ia_automatico"
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "a", zipfile.ZIP_DEFLATED) as jar:
        # Estrutura mínima para não dar erro no Minecraft
        toml = f"modLoader='javafml'\nloaderVersion='[1,]'\nlicense='MIT'\n[[mods]]\nmodId='{MOD_ID}'\nversion='1.0'\ndisplayName='Mod Automático'"
        jar.writestr("META-INF/mods.toml", toml)
        jar.writestr("pack.mcmeta", '{"pack": {"description": "IA", "pack_format": 15}}')
    
    buffer.seek(0)
    st.success("✅ Mod gerado! Clique abaixo para o Sentinela capturar.")
    
    # IMPORTANTE: O nome tem que ter "IA" para o sentinela.py funcionar
    st.download_button("📥 CLIQUE AQUI (O RESTO É AUTOMÁTICO)", data=buffer, file_name="MOD_IA_DAVI.jar")
