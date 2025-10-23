import os

class Settings:
 
    PROVIDER_BASE_URL: str = os.getenv("PROVIDER_BASE_URL", "https://api.exchangerate.host")


    PROVIDER_API_KEY: str | None = os.getenv("PROVIDER_API_KEY")
    PROVIDER_API_KEY_HEADER: str = os.getenv("PROVIDER_API_KEY_HEADER", "")  #

    SPREAD_BPS: int = int(os.getenv("SPREAD_BPS", "100"))

settings = Settings()
