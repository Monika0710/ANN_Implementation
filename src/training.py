from yaml import parse
from src.utils.common import read_config
import argparse


def training(config_path):
    config = read_config(config_path)
    print(config)



if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config.yaml",help="configuration")
    parsed_args=args.parse_args()

    training(config_path=parsed_args.config)