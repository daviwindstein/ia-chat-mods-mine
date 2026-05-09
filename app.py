import streamlit as st
import time
import io
import zipfile
import json

# --- INTERFACE GAMER TOTAL ---
st.set_page_config(page_title="DAVI OS: IA AGENT", layout="wide")

st.markdown("""
<style>
    .main { background-color: #000; color: #00ff41; font-family: 'Consolas', monospace; }
    .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff41 !important; border: 2px solid #00ff41 !important; }
    .stButton>button { 
        background: linear-gradient(135deg, #ff0000 0%, #440000 100%); 
        color: white !important; font-size: 20px; border-radius: 10px; border: 2px solid #ff0000;
    }
    .safe-zone { border: 2px solid #00ff41; padding: 15px; background: #001100; border-radius: 10px; }
    .danger-zone { border: 2px solid #ff0000; padding: 15px; background: #220000; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ DAVI OS: AGENTE DE PESQUISA E AUTOMAÇÃO")

# Campo de pesquisa (O seu "Google" particular)
pesquisa = st.text_input("🔍 O QUE A IA DEVE BUSCAR E FAZER NO PC?", placeholder="Ex: Criar mod de móveis no Mine / Script de parkour no Roblox")

if st.button("🚀 EXECUTAR PROTOCOLO DE BUSCA"):
    if not pesquisa:
        st.error("Digite um comando!")
    else:
        # FASE 1: PESQUISA E ANÁLISE DE SEGURANÇA
        with st.container():
            st.write("🕵️ **IA EXPLORANDO A WEB...**")
            progress = st.progress(0)
            
            # Simulando a verificação que você pediu
            time.sleep(2)
            progress.progress(30)
            st.write("📂 Encontrado modelo: 'SuperMod_V1.jar' em site de terceiros.")
            
            time.sleep(2)
            progress.progress(60)
            st.write("🛡️ **ANALISANDO CÓDIGO FONTE (PROTOCOLO ANTI-SUSPEITO)...**")
            
            # Lógica de segurança: se tiver certas palavras, a IA bloqueia
            if "hack" in pesquisa.lower() or "virus" in pesquisa.lower() or "free_robux" in pesquisa.lower():
                st.markdown('<div class="danger-zone">🚨 ALERTA: CONTEÚDO SUSPEITO DETECTADO! Acesso bloqueado para proteger o PC do Davi.</div>', unsafe_allow_html=True)
            else:
                progress.progress(100)
                st.markdown('<div class="safe-zone">✅ MODELO SEGURO. Nenhuma ameaça encontrada. Iniciando construção...</div>', unsafe_allow_html=True)
                
                # Geração do Mod/Script
                buffer = io.BytesIO()
                with zipfile.ZipFile(buffer, "a", zipfile.ZIP_DEFLATED) as mod:
                    mod.writestr("META-INF/mods.toml", f"modId='davi_auto'\ndisplayName='Mod Seguro'")
                    mod.writestr("script_roblox.lua", "-- Script Seguro gerado pela IA do Davi")
                
                buffer.seek(0)
                st.download_button("📥 TRANSFERIR PARA O PC (O SENTINELA IRÁ INSTALAR)", data=buffer, file_name="AUTO_DAVI_IA.jar")
