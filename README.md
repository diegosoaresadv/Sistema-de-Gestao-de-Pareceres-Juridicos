# Sistema de Gestão de Pareceres Jurídicos
## Volpe Advogados Associados | Cliente: Unimed Cuiabá

Sistema web para visualização e gestão de pareceres técnico-jurídicos desenvolvido com Streamlit.

---

## 📋 Descrição

Aplicativo web que permite à Unimed Cuiabá:
- Visualizar todos os pareceres jurídicos em uma interface moderna
- Filtrar pareceres por número de processo e classificação de risco
- Visualizar pareceres em HTML diretamente no navegador
- Baixar pareceres em formato HTML
- Acompanhar métricas gerais (total de pareceres, riscos, etc.)

---

## 🚀 Instalação

### 1. Instalar Python 3.8 ou superior

Certifique-se de ter o Python instalado em seu sistema.

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Estrutura de Pastas

Organize seus arquivos da seguinte forma:

```
projeto/
├── app_pareceres.py          # Aplicativo Streamlit principal
├── parecer_volpe.py           # Script para gerar pareceres HTML
├── relatorio_volpe.py         # Script para gerar relatórios HTML
├── processar_lote.py          # Script para processar vários pareceres
├── requirements.txt           # Dependências do projeto
├── LogoVolpe.jpeg            # Logo da Volpe (necessário)
├── pareceres/                # Pasta com arquivos JSON dos pareceres
│   ├── parecer_001.json
│   ├── parecer_002.json
│   └── ...
└── pareceres_html/           # Pasta onde os HTMLs serão salvos
    ├── parecer_001.html
    ├── parecer_002.html
    └── ...
```

---

## 📁 Preparação dos Dados

### 1. Criar as pastas necessárias

```bash
mkdir pareceres
mkdir pareceres_html
```

### 2. Adicionar os pareceres JSON

Coloque todos os arquivos JSON dos pareceres na pasta `pareceres/`

### 3. Gerar os HTMLs em lote

```bash
python processar_lote.py
```

Este comando irá:
- Ler todos os arquivos JSON da pasta `pareceres/`
- Gerar automaticamente os HTMLs correspondentes
- Salvar os HTMLs na pasta `pareceres_html/`

---

## 🎯 Como Executar

### Opção 1: Executar localmente

```bash
streamlit run app_pareceres.py
```

O aplicativo será aberto automaticamente no navegador em `http://localhost:8501`

### Opção 2: Especificar porta

```bash
streamlit run app_pareceres.py --server.port 8080
```

### Opção 3: Permitir acesso externo

```bash
streamlit run app_pareceres.py --server.address 0.0.0.0
```

---

## 🎨 Funcionalidades

### Dashboard Principal
- **Métricas Gerais**: Total de pareceres, quantidade por nível de risco
- **Filtros**: Busca por número de processo e classificação
- **Lista de Pareceres**: Cards com informações resumidas

### Visualização de Pareceres
- **Visualização Inline**: Ver o parecer HTML diretamente no navegador
- **Download**: Baixar o parecer HTML para visualização offline
- **Informações Detalhadas**: Número CNJ, parte contrária, natureza, valor, classificação

### Painel Lateral
- **Configurações**: Personalizar pastas de pareceres e HTMLs
- **Informações**: Contagem de documentos e status

---

## 📊 Formatos Suportados

### Pareceres Técnico-Jurídicos (Markdown)
```json
{
  "timestamp": "2025-11-04T05:59:48.710514",
  "hash": "abc123...",
  "resultado": "# PARECER TÉCNICO-JURÍDICO\n..."
}
```

### Análises Estruturadas
```json
{
  "timestamp": "2025-11-04T05:56:50.925377",
  "hash": "def456...",
  "resultado": {
    "numero_cnj": "0005586-53.2019.4.01.3600",
    "parte_contraria": "AGÊNCIA NACIONAL...",
    "natureza": "EMBARGOS À EXECUÇÃO FISCAL",
    ...
  }
}
```

---

## 🔧 Personalização

### Alterar pastas padrão

No aplicativo, use o painel lateral para configurar:
- **Pasta dos Pareceres JSON**: Onde estão os arquivos JSON
- **Pasta dos HTMLs**: Onde estão os arquivos HTML gerados

### Customizar cores e estilo

Edite a seção CSS no arquivo `app_pareceres.py` (linhas 30-140)

---

## 📝 Scripts Auxiliares

### processar_lote.py
Processa todos os JSONs e gera HTMLs automaticamente:

```bash
# Uso padrão
python processar_lote.py

# Especificando pastas personalizadas
python processar_lote.py pasta_jsons pasta_htmls LogoVolpe.jpeg
```

### parecer_volpe.py
Gera HTML individual de parecer markdown:

```bash
python parecer_volpe.py parecer.json saida.html LogoVolpe.jpeg
```

### relatorio_volpe.py
Gera HTML individual de relatório estruturado:

```bash
python relatorio_volpe.py dados.json saida.html LogoVolpe.jpeg
```

---

## 🐛 Solução de Problemas

### "Nenhum parecer encontrado"
- Verifique se os arquivos JSON estão na pasta correta
- Confirme que os JSONs têm a estrutura esperada

### "HTML não encontrado"
- Execute `python processar_lote.py` para gerar os HTMLs
- Verifique se a pasta de HTMLs está configurada corretamente

### Erro ao carregar logo
- Certifique-se que `LogoVolpe.jpeg` está no mesmo diretório
- Verifique as permissões de leitura do arquivo

---

## 🚀 Deploy em Produção

### Streamlit Cloud (Recomendado)

1. Crie um repositório no GitHub com os arquivos
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. Configure as pastas de dados
5. Deploy!

### Servidor Local

```bash
# Instalar como serviço (Linux)
sudo nano /etc/systemd/system/pareceres.service
```

Conteúdo do service:
```ini
[Unit]
Description=Sistema de Pareceres Volpe
After=network.target

[Service]
Type=simple
User=seu_usuario
WorkingDirectory=/caminho/para/projeto
ExecStart=/usr/bin/python3 -m streamlit run app_pareceres.py --server.port 8501
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable pareceres.service
sudo systemctl start pareceres.service
```

---

## 📞 Suporte

Para questões técnicas ou sugestões de melhorias, entre em contato com a equipe de desenvolvimento.

---

## 📄 Licença

© 2025 Volpe Advogados Associados. Todos os direitos reservados.

Sistema desenvolvido exclusivamente para uso interno da Unimed Cuiabá.

---

## 🔄 Atualizações

### Versão 1.0 (Novembro 2025)
- ✅ Interface web com Streamlit
- ✅ Visualização inline de pareceres
- ✅ Download de documentos
- ✅ Filtros e busca
- ✅ Métricas gerais
- ✅ Processamento em lote
- ✅ Suporte a múltiplos formatos JSON

---

**Desenvolvido com ❤️ por Volpe Advogados Associados**
