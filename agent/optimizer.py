# agent/optimizer.py

"""
AI Query Optimization Engine

This module:
1. Uses local LLM (Ollama) when available
2. Falls back to rule-based optimization when LLM unavailable (cloud deployment safe)
"""

def optimize_query(query):

    prompt = f"""
    You are a Snowflake database performance expert.

    Analyze this SQL query:
    {query}

    Identify:
    - performance problems
    - spill risks
    - inefficient patterns

    Then provide:
    - optimized query suggestion
    - explanation in simple English
    - expected impact on cost and performance
    """

    # -------------------------------------
    # TRY LOCAL LLM (OLLAMA)
    # -------------------------------------
    try:
        from agent.local_llm import call_local_llm
        response = call_local_llm(prompt)

        if response and len(response.strip()) > 0:
            return response

    except Exception as e:
        print("Local LLM unavailable, switching to fallback optimizer:", e)

    # -------------------------------------
    # FALLBACK OPTIMIZATION ENGINE
    # (Used in deployment environments)
    # -------------------------------------
    return rule_based_optimizer(query)


# ---------------------------------------------------
# RULE-BASED OPTIMIZATION (Cloud Safe)
# ---------------------------------------------------
def rule_based_optimizer(query):

    suggestions = []
    optimized_sql = query

    query_lower = query.lower()

    # Detect SELECT *
    if "select *" in query_lower:
        suggestions.append("Avoid SELECT *. Use only required columns to reduce scan size.")

    # Missing WHERE clause
    if "where" not in query_lower:
        suggestions.append("Add WHERE filters to reduce full table scans.")

    # No LIMIT
    if "limit" not in query_lower:
        suggestions.append("Use LIMIT when exploring large datasets.")

    # Possible join inefficiency
    if "join" in query_lower:
        suggestions.append("Ensure join keys are indexed and filtered.")

    # Simulated optimized SQL
    optimized_sql = f"""
    -- Optimized version suggestion
    SELECT required_columns
    FROM table
    WHERE appropriate_filters
    """

    explanation = """
    This query may cause large scans and increased compute usage.
    Applying filters and selecting only necessary columns reduces cost and improves execution time.
    """

    impact = """
    Expected Impact:
    - Reduced execution time
    - Lower Snowflake compute cost
    - Reduced spill risk
    - Improved warehouse stability
    """

    return f"""
    🔍 AI Optimization Result

    Original Query:
    {query}

    Suggested Optimized Query:
    {optimized_sql}

    Key Improvements:
    {chr(10).join(['- ' + s for s in suggestions])}

    Explanation:
    {explanation}

    {impact}
    """