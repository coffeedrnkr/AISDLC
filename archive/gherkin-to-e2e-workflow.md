---
title: "From Specs to Scripts: The Gherkin-to-E2E Workflow"
author: "Engineering Enablement"
date: "2025-01-24"
---

# 🚀 From Specs to Scripts: The Gherkin-to-E2E Workflow

## 1. Introduction

This document provides a concrete, step-by-step example of our defined process: taking a raw feature idea, converting it into an "AI-Ready" User Story, and witnessing how that story is automatically transformed into a robust End-to-End (E2E) test suite.

**The Golden Rule:** The quality of the automated test is directly proportional to the specificity of the Story and the Gherkin Acceptance Criteria.

---

## 2. Step 1: The Raw Requirement (Process Input)

Imagine a Product Manager (PM) comes to the team with a new feature request.

> **Raw Request:** "We need a way for users to save their favorite clothes so they can buy them later. Just a heart icon or something on the item card."

At this stage, this is **not** actionable for an AI agent. It lacks context, flow, and technical specificity.

---

## 3. Step 2: The Architecture & Design Phase (The Missing Link)

Before we can write a single Gherkin step, we must define *how* this feature will work technically. This process is often assisted by the **`Agent: Architect`**.

### 2.1 API Design (The Contract)
The Architect (or Tech Lead) updates the **Architecture Hub** with the new API definition. This is the contract that both the Frontend (and its tests) and the Backend will adhere to.

*   **Action:** Create `doc_info/architecture-hub/api-contracts/wishlist.yaml`
*   **Result:**
    ```yaml
    POST /api/wishlist/items:
      summary: Add item to wishlist
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                itemId: { type: string }
      responses:
        200:
          description: Item added successfully
    ```

### 2.2 UI Design (The Visuals)
The Designer updates the **Design Hub** (Figma) with the visual state.
*   **Action:** Define "Active" and "Inactive" states for the Heart Icon.

---

## 4. Step 3: The Refinement (The "Prompt Package")

With the Architecture and Design artifacts in place, the Tech Lead and Business Analyst (BA) generate the **AI-Ready Story**.

**Critical Addition:** They must explicitly link the UI behavior to our **Component Library** and the **API Contract** we just created.

### The Finalized Story Entry (Jira/Markdown)

**Title:** `[PROJ-201] Add "Favorite" Functionality to Item Card`

#### 1. Context & Links
*   **Epic:** `[PROJ-100] User Wishlist`
*   **Design:** `[Figma Link to "Heart" Interaction]`
*   **API Contract:** `[Link to wishlist.yaml]` (from Step 2)
*   **Data Model:** `[Link to UserWishlist Schema]`

#### 2. Gherkin Acceptance Criteria (The Test Contract)
```gherkin
Scenario: Successfully adding an item to the wishlist
  Given I am a logged-in user
  And I am viewing the "Summer Collection" grid
  When I click the "Favorite" button on the item "Blue Linen Shirt"
  Then the "Favorite" button should toggle to its "Active" state
  And I should see a toast notification saying "Added to Favorites"
  And the item count in the "Wishlist" header icon should increase by 1
```

#### 3. Technical Implementation Plan
*   **File to Modify:** `client/src/components/ItemCard.tsx`
*   **Logic:** Add `toggleFavorite` mutation calling `POST /api/wishlist/items`.
*   **UI Component:** Use the **`IconToggleButton`** from the Design System for the heart icon.
*   **UI Component:** Use the **`GlobalToast`** component for the notification.

---

## 5. Step 4: The Handover (AI Ingestion)

The story is moved to "Ready for Development." This triggers the `Agent: Generate-Tests`.

### How the AI "Thinks" (Internal Logic)

1.  **Parsing Gherkin:**
    *   It reads `When I click the "Favorite" button...` -> **Click Action**.

2.  **Resolving Layout (The "Blind" Logic):**
    *   It reads the Technical Plan: "Use `IconToggleButton`".
    *   It looks up the `IconToggleButton` spec in the library and sees it renders with `data-testid="icon-toggle-btn-{state}"`.
    *   **Result:** It knows *exactly* what selector to use without seeing the screen.

3.  **Resolving Data (The "Mock" Logic):**
    *   It reads the **API Contract** link.
    *   It knows exactly what the network request should look like (`POST /api/wishlist/items`).
    *   **Result:** It can auto-generate the `page.route` mock for the test:
        ```typescript
        await page.route('**/api/wishlist/items', route => route.fulfill({ status: 200 }));
        ```

---

## 6. Step 5: The Output (Generated Playwright Code)

The agent commits the following file to `tests/e2e/wishlist.spec.ts`:

```typescript
import { test, expect } from '@playwright/test';
import { setupUser, createCollection } from '../fixtures/test-data';

test.describe('Wishlist Functionality', () => {

  test('User can add an item to favorites', async ({ page }) => {
    // 0. Mock the API based on the Contract
    await page.route('**/api/wishlist/items', async route => {
      const json = await route.request().postDataJSON();
      expect(json.itemId).toBeDefined(); // Contract check!
      await route.fulfill({ status: 200 });
    });

    // 1. Given I am a logged-in user
    await setupUser(page);

    // 2. And I am viewing the "Summer Collection" grid
    await createCollection('Summer Collection', { items: ['Blue Linen Shirt'] });
    await page.goto('/collections/summer-collection');

    // 3. When I click the "Favorite" button on the item "Blue Linen Shirt"
    const itemCard = page.locator('article', { hasText: 'Blue Linen Shirt' });
    const favoriteBtn = itemCard.locator('[data-testid="icon-toggle-btn"]');
    await favoriteBtn.click();

    // 4. Then the "Favorite" button should toggle to its "Active" state
    await expect(favoriteBtn).toHaveAttribute('data-active', 'true');

    // 5. And I should see a toast notification
    const toast = page.locator('[data-testid="global-toast"]');
    await expect(toast).toContainText('Added to Favorites');
  });
});
```

---

## 7. Summary

| Input | Process | Output |
| :--- | :--- | :--- |
| **API Contract** (YAML) | Agent learns **Network Calls** | **Auto-Mocking** |
| **Story** (Text) | Engineer specifies **Components** | **Precise Selectors** |
| **Gherkin** (Behavior) | AI maps steps to **Playwright API** | **Executable Script** |
