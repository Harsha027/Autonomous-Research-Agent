from llm import ask_gemini


def summarize_results(topic, search_results):
    """
    Uses Gemini to analyze search results and generate
    a professional research report.
    """

    # Clean title
    report_title = topic.replace("Overview", "")
    report_title = report_title.replace("overview", "")
    report_title = report_title.replace("Fundamentals", "")
    report_title = report_title.replace("fundamentals", "")
    report_title = report_title.replace("Introduction", "")
    report_title = report_title.replace("introduction", "")
    report_title = report_title.strip(" :-")

    combined_text = ""

    for result in search_results:
        combined_text += f"""
Title: {result['title']}
Snippet: {result['snippet']}
Source: {result['link']}

"""

    prompt = f"""
You are an expert AI Research Analyst.

Your task is to create a high-quality research report using ONLY the information provided below.

Research Topic:
{report_title}

Collected Search Results:

{combined_text}

Instructions:

1. Read all search results carefully.
2. Remove duplicate information.
3. Merge similar ideas.
4. Prefer information that appears consistently across multiple sources.
5. Ignore weak or repetitive statements.
6. Prefer information from authoritative and trusted sources.
7. Do NOT invent facts.
8. Use only the provided search results.

Generate the report using exactly this structure.

# Research Report: {report_title}

## Key Points
- Write 5 to 7 concise bullet points.

## Important Findings
- Explain the topic in 2–4 well-structured paragraphs.

## References
- List ONLY the URLs from the provided search results.
- One URL per line.
- Do not modify URLs.
- Never merge multiple URLs into one line.

## Actionable Insights
- Provide 4–6 practical recommendations.

Formatting Rules:
- Use Markdown headings.
- Keep the report professional.
- Avoid repetition.
"""

    return ask_gemini(prompt)