from sqlmodel import Session, select
from .models import Payload
from .cache import get_or_create_transformed, generate_cache_key

def create_or_get_payload(session: Session, list_1, list_2):
    cache_key = generate_cache_key(list_1, list_2)

    existing = session.exec(
        select(Payload).where(Payload.cache_key == cache_key)
    ).first()

    if existing:
        return existing

    transformed_output = []

    for a, b in zip(list_1, list_2):
        transformed_output.append(get_or_create_transformed(session, a))
        transformed_output.append(get_or_create_transformed(session, b))

    output_string = ", ".join(transformed_output)

    payload = Payload(
        cache_key=cache_key,
        output=output_string
    )

    session.add(payload)
    session.commit()
    session.refresh(payload)

    return payload
