import os
import shutil
import time

# --- CONFIGURAÇÃO ---
# Onde os arquivos caem quando você clica em baixar
origem = os.path.expanduser("~/Downloads") 

# Onde o Minecraft guarda os mods (Caminho padrão do CurseForge/Minecraft)
destino = os.path.expanduser("~/AppData/Roaming/.minecraft/mods")

print("🤖 SENTINELA ATIVO: Vigiando downloads...")

while True:
    for arquivo in os.listdir(origem):
        # Se o arquivo for um MOD de Minecraft que a IA criou
        if arquivo.endswith(".jar") and "IA" in arquivo:
            caminho_completo = os.path.join(origem, arquivo)
            
            print(f"📦 Detectado: {arquivo}! Movendo para a pasta mods...")
            try:
                shutil.move(caminho_completo, os.path.join(destino, arquivo))
                print("✅ Mod instalado com sucesso automaticamente!")
            except Exception as e:
                print(f"❌ Erro ao mover: {e}")
                
    time.sleep(2) # Espera 2 segundos e olha de novo
