import arxiv
from src.research.paper import Paper

client = arxiv.Client()

def search_papers(query: str, max_results: int = 5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    return [Paper(
        title=result.title,
        authors=[author.name for author in result.authors],
        summary=result.summary,
        published=result.published,
        pdf_url=result.pdf_url
    ) for result in client.results(search)]
