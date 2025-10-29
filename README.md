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
