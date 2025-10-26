// bridge/index.js
/**
 * Bridge mínimo que expone endpoints para transferir tokens.
 * En producción reemplaza la implementación por Hedera Agent Kit / hedera-sdk-js.
 */
import express from "express";
import bodyParser from "body-parser";
import dotenv from "dotenv";
import axios from "axios";

dotenv.config();
const app = express();
app.use(bodyParser.json());

const PORT = process.env.PORT || 3001;

// ------------------------------------------------------------------
// STUBs: en local devolvemos un objeto simulado.
// Reemplazar con llamadas al Hedera SDK real.
app.post("/transfer-hts", async (req, res) => {
    try {
    const { tokenId, toAccount, amount } = req.body;
    // TODO: llamar a Hedera SDK para transferir HTS
    // Aquí devolvemos un resultado falso para desarrollo
    const fakeTx = { txId: `0.0.0-hts-${Date.now()}`, tokenId, toAccount, amount };
    return res.json({ status: "ok", tx: fakeTx });
    } catch (err) {
    console.error(err);
    return res.status(500).json({ error: err.message });
    }
});

app.post("/transfer-erc20", async (req, res) => {
    try {
    const { contract, to, amount } = req.body;
    // TODO: llamar a Hedera EVM via relé JSON-RPC o hedera-sdk-js
    const fakeTx = { txId: `0.0.0-erc20-${Date.now()}`, contract, to, amount };
    return res.json({ status: "ok", tx: fakeTx });
    } catch (err) {
    console.error(err);
    return res.status(500).json({ error: err.message });
    }
});

app.listen(PORT, () => {
    console.log(`Bridge (stub) escuchando en puerto ${PORT}`);
});
