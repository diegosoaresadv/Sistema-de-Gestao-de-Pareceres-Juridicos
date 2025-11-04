#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Inicialização do Sistema de Pareceres
Volpe Advogados Associados - Unimed Cuiabá
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    """Imprime o cabeçalho"""
    print("\n" + "="*60)
    print("  SISTEMA DE GESTÃO DE PARECERES JURÍDICOS")
    print("  Volpe Advogados Associados")
    print("="*60 + "\n")

def verificar_python():
    """Verifica versão do Python"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} encontrado")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário")
        print("   Por favor, atualize o Python")
        return False
    
    return True

def instalar_dependencias():
    """Instala as dependências necessárias"""
    try:
        import streamlit
        import markdown
        print("✓ Dependências já instaladas")
        return True
    except ImportError:
        print("📦 Instalando dependências...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✓ Dependências instaladas com sucesso")
            return True
        except Exception as e:
            print(f"❌ Erro ao instalar dependências: {e}")
            print("   Tente executar manualmente: pip install -r requirements.txt")
            return False

def criar_pastas():
    """Cria as pastas necessárias"""
    pastas = ['pareceres', 'pareceres_html']
    
    for pasta in pastas:
        pasta_path = Path(pasta)
        if not pasta_path.exists():
            pasta_path.mkdir(exist_ok=True)
            print(f"📁 Pasta '{pasta}' criada")
    
    print("✓ Estrutura de pastas OK")

def verificar_arquivos():
    """Verifica quantidade de arquivos"""
    pasta_json = Path('pareceres')
    pasta_html = Path('pareceres_html')
    
    num_jsons = len(list(pasta_json.glob('*.json'))) if pasta_json.exists() else 0
    num_htmls = len(list(pasta_html.glob('*.html'))) if pasta_html.exists() else 0
    
    print(f"\n📊 Status:")
    print(f"   - Pareceres JSON: {num_jsons}")
    print(f"   - Pareceres HTML: {num_htmls}")
    
    return num_jsons, num_htmls

def processar_pareceres():
    """Oferece processar pareceres"""
    num_jsons, num_htmls = verificar_arquivos()
    
    if num_jsons > 0 and num_htmls < num_jsons:
        print("\n💡 Existem pareceres JSON que ainda não foram processados.")
        resposta = input("   Deseja processar todos os pareceres agora? (s/n): ")
        
        if resposta.lower() in ['s', 'sim', 'y', 'yes']:
            print("\n🔄 Processando pareceres...\n")
            try:
                subprocess.run([sys.executable, "processar_lote.py"])
                print("\n✓ Processamento concluído")
            except Exception as e:
                print(f"\n⚠️  Erro ao processar: {e}")
                print("   Você pode processar manualmente depois com: python processar_lote.py")

def iniciar_streamlit():
    """Inicia o aplicativo Streamlit"""
    print("\n" + "="*60)
    print("🚀 Iniciando aplicativo Streamlit...")
    print("\n  O aplicativo abrirá automaticamente no navegador")
    print("  URL: http://localhost:8501")
    print("\n  Pressione Ctrl+C para encerrar")
    print("="*60 + "\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app_pareceres.py"])
    except KeyboardInterrupt:
        print("\n\n✓ Aplicativo encerrado")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar: {e}")
        print("\nTente iniciar manualmente com:")
        print("  streamlit run app_pareceres.py")

def main():
    """Função principal"""
    print_header()
    
    # Verificações
    if not verificar_python():
        return
    
    if not instalar_dependencias():
        return
    
    criar_pastas()
    
    processar_pareceres()
    
    # Inicia o aplicativo
    iniciar_streamlit()

if __name__ == "__main__":
    main()
