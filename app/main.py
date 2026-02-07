from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, select

from .database import engine, get_session
from .schemas import PayloadCreate, PayloadResponse, PayloadOutput
from .crud import create_or_get_payload
from .models import Payload

app = FastAPI(title="Caching Service")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/payload", response_model=PayloadResponse)
def create_payload(
    data: PayloadCreate,
    session: Session = Depends(get_session)
):
    if len(data.list_1) != len(data.list_2):
        raise HTTPException(status_code=400, detail="Lists must be of equal length")

    payload = create_or_get_payload(
        session,
        data.list_1,
        data.list_2
    )

    return {"id": payload.id}

@app.get("/payload/{payload_id}", response_model=PayloadOutput)
def get_payload(
    payload_id: int,
    session: Session = Depends(get_session)
):
    payload = session.exec(
        select(Payload).where(Payload.id == payload_id)
    ).first()

    if not payload:
        raise HTTPException(status_code=404, detail="Payload not found")

    return {"output": payload.output}
