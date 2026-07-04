from search import search_web
from summarizer import summarize_results
from llm import ask_gemini
from memory import save_history


def research(topic):
    """
    Complete autonomous research workflow.
    """

    # Save search history
    save_history(topic)

    try:
        # Generate an optimized search query
        search_prompt = f"""
You are an expert research assistant.

The user wants to research:

{topic}

Generate ONE effective web search query that is most likely to retrieve
high-quality and authoritative information.

Requirements:
- Maximum 8 words.
- Include important keywords.
- Avoid unnecessary words.
- Prefer terminology used by researchers and professionals.
- Return ONLY the search query.
"""

        optimized_query = ask_gemini(search_prompt).strip()

        print("Optimized Query:", optimized_query)

        # Search the web
        search_results = search_web(optimized_query)

        # Handle no search results
        if not search_results:
            return """
# No Results Found

Sorry, I couldn't find enough reliable information for this topic.

Please try:
- A more specific topic
- Different keywords
- Checking your internet connection.
"""

        # Generate research report using the optimized query
        # instead of the full user prompt for a cleaner title
        report = summarize_results(optimized_query, search_results)

        return report

    except Exception as e:
        return f"""
# Error

An unexpected error occurred while processing your request.

Details:
{str(e)}
"""