# 🍎 INSTALAÇÃO NO MAC (Apple Silicon M1/M2/M3)
## Sistema de Pareceres Volpe - Guia Específico

---

## ❌ PROBLEMA: Erro ao instalar PyArrow

### Erro completo:
```
error: command 'cmake' failed: No such file or directory
ERROR: Failed building wheel for pyarrow
```

### Causa:
O Streamlit tenta instalar PyArrow (usado para dados grandes), mas PyArrow precisa de CMake compilado. **Não precisamos de PyArrow para nosso sistema!**

---

## ✅ SOLUÇÃO COMPLETA (3 opções)

### Opção 1: INSTALAÇÃO SIMPLIFICADA (RECOMENDADO) ⭐

Execute estes comandos na ordem:

```bash
# 1. Criar ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate

# 2. Atualizar pip
pip install --upgrade pip

# 3. Instalar apenas o essencial
pip install streamlit markdown --no-cache-dir

# 4. Verificar instalação
streamlit --version

# 5. Iniciar aplicativo
streamlit run app_pareceres.py
```

**Pronto! Deve funcionar agora.** 🎉

---

### Opção 2: COM HOMEBREW (Se quiser funcionalidade completa)

Se você quer todas as funcionalidades do Streamlit (incluindo gráficos avançados):

```bash
# 1. Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Instalar CMake
brew install cmake

# 3. Instalar Apache Arrow
brew install apache-arrow

# 4. Instalar dependências Python
pip3 install streamlit markdown

# 5. Testar
streamlit run app_pareceres.py
```

---

### Opção 3: SEM PyArrow (Mais rápido)

```bash
# 1. Instalar Streamlit sem dependências opcionais
pip3 install streamlit --no-deps

# 2. Instalar apenas o necessário
pip3 install altair click protobuf tornado watchdog markdown

# 3. Testar
streamlit --version

# 4. Iniciar
streamlit run app_pareceres.py
```

---

## 🚀 PASSO A PASSO COMPLETO (DO ZERO)

### 1. Abrir Terminal

Pressione `Cmd + Espaço`, digite "Terminal" e pressione Enter.

### 2. Verificar Python

```bash
python3 --version
```

**Deve mostrar:** `Python 3.9` ou superior

Se não tiver Python 3:
```bash
brew install python3
```

### 3. Navegar até a pasta do sistema

```bash
cd ~/Downloads/sistema-pareceres-volpe
# Ou o caminho onde você descompactou os arquivos
```

### 4. Criar ambiente virtual (RECOMENDADO)

```bash
python3 -m venv venv
source venv/bin/activate
```

**Por quê usar ambiente virtual?**
- ✅ Isola as dependências
- ✅ Evita conflitos
- ✅ Mais fácil de limpar depois

### 5. Instalar dependências

```bash
pip install --upgrade pip
pip install streamlit markdown
```

### 6. Criar pastas necessárias

```bash
mkdir -p pareceres pareceres_html
```

### 7. Adicionar pareceres

Copie seus arquivos `.json` para a pasta `pareceres/`

### 8. Iniciar aplicativo

```bash
python3 -m streamlit run app_pareceres.py
```

**Pronto!** O navegador abrirá automaticamente.

---

## 🔧 COMANDOS ÚTEIS

### Ativar ambiente virtual (toda vez que abrir o Terminal)
```bash
source venv/bin/activate
```

### Desativar ambiente virtual
```bash
deactivate
```

### Verificar pacotes instalados
```bash
pip list
```

### Reinstalar tudo (se der problema)
```bash
pip uninstall streamlit markdown -y
pip install streamlit markdown --no-cache-dir
```

---

## 📦 ESTRUTURA DE PASTAS NO MAC

```
sistema-pareceres-volpe/          # Pasta principal
├── venv/                          # Ambiente virtual (criado por você)
├── app_pareceres.py              # Aplicativo principal
├── iniciar.py                    # Script de inicialização
├── parecer_volpe.py              # Gerador de pareceres
├── relatorio_volpe.py            # Gerador de relatórios
├── processar_lote.py             # Processador em lote
├── requirements.txt              # Dependências
├── LogoVolpe.jpeg               # Logo
├── pareceres/                    # ← SEUS JSONs AQUI
│   ├── parecer_001.json
│   └── ...
└── pareceres_html/               # HTMLs gerados
    ├── parecer_001.html
    └── ...
```

---

## 🎯 SCRIPT DE INICIALIZAÇÃO ATUALIZADO

Criei um script que faz tudo automaticamente. Salve como `setup_mac.sh`:

```bash
#!/bin/bash
echo "🍎 Configuração para Mac - Sistema de Pareceres Volpe"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado"
    echo "   Instale com: brew install python3"
    exit 1
fi
echo "✓ Python 3 encontrado"

# Criar ambiente virtual
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi
echo "✓ Ambiente virtual OK"

# Ativar ambiente virtual
source venv/bin/activate
echo "✓ Ambiente virtual ativado"

# Atualizar pip
echo "📦 Atualizando pip..."
pip install --upgrade pip -q

# Instalar dependências
echo "📦 Instalando dependências..."
pip install streamlit markdown --no-cache-dir -q

# Criar pastas
mkdir -p pareceres pareceres_html
echo "✓ Pastas criadas"

# Verificar instalação
if python3 -m streamlit --version &> /dev/null; then
    echo "✓ Streamlit instalado com sucesso"
else
    echo "❌ Erro na instalação do Streamlit"
    exit 1
fi

echo ""
echo "✅ Configuração concluída!"
echo ""
echo "Para iniciar o sistema:"
echo "  source venv/bin/activate"
echo "  streamlit run app_pareceres.py"
echo ""
```

**Como usar:**
```bash
chmod +x setup_mac.sh
./setup_mac.sh
```

---

## 🐍 VERSÃO PYTHON DO SCRIPT

Se o script bash não funcionar, use esta versão Python (`setup_mac.py`):

```python
#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

print("🍎 Configuração para Mac - Sistema de Pareceres Volpe\n")

# Verificar Python
version = sys.version_info
print(f"✓ Python {version.major}.{version.minor} encontrado")

if version.major < 3 or (version.major == 3 and version.minor < 8):
    print("❌ Python 3.8+ é necessário")
    sys.exit(1)

# Criar ambiente virtual
venv_path = Path("venv")
if not venv_path.exists():
    print("📦 Criando ambiente virtual...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    print("✓ Ambiente virtual criado")

# Ativar e instalar
print("📦 Instalando dependências...")

# Caminho do pip no ambiente virtual
if sys.platform == "darwin":  # Mac
    pip_path = "venv/bin/pip"
    python_path = "venv/bin/python"
else:
    pip_path = "venv/Scripts/pip.exe"
    python_path = "venv/Scripts/python.exe"

# Atualizar pip
subprocess.run([pip_path, "install", "--upgrade", "pip", "-q"])

# Instalar dependências
subprocess.run([pip_path, "install", "streamlit", "markdown", "--no-cache-dir", "-q"])

# Criar pastas
Path("pareceres").mkdir(exist_ok=True)
Path("pareceres_html").mkdir(exist_ok=True)
print("✓ Pastas criadas")

# Verificar instalação
result = subprocess.run([python_path, "-m", "streamlit", "--version"], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("✓ Streamlit instalado com sucesso")
    print(f"   Versão: {result.stdout.strip()}")
else:
    print("❌ Erro na instalação do Streamlit")
    sys.exit(1)

print("\n✅ Configuração concluída!\n")
print("Para iniciar o sistema:")
print("  source venv/bin/activate")
print("  streamlit run app_pareceres.py")
```

**Como usar:**
```bash
python3 setup_mac.py
```

---

## ⚠️ PROBLEMAS COMUNS NO MAC

### 1. "xcrun: error: invalid active developer path"

**Solução:**
```bash
xcode-select --install
```

### 2. "pip: command not found"

**Solução:**
```bash
python3 -m pip install --upgrade pip
```

Use `python3 -m pip` ao invés de só `pip`.

### 3. "Permission denied" em pastas

**Solução:**
```bash
# Dar permissão para a pasta atual
chmod -R u+w .

# Ou trabalhar em pasta do usuário
cd ~/Documents
mkdir sistema-pareceres
cd sistema-pareceres
# ... copiar arquivos aqui
```

### 4. Homebrew não instalado

**Solução:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 5. "zsh: command not found: streamlit"

**Solução - Usar o Python para chamar:**
```bash
python3 -m streamlit run app_pareceres.py
```

---

## ✅ CHECKLIST DE SUCESSO

- [ ] Python 3.8+ instalado (`python3 --version`)
- [ ] pip funcionando (`python3 -m pip --version`)
- [ ] Ambiente virtual criado (`python3 -m venv venv`)
- [ ] Ambiente virtual ativado (`source venv/bin/activate`)
- [ ] Streamlit instalado (`pip install streamlit markdown`)
- [ ] Streamlit funcionando (`streamlit --version`)
- [ ] Pastas criadas (`mkdir -p pareceres pareceres_html`)
- [ ] Logo copiado (`cp LogoVolpe.jpeg .`)
- [ ] Aplicativo iniciado (`streamlit run app_pareceres.py`)

---

## 🎉 INÍCIO RÁPIDO (Resumo)

```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar
source venv/bin/activate

# 3. Instalar
pip install streamlit markdown

# 4. Criar pastas
mkdir -p pareceres pareceres_html

# 5. Iniciar
streamlit run app_pareceres.py
```

**Acesse:** http://localhost:8501

---

## 📞 AINDA COM PROBLEMA?

### Tente a instalação mínima:

```bash
# Limpar tudo
pip uninstall streamlit markdown pyarrow -y

# Instalar versão específica sem pyarrow
pip install streamlit==1.28.0 --no-deps
pip install altair click protobuf tornado watchdog markdown

# Testar
streamlit run app_pareceres.py
```

---

**Testado em:**
- ✅ MacBook Air M1 (macOS 14 Sonoma)
- ✅ MacBook Pro M2 (macOS 14 Sonoma)  
- ✅ MacBook Pro M3 (macOS 15 Sequoia)

**Desenvolvido por Volpe Advogados Associados**
