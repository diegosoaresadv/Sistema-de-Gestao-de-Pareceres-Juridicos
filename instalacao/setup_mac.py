#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup Automático para Mac
Sistema de Pareceres Volpe - Unimed Cuiabá
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    print("\n" + "="*60)
    print("  🍎 SETUP PARA MAC - SISTEMA DE PARECERES VOLPE")
    print("="*60 + "\n")

def verificar_python():
    """Verifica se Python está OK"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} encontrado")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário")
        print("   Instale com: brew install python3")
        return False
    
    return True

def criar_ambiente_virtual():
    """Cria ambiente virtual se não existir"""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✓ Ambiente virtual já existe")
        return True
    
    print("📦 Criando ambiente virtual...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✓ Ambiente virtual criado")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar ambiente virtual: {e}")
        return False

def get_venv_paths():
    """Retorna caminhos do ambiente virtual"""
    if sys.platform == "darwin" or sys.platform == "linux":
        return {
            'python': 'venv/bin/python',
            'pip': 'venv/bin/pip',
            'streamlit': 'venv/bin/streamlit'
        }
    else:  # Windows
        return {
            'python': 'venv\\Scripts\\python.exe',
            'pip': 'venv\\Scripts\\pip.exe',
            'streamlit': 'venv\\Scripts\\streamlit.exe'
        }

def atualizar_pip(pip_path):
    """Atualiza o pip"""
    print("📦 Atualizando pip...")
    try:
        subprocess.run([pip_path, "install", "--upgrade", "pip", "-q"], check=True)
        print("✓ pip atualizado")
        return True
    except Exception as e:
        print(f"⚠️  Aviso: Não foi possível atualizar pip: {e}")
        return True  # Não crítico

def instalar_dependencias(pip_path):
    """Instala as dependências necessárias"""
    print("📦 Instalando Streamlit e Markdown...")
    print("   (Isso pode demorar alguns minutos...)")
    
    try:
        # Tenta instalação normal primeiro
        result = subprocess.run(
            [pip_path, "install", "streamlit", "markdown", "--no-cache-dir"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✓ Dependências instaladas com sucesso")
            return True
        
        # Se falhar, tenta sem pyarrow
        print("⚠️  Tentando instalação alternativa sem PyArrow...")
        
        # Desinstala qualquer coisa que possa estar parcialmente instalada
        subprocess.run([pip_path, "uninstall", "streamlit", "pyarrow", "-y"], 
                      capture_output=True)
        
        # Instala Streamlit sem dependências opcionais
        subprocess.run([pip_path, "install", "streamlit", "--no-deps"], check=True)
        
        # Instala dependências essenciais manualmente
        deps = ["altair", "click", "protobuf", "tornado", "watchdog", "markdown"]
        for dep in deps:
            print(f"   Instalando {dep}...")
            subprocess.run([pip_path, "install", dep, "-q"], check=True)
        
        print("✓ Dependências instaladas (modo alternativo)")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        print("\n💡 Tente manualmente:")
        print(f"   {pip_path} install streamlit markdown")
        return False

def criar_pastas():
    """Cria as pastas necessárias"""
    pastas = ['pareceres', 'pareceres_html']
    
    for pasta in pastas:
        pasta_path = Path(pasta)
        if not pasta_path.exists():
            pasta_path.mkdir(exist_ok=True)
            print(f"📁 Pasta '{pasta}' criada")
        else:
            print(f"✓ Pasta '{pasta}' já existe")

def verificar_instalacao(python_path):
    """Verifica se Streamlit foi instalado corretamente"""
    print("\n🔍 Verificando instalação...")
    
    try:
        result = subprocess.run(
            [python_path, "-m", "streamlit", "--version"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✓ Streamlit instalado: {version}")
            return True
        else:
            print("❌ Streamlit não está funcionando corretamente")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao verificar instalação: {e}")
        return False

def verificar_logo():
    """Verifica se o logo existe"""
    logo_path = Path("LogoVolpe.jpeg")
    if logo_path.exists():
        print("✓ Logo encontrado")
        return True
    else:
        print("⚠️  Logo 'LogoVolpe.jpeg' não encontrado")
        print("   O sistema funcionará, mas sem o logo no cabeçalho")
        return False

def contar_arquivos():
    """Conta arquivos nas pastas"""
    pasta_json = Path('pareceres')
    pasta_html = Path('pareceres_html')
    
    num_jsons = len(list(pasta_json.glob('*.json'))) if pasta_json.exists() else 0
    num_htmls = len(list(pasta_html.glob('*.html'))) if pasta_html.exists() else 0
    
    print(f"\n📊 Status dos arquivos:")
    print(f"   - Pareceres JSON: {num_jsons}")
    print(f"   - Pareceres HTML: {num_htmls}")
    
    if num_jsons == 0:
        print("\n💡 Dica: Coloque seus arquivos .json na pasta 'pareceres/'")
    
    return num_jsons, num_htmls

def print_instrucoes_uso(python_path, streamlit_path):
    """Imprime instruções de uso"""
    print("\n" + "="*60)
    print("  ✅ CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    
    print("\n📝 COMO USAR:\n")
    
    print("1️⃣  Ativar o ambiente virtual:")
    print("   source venv/bin/activate\n")
    
    print("2️⃣  Adicionar pareceres (se ainda não adicionou):")
    print("   Copie seus arquivos .json para a pasta 'pareceres/'\n")
    
    print("3️⃣  Processar pareceres (gerar HTMLs):")
    print(f"   {python_path} processar_lote.py\n")
    
    print("4️⃣  Iniciar o aplicativo:")
    print(f"   {python_path} -m streamlit run app_pareceres.py")
    print("   OU")
    print(f"   {streamlit_path} run app_pareceres.py\n")
    
    print("🌐 O aplicativo abrirá automaticamente em:")
    print("   http://localhost:8501\n")
    
    print("="*60)

def main():
    """Função principal"""
    print_header()
    
    # Verificações
    if not verificar_python():
        sys.exit(1)
    
    if not criar_ambiente_virtual():
        sys.exit(1)
    
    # Obter caminhos do ambiente virtual
    paths = get_venv_paths()
    
    # Atualizar pip
    atualizar_pip(paths['pip'])
    
    # Instalar dependências
    if not instalar_dependencias(paths['pip']):
        sys.exit(1)
    
    # Criar pastas
    criar_pastas()
    
    # Verificar instalação
    if not verificar_instalacao(paths['python']):
        print("\n⚠️  Instalação não verificada completamente")
        print("   Mas você pode tentar iniciar o aplicativo")
    
    # Verificar logo
    verificar_logo()
    
    # Contar arquivos
    contar_arquivos()
    
    # Instruções finais
    print_instrucoes_uso(paths['python'], paths['streamlit'])
    
    print("\n💡 Dica: Para facilitar, use o script 'iniciar.py' depois da configuração")

if __name__ == "__main__":
    main()
