import pyautogui
import os
import time
import shutil

# Configurações de caminhos
DOWNLOADS = os.path.expanduser("~/Downloads")
MINE_MODS = os.path.expanduser("~/AppData/Roaming/.minecraft/mods")

def instalar_e_testar():
    for arquivo in os.listdir(DOWNLOADS):
        if arquivo.startswith("AUTO_DAVI_IA") and arquivo.endswith(".jar"):
            print(f"🤖 IA DETECTOU NOVO MOD: {arquivo}")
            
            # 1. MOVE O ARQUIVO SOZINHA
            shutil.move(os.path.join(DOWNLOADS, arquivo), os.path.join(MINE_MODS, arquivo))
            print("🚚 Mod movido para a pasta do Minecraft!")

            # 2. ABRE O JOGO (Simulação de clique)
            # Aqui você configuraria a posição do botão do seu Minecraft
            print("🎮 Abrindo Minecraft para testar...")
            # pyautogui.click(x=100, y=200) # Exemplo: clicar no ícone
            
            return True
    return False

print("🟢 AGENTE LOCAL ATIVO. Aguardando comando do site...")
while True:
    instalar_e_testar()
    time.sleep(5)
