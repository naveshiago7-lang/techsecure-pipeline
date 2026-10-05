# TechSecure Solutions - Esteira CI/CD Segura (AP II DevSecOps)

Prova de conceito de uma pipeline CI/CD com segurança integrada, usando
**Python (Flask)**, **Docker**, **GitHub Actions**, **Bandit** e **Trivy**.

## Fluxo
Código -> Build -> Teste -> Security Scan -> Build da imagem -> Deploy -> Container

## Estrutura
- `app.py` - aplicação Flask (rotas `/` e `/health`)
- `test_app.py` - testes automatizados (pytest)
- `Dockerfile` - imagem da aplicação (usuário não-root, gunicorn)
- `.github/workflows/ci.yml` - pipeline
- `requirements.txt` - dependências (versões fixas)

## Rodar localmente
```bash
pip install -r requirements-dev.txt
pytest -v
docker build -t techsecure-app .
docker run -d --name techsecure-app -p 5000:5000 techsecure-app
curl http://localhost:5000/health
```

## Segurança
- **Bandit (SAST):** analisa o código Python.
- **Trivy (SCA + imagem):** procura CVEs nas dependências e na imagem Docker.

## Integrantes
(preencher)
