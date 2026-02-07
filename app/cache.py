import hashlib
from sqlmodel import Session, select
from .models import TransformedString

def transformer_function(value: str) -> str:
    return value.upper()

def get_or_create_transformed(session: Session, value: str) -> str:
    statement = select(TransformedString).where(
        TransformedString.original == value
    )
    result = session.exec(statement).first()

    if result:
        return result.transformed

    transformed = transformer_function(value)
    record = TransformedString(
        original=value,
        transformed=transformed
    )
    session.add(record)
    session.commit()
    session.refresh(record)

    return transformed

def generate_cache_key(list_1, list_2) -> str:
    combined = "|".join(list_1) + "||" + "|".join(list_2)
    return hashlib.sha256(combined.encode()).hexdigest()
