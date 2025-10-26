# Hedera A2A Agents Backend

🚀 **Proyecto Backend para Agentes A2A en Hedera**  

Este proyecto implementa un backend de prueba para agentes A2A (**Agent-to-Agent**) usando **FastAPI**, conexión a Hedera Testnet y un bridge Node.js para liquidación de tokens. Incluye un contrato inteligente **StableCoin** en Solidity desplegable en redes EVM compatibles de Hedera.  

---

## 🔹 Características

- Backend en **FastAPI** con endpoints para:
  - Registro y login de usuarios
  - Recepción de mensajes A2A (JSON-RPC 2.0)
  - Creación de `PaymentIntent` para transferencias HTS o ERC20
- Gestión de **AES-GCM encryption** para mensajes
- Bridge mínimo en **Node.js** que simula transferencias de tokens
- Contrato **StableCoin** en Solidity (ERC-20)
- Conexión a **Hedera Testnet** usando claves de prueba

---

## 📂 Estructura del Proyecto

hedera_a2a_agents/
│
├─ backend/ # FastAPI backend
│ ├─ agents/ # Lógica A2A
│ ├─ core/ # Configuración, DB, seguridad
│ ├─ routers/ # Endpoints FastAPI
│ ├─ utils/ # Helpers de cifrado
│ └─ main.py # App FastAPI principal
│
├─ bridge/ # Bridge Node.js (simulación de transacciones)
│
├─ contracts/ # Contratos Solidity para Foundry
│ └─ StableCoin.sol
│
├─ stablecoin/ # Submódulo o contrato importado (dependencia)
│
├─ static/ # CSS y JS
├─ templates/ # HTML para panel de control
├─ package.json # Dependencias Node.js
└─ README.md

🛠️ Configuración

Crear archivo .env en el backend:

HEDERA_ACCOUNT_ID=0.0.xxxxxx
HEDERA_PRIVATE_KEY=302e...
HEDERA_NETWORK=testnet
PORT=3001
AES_KEY_B64=<clave_base64_generada>


Inicializar virtual environment Python:

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt


Inicializar base de datos SQLite (dev) y crear tablas:

uvicorn backend.main:app --reload

🚀 Ejecución
Backend FastAPI
uvicorn backend.main:app --reload


Acceder a: http://127.0.0.1:8000

Bridge Node.js
cd bridge
node index.js


Escuchará en http://localhost:3001

💳 Uso de PaymentIntent

Ejemplo JSON para POST /payments/create:

{
  "payer": "0.0.12345",
  "payee": "0.0.67890",
  "amount": 100,
  "currency": "HTS",
  "token_id": "0.0.54321"
}

🏦 StableCoin (ERC-20)

Contrato StableCoin.sol compatible con EVM

Funciones:

mint(address to, uint256 amount) – solo owner

burn(address from, uint256 amount) – solo owner

Se puede desplegar con Foundry:

forge script script/DeployStableCoin.s.sol --broadcast

📜 Licencia

MIT License © 2025
