@echo off
REM Script de Inicialização do Sistema de Pareceres
REM Volpe Advogados Associados

echo ==================================================
echo   SISTEMA DE GESTÃO DE PARECERES JURÍDICOS
echo   Volpe Advogados Associados
echo ==================================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

echo ✓ Python encontrado

REM Verifica se as dependências estão instaladas
python -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 Instalando dependências...
    pip install -r requirements.txt
    echo ✓ Dependências instaladas
) else (
    echo ✓ Dependências já instaladas
)

REM Verifica estrutura de pastas
if not exist "pareceres" (
    echo 📁 Criando pasta 'pareceres'...
    mkdir pareceres
)

if not exist "pareceres_html" (
    echo 📁 Criando pasta 'pareceres_html'...
    mkdir pareceres_html
)

echo ✓ Estrutura de pastas OK
echo.

REM Conta arquivos
dir /b pareceres\*.json 2>nul | find /c /v "" > temp_count.txt
set /p num_jsons=<temp_count.txt
del temp_count.txt

dir /b pareceres_html\*.html 2>nul | find /c /v "" > temp_count.txt
set /p num_htmls=<temp_count.txt
del temp_count.txt

echo 📊 Status:
echo    - Pareceres JSON: %num_jsons%
echo    - Pareceres HTML: %num_htmls%
echo.

REM Se há JSONs mas poucos HTMLs, oferece processar
if %num_jsons% gtr 0 (
    if %num_htmls% lss %num_jsons% (
        echo 💡 Existem pareceres JSON que ainda não foram processados.
        set /p processar="   Deseja processar todos os pareceres agora? (s/n) "
        if /i "%processar%"=="s" (
            python processar_lote.py
        )
    )
)

echo.
echo 🚀 Iniciando aplicativo Streamlit...
echo.
echo ==================================================
echo   O aplicativo abrirá automaticamente no navegador
echo   URL: http://localhost:8501
echo   Pressione Ctrl+C para encerrar
echo ==================================================
echo.

streamlit run app_pareceres.py

pause
