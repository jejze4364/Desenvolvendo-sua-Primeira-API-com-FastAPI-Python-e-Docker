# 🚀 Desenvolvendo sua Primeira API com FastAPI, Python e Docker
Este projeto foi desenvolvido como parte do desafio prático da DIO (Digital Innovation One), com o objetivo de aplicar conceitos de desenvolvimento de APIs modernas utilizando FastAPI, SQLAlchemy, Docker e boas práticas de desenvolvimento web com Python.

A proposta aqui é construir uma API funcional para cadastro e gestão de atletas, com foco em performance, clareza e organização de código — tudo pronto para evoluir e ser apresentado em entrevistas técnicas. 🧠💼

✅ Funcionalidades implementadas
📌 Cadastro de Atletas com nome, CPF, centro de treinamento e categoria

🔍 Consulta com filtros (query parameters) por nome e CPF

📃 Respostas customizadas nos endpoints, com retorno apenas das informações relevantes

🛑 Tratamento de exceções de integridade: impede o cadastro de CPFs duplicados com mensagem personalizada

📄 Paginação com fastapi-pagination: controle de limite e offset nos endpoints

🐳 Ambiente containerizado com Docker para fácil execução e portabilidade

🗃️ Banco de dados com SQLAlchemy e SQLite (ou outro, se preferir)

⚙️ Como executar localmente
bash
Copiar
Editar
# 1. Clone o repositório
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

# 2. Suba o projeto com Docker
docker-compose up --build

# 3. Acesse a documentação da API
http://localhost:8000/docs
🧪 Exemplo de tratamento de exceção
Se um atleta com o mesmo CPF já estiver cadastrado:

json
Copiar
Editar
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678900"
}
➡️ HTTP Status: 303 See Other

🔗 Links úteis
Repositório base do desafio (DIO)

Documentação FastAPI

fastapi-pagination (PyPI)

✍️ Sobre o projeto
Este repositório representa uma oportunidade de aplicar o que foi aprendido ao longo do curso da DIO. A ideia é não só replicar, mas também personalizar, melhorar e evoluir esse projeto para torná-lo um item relevante no portfólio pessoal.

💬 Quer colaborar?
Comente aqui no fórum com seu usuário GitHub e venha participar com a gente desse ambiente colaborativo de estudo e desenvolvimento! 😄
