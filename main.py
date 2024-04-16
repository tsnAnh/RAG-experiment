import os

import langchain
from langchain_community.llms import Ollama
from langchain_community.document_loaders import GithubFileLoader
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')

loader = GithubFileLoader(
    repo="tsnAnh/flutter-bloc-base-source-code",
    access_token=TOKEN,
    github_api_url="https://api.github.com",
    file_filter=lambda file_path: file_path.endswith(
        ".dart"
    ),
)
loader.branch = 'development'

documents = loader.load()
print(documents)
