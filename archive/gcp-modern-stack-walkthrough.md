---
title: "The Modern Google Cloud Trace: From Code Back to PRD"
author: "Engineering Enablement"
date: "2025-01-25"
---

# ☁️ The Modern Google Cloud Trace: From Code Back to PRD

## 1. The "Golden Path" Stack

You asked to focus on the **most modern** Google Cloud components. In 2025, for a scalable, AI-powered web app, the industry standard "Golden Path" is:

1.  **Compute:** **Cloud Run** (Serverless Containers). *Why?* No clusters to manage, scales to zero, handles web + websockets.
2.  **Data:** **Firestore** (NoSQL Document Store). *Why?* Real-time sync, massive scale, flex schema perfect for app dev.
3.  **AI:** **Vertex AI** (Gemini 1.5 Pro). *Why?* Native integration, multimodal (understands images of clothes).

Let’s walk **Backwards** through each one.

---

## 2. Component 1: Cloud Run (The API Layer)

This is where your Python/FastAPI backend lives.

### Step A: The Final Code (The Destination)
**File:** `src/main.py`
```python
from fastapi import FastAPI
from .generated_client import models # <--- generated from spec!

app = FastAPI()

@app.post("/outfits/recommend", response_model=models.OutfitResponse)
async def recommend(request: models.RecommendationRequest):
    # Logic here...
    return outfit
```
*   **Modern Feature:** This runs in a Docker container that Google "spins up" only when a request comes in.

### Step B: The Spec (The Generator)
**File:** `doc_info/architecture-hub/api-contracts/clothes_picker_api.yaml`
The code above wasn't guessed. It was generated from this definition:
```yaml
paths:
  /outfits/recommend:
    post:
      requestBody: RecommendationRequest
      responses: OutfitResponse
```

### Step C: The Origin (The PRD)
**File:** `doc_info/PRD.md`
**Requirement 4.1:** "The system must provide an API endpoint that generates an outfit recommendation in under 2 seconds."
*   *Why Cloud Run?* Because the PRD said "Global Availability" and "Low Operational Cost". Cloud Run handles global scaling automatically.

---

## 3. Component 2: Firestore (The Data Layer)

This is where users, clothes, and outfits are stored.

### Step A: The Final Code (The Destination)
**File:** `src/services/clothes_repo.py`
```python
from google.cloud import firestore

client = firestore.Client()

def add_clothing_item(user_id: str, item_data: dict):
    # Modern GCP: No SQL setup needed. Just writing JSON documents.
    doc_ref = client.collection("users").document(user_id).collection("items").document()
    doc_ref.set(item_data)
```
*   **Modern Feature:** We are using **Subcollections** (`users/{id}/items/{id}`) which scales infinitely better than SQL table joins for this use case.

### Step B: The Spec (The Generator)
**File:** `doc_info/architecture-hub/data-models/clothes_picker.dbml`
The structure of `item_data` was defined here:
```dbml
Table clothing_items {
  user_id integer
  warmth_rating integer
  laundry_status varchar
}
```

### Step C: The Origin (The PRD)
**File:** `doc_info/PRD.md`
**Requirement 2.3:** "The User must be able to view their digital closet from any device, with offline support."
*   *Why Firestore?* Because the PRD requested "Mobile Offline Support" (Firestore has native offline cache SDKs) and "Hierarchical Data" (User -> Closet -> Item).

---

## 4. Component 3: Vertex AI (The Intelligence)

This is the Brain that picks the outfit.

### Step A: The Final Code (The Destination)
**File:** `src/services/stylist.py`
```python
import vertexai
from vertexai.generative_models import GenerativeModel

def pick_outfit(wardrobe, weather):
    model = GenerativeModel("gemini-1.5-pro")
    
    # Modern GCP: System Instructions are passed as config, not hardcoded strings
    response = model.generate_content(
        contents=[f"Weather: {weather}. Wardrobe: {wardrobe}"],
        system_instruction=load_prompt() # <--- Loads from config
    )
    return response.text
```

### Step B: The Spec (The Prompt Package)
**File:** `doc_info/architecture-hub/prompts/stylist_system_prompt.md`
Before we wrote Python, we wrote the "Personality" of the AI here.
> "You are a pragmatic stylist. Do not suggest Wool in Summer. prioritizing Comfort."

### Step C: The Origin (The PRD)
**File:** `doc_info/PRD.md`
**Requirement 3.0:** "The recommendation engine must understand 'style' and 'weather nuance', not just perform simple filtering."
*   *Why Vertex AI?* Because the PRD demanded "Reasoning" ("Why did you pick this?"), which a SQL query cannot do.

---

## 5. Summary Trace

| The Origin (Requirement) | The Spec (Contract) | The Final Code (Implementation) | GCP Component |
| :--- | :--- | :--- | :--- |
| **"Fast Global API"** | OpenAPI YAML | FastAPI Root | **Cloud Run** |
| **"Offline Closet"** | DBML / JSON Schema | Firestore Client | **Firestore** |
| **"Smart Advice"** | System Prompt MD | GenAI SDK | **Vertex AI** |
