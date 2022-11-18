from beanie import Document


def create_query(body: dict, model: type[Document]) -> dict:
    """Create an orm query from a dict.
    Args:
        body (dict): payload.
        model (type[Document]): orm model.
    Returns:
        dict: orm query.
    """
    return {getattr(model, key): value for key, value in body.items()}
