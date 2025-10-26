from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import payments, auth, a2a

app = FastAPI(title="Hedera A2A Backend")

# Servir archivos estáticos y templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Incluir routers de la app
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(a2a.router, prefix="/a2a", tags=["A2A"])
