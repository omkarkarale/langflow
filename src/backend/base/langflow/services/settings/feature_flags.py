from pydantic_settings import BaseSettings


class FeatureFlags(BaseSettings):
    mvp_components: bool = False
    mcp_composer: bool = False

    class Config:
        env_prefix = "LANGFLOW_FEATURE_"


FEATURE_FLAGS = FeatureFlags()
