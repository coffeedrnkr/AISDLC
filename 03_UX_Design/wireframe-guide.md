# The Wireframe Guide

## 1. Introduction

Wireframes are a critical component of the design process in our AI-augmented SDLC. They are low-fidelity, simplified visual representations of an application's user interface (UI). Their primary purpose is to establish the basic structure, layout, and user flow of a screen or feature before any detailed design work or coding begins.

By focusing on structure over style, wireframes allow us to quickly and efficiently iterate on the user experience, ensuring that it is intuitive and aligned with user needs. They also provide essential context for our AI coding assistants, helping them to generate more accurate and relevant UI code.

## 2. The Role of Wireframes in the AI-Augmented SDLC

In our development process, wireframes serve several key purposes:

-   **Clarify Requirements:** Wireframes translate the abstract requirements of a user story into a concrete visual representation, ensuring that everyone on the team has a shared understanding of the feature.
-   **Facilitate Collaboration:** They provide a common ground for designers, developers, and product owners to discuss and refine the user experience.
-   **Guide AI Code Generation:** When a user story includes a link to a wireframe, our AI coding assistants can use it as a visual reference to generate more accurate and context-aware UI code.
-   **Accelerate Development:** By resolving structural and layout issues early in the process, wireframes help to reduce the amount of rework required during the coding and testing phases.

## 3. Creating Effective Wireframes

To be effective, wireframes should be:

-   **Low-Fidelity:** Focus on structure and layout, not on colors, fonts, or other visual details. Use simple shapes and placeholders to represent UI elements.
-   **Clear and Concise:** The wireframe should be easy to understand and should clearly communicate the intended user flow.
-   **Linked to User Stories:** Every wireframe should be directly linked to a specific user story in the "Context & Links" section. This provides the necessary context for both human developers and AI assistants.
-   **Stored in the Design Hub:** All wireframes should be stored in the `docs/ux-design/wireframes` directory.

## 4. Tools for Creating Wireframes

You can use any tool you are comfortable with to create wireframes. Some popular options include:

-   [Balsamiq](https://balsamiq.com/)
-   [Figma](https://www.figma.com/)
-   [Sketch](https://www.sketch.com/)
-   [Excalidraw](https://excalidraw.com/)

The output of these tools should be exported as an image (e.g., PNG, SVG) and placed in the `docs/ux-design/wireframes` directory.

## 5. Example Wireframe

Here is an example of a simple wireframe for a user profile page:

![User Profile Wireframe](wireframes/user-profile-wireframe.png)

This wireframe clearly shows the layout of the page, the placement of the user's profile picture and name, and the tabs for "Profile," "Account," and "Settings." This level of detail is sufficient to guide a developer and an AI assistant in building the basic structure of the page.
