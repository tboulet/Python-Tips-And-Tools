from hydra import main
from omegaconf import DictConfig


@main(version_base=None, config_path="configs", config_name="config1")
def main_fn(config : DictConfig) -> None:
    print(config)

if __name__ == "__main__":
    main_fn()