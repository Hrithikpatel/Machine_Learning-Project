from asyncio.windows_utils import pipe
from housing.pipeline.pipeline import Pipeline

def main():
    pipeline=Pipeline()
    pipeline.run_pipeline()

if "__name__"=="__main__":
    main()