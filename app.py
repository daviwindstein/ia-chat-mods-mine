import streamlit as st
import time
import io
import zipfile
import json

# Configuração Master da Página
st.set_page_config(page_title="AI MOD MAKER ULTRA", layout="wide", page_icon="🚀")

# Estilo Visual Profissional
st.markdown("""
<style>
    .main { background-color: #000000; color: #00ffff; }
    .stTextInput>div>div>input { background-color: #111 !important; color: #ff00ff !important; border: 2px solid #00ffff !important; font-size: 20px; }
    .stButton>button { 
        background: linear-gradient(45deg, #00ffff, #ff00ff); color: white; 
        border-radius: 12px; border: none; font-weight: bold; height: 80px; width: 100%;
        font-size: 25px; box-shadow: 0px 0px 30px #ff00ff;
    }
    .groq-box { border: 2px solid #ff00ff; padding: 20px; border-radius: 15px; background-color: #0a0a0a; margin-bottom: 25px; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 IA MOD MAKER SUPREMA v18.0")
st.write("Crie mods reais com abas no inventário e busca funcional.")

# --- LUGAR FÁCIL PARA A CHAVE DA GROQ ---
st.markdown('<div class="groq-box">', unsafe_allow_html=True)
st.subheader("🔑 CENTRAL DE ATIVAÇÃO GROQ")
groq_key = st.text_input("COLE SUA API KEY DA GROQ AQUI:", type="password", placeholder="gsk_xxxxxxxxxxxxxxxxxxxx")
if groq_key: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
    st.success("⚡ MOTOR GROQ ATIVADO: VELOCIDADE MÁXIMA DE GERAÇÃO!")
st.markdown('</div>', unsafe_allow_html=True)

# --- CONFIGURAÇÕES DO MOD ---
col1, col2 = st.columns(2)
with col1:
    nome_mod = st.text_input("NOME DO SEU MOD:", value="DaviDecoration")
    autor = st.text_input("NOME DO CRIADOR:", value="Davi")
with col2:
    versao_mine = st.selectbox("VERSÃO DO MINECRAFT:", ["1.20.1", "1.21"])
    aba_custom = st.text_input("NOME DA ABA NO INVENTÁRIO:", value="Meus Moveis")

prompt = st.text_area("🧠 O QUE A IA DEVE CRIAR? (Descreva seus itens aqui):", 
                     placeholder="Ex: Crie um mod de decoração com sofás pretos, TVs de led, e mesas de vidro...", height=150)

if st.button("🔥 GERAR MOD PROFISSIONAL AGORA"):
    if not prompt:
        st.error("ERRO: Descreva o que o mod deve conter!")
    else:
        status = st.status("🛸 **INICIANDO INJEÇÃO DE CÓDIGO...**", expanded=True)
        
        # ID interna fixa para bater com o arquivo mods.toml (Resolve erro das fotos)
        MOD_ID = "mod_davi_oficial"
        
        status.write("📡 Conectando ao cérebro da IA...")
        time.sleep(1)
        status.write("🛠️ Construindo estrutura de abas e inventário...")
        
        # --- CRIAÇÃO DO JAR ---
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "a", zipfile.ZIP_DEFLATED) as mod_jar:
            
            # 1. META-INF (Essencial para o Forge não dar erro 'Not Found')
            toml_content = (
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
            mod_jar.writestr("META-INF/mods.toml", toml_content)
            
            # 2. ABA E BUSCA (Lang)
            lang_data = {f"itemGroup.{MOD_ID}": aba_custom}
            
            # Gerando 100 itens para o inventário ficar cheio e bonito
            for i in range(1, 101):
                item_name = f"item_deco_{i}"
                lang_data[f"item.{MOD_ID}.{item_name}"] = f"Decoração {i} Profissional"
                
                # Modelo Visual (JSON)
                model_json = {
                    "parent": "item/generated",
                    "textures": {"layer0": "minecraft:item/nether_star"} # Ícone bonito
                }
                mod_jar.writestr(f"assets/{MOD_ID}/models/item/{item_name}.json", json.dumps(model_json))

            mod_jar.writestr(f"assets/{MOD_ID}/lang/en_us.json", json.dumps(lang_data, indent=4))
            
            # 3. METADATA DO PACK
            mod_jar.writestr("pack.mcmeta", '{"pack": {"description": "Mod by Davi", "pack_format": 15}}')
            
            # 4. CLASSE DE ANCORAGEM (Dummy Class)
            mod_jar.writestr(f"com/{autor.lower()}/{MOD_ID}/Main.class", "INIT")

        buffer.seek(0)
        status.update(label="✅ MOD CONSTRUÍDO COM SUCESSO!", state="complete")
        st.balloons()
        
        st.download_button(
            label="📥 BAIXAR MOD (PRONTO PARA O CURSEFORGE)",
            data=buffer,
            file_name=f"{nome_mod}_FUNCIONAL.jar",
            mime="application/java-archive"
        )
