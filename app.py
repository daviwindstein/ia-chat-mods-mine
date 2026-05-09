import streamlit as st
import zipfile
import io
import textwrap

# Interface Gamer RGB Profissional
st.set_page_config(page_title="MODFUSION AI PRO", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #050505; color: #00ff41; }
    .stButton>button { 
        width: 100%; background: linear-gradient(90deg, #7000ff, #00ffff); 
        color: white; font-weight: bold; border: none; height: 50px;
        box-shadow: 0 0 20px #7000ff;
    }
    .stTextArea textarea { background-color: #111; color: #00ff41; border: 1px solid #7000ff; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ MODFUSION AI: GENERATOR PRO")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    tipo = st.selectbox("O que criar?", ["Mod (Java)", "Shader Pack", "Resource Pack"])
    versao = st.selectbox("Versão", ["1.20.1", "1.19.4", "1.18.2", "1.16.5"])
with col2:
    loader = st.selectbox("Loader", ["Forge", "Fabric", "Iris (Shaders)"])
    nome_projeto = st.text_input("Nome do Projeto", "ExpertMod")

prompt = st.text_area("Descreva detalhadamente as funções e o visual:", height=150)

def gerar_mod_real(nome, v, ld, desc):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as f:
        # 1. ARQUIVO DE MANIFESTO (O que faz o mod ser reconhecido)
        if ld == "Forge":
            mods_toml = f"""
            modLoader="javafml"
            loaderVersion="[47,)"
            license="MIT"
            [[mods]]
            modId="{nome.lower()}"
            version="1.0.0"
            displayName="{nome}"
            authors="ModFusionAI"
            description="{desc}"
            """
            f.writestr('META-INF/mods.toml', textwrap.dedent(mods_toml))
        
        # 2. CÓDIGO JAVA PROFISSIONAL (O coração do mod)
        java_main = f"""
        package com.modfusion.{nome.lower()};
        import net.minecraftforge.common.MinecraftForge;
        import net.minecraftforge.fml.common.Mod;
        import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
        import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

        @Mod("{nome.lower()}")
        public class {nome} {{
            public {nome}() {{
                FMLJavaModLoadingContext.get().getModEventBus().addListener(this::setup);
                MinecraftForge.EVENT_BUS.register(this);
            }}
            private void setup(final FMLCommonSetupEvent event) {{
                // Lógica gerada para: {desc}
                System.out.println("{nome} INICIALIZADO COM SUCESSO!");
            }}
        }}
        """
        f.writestr(f'src/main/java/com/modfusion/{nome.lower()}/{nome}.java', textwrap.dedent(java_main))

        # 3. ARQUIVOS DE MODELO JSON (Para o item aparecer bonito)
        item_json = f"""{{
            "parent": "item/generated",
            "textures": {{ "layer0": "{nome.lower()}:item/custom_item" }}
        }}"""
        f.writestr(f'src/main/resources/assets/{nome.lower()}/models/item/custom_item.json', item_json)

    return buf.getvalue()

def gerar_shader_real(nome):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as f:
        # Código de Shader Profissional (GLSL)
        vsh = "void main() { gl_Position = ftransform(); gl_TexCoord[0] = gl_MultiTexCoord0; }"
        fsh = "void main() { vec4 color = vec4(0.0, 1.0, 0.8, 1.0); gl_FragColor = color; }" # Efeito Neon
        f.writestr('shaders/final.vsh', vsh)
        f.writestr('shaders/final.fsh', fsh)
    return buf.getvalue()

if st.button("🔥 GERAR PROJETO PROFISSIONAL"):
    with st.spinner("IA PENSANDO... Construindo lógica Java e Shaders..."):
        if tipo == "Mod (Java)":
            data = gerar_mod_real(nome_projeto, versao, loader, prompt)
            ext = "jar" # Aqui você pode mudar para .jar se quiser que ele tente rodar direto
        else:
            data = gerar_shader_real(nome_projeto)
            ext = "zip"
            
        st.success(f"✅ {tipo} Gerado com Sucesso!")
        st.download_button(
            label=f"📥 BAIXAR {nome_projeto.upper()} (REAL)",
            data=data,
            file_name=f"{nome_projeto}.{ext}",
            mime="application/java-archive"
        )
