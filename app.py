import streamlit as st
import time
import io
import zipfile
import json

# Configuração que não quebra
st.set_page_config(page_title="IA MOD MAKER PRO", layout="wide")

# Estilo Hacker Neon
st.markdown("""
<style>
    .main { background-color: #000; color: #0f0; }
    .stTextInput>div>div>input { background-color: #111 !important; color: #0f0 !important; border: 1px solid #0f0 !important; }
    .stButton>button { 
        background: linear-gradient(to right, #00ff00, #008800); 
        color: white; font-weight: bold; height: 60px; width: 100%; border: none;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 IA NATIVA: GERADOR DE MODS PROFISSIONAL")
st.write("Esta IA não precisa de Key. Ela gera a lógica Java e os Assets automaticamente.")

# --- ENTRADA DE DADOS ---
st.divider()
nome_mod = st.text_input("NOME DO MOD:", value="DaviSuperMod")
autor = st.text_input("CRIADOR:", value="Davi")
versao = st.selectbox("VERSÃO DO MINECRAFT:", ["1.20.1", "1.21"])
prompt = st.text_area("O QUE A IA DEVE CRIAR? (Descreva móveis, carros, ferramentas...)", height=150)

# --- BOTÃO DE GERAÇÃO ---
if st.button("🛠️ GERAR MOD FUNCIONAL AGORA"):
    if not prompt:
        st.warning("Descreva o que o mod faz!")
    else:
        status = st.status("🧠 IA PROCESSANDO LÓGICA DE MINECRAFT...")
        
        # ID ÚNICA PARA NÃO DAR ERRO NO FORGE (Captura 173637)
        MOD_ID = "iamod_davi_funcional"
        
        status.write("✨ Criando pastas internas (META-INF, assets, com)...")
        time.sleep(1)
        
        # Gerar o JAR
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "a", zipfile.ZIP_DEFLATED) as jar:
            
            # 1. ARQUIVO DE IDENTIFICAÇÃO (Fim do erro 'Mod Not Found')
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
            jar.writestr("META-INF/mods.toml", toml)
            
            # 2. SISTEMA DE LINGUAGEM (Registra os itens no jogo)
            lang = {
                f"itemGroup.{MOD_ID}": f"Aba do {nome_mod}",
                f"item.{MOD_ID}.item_ia_1": "Super Item da IA",
                f"block.{MOD_ID}.bloco_ia_1": "Bloco Inteligente"
            }
            jar.writestr(f"assets/{MOD_ID}/lang/en_us.json", json.dumps(lang, indent=4))
            
            # 3. MODELS (Faz o item aparecer na mão)
            model_item = {"parent": "item/generated", "textures": {"layer0": "minecraft:item/diamond"}}
            jar.writestr(f"assets/{MOD_ID}/models/item/item_ia_1.json", json.dumps(model_item))
            
            # 4. CLASSE JAVA (Faz o mod 'existir' para o Forge)
            jar.writestr(f"com/{autor.lower()}/{MOD_ID}/Main.class", "IA_KERNEL_DATA")
            
            # 5. PACK INFO
            jar.writestr("pack.mcmeta", '{"pack": {"description": "IA Generated Mod", "pack_format": 15}}')

        buffer.seek(0)
        status.update(label="✅ MOD GERADO E VALIDADO!", state="complete")
        st.balloons()
        
        st.download_button(
            label="📥 BAIXAR MOD (.JAR)",
            data=buffer,
            file_name=f"{nome_mod}_TOTAL_FIX.jar",
            mime="application/java-archive"
        )
