# 🚀 GUIA RÁPIDO - Sistema de Pareceres
## Volpe Advogados Associados | Unimed Cuiabá

---

## ⚡ INÍCIO RÁPIDO (3 passos)

### 1️⃣ INSTALAR
```bash
pip install -r requirements.txt
```

### 2️⃣ ADICIONAR PARECERES
Coloque os arquivos `.json` na pasta `pareceres/`

### 3️⃣ INICIAR
**Linux/Mac:**
```bash
./iniciar.sh
```

**Windows:**
```
iniciar.bat
```

**Ou manualmente:**
```bash


```

---

## 📁 ESTRUTURA DE ARQUIVOS

```
📦 sistema-pareceres/
│
├── 🚀 iniciar.sh              # Iniciar (Linux/Mac)
├── 🚀 iniciar.bat             # Iniciar (Windows)
│
├── 📱 app_pareceres.py        # Aplicativo principal
├── 🔧 processar_lote.py       # Processar múltiplos pareceres
├── 📄 parecer_volpe.py        # Gerar HTML de parecer
├── 📄 relatorio_volpe.py      # Gerar HTML de relatório
│
├── 📋 requirements.txt        # Dependências
├── 📖 README.md               # Documentação completa
│
├── 🖼️ LogoVolpe.jpeg          # Logo (necessário!)
│
├── 📁 pareceres/              # COLOQUE OS JSONs AQUI
│   ├── parecer_001.json
│   ├── parecer_002.json
│   └── ...
│
└── 📁 pareceres_html/         # HTMLs gerados automaticamente
    ├── parecer_001.html
    ├── parecer_002.html
    └── ...
```

---

## 🎯 COMO USAR

### PASSO A PASSO

1. **Adicionar pareceres**
   - Coloque os arquivos `.json` na pasta `pareceres/`

2. **Processar pareceres** (Opcional - pode ser feito pelo app)
   ```bash
   python processar_lote.py
   ```

3. **Iniciar aplicativo**
   ```bash
   streamlit run app_pareceres.py
   ```

4. **Acessar no navegador**
   - Abra: http://localhost:8501
   - O navegador abrirá automaticamente

---

## 💡 FUNCIONALIDADES

### 🏠 DASHBOARD
- ✅ Total de pareceres
- ✅ Pareceres por risco (Alto/Médio/Baixo)
- ✅ Visão geral colorida

### 🔍 FILTROS
- ✅ Buscar por número do processo
- ✅ Filtrar por classificação de risco
- ✅ Busca instantânea

### 📄 PARECERES
- ✅ Lista completa de pareceres
- ✅ Informações resumidas em cards
- ✅ Visualização HTML inline
- ✅ Download de documentos
- ✅ Badges de risco coloridos

### ⚙️ CONFIGURAÇÕES
- ✅ Personalizar pastas
- ✅ Atualização automática
- ✅ Interface responsiva

---

## 🎨 INTERFACE

### CORES DOS BADGES

🔴 **VERMELHO** = Alto Risco / Provável
- Requer atenção imediata

🟠 **LARANJA** = Médio Risco / Possível  
- Monitoramento regular

🟢 **VERDE** = Baixo Risco / Remota
- Situação controlada

---

## 🔧 COMANDOS ÚTEIS

### Processar um parecer específico
```bash
python parecer_volpe.py parecer.json saida.html
```

### Processar todos de uma vez
```bash
python processar_lote.py
```

### Iniciar em porta específica
```bash
streamlit run app_pareceres.py --server.port 8080
```

### Permitir acesso externo
```bash
streamlit run app_pareceres.py --server.address 0.0.0.0
```

---

## ❓ PROBLEMAS COMUNS

### "Nenhum parecer encontrado"
**Solução:** Coloque arquivos `.json` na pasta `pareceres/`

### "HTML não encontrado"
**Solução:** Execute `python processar_lote.py`

### "Logo não encontrado"
**Solução:** Certifique-se que `LogoVolpe.jpeg` está no diretório

### Erro ao instalar dependências
**Solução:** 
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📞 SUPORTE

Para dúvidas ou problemas:
1. Consulte o README.md completo
2. Verifique a documentação do Streamlit
3. Entre em contato com a equipe técnica

---

## ✅ CHECKLIST DE USO

- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Pasta `pareceres/` criada
- [ ] Pasta `pareceres_html/` criada
- [ ] Logo `LogoVolpe.jpeg` no diretório
- [ ] Arquivos JSON adicionados
- [ ] Pareceres processados
- [ ] Aplicativo iniciado

---

## 🎓 DICAS PRO

1. **Organização**
   - Use nomes descritivos para os arquivos JSON
   - Mantenha backup dos pareceres originais

2. **Performance**
   - Processe os HTMLs antes de iniciar o app
   - Limite arquivos muito grandes (>50MB)

3. **Segurança**
   - Não exponha o servidor publicamente sem autenticação
   - Use VPN para acesso remoto

4. **Produção**
   - Configure domínio próprio
   - Use HTTPS
   - Implemente backup automático

---

**© 2025 Volpe Advogados Associados**

Sistema desenvolvido exclusivamente para Unimed Cuiabá
