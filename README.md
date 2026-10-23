# ISDB — Site institucional em Python/Django

Site vitrine para o Instituto Superior Dom Bosco, com páginas públicas e painel administrativo Django. Inclui gestão de cursos, notícias, eventos, configuração institucional e mensagens de contacto.

## Requisitos
- Python 3.10 ou superior (recomendado Python 3.12)
- pip

## Instalação no Windows
Abra o terminal na pasta `isdb-django` e execute:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Se o PowerShell bloquear a ativação, pode executar diretamente:
```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py createsuperuser
.\venv\Scripts\python.exe manage.py runserver
```

## Instalação no Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Abrir o site
- Site público: http://127.0.0.1:8000/
- Painel administrativo: http://127.0.0.1:8000/admin/

Entre no painel com o utilizador e a palavra-passe definidos no comando `createsuperuser`.

## Configurar o conteúdo
No painel, crie:
1. Uma configuração do site: nome, frase, descrição, logótipo, imagem principal, e-mail, telefone e endereço.
2. Cursos e marque-os como publicados.
3. Notícias e marque-as como publicadas.
4. Eventos, quando necessário.

O site mostra apenas os conteúdos marcados como publicados. As mensagens enviadas pelo formulário de contacto aparecem em “Mensagens de contacto” no painel.

## Antes de publicar na internet
Este projeto usa SQLite para começar localmente. Para produção, configure PostgreSQL, `DJANGO_SECRET_KEY` através de variável de ambiente, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS` com o domínio correto, HTTPS, backups e armazenamento persistente para ficheiros enviados. Configure também `python manage.py collectstatic` e um serviço de hospedagem compatível com Django. Não utilize a chave secreta de desenvolvimento em produção.

Os textos e contactos de exemplo devem ser substituídos por informação oficial do ISDB. A imagem de fundo externa é apenas ilustrativa; use imagens com autorização de utilização e o logótipo oficial.
