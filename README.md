1. Learn the concept of the Path and Query Parameter
2. Learn the concept of serialization, and deserialization, related it with post, and put
    Think of serialization like:    
        - Writing your thoughts (object) into a letter (JSON)
        - Sending it via post (HTTP)
        - The receiver reads it and understands it

    You can’t send raw Python objects over the internet, so they must be serialized.
    Fastapi uses the pydantic models for that purpose
    Serialization is the process of converting in-memory objects into a transportable format like JSON, while deserialization converts it back into usable objects. FastAPI uses Pydantic models to handle serialization, deserialization, and validation automatically.