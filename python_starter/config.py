class Config:
    GREETING = "Hey there!"

    def __init__(self) -> None:
        raise PermissionError("Cannot instantiate config container class")
