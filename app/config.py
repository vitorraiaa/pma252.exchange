import os

class Settings:
    # 3rd-party provider (default: exchangerate.host — gratuito, sem key)
    PROVIDER_BASE_URL: str = os.getenv("PROVIDER_BASE_URL", "https://api.exchangerate.host")

    # Caso mude para um provedor que exige API key
    PROVIDER_API_KEY: str | None = os.getenv("PROVIDER_API_KEY")
    PROVIDER_API_KEY_HEADER: str = os.getenv("PROVIDER_API_KEY_HEADER", "")  # ex.: "apikey" ou "x-api-key"

    # Spread em basis points (bps). 100 bps = 1.00%
    SPREAD_BPS: int = int(os.getenv("SPREAD_BPS", "100"))

settings = Settings()
