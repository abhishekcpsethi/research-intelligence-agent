from src.research.arxiv_client import search_papers
from langchain.tools import tool

@tool
def search_research_papers(
    query: str,
    max_results: int = 5,
) -> list[dict]:
    """
    Search for academic research papers.

    Use this tool when research papers are needed
    for investigating a technical or scientific topic.
    """

    papers = search_papers(
        query=query,
        max_results=max_results,
    )

    return [
        {
            "title": paper.title,
            "authors": paper.authors,
            "summary": paper.summary,
            "published": paper.published.isoformat(),
            "pdf_url": paper.pdf_url,
        }
        for paper in papers
    ]