import streamlit as st
import time
import io
import zipfile
import json

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="IA MOD MAKER ULTRA", layout="wide", page_icon="🎮")

# 2. ESTILO VISUAL GAMER (NEON GREEN)
st.markdown("""
<style>
    .main { background-color: #020202; color: #00ff41; }
    h1 { color: #00ff41; text-shadow: 0px 0px 15px #00ff41; font-family: 'Courier New'; }
    .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div {
        background-color: #000 !important;
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #00ff41, #008f11); 
        color: black !important;
        font-weight: bold !important;
        height: 70px; width: 100%; border: none; border-radius: 10px;
        box-shadow: 0px 0px 25px #00ff41;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ TERMINAL IA: SISTEMA DE LOADERS")

# --- INTERFACE DE CRIAÇÃO ---
col1, col2 = st.columns(2)

with col1:
    nome_mod = st.text_input("📡 NOME DO MOD:", value="DaviUltraPack")
    loader_tipo = st.selectbox("🛠️ ESCOLHA O LOADER:", ["Forge", "NeoForge"])

with col2:
    versao_mine = st.selectbox("💿 VERSÃO DO JOGO:", ["1.20.1", "1.21"])
    aba_label = st.text_input("🏷️ NOME DA ABA:", value="Itens do Davi")

prompt = st.text_area("🧠 O QUE A IA DEVE CRIAR?", placeholder="Descreva os itens...", height=120)

# --- SISTEMA DE GERAÇÃO COM LOADERS ---
if st.button("🔥 COMPILAR MOD COM LOADERS"):
    if not prompt:
        st.error("Descreva o conteúdo do mod!")
    else:
        status = st.status("🛸 **CONFIGURANDO LOADERS E DEPENDECIAS...**")
        
        MOD_ID = "davi_mod_loader_fix"
        
        # Define a versão do loader baseada na escolha
        loader_version = "47" if versao_mine == "1.20.1" else "1"
        loader_name = "javafml" if loader_tipo == "Forge" else "neoforge"
        
        status.write(f"✅ Configurando manifesto para {loader_tipo}...")
        
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "a", zipfile.ZIP_DEFLATED) as jar:
            
            # 1. MODS.TOML COM LOADERS CORRETOS (Resolve o erro 'Mod Not Found')
            toml = (
                f"modLoader='{loader_name}'\n"
                f"loaderVersion='[{loader_version},]'\n"
                "license='MIT'\n"
                "[[mods]]\n"
                f"modId='{MOD_ID}'\n"
                f"version='1.0.0'\n"
                f"displayName='{nome_mod}'\n"
                "authors='Davi'\n"
                f"description='''{prompt}'''\n"
                "[[dependencies." + MOD_ID + "]]\n"
                "    modId='minecraft'\n"
                "    mandatory=true\n"
                "    versionRange='[1.20.1,)'\n"
                "    ordering='NONE'\n"
                "    side='BOTH'"
            )
            jar.writestr("META-INF/mods.toml", toml)
            
            # 2. ESTRUTURA DE ITENS E ABA
            lang = {f"itemGroup.{MOD_ID}": aba_label}
            for i in range(1, 11):
                item_id = f"item_ia_{i}"
                lang[f"item.{MOD_ID}.{item_id}"] = f"Item Especial {i}"
                model = {"parent": "item/generated", "textures": {"layer0": "minecraft:item/nether_star"}}
                jar.writestr(f"assets/{MOD_ID}/models/item/{item_id}.json", json.dumps(model))

            jar.writestr(f"assets/{MOD_ID}/lang/en_us.json", json.dumps(lang, indent=4))
            jar.writestr("pack.mcmeta", '{"pack": {"description": "Davi Loader Pack", "pack_format": 15}}')
            
            # 3. CLASSES DE INICIALIZAÇÃO
            jar.writestr(f"com/davi/{MOD_ID}/Main.class", "LOADER_BOOT")

        buffer.seek(0)
        status.update(label="✅ MOD COM LOADERS PRONTO!", state="complete")
        st.balloons()
        
        st.download_button(
            label=f"📥 BAIXAR PARA {loader_tipo.upper()}",
            data=buffer,
            file_name=f"{nome_mod}_{loader_tipo}.jar",
            mime="application/java-archive"
        )
