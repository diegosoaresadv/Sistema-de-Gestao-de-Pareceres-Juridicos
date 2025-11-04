# 🔧 SOLUÇÃO DE PROBLEMAS - Mac OS
## Sistema de Pareceres Volpe

---

## ❌ Erro: "Permission denied" ao executar ./iniciar.sh

### Problema
```bash
bash-3.2$ ./iniciar.sh
bash: ./iniciar.sh: Permission denied
```

### Causa
O arquivo não tem permissão de execução no Mac OS.

---

## ✅ SOLUÇÕES (escolha uma)

### Solução 1: Dar permissão ao script (RECOMENDADO)

```bash
chmod +x iniciar.sh
./iniciar.sh
```

**Explicação:**
- `chmod +x` dá permissão de execução ao arquivo
- Depois pode executar normalmente com `./iniciar.sh`

---

### Solução 2: Usar o script Python (SEM NECESSIDADE DE PERMISSÃO)

```bash
python3 iniciar.py
```

**Vantagens:**
- ✅ Não precisa de permissão especial
- ✅ Funciona em qualquer sistema
- ✅ Mais portável
- ✅ Mesmas funcionalidades do .sh

---

### Solução 3: Executar com bash

```bash
bash iniciar.sh
```

**Explicação:**
- Executa o arquivo diretamente com o bash
- Não precisa de permissão de execução

---

### Solução 4: Usar Python diretamente (MANUAL)

Se nenhuma das anteriores funcionar, execute os comandos manualmente:

```bash
# 1. Instalar dependências
pip3 install -r requirements.txt

# 2. Criar pastas (se não existirem)
mkdir -p pareceres pareceres_html

# 3. Processar pareceres (opcional)
python3 processar_lote.py

# 4. Iniciar aplicativo
streamlit run app_pareceres.py
```

---

## 🍎 DICAS PARA MAC OS

### 1. Usar Python 3
No Mac, sempre use `python3` ao invés de `python`:

```bash
python3 iniciar.py          # ✅ Correto
python iniciar.py           # ❌ Pode usar Python 2
```

### 2. Usar pip3
Da mesma forma, use `pip3`:

```bash
pip3 install -r requirements.txt    # ✅ Correto
pip install -r requirements.txt     # ❌ Pode usar pip do Python 2
```

### 3. Verificar versão do Python
```bash
python3 --version
```

Deve mostrar: `Python 3.8` ou superior

### 4. Instalar Python 3 (se necessário)
Se Python 3 não estiver instalado:

```bash
# Opção 1: Homebrew (recomendado)
brew install python3

# Opção 2: Download direto
# Baixar de: https://www.python.org/downloads/
```

---

## 🔍 DIAGNÓSTICO DE PROBLEMAS

### Verificar se Python 3 está instalado
```bash
which python3
python3 --version
```

**Saída esperada:**
```
/usr/local/bin/python3
Python 3.11.x
```

### Verificar se Streamlit está instalado
```bash
python3 -m streamlit --version
```

**Saída esperada:**
```
Streamlit, version 1.28.x
```

### Verificar estrutura de arquivos
```bash
ls -la
```

**Deve mostrar:**
- app_pareceres.py
- iniciar.py
- iniciar.sh
- requirements.txt
- LogoVolpe.jpeg
- pareceres/ (pasta)
- pareceres_html/ (pasta)

---

## 🚀 ORDEM RECOMENDADA DE EXECUÇÃO

### Para Mac OS (MAIS FÁCIL)

```bash
# 1. Navegar até a pasta do sistema
cd caminho/para/sistema-pareceres

# 2. Usar o script Python (não precisa permissão)
python3 iniciar.py
```

**Pronto!** O script fará tudo automaticamente:
- ✅ Verificar Python
- ✅ Instalar dependências
- ✅ Criar pastas
- ✅ Oferecer processar pareceres
- ✅ Iniciar aplicativo

---

## ⚡ INÍCIO SUPER RÁPIDO

Se você só quer iniciar o aplicativo rapidamente (já tem tudo configurado):

```bash
streamlit run app_pareceres.py
```

Ou:

```bash
python3 -m streamlit run app_pareceres.py
```

---

## 🛠️ PROBLEMAS COMUNS E SOLUÇÕES

### "streamlit: command not found"

**Solução:**
```bash
pip3 install streamlit
```

Ou use:
```bash
python3 -m streamlit run app_pareceres.py
```

---

### "No module named 'streamlit'"

**Solução:**
```bash
pip3 install -r requirements.txt
```

---

### "ModuleNotFoundError: No module named 'markdown'"

**Solução:**
```bash
pip3 install markdown
```

---

### Porta 8501 já em uso

**Solução 1 - Usar outra porta:**
```bash
streamlit run app_pareceres.py --server.port 8502
```

**Solução 2 - Parar processo anterior:**
```bash
# Encontrar o processo
lsof -ti:8501

# Matar o processo (substitua PID pelo número retornado)
kill -9 PID
```

---

### Aplicativo não abre no navegador

**Solução:**
Abra manualmente:
```
http://localhost:8501
```

Ou especifique para não abrir automaticamente:
```bash
streamlit run app_pareceres.py --server.headless true
```

---

## 📝 COMANDOS ÚTEIS PARA MAC

### Ver processos Streamlit rodando
```bash
ps aux | grep streamlit
```

### Parar todos os processos Streamlit
```bash
pkill -f streamlit
```

### Ver porta em uso
```bash
lsof -i :8501
```

### Limpar cache do Streamlit
```bash
streamlit cache clear
```

---

## 🎯 RESUMO - 3 FORMAS DE INICIAR

### 1️⃣ Forma mais fácil (Python)
```bash
python3 iniciar.py
```

### 2️⃣ Forma com script bash
```bash
chmod +x iniciar.sh
./iniciar.sh
```

### 3️⃣ Forma direta
```bash
streamlit run app_pareceres.py
```

---

## 📞 AINDA COM PROBLEMAS?

### Checklist de verificação:

- [ ] Python 3.8+ instalado? (`python3 --version`)
- [ ] pip3 funciona? (`pip3 --version`)
- [ ] Dependências instaladas? (`pip3 install -r requirements.txt`)
- [ ] Na pasta correta? (`ls` deve mostrar app_pareceres.py)
- [ ] Logo presente? (`ls LogoVolpe.jpeg`)
- [ ] Pastas criadas? (`ls -d pareceres pareceres_html`)

### Se tudo estiver OK mas não funcionar:

Execute passo a passo:

```bash
# 1. Verificar Python
python3 --version

# 2. Instalar dependências
pip3 install streamlit markdown

# 3. Testar Streamlit
python3 -m streamlit hello

# 4. Se o teste funcionar, iniciar seu app
python3 -m streamlit run app_pareceres.py
```

---

## ✅ TESTADO EM:

- ✅ macOS Monterey (12.x)
- ✅ macOS Ventura (13.x)
- ✅ macOS Sonoma (14.x)
- ✅ Python 3.8, 3.9, 3.10, 3.11, 3.12

---

**Desenvolvido por Volpe Advogados Associados**
**Suporte: Consulte o README.md para mais informações**
