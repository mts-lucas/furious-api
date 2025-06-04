from typing import Literal, Optional

from pydantic import Field, PostgresDsn, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Modo de Operação
    DB_MODE: Literal["sync", "async"] = Field(default="sync")
    
    # Configuração do banco de dados
    DB_ENGINE: Literal["sqlite", "postgresql"] = Field(default="sqlite")
    DB_USER: Optional[str] = Field(default=None)
    DB_PASSWORD: Optional[str] = Field(default=None)
    DB_HOST: Optional[str] = Field(default=None)
    DB_PORT: Optional[str] = Field(default=None)
    DB_NAME: Optional[str] = Field(default=None)
    
    # URL direta (sobrescreve os campos acima se especificada)
    DATABASE_URL: Optional[str] = Field(default=None)

    # Segurança
    SECRET_KEY: str = Field(default="your-secret-key")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    ALLOW_ORIGINS=Field(default=["*"])
    ALLOW_CREDENTIALS=Field(default=True)
    ALLOW_METHODS=Field(default=["*"])
    ALLOW_HEADERS=Field(default=["*"])
    CORS_CONFIG= {
        "allow_origins": ALLOW_ORIGINS,
        "allow_credentials": ALLOW_CREDENTIALS,
        "allow_methods": ALLOW_METHODS,
        "allow_headers": ALLOW_HEADERS,
    }

    # Informações do Projeto
    PROJECT_NAME: str = Field(default="FuriousAPI ToolKit Template")
    PROJECT_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: dict) -> str:
        if v:
            return v
        
        engine = values.get("DB_ENGINE")
        mode = values.get("DB_MODE")
        
        if engine == "postgresql":
            scheme = "postgresql+asyncpg" if mode == "async" else "postgresql"
            return PostgresDsn.build(
                scheme=scheme,
                username=values.get("DB_USER"),
                password=values.get("DB_PASSWORD"),
                host=values.get("DB_HOST"),
                port=values.get("DB_PORT", "5432"),
                path=values.get("DB_NAME") or "",
            )
        
        return "sqlite:///./database.db"

settings = Settings()