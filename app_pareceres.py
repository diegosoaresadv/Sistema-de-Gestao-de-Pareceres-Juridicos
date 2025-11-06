#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Gestão de Pareceres Jurídicos
Volpe Advogados Associados
Cliente: Unimed Cuiabá

Aplicativo Streamlit para visualização de pareceres técnico-jurídicos
"""

import streamlit as st
import json
import os
from pathlib import Path
from datetime import datetime
import base64
import re
import hmac


# Remove do histórico do Git
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secrets.json" \
  --prune-empty --tag-name-filter cat -- --all

# Força o push
git push origin --force --all

# Configuração da página
st.set_page_config(
    page_title="Pareceres Jurídicos - Unimed Cuiabá",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Função para carregar credenciais do arquivo de segredos
def load_credentials():
    """Carrega as credenciais do arquivo secrets.json"""
    secrets_file = Path("secrets.json")
    
    if not secrets_file.exists():
        st.error("""
        ⚠️ **Arquivo de credenciais não encontrado!**
        
        Crie um arquivo chamado `secrets.json` na mesma pasta do aplicativo com o seguinte formato:
        
        ```json
        {
            "username": "seu_usuario",
            "password": "sua_senha"
        }
        ```
        
        **IMPORTANTE:** Adicione `secrets.json` ao seu `.gitignore` para não compartilhar suas credenciais!
        """)
        st.stop()
    
    try:
        with open(secrets_file, 'r', encoding='utf-8') as f:
            credentials = json.load(f)
            
        if "username" not in credentials or "password" not in credentials:
            st.error("❌ O arquivo secrets.json deve conter os campos 'username' e 'password'")
            st.stop()
            
        return credentials["username"], credentials["password"]
        
    except json.JSONDecodeError:
        st.error("❌ Erro ao ler o arquivo secrets.json. Verifique se o formato JSON está correto.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Erro ao carregar credenciais: {str(e)}")
        st.stop()


# Função de autenticação
def check_password():
    """Retorna `True` se o usuário inseriu a senha correta."""
    
    # Carrega as credenciais do arquivo
    valid_username, valid_password = load_credentials()
    
    def password_entered():
        """Verifica se a senha inserida está correta."""
        if hmac.compare_digest(st.session_state["username"], valid_username) and \
           hmac.compare_digest(st.session_state["password"], valid_password):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Remove a senha da sessão
            del st.session_state["username"]  # Remove o usuário da sessão
        else:
            st.session_state["password_correct"] = False

    # Retorna True se a senha já foi validada
    if st.session_state.get("password_correct", False):
        return True

    # Mostra tela de login
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0;">
        <h1>⚖️ Sistema de Gestão de Pareceres Jurídicos</h1>
        <h3>Volpe Advogados Associados | Cliente: Unimed Cuiabá</h3>
        <p style="margin-top: 2rem; font-size: 1.2em;">Por favor, faça login para acessar o sistema</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.text_input("Usuário", key="username", on_change=password_entered)
        st.text_input("Senha", type="password", key="password", on_change=password_entered)
        
        if "password_correct" in st.session_state and not st.session_state["password_correct"]:
            st.error("😕 Usuário ou senha incorretos")
    
    return False


# CSS customizado com cores da Volpe
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    h1 {
        color: #1e4d6b;
        font-weight: 600;
    }
    
    h2, h3 {
        color: #2a6587;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #1e4d6b 0%, #2a6587 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #2a6587 0%, #4a90b5 100%);
        box-shadow: 0 4px 12px rgba(30, 77, 107, 0.3);
    }
    
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        margin-bottom: 1rem;
        border-left: 4px solid #5fa8d3;
    }
    
    .badge-provavel {
        background: linear-gradient(135deg, #f56565, #fc8181);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        display: inline-block;
    }
    
    .badge-possivel {
        background: linear-gradient(135deg, #ed8936, #f6ad55);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        display: inline-block;
    }
    
    .badge-remota {
        background: linear-gradient(135deg, #48bb78, #68d391);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        display: inline-block;
    }
    
    .badge-alto {
        background: linear-gradient(135deg, #f56565, #fc8181);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        display: inline-block;
    }
    
    .badge-medio {
        background: linear-gradient(135deg, #ed8936, #f6ad55);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        display: inline-block;
    }
    
    .badge-baixo {
        background: linear-gradient(135deg, #48bb78, #68d391);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        display: inline-block;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1e4d6b 0%, #4a90b5 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(30, 77, 107, 0.15);
    }
    
    .metric-value {
        font-size: 2.5em;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9em;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .html-card {
        background: white;
        padding: 1.2rem;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
        margin-bottom: 0.8rem;
        border-left: 4px solid #5fa8d3;
        transition: all 0.3s ease;
    }
    
    .html-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)


def buscar_pareceres_json(pasta="pareceres"):
    """Busca todos os arquivos JSON de pareceres na pasta especificada"""
    pareceres = []
    pasta_path = Path(pasta)
    
    if not pasta_path.exists():
        return pareceres
    
    for arquivo in pasta_path.glob("**/*.json"):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                
                # Extrai informações básicas
                info = {
                    'arquivo': str(arquivo),
                    'nome': arquivo.name,
                    'timestamp': dados.get('timestamp', ''),
                    'hash': dados.get('hash', ''),
                }
                
                # Verifica se é um parecer completo ou análise estruturada
                if 'resultado' in dados:
                    resultado = dados['resultado']
                    
                    # Se resultado é string (markdown)
                    if isinstance(resultado, str):
                        info['tipo'] = 'parecer_markdown'
                        info['numero_processo'] = extrair_numero_processo(resultado)
                        info['classificacao'] = extrair_classificacao(resultado)
                        info['valor'] = extrair_valor(resultado)
                        info['parte_contraria'] = extrair_parte_contraria(resultado)
                        info['natureza'] = extrair_natureza(resultado)
                    
                    # Se resultado é dict (análise estruturada)
                    elif isinstance(resultado, dict):
                        info['tipo'] = 'analise_estruturada'
                        info['numero_processo'] = resultado.get('numero_cnj', 'N/A')
                        info['classificacao'] = resultado.get('probabilidade_perda', 'Não informado')
                        info['valor'] = resultado.get('valor_contingencia', 'N/A')
                        info['parte_contraria'] = resultado.get('parte_contraria', 'N/A')
                        info['natureza'] = resultado.get('natureza', 'N/A')
                        info['fase'] = resultado.get('fase', 'N/A')
                
                pareceres.append(info)
                
        except Exception as e:
            st.sidebar.warning(f"Erro ao ler {arquivo.name}: {str(e)}")
            continue
    
    return pareceres


def buscar_arquivos_html(pasta_html="pareceres_html"):
    """Busca todos os arquivos HTML na pasta especificada"""
    arquivos_html = []
    pasta_html_path = Path(pasta_html)
    
    if not pasta_html_path.exists():
        return arquivos_html
    
    for arquivo in pasta_html_path.glob("**/*.html"):
        try:
            # Obtém informações do arquivo
            stat = arquivo.stat()
            
            info = {
                'caminho': str(arquivo),
                'nome': arquivo.name,
                'tamanho': stat.st_size,
                'tamanho_formatado': formatar_tamanho(stat.st_size),
                'data_modificacao': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'timestamp_modificacao': stat.st_mtime
            }
            
            # Tenta extrair informações do conteúdo HTML
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                    info['numero_processo'] = extrair_numero_processo_html(conteudo)
                    info['titulo'] = extrair_titulo_html(conteudo)
            except:
                info['numero_processo'] = 'N/A'
                info['titulo'] = arquivo.stem
            
            arquivos_html.append(info)
            
        except Exception as e:
            st.sidebar.warning(f"Erro ao processar {arquivo.name}: {str(e)}")
            continue
    
    return arquivos_html


def formatar_tamanho(tamanho_bytes):
    """Formata o tamanho do arquivo em unidades legíveis"""
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if tamanho_bytes < 1024.0:
            return f"{tamanho_bytes:.1f} {unidade}"
        tamanho_bytes /= 1024.0
    return f"{tamanho_bytes:.1f} TB"


def extrair_numero_processo_html(html_content):
    """Extrai o número do processo do conteúdo HTML"""
    # Procura por padrões CNJ
    match = re.search(r'\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}', html_content)
    if match:
        return match.group(0)
    
    # Procura por "Número do Processo" ou "Processo:"
    match = re.search(r'(?:Número do Processo|Processo)[:\s]*([0-9\-\.]+)', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    return 'N/A'


def extrair_titulo_html(html_content):
    """Extrai o título do HTML"""
    match = re.search(r'<title>(.+?)</title>', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    match = re.search(r'<h1[^>]*>(.+?)</h1>', html_content, re.IGNORECASE)
    if match:
        return re.sub(r'<[^>]+>', '', match.group(1)).strip()
    
    return 'Documento sem título'


def extrair_numero_processo(texto):
    """Extrai o número do processo do parecer markdown"""
    match = re.search(r'\*\*Número do Processo \(CNJ\):\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    return "N/A"


def extrair_classificacao(texto):
    """Extrai a classificação de risco do parecer markdown"""
    match = re.search(r'\*\*Classificação:\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    
    # Tenta buscar por RISCO ALTO/MÉDIO/BAIXO
    if 'RISCO ALTO' in texto:
        return 'RISCO ALTO'
    elif 'RISCO MÉDIO' in texto or 'RISCO MÉDIO-BAIXO' in texto:
        return 'RISCO MÉDIO'
    elif 'PROVÁVEL' in texto:
        return 'PROVÁVEL'
    elif 'POSSÍVEL' in texto:
        return 'POSSÍVEL'
    elif 'REMOTA' in texto:
        return 'REMOTA'
    
    return "Não informado"


def extrair_valor(texto):
    """Extrai o valor da causa do parecer markdown"""
    match = re.search(r'\*\*Valor da Causa:\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    
    match = re.search(r'R\$\s*[\d\.,]+', texto)
    if match:
        return match.group(0)
    
    return "N/A"


def extrair_parte_contraria(texto):
    """Extrai a parte contrária do parecer markdown"""
    match = re.search(r'\*\*Parte Contrária:\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    
    match = re.search(r'\*\*Autor:\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    
    return "N/A"


def extrair_natureza(texto):
    """Extrai a natureza da ação do parecer markdown"""
    match = re.search(r'\*\*Natureza:\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    
    match = re.search(r'\*\*Tipo de Ação:\*\* (.+)', texto)
    if match:
        return match.group(1).strip()
    
    return "N/A"


def buscar_html_correspondente(caminho_json, pasta_html="pareceres_html"):
    """Busca o arquivo HTML correspondente ao JSON"""
    pasta_html_path = Path(pasta_html)
    
    if not pasta_html_path.exists():
        return None
    
    # Extrai o nome base do arquivo JSON
    nome_base = Path(caminho_json).stem
    
    # Tenta diferentes padrões de nomes
    padroes = [
        f"{nome_base}.html",
        f"parecer_{nome_base}.html",
        f"relatorio_{nome_base}.html",
    ]
    
    # Busca por número de processo no nome
    for arquivo_html in pasta_html_path.glob("*.html"):
        for padrao in padroes:
            if padrao in arquivo_html.name or nome_base in arquivo_html.name:
                return str(arquivo_html)
    
    return None


def get_badge_html(classificacao):
    """Retorna o HTML do badge de classificação"""
    classificacao_upper = str(classificacao).upper()
    
    if 'PROVÁVEL' in classificacao_upper or 'ALTO' in classificacao_upper:
        classe = 'badge-provavel'
    elif 'POSSÍVEL' in classificacao_upper or 'MÉDIO' in classificacao_upper:
        classe = 'badge-possivel'
    elif 'REMOTA' in classificacao_upper or 'BAIXO' in classificacao_upper:
        classe = 'badge-remota'
    else:
        classe = 'badge-medio'
    
    return f'<span class="{classe}">{classificacao}</span>'


def exibir_html(caminho_html):
    """Exibe o conteúdo de um arquivo HTML no Streamlit"""
    try:
        with open(caminho_html, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Exibe o HTML usando components
        st.components.v1.html(html_content, height=800, scrolling=True)
        
    except Exception as e:
        st.error(f"Erro ao carregar o HTML: {str(e)}")


def exibir_pdf_download(caminho_html):
    """Cria botão de download do HTML"""
    try:
        with open(caminho_html, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        b64 = base64.b64encode(html_content.encode()).decode()
        nome_arquivo = Path(caminho_html).name
        
        href = f'<a href="data:text/html;base64,{b64}" download="{nome_arquivo}" style="text-decoration: none;"><button style="background: linear-gradient(135deg, #1e4d6b 0%, #2a6587 100%); color: white; border: none; padding: 0.5rem 1rem; border-radius: 8px; font-weight: 600; cursor: pointer;">📥 Baixar Parecer HTML</button></a>'
        
        st.markdown(href, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Erro ao criar download: {str(e)}")


def pagina_pareceres_json(pasta_pareceres, pasta_html):
    """Página de visualização dos pareceres baseados em JSON"""
    
    # Busca os pareceres
    with st.spinner("🔍 Carregando pareceres..."):
        pareceres = buscar_pareceres_json(pasta_pareceres)
    
    if not pareceres:
        st.warning(f"⚠️ Nenhum parecer encontrado na pasta '{pasta_pareceres}'")
        st.info("💡 **Como usar:**\n\n1. Coloque os arquivos JSON dos pareceres na pasta configurada\n2. Coloque os arquivos HTML correspondentes na pasta de HTMLs\n3. Os pareceres serão listados automaticamente")
        return
    
    # Métricas
    st.subheader("📊 Resumo Geral")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Pareceres</div>
            <div class="metric-value">{len(pareceres)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        alto_risco = sum(1 for p in pareceres if 'PROVÁVEL' in str(p.get('classificacao', '')).upper() or 'ALTO' in str(p.get('classificacao', '')).upper())
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Alto Risco</div>
            <div class="metric-value">{alto_risco}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        medio_risco = sum(1 for p in pareceres if 'POSSÍVEL' in str(p.get('classificacao', '')).upper() or 'MÉDIO' in str(p.get('classificacao', '')).upper())
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Médio Risco</div>
            <div class="metric-value">{medio_risco}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        baixo_risco = sum(1 for p in pareceres if 'REMOTA' in str(p.get('classificacao', '')).upper() or 'BAIXO' in str(p.get('classificacao', '')).upper())
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Baixo Risco</div>
            <div class="metric-value">{baixo_risco}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Filtros
    st.subheader("🔍 Filtros")
    
    col1, col2 = st.columns(2)
    
    with col1:
        filtro_processo = st.text_input("🔎 Buscar por número do processo", "")
    
    with col2:
        todas_classificacoes = list(set([p.get('classificacao', 'N/A') for p in pareceres]))
        filtro_classificacao = st.selectbox(
            "📊 Filtrar por classificação",
            ["Todas"] + todas_classificacoes
        )
    
    # Aplica filtros
    pareceres_filtrados = pareceres
    
    if filtro_processo:
        pareceres_filtrados = [p for p in pareceres_filtrados if filtro_processo.upper() in str(p.get('numero_processo', '')).upper()]
    
    if filtro_classificacao != "Todas":
        pareceres_filtrados = [p for p in pareceres_filtrados if p.get('classificacao') == filtro_classificacao]
    
    st.markdown("---")
    
    # Lista de pareceres
    st.subheader(f"📋 Lista de Pareceres ({len(pareceres_filtrados)})")
    
    if not pareceres_filtrados:
        st.warning("Nenhum parecer encontrado com os filtros aplicados.")
        return
    
    # Ordena por data (mais recentes primeiro)
    pareceres_filtrados.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    
    for idx, parecer in enumerate(pareceres_filtrados):
        with st.expander(f"📄 {parecer.get('numero_processo', 'N/A')} - {parecer.get('natureza', 'N/A')[:50]}..."):
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                <div class="card">
                    <h3>Informações do Processo</h3>
                    <p><strong>Número CNJ:</strong> {parecer.get('numero_processo', 'N/A')}</p>
                    <p><strong>Parte Contrária:</strong> {parecer.get('parte_contraria', 'N/A')}</p>
                    <p><strong>Natureza:</strong> {parecer.get('natureza', 'N/A')}</p>
                    <p><strong>Valor:</strong> {parecer.get('valor', 'N/A')}</p>
                    <p><strong>Classificação:</strong> {get_badge_html(parecer.get('classificacao', 'N/A'))}</p>
                    <p><strong>Data da Análise:</strong> {parecer.get('timestamp', 'N/A')[:19]}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### 📊 Ações")
                
                # Busca HTML correspondente
                html_path = buscar_html_correspondente(parecer['arquivo'], pasta_html)
                
                if html_path:
                    if st.button(f"👁️ Visualizar Parecer", key=f"view_json_{idx}"):
                        st.session_state[f'mostrar_html_json_{idx}'] = True
                    
                    exibir_pdf_download(html_path)
                else:
                    st.warning("HTML não encontrado")
                
                st.info(f"**Arquivo:** {parecer['nome']}")
            
            # Exibe HTML se solicitado
            if st.session_state.get(f'mostrar_html_json_{idx}', False):
                st.markdown("---")
                st.markdown("### 📄 Visualização do Parecer")
                
                if st.button(f"❌ Fechar Visualização", key=f"close_json_{idx}"):
                    st.session_state[f'mostrar_html_json_{idx}'] = False
                    st.rerun()
                
                html_path = buscar_html_correspondente(parecer['arquivo'], pasta_html)
                if html_path:
                    exibir_html(html_path)


def pagina_arquivos_html(pasta_html):
    """Página de visualização de todos os arquivos HTML"""
    
    # Busca todos os arquivos HTML
    with st.spinner("🔍 Carregando arquivos HTML..."):
        arquivos_html = buscar_arquivos_html(pasta_html)
    
    if not arquivos_html:
        st.warning(f"⚠️ Nenhum arquivo HTML encontrado na pasta '{pasta_html}'")
        st.info("💡 **Dica:** Coloque os arquivos HTML dos pareceres na pasta configurada para visualizá-los aqui.")
        return
    
    # Métricas
    st.subheader("📊 Resumo dos Arquivos HTML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Arquivos</div>
            <div class="metric-value">{len(arquivos_html)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        tamanho_total = sum(a['tamanho'] for a in arquivos_html)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Tamanho Total</div>
            <div class="metric-value">{formatar_tamanho(tamanho_total)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if arquivos_html:
            mais_recente = max(arquivos_html, key=lambda x: x['timestamp_modificacao'])
            data_recente = datetime.fromtimestamp(mais_recente['timestamp_modificacao']).strftime('%d/%m/%Y')
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Última Modificação</div>
                <div class="metric-value" style="font-size: 1.5em;">{data_recente}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Filtro de busca
    st.subheader("🔍 Buscar Arquivos")
    filtro_busca = st.text_input("🔎 Buscar por nome do arquivo ou número do processo", "")
    
    # Aplica filtro
    arquivos_filtrados = arquivos_html
    if filtro_busca:
        arquivos_filtrados = [
            a for a in arquivos_html 
            if filtro_busca.upper() in a['nome'].upper() or 
               filtro_busca.upper() in str(a.get('numero_processo', '')).upper() or
               filtro_busca.upper() in str(a.get('titulo', '')).upper()
        ]
    
    st.markdown("---")
    
    # Opções de ordenação
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(f"📁 Arquivos HTML ({len(arquivos_filtrados)})")
    with col2:
        ordem = st.selectbox(
            "Ordenar por:",
            ["Mais recentes", "Mais antigos", "Nome (A-Z)", "Nome (Z-A)", "Maior tamanho", "Menor tamanho"]
        )
    
    # Ordena os arquivos
    if ordem == "Mais recentes":
        arquivos_filtrados.sort(key=lambda x: x['timestamp_modificacao'], reverse=True)
    elif ordem == "Mais antigos":
        arquivos_filtrados.sort(key=lambda x: x['timestamp_modificacao'])
    elif ordem == "Nome (A-Z)":
        arquivos_filtrados.sort(key=lambda x: x['nome'])
    elif ordem == "Nome (Z-A)":
        arquivos_filtrados.sort(key=lambda x: x['nome'], reverse=True)
    elif ordem == "Maior tamanho":
        arquivos_filtrados.sort(key=lambda x: x['tamanho'], reverse=True)
    elif ordem == "Menor tamanho":
        arquivos_filtrados.sort(key=lambda x: x['tamanho'])
    
    if not arquivos_filtrados:
        st.warning("Nenhum arquivo encontrado com os filtros aplicados.")
        return
    
    # Lista os arquivos em cards
    for idx, arquivo in enumerate(arquivos_filtrados):
        with st.expander(f"📄 {arquivo['nome']} | {arquivo['tamanho_formatado']}"):
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                <div class="html-card">
                    <h3>📋 {arquivo.get('titulo', 'Sem título')}</h3>
                    <p><strong>📁 Arquivo:</strong> {arquivo['nome']}</p>
                    <p><strong>📊 Tamanho:</strong> {arquivo['tamanho_formatado']}</p>
                    <p><strong>📅 Última modificação:</strong> {arquivo['data_modificacao']}</p>
                    <p><strong>🔢 Número do Processo:</strong> {arquivo.get('numero_processo', 'N/A')}</p>
                    <p><strong>📂 Caminho:</strong> <code>{arquivo['caminho']}</code></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### 📊 Ações")
                
                if st.button(f"👁️ Visualizar", key=f"view_html_{idx}"):
                    st.session_state[f'mostrar_html_{idx}'] = True
                
                exibir_pdf_download(arquivo['caminho'])
            
            # Exibe HTML se solicitado
            if st.session_state.get(f'mostrar_html_{idx}', False):
                st.markdown("---")
                st.markdown("### 📄 Visualização do Arquivo")
                
                if st.button(f"❌ Fechar Visualização", key=f"close_html_{idx}"):
                    st.session_state[f'mostrar_html_{idx}'] = False
                    st.rerun()
                
                exibir_html(arquivo['caminho'])


def main():
    """Função principal do aplicativo"""
    
    # Verifica autenticação antes de mostrar o conteúdo
    if not check_password():
        st.stop()  # Para a execução se não estiver autenticado
    
    # Header
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("⚖️ Sistema de Gestão de Pareceres Jurídicos")
        st.markdown("### Volpe Advogados Associados | Cliente: Unimed Cuiabá")
    
    with col2:
        st.image("LogoVolpe.jpeg" if Path("LogoVolpe.jpeg").exists() else "https://via.placeholder.com/200x80?text=Volpe", width=200)
    
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("⚙️ Configurações")
    
    pasta_pareceres = st.sidebar.text_input(
        "Pasta dos Pareceres JSON",
        value="pareceres",
        help="Pasta contendo os arquivos JSON dos pareceres"
    )
    
    pasta_html = st.sidebar.text_input(
        "Pasta dos HTMLs",
        value="pareceres_html",
        help="Pasta contendo os arquivos HTML gerados"
    )
    
    st.sidebar.markdown("---")
    
    # Seleção de visualização
    st.sidebar.header("📑 Visualização")
    modo_visualizacao = st.sidebar.radio(
        "Escolha o modo de visualização:",
        ["📊 Pareceres com JSON", "📁 Todos os Arquivos HTML"],
        help="Pareceres com JSON: visualiza pareceres estruturados com metadados\nTodos os Arquivos HTML: lista todos os HTMLs da pasta"
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### ℹ️ Informações
    
    **Pareceres com JSON:**
    - Exibe pareceres estruturados
    - Mostra métricas e classificações
    - Permite filtros avançados
    
    **Todos os Arquivos HTML:**
    - Lista todos os HTMLs da pasta
    - Útil para pareceres sem JSON
    - Permite busca por nome
    """)
    
    # Renderiza a página selecionada
    if modo_visualizacao == "📊 Pareceres com JSON":
        pagina_pareceres_json(pasta_pareceres, pasta_html)
    else:
        pagina_arquivos_html(pasta_html)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #718096; padding: 2rem 0;">
        <p><strong>Volpe Advogados Associados</strong></p>
        <p>Sistema de Gestão de Pareceres Jurídicos | Desenvolvido com Streamlit</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
