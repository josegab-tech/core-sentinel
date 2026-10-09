from fastapi import FastAPI, HTTPException
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("coresentinel_logger")

app = FastAPI(title="CoreSentinel Target Service")

@app.get("/")
def read_root():
    logger.info("STATUS_CHECK: Serviço respondendo normalmente [200 OK]")
    return {"status": "online", "system": "CoreSentinel Active Target"}

@app.get("/error")
def trigger_error():
    logger.error("SYSTEM_FAILURE: Falha simulada na conexão com banco de dados [500 ERROR]")
    raise HTTPException(status_code=500, detail="Simulated Database Connection Failure")