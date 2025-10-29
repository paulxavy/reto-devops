# DevOps Pipeline 

## Resumen
Microservicio FastAPI que expone `POST /DevOps` protegido con:
- API Key header `X-Parse-REST-API-Key` (valor por defecto: `2f5ae96c-b558-4c7b-a590-a501ae1c3f6c`)
- JWT header `X-JWT-KWY` (firmado con HS256 y `JWT_SECRET`)

La respuesta esperada al enviar el JSON:
{
  "message": "Hello <to> your message will be sent"
}

Cualquier método distinto a POST sobre `/DevOps` responde `ERROR`.

## Estructura del proyecto
```
.
├── .github/
│   └── workflows/
│       └── devops.yml               
│
├── app/
│   ├── __init__.py
│   ├── config.py                    
│   ├── main.py                      
│   └── schemas.py                   
│
├── infra/
│   ├── kubernetes/
│   │   ├── deployment.yaml          
│   │   └── service.yaml             
│   └── terraform/
│       ├── main.tf                  
│       ├── outputs.tf               
│       ├── provider.tf              
│       ├── terraform.tfvars        
│       └── variables.tf             
│
├── tests/
│   └── test_app.py                  
│
├── .dockerignore
├── .env.example                     
├── .flake8                          
├── Dockerfile                       
├── gen_jwt.py                       
├── requirements.txt                 
└── README.md                        

```

## Requisitos
- Docker
- Python 3.11 (si quieres ejecutar gen_jwt.py local sin Docker)

## Ejecutar local con Docker (recomendado)
1. Copia `.env.example` a `.env` y ajusta valores:
   ```bash
   cp .env.example .env
   # editar .env -> cambiar JWT_SECRET a algo seguro
   ```

2. Construir imagen:
   ```bash
   docker build -t devops-challenge:local .
   ```

3. Ejecutar contenedor usando el .env:
   ```bash
   docker run --env-file .env -p 8090:8090 devops-challenge:local
   ```

4. Generar JWT (desde tu máquina local):
   ```bash
   export JWT_SECRET=$(grep JWT_SECRET .env | cut -d'=' -f2)
   python3 gen_jwt.py --exp 120
   # copia el token
   ```

5. Probar con curl:
   ```bash
   JWT=<token_generado>
   curl -X POST \
     -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
     -H "X-JWT-KWY: ${JWT}" \
     -H "Content-Type: application/json" \
     -d '{ "message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45 }' \
     http://localhost:8090/DevOps
   ```

## Ejecutar sin Docker (solo para desarrollo)
1. Instalar dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Exportar vars y ejecutar:
   ```bash
   export API_KEY=2f5ae96c-b558-4c7b-a590-a501ae1c3f6c
   export JWT_SECRET=mi_secret_seguro
   uvicorn app.main:app --host 0.0.0.0 --port 8090
   ```

## Tests
Para ejecutar tests:
```bash
pytest --cov=app
```

## Notas de seguridad
- NO subir `.env` con secretos al repo. Usa GitHub Secrets para pipeline y Kubernetes Secrets para despliegue.
- JWT_SECRET debe ser una cadena segura en producción.
