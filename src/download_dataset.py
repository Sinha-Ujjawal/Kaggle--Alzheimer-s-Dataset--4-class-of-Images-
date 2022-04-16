from pathlib import Path
import kaggle

DATASET_NAME = "tourist55/alzheimers-dataset-4-class-of-images"
OUTPUT_PATH = Path(__file__).parent.parent / "data" / "raw"

def main():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(
        DATASET_NAME,
        path=OUTPUT_PATH,
        unzip=True,
        quiet=False,
    )


if __name__ == "__main__":
    main()
