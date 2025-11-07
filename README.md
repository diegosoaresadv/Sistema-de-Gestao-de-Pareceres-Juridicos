# Sistema de Gestão de Pareceres Jurídicos

Sistema desenvolvido para Volpe Advogados Associados - Cliente: Unimed Cuiabá

## 🔐 Configuração de Segurança

### Primeira Instalação

1. **Clone o repositório**
   ```bash
   git clone <seu-repositorio>
   cd <pasta-do-projeto>
   ```

2. **Crie o arquivo de credenciais**
   
   Copie o arquivo de exemplo:
   ```bash
   cp secrets.json.example secrets.json
   ```
   
   Ou crie manualmente um arquivo `secrets.json` na raiz do projeto com o seguinte conteúdo:
   ```json
   {
       "username": "seu_usuario",
       "password": "sua_senha"
   }
   ```

3. **IMPORTANTE: Verifique o .gitignore**
   
   O arquivo `.gitignore` já está configurado para ignorar o `secrets.json`. 
   **NUNCA** faça commit deste arquivo!
   
   Verifique se está funcionando:
   ```bash
   git status
   ```
   O arquivo `secrets.json` NÃO deve aparecer na lista de arquivos modificados.

## 📦 Instalação

1. **Instale as dependências**
   ```bash
   pip install streamlit
   ```

2. **Execute o aplicativo**
   ```bash
   streamlit run app_pareceres.py
   ```

## 📁 Estrutura de Pastas

```
.
├── app_pareceres.py          # Aplicativo principal
├── secrets.json              # Credenciais (NÃO COMMITAR!)
├── secrets.json.example      # Exemplo de configuração
├── .gitignore                # Arquivos ignorados pelo Git
├── README.md                 # Este arquivo
├── pareceres/                # Pasta com arquivos JSON
├── pareceres_html/           # Pasta com arquivos HTML
└── LogoVolpe.jpeg            # Logo (opcional)
```

## 🔒 Segurança

- ✅ As credenciais estão em arquivo separado (`secrets.json`)
- ✅ O arquivo está no `.gitignore`
- ✅ Comparação segura usando `hmac.compare_digest()`
- ✅ Senhas removidas da sessão após validação

## ⚙️ Configuração das Pastas

No sidebar do aplicativo, você pode configurar:
- **Pasta dos Pareceres JSON**: Local dos arquivos `.json`
- **Pasta dos HTMLs**: Local dos arquivos `.html`

## 🚀 Uso

1. Acesse o aplicativo no navegador
2. Faça login com suas credenciais
3. Navegue pelos pareceres usando os filtros disponíveis

## 📝 Notas para Desenvolvedores

### Compartilhando o Projeto

Quando compartilhar o código com sua equipe:

1. **NÃO** inclua o arquivo `secrets.json`
2. **Inclua** o arquivo `secrets.json.example`
3. **Instrua** cada membro da equipe a:
   - Copiar `secrets.json.example` para `secrets.json`
   - Inserir suas próprias credenciais
   - Verificar que o arquivo não aparece no `git status`

### Alterando Credenciais

Para alterar usuário ou senha, simplesmente edite o arquivo `secrets.json`:

```json
{
    "username": "novo_usuario",
    "password": "nova_senha_segura"
}
```

Salve o arquivo e reinicie a aplicação.

## 🆘 Solução de Problemas

### Erro: "Arquivo de credenciais não encontrado"

**Solução:** Crie o arquivo `secrets.json` na mesma pasta do `app_pareceres.py`

### Erro ao fazer login

**Solução:** Verifique se o `secrets.json` está no formato correto (JSON válido)

### Git está tentando commitar secrets.json

**Solução:** 
```bash
# Remove do tracking do git (se já foi adicionado)
git rm --cached secrets.json

# Verifica se o .gitignore está funcionando
git status
```

## 📞 Suporte

Para dúvidas ou problemas, entre em contato com a equipe de desenvolvimento.

---

**Volpe Advogados Associados** | Sistema desenvolvido com Streamlit
