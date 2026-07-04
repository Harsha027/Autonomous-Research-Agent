from ddgs import DDGS


def search_web(query: str, max_results: int = 10):
    """
    Searches the web using DDGS and returns the best search results.
    """

    trusted_domains = [
        "wikipedia.org",
        "ibm.com",
        "microsoft.com",
        "aws.amazon.com",
        "cloud.google.com",
        "developers.google.com",
        "huggingface.co",
        "nvidia.com",
        "openai.com",
        "coursera.org",
        "britannica.com",
        "geeksforgeeks.org"
    ]

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(query, max_results=max_results)

            # First keep trusted websites
            for result in search_results:

                title = result.get("title", "")
                link = result.get("href", "")
                snippet = result.get("body", "")

                if not (title and link and snippet):
                    continue

                if any(domain in link for domain in trusted_domains):

                    results.append({
                        "title": title,
                        "link": link,
                        "snippet": snippet
                    })

            # If trusted sources are fewer than 5,
            # fill remaining slots with other results.

            if len(results) < 5:

                for result in search_results:

                    title = result.get("title", "")
                    link = result.get("href", "")
                    snippet = result.get("body", "")

                    if not (title and link and snippet):
                        continue

                    if all(r["link"] != link for r in results):

                        results.append({
                            "title": title,
                            "link": link,
                            "snippet": snippet
                        })

                    if len(results) == 5:
                        break

    except Exception:
        return []

    return results