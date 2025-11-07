#!/bin/bash
# Script de Inicialização do Sistema de Pareceres
# Volpe Advogados Associados

echo "=================================================="
echo "  SISTEMA DE GESTÃO DE PARECERES JURÍDICOS"
echo "  Volpe Advogados Associados"
echo "=================================================="
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale o Python 3.8 ou superior."
    exit 1
fi

echo "✓ Python encontrado"

# Verifica se as dependências estão instaladas
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "📦 Instalando dependências..."
    pip install -r requirements.txt
    echo "✓ Dependências instaladas"
else
    echo "✓ Dependências já instaladas"
fi

# Verifica estrutura de pastas
if [ ! -d "pareceres" ]; then
    echo "📁 Criando pasta 'pareceres'..."
    mkdir pareceres
fi

if [ ! -d "pareceres_html" ]; then
    echo "📁 Criando pasta 'pareceres_html'..."
    mkdir pareceres_html
fi

echo "✓ Estrutura de pastas OK"

# Conta arquivos
num_jsons=$(ls -1 pareceres/*.json 2>/dev/null | wc -l)
num_htmls=$(ls -1 pareceres_html/*.html 2>/dev/null | wc -l)

echo ""
echo "📊 Status:"
echo "   - Pareceres JSON: $num_jsons"
echo "   - Pareceres HTML: $num_htmls"
echo ""

# Se há JSONs mas poucos HTMLs, oferece processar
if [ $num_jsons -gt 0 ] && [ $num_htmls -lt $num_jsons ]; then
    echo "💡 Existem pareceres JSON que ainda não foram processados."
    read -p "   Deseja processar todos os pareceres agora? (s/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        python3 processar_lote.py
    fi
fi

echo ""
echo "🚀 Iniciando aplicativo Streamlit..."
echo ""
echo "=================================================="
echo "  O aplicativo abrirá automaticamente no navegador"
echo "  URL: http://localhost:8501"
echo "  Pressione Ctrl+C para encerrar"
echo "=================================================="
echo ""

streamlit run app_pareceres.py
