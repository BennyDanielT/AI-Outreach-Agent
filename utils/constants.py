import os

api_key = os.environ.get("GOOGLE_API_KEY")
cx = os.environ.get("CX_KEY")


SEARCH_ENGINE_URL = (
    f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_terms}"
)
