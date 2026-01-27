---
title: "Design System Guide"
author: "A Guide for Designers and Developers"
date: "2025-11-05"
---

# Design System Guide

## 1. Introduction

The Design System is a comprehensive library of reusable components, patterns, and guidelines that ensure visual and functional consistency across all applications. It serves as the bridge between design and development, providing a shared language for designers, developers, and product teams.

In the AI-Augmented SDLC, the Design System is a critical component of the Design Hub, enabling AI coding assistants to generate consistent, on-brand UI code.

---

## 2. Purpose and Benefits

### For Designers
- **Consistency:** Ensure all designs follow the same principles
- **Efficiency:** Reuse components instead of redesigning from scratch
- **Collaboration:** Shared language with developers

### For Developers
- **Speed:** Use pre-built components instead of building from scratch
- **Quality:** Components are tested and accessible
- **AI-Friendly:** Well-documented components enable accurate AI code generation

### For Product Teams
- **Faster Delivery:** Reduced design and development time
- **Brand Consistency:** Unified experience across products
- **Scalability:** Easy to maintain and evolve

---

## 3. Design System Structure

The Design System is organized into four layers:

```
Design System
├── Design Tokens (foundation)
├── Components (building blocks)
├── Patterns (combinations)
└── Guidelines (principles)
```

---

## 4. Design Tokens

Design tokens are the atomic design decisions that define the visual language.

### Color Palette

**Primary Colors**
- `--color-primary`: #1E40AF (Brand Blue)
- `--color-primary-dark`: #1E3A8A
- `--color-primary-light`: #3B82F6

**Semantic Colors**
- `--color-success`: #10B981 (Green)
- `--color-warning`: #F59E0B (Orange)
- `--color-error`: #EF4444 (Red)
- `--color-info`: #3B82F6 (Blue)

**Neutral Colors**
- `--color-gray-50`: #F9FAFB
- `--color-gray-100`: #F3F4F6
- `--color-gray-500`: #6B7280
- `--color-gray-900`: #111827

### Typography

**Font Families**
- `--font-primary`: "Inter", sans-serif (body text)
- `--font-heading`: "Inter", sans-serif (headings)
- `--font-mono`: "Fira Code", monospace (code)

**Font Sizes**
- `--text-xs`: 0.75rem (12px)
- `--text-sm`: 0.875rem (14px)
- `--text-base`: 1rem (16px)
- `--text-lg`: 1.125rem (18px)
- `--text-xl`: 1.25rem (20px)
- `--text-2xl`: 1.5rem (24px)
- `--text-3xl`: 1.875rem (30px)

**Font Weights**
- `--font-normal`: 400
- `--font-medium`: 500
- `--font-semibold`: 600
- `--font-bold`: 700

### Spacing

Based on 8px grid system:
- `--space-1`: 0.25rem (4px)
- `--space-2`: 0.5rem (8px)
- `--space-3`: 0.75rem (12px)
- `--space-4`: 1rem (16px)
- `--space-6`: 1.5rem (24px)
- `--space-8`: 2rem (32px)
- `--space-12`: 3rem (48px)
- `--space-16`: 4rem (64px)

### Border Radius
- `--radius-sm`: 0.25rem (4px)
- `--radius-md`: 0.5rem (8px)
- `--radius-lg`: 1rem (16px)
- `--radius-full`: 9999px (fully rounded)

### Shadows
- `--shadow-sm`: 0 1px 2px 0 rgba(0,0,0,0.05)
- `--shadow-md`: 0 4px 6px -1px rgba(0,0,0,0.1)
- `--shadow-lg`: 0 10px 15px -3px rgba(0,0,0,0.1)

---

## 5. Components

### Component Documentation Standard

Each component should be documented with:
1. **Purpose:** What problem does it solve?
2. **Anatomy:** Visual breakdown of component parts
3. **Props/Attributes:** All configurable options
4. **States:** Default, hover, active, disabled, error
5. **Accessibility:** ARIA labels, keyboard navigation
6. **Usage Guidelines:** When to use, when NOT to use
7. **Code Examples:** React/Vue/HTML examples
8. **AI Prompt Examples:** How to ask AI to generate this component

### Core Components

#### Button

**Purpose:** Trigger actions and navigation

**Variants:**
- Primary (main actions)
- Secondary (alternative actions)
- Tertiary (subtle actions)
- Danger (destructive actions)

**Sizes:** Small, Medium, Large

**States:** Default, Hover, Active, Disabled, Loading

**Example Usage:**
```jsx
<Button variant="primary" size="medium">
  Save Changes
</Button>
```

**AI Prompt Example:**
> "Create a primary button with the text 'Submit' using our design system"

---

#### Input Field

**Purpose:** Collect text input from users

**Types:** Text, Email, Password, Number, Search

**States:** Default, Focus, Error, Disabled, Success

**Includes:** Label, Input, Helper Text, Error Message

**Example Usage:**
```jsx
<Input
  label="Email Address"
  type="email"
  placeholder="you@example.com"
  helperText="We'll never share your email"
  required
/>
```

---

#### Card

**Purpose:** Group related content in a container

**Variants:**
- Default (basic container)
- Elevated (with shadow)
- Interactive (clickable)

**Example Usage:**
```jsx
<Card variant="elevated">
  <CardHeader>
    <h3>Card Title</h3>
  </CardHeader>
  <CardBody>
    <p>Card content goes here</p>
  </CardBody>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>
```

---

#### Modal/Dialog

**Purpose:** Focus user attention on a specific task

**Sizes:** Small (400px), Medium (600px), Large (800px)

**Includes:** Overlay, Container, Header, Body, Footer, Close Button

**Accessibility:** Traps focus, ESC to close, ARIA role="dialog"

---

#### Navigation Bar

**Purpose:** Primary site navigation

**Variants:**
- Horizontal (top navigation)
- Vertical (sidebar navigation)

**Includes:** Logo, Nav Items, User Menu, Mobile Toggle

---

### Component Inventory

| Component | File Location | Storybook | Status |
|-----------|--------------|-----------|--------|
| Button | `components/Button.tsx` | [Link](#) | ✅ Stable |
| Input | `components/Input.tsx` | [Link](#) | ✅ Stable |
| Card | `components/Card.tsx` | [Link](#) | ✅ Stable |
| Modal | `components/Modal.tsx` | [Link](#) | ✅ Stable |
| Navigation | `components/Navigation.tsx` | [Link](#) | 🚧 In Progress |
| Table | `components/Table.tsx` | [Link](#) | 📝 Planned |

---

## 6. Patterns

Patterns are combinations of components that solve common UI problems.

### Authentication Patterns

#### Login Form
- Email input + Password input + "Remember me" checkbox + Submit button
- "Forgot password?" link + "Sign up" link

#### Registration Form
- Name + Email + Password + Confirm Password + Terms acceptance
- Password strength indicator

### Data Display Patterns

#### Data Table with Actions
- Table + Pagination + Search + Filters + Action buttons per row

#### Dashboard Cards
- Grid of Cards with KPI metrics + Charts + Trend indicators

### Form Patterns

#### Multi-Step Form
- Step indicator + Form sections + Previous/Next navigation + Progress bar

---

## 7. Design Guidelines

### Accessibility (WCAG 2.1 AA)

**Color Contrast:**
- Text on background must meet 4.5:1 ratio minimum
- Large text (18pt+) must meet 3:1 ratio minimum

**Keyboard Navigation:**
- All interactive elements must be keyboard accessible
- Focus indicators must be visible (outline or border)
- Tab order must be logical

**Screen Readers:**
- All images need alt text
- Forms need proper labels
- Use semantic HTML
- ARIA labels where needed

### Responsive Design

**Breakpoints:**
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

**Guidelines:**
- Mobile-first approach
- Touch targets minimum 44x44px
- Test on real devices

### Animation and Motion

**Principles:**
- **Purposeful:** Animations should enhance UX, not distract
- **Performant:** Use CSS transforms (translate, scale) over position
- **Respectful:** Honor `prefers-reduced-motion` for accessibility

**Duration:**
- Quick: 150ms (micro-interactions)
- Medium: 300ms (component transitions)
- Slow: 500ms (page transitions)

**Easing:**
- `ease-out`: Entering animations
- `ease-in`: Exiting animations
- `ease-in-out`: Transitions

---

## 8. Using the Design System in Stories

When creating AI-Ready Stories, reference the Design System:

**In the "Context & Links" section:**
```markdown
## Context & Links
- **Parent Epic:** PROJ-123
- **PRD:** [Link to PRD]
- **API Contract:** [Link to OpenAPI spec]
- **Design Hub:**
  - **Wireframe:** [Link to wireframe]
  - **Components:** Button (Primary), Input (Email), Card (Elevated)
  - **Pattern:** Login Form Pattern
```

**In the "AI Collaboration Plan" section:**
```markdown
## AI Collaboration Plan
1. **You (Developer):** Review the Login Form Pattern in the Design System
2. **AI Assistant:** "Generate a login form using our design system's Button and Input components, following the Login Form Pattern"
3. **You:** Integrate with authentication API
4. **AI Assistant:** "Generate form validation using our Input component's error states"
```

This ensures AI generates code that matches your design system.

---

## 9. Governance and Evolution

### Adding New Components

1. **Proposal:** Designer proposes new component with use case
2. **Review:** Design team reviews for reusability and consistency
3. **Documentation:** Component fully documented per standard
4. **Implementation:** Built and tested
5. **Review & Approval:** Code review and design review
6. **Publication:** Added to Storybook and component library

### Updating Existing Components

- **Minor Updates:** Bug fixes, accessibility improvements (no approval needed)
- **Major Updates:** API changes, visual changes (requires approval)
- **Breaking Changes:** Deprecation period, migration guide required

### Deprecation Process

1. **Mark as Deprecated:** Add warning to documentation
2. **Migration Guide:** Provide alternative and migration steps
3. **Grace Period:** Minimum 3 months before removal
4. **Removal:** Delete from component library

---

## 10. Tools and Resources

### For Designers
- **Figma Library:** [Link to Figma Design System]
- **Design Tokens:** [Link to token JSON file]
- **Icon Library:** [Link to icon set]

### For Developers
- **Component Library:** [Link to npm package or repo]
- **Storybook:** [Link to Storybook instance]
- **Code Examples:** [Link to example repo]

### For Everyone
- **Design System Website:** [Link to public documentation]
- **Slack Channel:** #design-system
- **Office Hours:** Tuesdays 2-3pm

---

## 11. Integration with AI Agents

### For `Agent: Write-Stories`

When generating stories, the agent should:
- Reference specific components from the Design System
- Include links to Storybook documentation
- Specify component variants and states needed

### For `Agent: Generate-Code`

When generating UI code, the agent should:
- Import components from the design system library
- Use design tokens instead of hardcoded values
- Follow component usage patterns from documentation
- Apply accessibility guidelines automatically

**Example AI Context:**
```
You are generating React code for a user profile page.
Use our design system components:
- Import Button from '@company/design-system'
- Import Card from '@company/design-system'
- Import Input from '@company/design-system'
Use design tokens for colors: var(--color-primary)
Follow our accessibility guidelines (WCAG 2.1 AA)
Reference: [Link to Design System]
```

---

## 12. Conclusion

The Design System is a living system that evolves with our products and user needs. It balances consistency with flexibility, enabling teams to move fast while maintaining quality.

By integrating the Design System into our AI-Augmented SDLC, we ensure that AI-generated code is not just functional, but also beautiful, accessible, and on-brand.

---

## Appendix: Design Token Export Formats

### CSS Variables
```css
:root {
  --color-primary: #1E40AF;
  --text-base: 1rem;
  --space-4: 1rem;
}
```

### JavaScript/TypeScript
```typescript
export const tokens = {
  color: {
    primary: '#1E40AF',
  },
  text: {
    base: '1rem',
  },
  space: {
    4: '1rem',
  },
};
```

### JSON (for AI consumption)
```json
{
  "color": {
    "primary": "#1E40AF"
  },
  "text": {
    "base": "1rem"
  },
  "space": {
    "4": "1rem"
  }
}
```
