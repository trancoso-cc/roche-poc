"""
recommender_gptmodel — simple recommender backed by Azure OpenAI.

Deployment: roche-test-gpt-4.1-mini (hai-roche-ai-foundry, resource group hai-roche-poc)
Endpoint:   https://hai-roche-ai-foundry.cognitiveservices.azure.com/

    pip install "openai>=1.40"
    export AZURE_OPENAI_API_KEY="..."
    python recommender_gptmodel.py "employee wants to move from lab ops into data science"
"""

import json
import os
import sys

from openai import AzureOpenAI

ENDPOINT = "https://hai-roche-ai-foundry.cognitiveservices.azure.com/"
DEPLOYMENT = "roche-test-gpt-4.1-mini"
API_VERSION = "2024-10-21"

SYSTEM = (
    "You are a Roche internal recommender. Given a short situation, return three "
    "practical recommendations. Reply as JSON: "
    '{"recommendations": [{"title": str, "why": str}]}'
)


def recommend(situation: str) -> list[dict]:
    key = os.environ.get("AZURE_OPENAI_API_KEY")
    if not key:
        sys.exit("Set AZURE_OPENAI_API_KEY first.")

    client = AzureOpenAI(azure_endpoint=ENDPOINT, api_key=key, api_version=API_VERSION)

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": situation},
        ],
        temperature=0.2,
        max_tokens=500,
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)["recommendations"]


if __name__ == "__main__":
    situation = " ".join(sys.argv[1:]) or "employee asking how to plan a career move"

    for i, rec in enumerate(recommend(situation), 1):
        print(f"{i}. {rec['title']}")
        print(f"   {rec['why']}\n")
