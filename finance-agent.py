from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.embedder.fastembed import FastEmbedEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

agent=Agent(
    model=Ollama(id="llama3.2", options={"num_ctx": 16384}),
    description="You are a Tech Financial expert specializing in Amazon company analysis!",
    instructions=[
        "Search your knowledge base for Amazon company investment and revenue.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results.",
        "Provide detailed analysis with specific numbers and percentages when available."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://s2.q4cdn.com/299287126/files/doc_financials/2024/ar/Amazon-com-Inc-2023-Shareholder-Letter.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="amazon_docs",
            search_type=SearchType.vector,
            embedder=FastEmbedEmbedder(id="BAAI/bge-small-en-v1.5"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

if agent.knowledge is not None:
    agent.knowledge.load()
    
agent.print_response("What is revenue distribution of Amazon in 2023",stream=True)

