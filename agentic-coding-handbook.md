# Agentic Coding Handbook - Complete Book


_This is a combined version of the entire Agentic Coding Handbook, generated automatically from all the individual markdown files._


---


# Agentic Coding Handbook

In early 2025, we set out to explore a bold question: can AI-powered development fundamentally change how we build software? After a carefully controlled experiment comparing AI-assisted and traditional teams, the answer was clear: yes, it can.

Using tools like Cursor and GitHub Copilot Agent, our AI-assisted teams delivered projects 45% faster, with high code quality and much less manual effort. But the real breakthrough was learning a new way of working. Success came from mastering a different mindset: writing clear prompts, breaking work into smaller steps, focusing on structured specifications (spec-first), and maintaining strong code review discipline to ensure quality.

Before AI agents, developers wrote every line manually and progress depended heavily on personal expertise and speed. Now, engineers orchestrate AI: guiding it with prompts, validating outputs, and accelerating development across the full stack. Tasks that took hours such as scaffolding services or building UI screens now happen in minutes.

AI Coding Agents work inside your IDE. You describe what you want in a chat interface, and the agent generates or modifies code across multiple files. They understand your project structure and external contexts (through Model Context Providers). They don't just autocomplete, they help implement real features, following your project's quality guidelines — and their suggestions reflect best practices found in public code across the industry.

The goal of this handbook is to teach you how to work with AI agents effectively and responsibly. You'll learn practical workflows that unlock faster delivery, cross-stack flexibility, and higher creativity while keeping you, the engineer, fully in control.

## Quick Navigation

The sidebar contains everything you need to master agentic coding. Here are the main sections:

### 🚀 **[Getting Started](getting-started/)**

Your first steps with AI-powered development and the mindset shift required.

### 🔄 **[Core Workflows](core-workflows/)**

Battle-tested patterns that our teams use daily to deliver high-quality software.

### 🧠 **[Prompt Engineering](prompt-engineering/)**

Master the art of communicating effectively with AI coding agents.

### 🛠️ **[Tools & Setup](tools-setup/)**

Configure your development environment for maximum effectiveness.

### 💡 **[Examples & Templates](examples/)**

Ready-to-use prompts, scripts, and documentation templates.

## Keep Reading

Start your agentic coding journey with our comprehensive guide: [Getting Started](./getting-started.md)

---

_Use the navigation sidebar to explore each section. Every page includes practical examples, common pitfalls, and step-by-step guidance to help you succeed with agentic coding._


---


# 🚀 Getting Started

Welcome to agentic coding! This section will get you up and running with AI-powered development.

In early 2025, we discovered that AI-assisted teams delivered projects 45% faster with high code quality. The key was learning a new mindset: writing clear prompts, breaking work into smaller steps, and maintaining strong code review discipline.

## What You'll Learn

- **Quick Start** - Your first steps with agentic coding tools
- **Vibe Coding** - Understanding the mindset shift required for AI collaboration
- **Real Examples** - Success stories from our team experiments

## Quick Links

- [Getting Started Guide](GETTING_STARTED.md)
- [Vibe Coding Philosophy](VIBE_CODING.md)
- [Team Experiences](TEAM_EXPERIENCES.md)

Ready to transform how you build software? Let's begin! 🚀


---


# Getting Started

To work effectively with AI coding agents at Modus Create, your first step is setting up GitHub Copilot Agent inside Visual Studio Code.

- **Install Visual Studio Code**: If you’re not already using VS Code you Download and install it here [Visual Studio Code Setup Guide](https://code.visualstudio.com/docs/setup/setup-overview);

- **Request Your GitHub Copilot Subscription**: Modus provides GitHub Copilot licenses for all engineers. Before setting up Copilot, you must request your subscription by requesting at Modus IT Service Desk Portal;

- **Install GitHub Copilot Extension**: Install the GitHub Copilot extension by following the guide at [GitHub Copilot for VS Code](https://code.visualstudio.com/docs/copilot/setup);

- **Enable GitHub Copilot Agent Mode**: As of today, April 28th 2025, Agent mode requires to be manually enabled by following the guidance at [Copilot Agent Mode Setup](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode);

After going through the above steps, you should be able to see the agent option:

![Agent Mode Enabled](./assets/agent_mode.png)

## References

- [Copilot agent mode new features in Visual Studio Code | GitHub Checkout](https://www.youtube.com/watch?v=aKx5I0Mrr9g)
- [VS Code Agent Mode Just Changed Everything](https://www.youtube.com/watch?v=dutyOc_cAEU)

## Keep Reading

[Managing the Agent Context](./CONTEX.md)


---


# Agentic Coding at Modus vs Vibe Coding

## Our Rule of Thumb

> If you wouldn’t merge that code from a human junior dev without reading it, don’t do it for an LLM either.

“Vibe coding” is a term popularized by Andrej Karpathy to describe a casual, intuition-led approach to programming with AI, where developers rely heavily on code suggestions and iterations without overthinking or deeply reviewing each step. It's most commonly used for:

- Exploration and prototyping: You lean into the AI’s suggestions, quickly iterating on ideas or building throwaway features.
- Rapid UIs and scripts: When time-to-value matters more than polish.
- Learning and discovery: Trying absurd ideas, seeing what sticks, and building intuition for how LLMs behave.

A typical vibe coding session might look like:

```
“Make the button redder.”
```

```
“Now fetch the data from that API.”
```

```
“Oops, that didn’t work — here’s the error message, fix it.”
```

> It’s fast. It's fun. But it’s not a production workflow.

## Our definition

> Agentic Coding is not about giving up control. It’s about shifting your mindset from manually writing every line of code to collaborating with AI agents to move faster, stay in flow, and reduce cognitive load — without compromising on quality or safety.

### What Agentic Coding is

- A way to speed up development using AI tools (like Copilot, Cursor, Claude, etc.) to generate scaffolds, functions, test cases, and boilerplate.
- A workflow focused on goal-driven prompting and quick iterations, reducing time spent on syntax and boilerplate so you can focus on product logic.
- A creative, exploratory process where developers guide the AI with clear intentions and validate the results critically.
- A team-level practice that works best when paired with strong code review, automated tests, and shared engineering standards.
- A mindset of "pairing with AI" — not replacing your thinking, but accelerating it.

### What Agentic Coding is not

- It's not about accepting AI suggestions blindly without review or testing.
- It's not an excuse to skip documentation, validation, or best practices.
- It’s not a replacement for design discussions, team alignment, or system thinking.
- It’s not a solo act — it benefits from shared learnings, reusable prompts, and peer review.
- It’s not a shortcut to skip understanding — it’s a tool to speed up understanding and execution.

Agentic Coding is not a license for careless software engineering. When AI becomes your coding partner, the developer's role shifts — not disappears. On our team:

- We never accept code blindly from an LLM.
- We enforce code reviews — AI-generated or not.
- We test everything. If the code hasn’t run, it doesn’t exist.
- We document AI usage decisions and implementation tradeoffs.

## Core Principles of Agentic Coding

To code with agents effectively — and responsibly — developers must adopt a mindset that balances speed with structure. The following principles guide how we approach AI-assisted software development at Modus Create:

- **Prompt with intent**: Every coding session begins with clear goals. You don’t just "ask the AI to code" — you guide it with purpose. Good prompting is focused, testable, and grounded in real requirements.
- **Work in small, shippable units**: AI is most effective when given scoped, incremental tasks. Break work down into vertical slices and implement one behavior at a time. Large, vague prompts lead to hallucination and low-quality output.
- **Stay in flow, but don’t skip validation**: Agentic coding is about reducing cognitive load — not cutting corners. Test early. Validate output. Use pre-commit hooks, linters, and self-correction loops to enforce quality along the way.
- **Use version control deliberately**: Reset when stuck. Commit often. Don’t stack partial attempts or let unclear state accumulate — clean starts are cheaper than debugging bloated AI output.
- **AI is a collaborator, not a replacement**: Your job doesn’t disappear — it evolves. You review the code, manage the plan, and make the architectural decisions. If you wouldn’t accept sloppy work from a junior developer, don’t accept it from a model either.
- **Exploration is encouraged — with boundaries**: Use common vibe coding for prototyping, learning, and generating ideas. But when you move to production, apply rigor. Reuse what works, test what matters, and document what changes.
- **Structure beats speed in the long run**: Following structured workflows (like “Explore → Plan → Code → Commit”) leads to better outcomes than fast, unstructured iteration. The fastest way to ship is building clean, testable, maintainable code — even with AI.

## References

![YC thoughts on Vibe Coding](./assets/yc_vibe_coding.png)

- [Vibe Coding Is The Future](https://www.ycombinator.com/library/ME-vibe-coding-is-the-future)
- [How To Get The Most Out Of Vibe Coding](https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding)

## Keep Reading

[Getting Started](./GETTING_STARTED.md)


---


# Team's Experiences

Please create a page under this page and share your experiences from applying the learnings from this handbook and overall learnings from your own experiments.

## Questions that are are key to be answered:

- What are the main use cases you see value using coding agents?
- What tools have you used? (Cursor, Copilot, Windsurf, Claude, Codex)
- What are the major pain points you faced and how you have overcome it?
- What are the major interesting things you learned?
- Share any rules, instructions, scripts, MCPs or other tools you have approached?
- Please make sure to share screenshots and looms to ease the understanding.

## Keep Reading

[Core Workflows](./core-workflows.md)


---


# 🔄 Core Workflows

Master the fundamental patterns that make agentic coding effective. These workflows are battle-tested approaches that our teams use daily to deliver high-quality software with AI assistance.

## Essential Workflows

Each workflow addresses a specific challenge in AI-assisted development:

- **Spec-First** - Start with clear specifications before coding
- **Test-Driven Development** - TDD adapted for AI collaboration
- **Memory Bank** - Maintain context across sessions
- **Visual Feedback** - Iterate with visual confirmation
- **Exploratory** - Understand unfamiliar codebases
- **Debug** - Systematic problem-solving with AI
- **Auto Validations** - Automated quality gates

## How to Use These Workflows

1. **Start with Spec-First** for any new feature
2. **Use Memory Bank** for complex, multi-session projects
3. **Apply TDD** when quality is critical
4. **Use Debug Workflow** when things go wrong
5. **Combine workflows** as needed for your specific context

Each workflow includes practical examples, common pitfalls, and step-by-step guidance.


---


# Workflows

Agentic coding is not just about writing code faster with AI — it’s about adopting a new way of thinking and working. It shifts the developer’s role from line-by-line author to high-leverage problem solver, using AI tools to explore, plan, scaffold, validate, and iterate. To make this shift effective and repeatable, we rely on structured workflows grounded in a set of core principles.

## Core Principles of Agentic Coding Workflows

Prompting is the new coding interface: You don’t tell the AI just what to do — you show it how to think. Clear, scoped, and iterative prompts are essential.

Work in small, testable units: Break down tasks into vertical slices. The smaller the prompt scope, the better the quality of the AI’s response.

Context is everything: AI doesn’t “know” your project unless you tell it. Use tools like prompt plans, spec.md, MCPs, and .copilot-instructions.md to load the right information.

Validate early, validate often: TDD, pre-commit hooks, and self-correction loops turn validation into part of the coding loop — not an afterthought.

AI is a collaborator, not a replacement: Human judgment is still required for architecture, edge cases, and code reviews. The AI is there to scale your intent, not to replace it.

Use Git to keep track of changes: Work with AI to chunk the work in smaller batches and keep the practice of committing to git after coding, reviewing and testing each one of the batches. If changes are made to the wrong file due hallucinations, reverting the step is easy.

## Workflows are

- **[Spec-First Approach](./WORKFLOW_SPEC_FIRST_APPROACH.md):** AI coding agents like Copilot or Cursor rely entirely on what you give them as input. If your context is vague or scattered, the AI will produce code that’s inaccurate, inconsistent, or overly generic. That’s where Spec-First approach shines: it is an practice that allows you to feed the AI a high-quality, focused scope of work, leading to better outputs with fewer corrections.

- **[Automatic Code Validations](./WORKFLOW_AUTO_VALIDATIONS.md):** A powerful capability of AI coding agents is their ability to run code validation tools, analyze the feedback, and self-correct the code until it meets all defined quality standards. This turns your prompting loop into a smarter, more reliable workflow, where the AI not only writes code but also learns from validation outputs and fixes issues automatically.

- **[Test Driven Development](./WORKFLOW_TDD.md):** Test-Driven Development (TDD) and Agentic Coding may seem like opposites — one is structured and disciplined, the other fluid and intuitive. But when paired, they create a powerful feedback loop: TDD gives structure to your flow, and Agentic coding gives speed to your structure.This combination shines when you’re working with complex logic files, such as pricing engines, rules-based validators, or multi-condition workflows. Instead of prompting the AI to generate everything at once, you describe one behavior at a time through tests — and let the AI build up the logic incrementally, safely, and cleanly.

- **[Exploratory & Refactoring Workflow](./WORKFLOW_EXPLORATORY.md):** Explore → Plan → Code → Commit, AI tools like Claude, Cursor, and GitHub Copilot are not just code generators — they are reasoning engines. When used intentionally, they can help engineers dissect complex problems, map systems, and implement safe, scalable solutions. This workflow focuses on using AI for exploration and strategy before coding begins.

- **[Visual Feedback Workflow with AI Agents](./WORKFLOW_VISUAL_FEEDBACK.md):** When working on frontends, code alone doesn’t always tell the full story. What users see — and how the UI behaves across screen sizes, states, and interactions — is critical to quality. This workflow introduces how to use screenshots and browser context as inputs for AI-assisted iteration. By pairing screenshots with prompts and augmenting context via browser-based MCPs, developers can give AI direct visibility into what’s wrong — and receive precise, design-aligned suggestions for improvement.

- **[Debugging Workflow for Agentic Coding](./WORKFLOW_DEBUG.md):** Debugging in a Agentic coding workflow is not about blindly fixing bugs — it’s about building a feedback loop where AI helps identify, explain, and resolve issues systematically. This page outlines the core techniques to debug efficiently with AI agents, using tools like Cursor, Claude, and Model Context Providers (MCPs), while maintaining speed, quality, and confidence.

- **[Memory Bank](./WORKFLOW_MEMORY_BANK.md):** AI models like Copilot and Cursor don’t have persistent memory. They forget everything when you close the tab. That’s where the Memory Bank comes in. A Memory Bank is a structured, markdown-based documentation system that acts as long-term memory for your AI agent. It allows the assistant to “remember” your project context, decisions, and progress across.

## Keep Reading

[MCP Use Cases](./MCPS.md)


---


# Spec-First Approach

AI coding agents like Copilot or Cursor rely entirely on what you give them as input. If your context is vague or scattered, the AI will produce code that’s inaccurate, inconsistent, or overly generic. That’s where Spec-First approach shines: it is an practice that allows you to feed the AI a high-quality, focused scope of work, leading to better outputs with fewer corrections.

Spec-First is about starting the agent conversation with clarity, not code. Instead of jumping into implementation, you begin by collaborating with the AI to generate a detailed, structured specification of the feature. This gives both you and the model a shared understanding before a single line of code is written.

But here’s the key: you don’t write the spec manually. You generate it by prompting the AI inside Copilot Agent Mode, with access to your codebase, using a reasoning-capable model.

## Why This Matters

- LLMs don’t read your mind. They need structured, explicit context.
- A well-written spec gives the AI a clear mental model of the feature.
- It enables prompt modularity — breaking work into smaller, action oriented and atomic level chunks.
- It makes AI collaboration more predictable, testable, and scalable.

## How to Apply Spec-First in Practice

**Open GitHub Copilot Chat in Agent Mode:** Make sure Agent Mode is active and has access to the codebase (using #codebase or context attachments). This gives the AI visibility into file structure, dependencies, and naming conventions, making its responses more grounded and accurate.

**Use a Reasoning Model:** Pick a model or enable reasoning in models like Claude Sonnet 3.7, GPT o\* or Gemini 2.5 Pro. These models excel at multi-step thinking and structured dialogue, which is ideal for generating specs. Gemini 2.5 Pro has a larger context window, which will help to write a better plan over a larger codebase.

**Create the files plan.md and todo.md:** Creating plan.md and todo.md ensures that AI coding agents work from a clear, structured understanding of the project. plan.md captures the full implementation blueprint, while todo.md breaks it into small, promptable tasks, enabling safer, more accurate code generation, better validation checkpoints, and faster, more reliable development cycles.

## Keep Reading

[Test-Driven Development](./WORKFLOW_TDD.md)


---


# Test Driven Development

Test-Driven Development (TDD) and Agentic Coding may seem like opposites — one is structured and disciplined, the other fluid and intuitive. But when paired, they create a powerful feedback loop: TDD gives structure to your flow, and Agentic coding gives speed to your structure.

This combination shines when you’re working with complex logic files, such as pricing engines, rules-based validators, or multi-condition workflows. Instead of prompting the AI to generate everything at once, you describe one behavior at a time through tests — and let the AI build up the logic incrementally, safely, and cleanly.

## Why TDD Makes Agentic Coding Better

- **Tests act as prompts:** In the AI-assisted workflow, a test becomes a natural language spec that guides the AI toward exactly the behavior you expect. Instead of saying "generate a function that filters valid emails," you say it('should return only valid emails from a mixed list') and the AI writes the code to pass that test.

- **You reduce hallucination:** The more precise the prompt (in this case, the test), the more accurate the generation.
  TDD keeps the LLM focused on small, testable goals instead of bloated implementations.

- **It builds confidence:** When every code generation step is validated by a test, you know it's working. This is crucial when you’re using AI as your pair.

- **It keeps you in flow:** Tests give you checkpoints. Instead of stopping to debug a vague output, you just write the next test and let the AI catch up.

- **It reinforces clean, behavioral thinking:** TDD forces you to describe what the code should do, not how to write it. That’s exactly how we should prompt LLMs.

## TDD Tips for Agentic Coders

- Start with high-value behavior first, not edge cases.
- Use descriptive test names — the clearer the test, the better the AI result.
- Keep test scopes tight: one behavior per prompt.
- Let the AI refactor — ask it to "clean up the logic but keep all tests green".
- Use pre-commit hooks to run tests and stop bad code from merging.

## Example of Prompt and its output

```txt
### Prompt: Generate TDD Plan from Business Logic

I’m implementing a new feature based on the following business rules from a Jira ticket.
Please help me break it down into a clear **Test-Driven Development flow**, where each step represents a test to be written and the logic to be implemented to pass it.
Output the result as a **markdown checklist** (`tdd-plan.md`) using `[ ]` for each step.
The structure should guide me to:

* Write one test at a time
* Implement just enough code to pass it
* Add more rules incrementally
* Include edge cases and input validation
* Refactor at the end if needed

Here are the business rules:

\`\`\`markdown
Feature: calculate_invoice_total(items, customer_location)

Business rules:

1. Each item has:
   - price (number)
   - quantity (integer)
   - taxable (boolean)

2. Tax rules:
   - For customers in NY: apply 8.875% tax on taxable items
   - For customers in CA: apply 7.25% tax on taxable items
   - For all other locations: apply 5% tax on taxable items
   - Non-taxable items do not receive any tax

3. Discounts:
   - If subtotal (before tax) is greater than $1,000, apply a 5% discount on the subtotal
   - If the total quantity of all items is 10 or more, subtract a $15 shipping discount from the total

4. Final total = subtotal - discounts + tax

5. Edge cases:
   - If item list is empty, return total = 0
   - If location is missing or unknown, default to 5% tax
   - Negative prices or quantities are invalid and should raise an error
\`\`\`

Format the result like this:

\`\`\`markdown
# TDD Plan: [Feature Name]

\[ ] Write test for \[simple behavior]
\[ ] Implement logic to pass test
\[ ] Write test for \[next rule]
\[ ] Update implementation to pass
\[ ] Add test for edge case \[X]
\[ ] Refactor logic for clarity
\`\`\`

You can group tests by theme if needed. Only include things that should be verified through tests.
Avoid assumptions — reason from the rules given.
Before starting creating the file, you can ask questions to the user to clarify your understanding.
Check the boxes above as you progress. This is important, DO NOT FORGET ABOUT THIS.
```

Output:

```txt
# TDD Plan: Calculate Invoice Total

## Setup

- [ ] Create the basic function structure `calculate_invoice_total(items, customer_location)`
- [ ] Set up testing framework

## Basic Functionality

- [ ] Write test for empty items list returning 0
- [ ] Implement logic to return 0 for empty items list
- [ ] Write test for calculating subtotal with a single non-taxable item
- [ ] Implement logic to calculate basic subtotal (price * quantity)
- [ ] Write test for calculating subtotal with multiple non-taxable items
- [ ] Update implementation to handle multiple items

## Tax Rules

- [ ] Write test for default tax rate (5%) with a taxable item
- [ ] Implement logic to apply default tax rate
- [ ] Write test for NY tax rate (8.875%) with taxable item
- [ ] Update implementation to handle NY tax rate
- [ ] Write test for CA tax rate (7.25%) with taxable item
- [ ] Update implementation to handle CA tax rate
- [ ] Write test for mixing taxable and non-taxable items
- [ ] Update implementation to only apply tax to taxable items

## Discount Rules

- [ ] Write test for 5% discount on subtotal > $1,000
- [ ] Implement logic for subtotal discount
- [ ] Write test for $15 shipping discount when total quantity ≥ 10
- [ ] Implement logic for shipping discount
- [ ] Write test for both discounts applying simultaneously
- [ ] Update implementation to handle both discount types

## Edge Cases and Validation

- [ ] Write test for missing location defaulting to 5% tax rate
- [ ] Update implementation to handle missing location
- [ ] Write test for unknown location defaulting to 5% tax rate
- [ ] Update implementation to handle unknown locations
- [ ] Write test for negative price validation
- [ ] Implement error handling for negative prices
- [ ] Write test for negative quantity validation
- [ ] Implement error handling for negative quantities

## Final Calculations

- [ ] Write test for final total calculation (subtotal - discounts + tax)
- [ ] Verify implementation correctly calculates final total
- [ ] Write test for complex scenario with all rules applied
- [ ] Ensure implementation handles all business rules correctly

## Refactoring (if needed)

- [ ] Refactor tax calculation into separate method for clarity
- [ ] Refactor discount calculation into separate method
- [ ] Ensure all tests still pass after refactoring
```

## References

- [TDD with Github Copilot Agent](https://www.loom.com/share/d442996affe14bdea81014183f633988)

## Keep Reading

[Automatic Code Validations](./WORKFLOW_AUTO_VALIDATIONS.md)


---


# Memory Bank

AI models like Copilot and Cursor don’t have persistent memory. They forget everything when you close the tab. That’s where the Memory Bank comes in. A Memory Bank is a structured, markdown-based documentation system that acts as long-term memory for your AI agent. It allows the assistant to “remember” your project context, decisions, and progress across sessions.

## Why It Matters

When using an AI coding agent, continuity matters. Without memory, you waste time re-explaining what the project is, what’s been done, and what patterns to follow. The Memory Bank solves this by externalizing memory into a set of files the agent can read, reference, and update.

## Typical Memory Bank Files

- `projectbrief.md:` Overall scope and goals
- `productContext.md:` UX, users, and problems being solved
- `systemPatterns.md:` Architecture, design patterns, and decisions
- `techContext.md:`Stack, dependencies, and constraints
- `activeContext.md:` Current task, context, and working notes
- `progress.md:` Status log of what’s done and what’s pending

These files live in a folder like `/memory-bank/` or `.github/copilot-instructions.md` and are read at the start of each session. Cursor or Copilot Agent can be guided via custom instructions to always load and update these files.

## How It Works in Practice

- You and the agent update the memory as you go.
- You can ask the agent to “update memory” when progress is made.
- This keeps the AI grounded and reduces hallucinations or rework.
- With an MCP server (like @alioshr/memory-bank-mcp), you can even manage memory banks across multiple projects remotely.

Benefits

- **Persistence:** Memory is retained between sessions.
- **Fewer mistakes:** Past issues and decisions are remembered.
- **Faster onboarding:** Anyone (AI or human) can quickly get up to speed.
- **Better collaboration:** Memory Bank becomes your single source of truth.

This is how we turn stateless LLMs into project-aware partners. You write code — the AI helps more effectively.

## ✅ What should live in a Memory Bank

- **Architecture decisions and design patterns:** Such as `We use hexagonal architecture in the backend. Controllers should not contain business logic.`
- **Project constraints and stack-specific rules:** Such as `Use TanStack Query for all data fetching. Avoid raw fetch or Axios.`
- **Current focus and open technical challenges:** Such as `Currently refactoring authentication flow. Login and refresh token logic is under review.`

## ❌ What should not live in a Memory Bank

- **Sensitive credentials or secrets:** Never include tokens, passwords, database URLs, or access keys — these don’t help AI and create security risks.
- **Detailed code snippets or implementation blocks:** Avoid dumping large functions or full classes — use summaries or refer to file names instead.
- **Unfiltered chat transcripts or raw meeting notes:** Keep content structured, relevant, and purposeful — memory is for context, not clutter.

## Setting Up a Memory Bank with GitHub Copilot

GitHub Copilot doesn’t have built-in memory between sessions, but you can simulate it by using project-level instruction files that act as a persistent Memory Bank. These files are automatically loaded into the model’s context when you prompt inside your project — allowing the AI to "remember" decisions, architecture, conventions, and current tasks.

## Step-by-Step Setup

- Create a `.github/copilot-instructions.m`d file: This is the file GitHub Copilot Agent will read for project-level context. It should live at the root of your project, under a `.github/` folder.
- Define the structure: We recommend structuring the file using the Memory Bank pattern from our experiment:

```txt
# projectbrief.md
Describes the overall goals of the project, what we're building, and for whom.

# productContext.md
Why this project exists, the problems it solves, user experience goals, and business context.

# systemPatterns.md
Document architecture choices, common design patterns, and preferred technical structures.

# techContext.md
Describe technologies used, external APIs, dev setup, tooling decisions, and known constraints.

# activeContext.md
Current task, recent changes, open issues, known challenges, and next steps.

# progress.md
Track completed features, blockers, and evolving decisions over time.
```

You can either embed all this content into `.github/copilot-instructions.md` or split them into files under a folder like `/memory-bank/`, then reference that folder in the Copilot instruction file.

- **Keep it in Markdown:** Both Copilot and Cursor expect markdown format. This ensures the content is readable by both humans and models.

- **Keep it short, structured, and current:** While Copilot can read up to 128K tokens (depending on the model might go up to 1mi tokens), it’s best to keep each file concise. Focus on high-value details the AI can use during code generation or review.

- **Update it regularly:** Whenever major changes are made — new architecture, refactors, or bugs fixed — update activeContext.md and progress.md. You can also prompt the AI with: `Summarize the last 3 pull requests and update activeContext.md`.

- **Optional: Use a Folder Instead of a Single File:** If your project is large or you want modular memory, you can place your Memory Bank files in a folder named /memory-bank/ and then copy summaries or key sections into .github/copilot-instructions.md. This lets humans and AIs reference the same content without overloading a single file.

## Example Instruction (for `.github/copilot-instructions.md`)

```txt
# Copilot Memory Bank

This project uses React + NestJS. All backend code should follow a hexagonal architecture. Frontend code should use TanStack Query and controlled inputs.

Use JWT for authentication and handle all errors using a standard ErrorHandler service.

Refer to the following memory files for deeper project understanding:

- `memory-bank/projectbrief.md`
- `memory-bank/systemPatterns.md`
- `memory-bank/techContext.md`
- `memory-bank/activeContext.md`
```

## References

- [How to Use a Memory Bank in Copilot](https://www.loom.com/share/152cea77575148b8af9fe8538ed30c30?sid=e3dd85c5-60e4-4d54-973c-4d4a3ff89917)
- [10x your Cursor Workflow with Memory Bank](https://www.youtube.com/watch?si=EiHdLnUQMBanl_eO&v=Uufa6flWid4&feature=youtu.be&themeRefresh=1)

## Keep Reading

[Model Context Providers (MCPs)](./MCPS.md)


---


# Visual Feedback Workflow with AI Agents

When working on frontends, code alone doesn’t always tell the full story. What users see — and how the UI behaves across screen sizes, states, and interactions — is critical to quality. This workflow introduces how to use screenshots and browser context as inputs for AI-assisted iteration.

By pairing screenshots with prompts and augmenting context via browser-based MCPs, developers can give AI direct visibility into what’s wrong — and receive precise, design-aligned suggestions for improvement.

## When to Use This Workflow

- After generating a UI screen with AI and you want to validate spacing, layout, or responsiveness
- When reviewing visual bugs reported by QA or designers
- When refactoring visual components or improving cross-browser compatibility

## Capture a Screenshot for Feedback

Use your browser’s built-in tools or a screenshot extension to capture:

- A full-page screenshot
- A clipped component or layout section
- A specific device viewport (e.g. mobile)

Save the image and drop it directly into Cursor (or Claude if supported), then use a prompt like:

```txt
Here’s what the UI looks like. The layout doesn’t match the Figma design — spacing is off and the sidebar is misaligned. What improvements can we make to align with a clean, balanced layout?
```

## Tips

- Point out specific problems (“font size too large on buttons”, “image is overflowing container”)
- Use annotations if supported by the tool (e.g., cursor artifacts or Claude screenshots)

## Add Browser Context with MCPs

For deeper debugging or responsive fixes, feed AI more signals using browser-based Modular Context Providers (MCPs):

Available Browser Contexts via MCPs:

- Console Logs Prompt: `Use browser MCP to fetch latest errors and logs. What do these console warnings mean?`
- DOM Structure Prompt: `Fetch current DOM and analyze why #sidebar has overlapping margin.`
- Network Activity Prompt: `Analyze failed network calls on page load using captured logs. Suggest fixes.`

Use a browser MCP (e.g., Chrome DevTools MCP) to automatically extract these values into context for the AI to reason about layout bugs, render issues, or API failures.

## Iterate and Apply Fixes

After analyzing the feedback, prompt the AI to generate safe changes step-by-step:

```txt
Based on the feedback, update the CSS for the header to improve vertical alignment and add spacing between nav items.
```

### Use AI to:

- Refactor layout
- Suggest style tokens from your design system
- Detect visual regressions between versions
- Repeat by capturing new screenshots after each iteration to validate progress.

### Benefits of the Visual Feedback Workflow

- Makes invisible problems visible — especially spacing, color, font, and layout inconsistencies
- Accelerates alignment with design intent (e.g., Figma specs)
- Helps non-technical stakeholders (QA, design) participate in reviews using screenshots
- Combines what the user sees with what the code is doing under the hood

## Example Prompts

```txt
Here’s a screenshot of the user profile screen. Improve the layout to match a clean card-based structure with better spacing.
```

```txt
Use the DOM structure to suggest accessibility fixes based on ARIA roles and contrast.
```

```txt
Given the failed API call shown in network logs, what’s likely missing in the fetch logic?
```

## References

- [Using Copilot with Visual Feedback](https://www.loom.com/share/a811bd60a39e4bd38073637e24101af8?sid=f3e88fab-2768-44bb-8b66-970229dbaee6)

## Keep Reading

[Debugging Workflow](./WORKFLOW_DEBUG.md)


---


# Exploratory & Refactoring Workflow

> **_Explore → Plan → Code → Commit_**

AI tools like Claude, Cursor, and GitHub Copilot are not just code generators — they are reasoning engines. When used intentionally, they can help engineers dissect complex problems, map systems, and implement safe, scalable solutions. This workflow focuses on using AI for exploration and strategy before coding begins.

## Explore – Understand the Problem & Codebase

Before jumping into implementation, prompt the AI to explore the system like a senior engineer would. Ask it to:

- Summarize how a module or flow works: `How does the authentication middleware interact with the session manager?`
- Trace dependencies or call hierarchies: `Which services rely on PaymentService?`
- Review relevant files without writing any code: `Read the files related to logging, but do not write any code yet. Just summarize what they do.`
- Visualize architecture: `Generate a component diagram showing the flow from createInvoice() to downstream services.`

This builds context and exposes unknowns before planning a solution.

## Plan – Reason Through the Solution

Once the problem is understood, ask the AI to make a plan:

- Break down the problem: `What steps are required to decouple the billing module from user management?`
- Think before acting: Use prompts like `Think hard before answering` or `Ultrathink mode: what are the tradeoffs of each solution path?`
- Identify risks or impact: `If we refactor NotificationService, what might break downstream?`
- Generate a step-by-step implementation roadmap: `Write a plan to migrate this legacy feature without regressions.`

Encourage the AI to validate assumptions and propose alternative solutions when appropriate.

## Code – Build Safely and Iteratively

With a plan in place, start coding:

- Prompt the AI to write code one slice at a time, aligned to the plan. `Implement step 1 of the plan: extract logging into a standalone module.`
- Use safety net practices:
  - Write or run unit tests before and after each change
  - Use AI to generate test cases for edge behaviors
  - Refactor in small chunks, validating at each step
  - Ask for help in keeping scope clean: `Refactor this method but keep all existing tests green.`

## Commit – Finalize, Document, and Share

Once the solution is complete:

- Ask the AI to summarize changes:
  "Generate a changelog summary and commit message based on the last 3 modified files."
- Auto-update documentation:
  "Update the README and Swagger docs to reflect changes to GET /users."
- Push and open a PR, optionally using Claude/Cursor commands like /commit, /pr, or GitHub CLI integration.

## Benefits of the Exploratory Workflow

- Reduces blind spots before writing code
- Improves reasoning, planning, and system understanding
- Supports safer, modular implementations
- Boosts onboarding speed for unfamiliar codebases
- Encourages discipline without blocking creativity

## References

- [Refactoring Code with AI Assistance](https://www.loom.com/share/bc30c068b8c54038aaa02697ea69a9bd?sid=9ba2d4db-239a-4017-838d-c3195e67fc38)

## Keep Reading

[Visual Feedback Workflow](./WORKFLOW_VISUAL_FEEDBACK.md)


---


# Debugging Workflow for Agentic Coding

Debugging in a Agentic coding workflow is not about blindly fixing bugs — it’s about building a feedback loop where AI helps identify, explain, and resolve issues systematically.

This page outlines the core techniques to debug efficiently with AI agents, using tools like Cursor, Claude, and Model Context Providers (MCPs), while maintaining speed, quality, and confidence.

## Principles Behind Agentic Debugging

- AI can think, but it needs context — error messages, logs, screenshots, and expectations.
- Debugging isn’t a guessing game — it’s a structured narrowing of possible causes.
- Reason before fixing — the best bugfixes come after deliberate analysis.
- Debugging is also about prevention — adding logs, tests, and checkpoints helps catch bugs before they escalate.

## Agentic Debugging Workflow

### Let AI iterate over its own fix and testing loop

Start with a low-stakes prompt using Agent Mode:

```txt
The login form isn’t submitting. Iterate the the loop of attempting to submit, understanding the issue and fixing.
```

Use it when the bug is simple or safe to attempt fixing directly. Cursor excels at debugging React, Next.js, or backend projects this way — particularly via terminal-aware agents.

### Prompt AI to Reason First, Then Act

Use reasoning-first prompts before allowing code changes:

```txt
List 5–7 possible causes for this issue and propose diagnostics for each. Don’t write code yet.
```

This activates Chain-of-Thought logic and prevents AI from jumping to premature fixes.

### Add Logs to Help the AI Debug

Ask the AI to inject logs or debug statements before solving:

```txt
Add logs to print input payload, validation output, and DB query results in this flow.
```

After running the app, copy the output back into the chat or attach logs using Copilot terminal or browser integrations.

### Feed Logs and Errors from the Right Contexts

Use MCPs to supply runtime feedback:

- Browser Console → for UI bugs and script failures
- Terminal Logs → for backend and test runs
- Cloud Logs → from CloudWatch, Kibana, Grafana Loki

Example prompt:

```txt
Use MCP to fetch the last logs from CloudWatch and identify the cause of the 502 error.
```

Paste logs directly when MCPs are unavailable:

```txt
This error occurred after login: TypeError: Cannot read properties of null — fix based on this trace.
```

### Investigate Code Changes via GitHub MCPs

Sometimes bugs are caused by recent commits.

Use:

```txt
Fetch the latest GitHub PRs that changed the auth.ts file. Summarize the changes and identify what could have broken session persistence.
```

This gives the AI critical historical context to connect changes to symptoms.

### Keep Debugging State Clean

- Start a new chat or agent session when context gets noisy
- Revert broken branches using version control or Cursor's "Revert to checkpoint" feature
- Prompt: `Reset the state to the last working version before commit a1b2c3.`

### Two-Stage Debugging Loop

Use this method when bugs are tricky:

- Ask AI to hypothesize and explain.
- Only implement if the plan makes sense to you.
- Favor to use TDD to execute the fix, by writing new tests and running existing ones on every change.
- Validate one step at a time — don’t let the AI go rogue across files.

Prompt:

```txt
Explain what’s broken and how to fix it, but do not modify any files yet.
```

### Preventive Debugging Practices

- Always run locally before committing. Confirm the bug is reproducible.
- Use spec.md and prompt plans to describe expectations clearly.
- Create checkpoint commits after major milestones.
- Add unit and behavior tests to document expected behavior before refactoring.

## Summary: Debugging with AI, Done Right

| **Practice**                | **Benefit**                    |
| --------------------------- | ------------------------------ |
| YOLO Mode                   | Fast fixes for obvious bugs    |
| Chain-of-Thought Prompts    | Prevents wild guesses          |
| Logging Before Fixing       | Easier diagnosis               |
| MCPs for Logs & Errors      | Real production context        |
| GitHub MCP for Code Changes | Tracks regressions             |
| Two-Stage Debugging         | Reduces rework and scope creep |
| Checkpoints & Resets        | Keeps dev environment clean    |

Debugging is where most engineers waste time. With structured prompting, context injection, and thoughtful reasoning, agentic debugging becomes a superpower — not a struggle.

## References

- [Using Copilot to Debug the Front End](https://www.loom.com/share/50de880c8ce5466d9d21c56e9d00bc30?sid=0c35aea6-596f-46e5-a9e3-3e6d6867b6fc)

## Keep Reading

[Memory Bank Workflow](./WORKFLOW_MEMORY_BANK.md)


---


# Automatic Code Validations

A powerful capability of AI coding agents is their ability to run code validation tools, analyze the feedback, and self-correct the code until it meets all defined quality standards. This turns your prompting loop into a smarter, more reliable workflow, where the AI not only writes code but also learns from validation outputs and fixes issues automatically.

## Why It Matters

In our experiment, this approach drastically reduced rework, improved code quality, and made the AI a more useful coding assistant. Instead of shipping code with hidden lint errors or poor complexity, the agent could catch and fix these issues in real time, before a human even reviewed it.

## How It Works

- The developer prompts the AI to implement a function or feature.
- The AI writes the code and runs validation scripts (linters, formatters, test suites, etc.).
- If a validation fails, the AI uses the feedback from the terminal output as new context and iterates.
- Once all validations pass, the AI can move on and proceed with committing the code.

## Example: Cognitive Complexity with Lizard

We use a pre-configured script that runs [Lizard](https://github.com/terryyin/lizard) and enforces a cognitive complexity limit of 10.

- The AI writes a new function.
- It runs the Lizard script.
- The script returns: `Function X has cognitive complexity of 15`
- The AI picks up this feedback and rewrites the function to bring complexity under the limit.

This loop can be applied to many validation tools.

## Common Validations Used in the Loop

- Linters (e.g., ESLint)
- Formatters (e.g., Prettier)
- Unit tests (e.g., Jest, Vitest)
- Code complexity analyzers (e.g., Lizard, SonarQube)
- Static analysis tools (e.g., TypeScript compiler, Horusec, Bandit)

## Git Integration with Pre-Commit / Pre-Push Hooks

This self-correction loop can also be extended to Git commands. For example:

- You ask the AI: `Stage and commit all changes that pass our validations.`
- The AI:
  - Runs the pre-commit hooks
  - Captures the output
  - Fixes any issues that arise
  - Repeats until validations pass
  - Then commits the changes

This ensures that no invalid code ever gets committed, keeping your repo clean and compliant with team rules.

## References

- [Enhancing Code Quality with AI](https://www.loom.com/share/32bd23d355d9438587d55d7a87b58ed1)

## Keep Reading

[Exploratory & Refactoring Workflow](./WORKFLOW_EXPLORATORY.md)


---


# 🧠 Prompt Engineering

Learn to communicate effectively with AI coding agents. Prompt quality was one of the most critical success factors in our experiments - good prompts led to clean, scalable code, while vague prompts caused hallucinations and wasted time.

## Why Prompt Engineering Matters

A prompt is the main way you feed task-level context to AI. Since the model can't guess what you're thinking, it relies entirely on what you say and how you say it.

**Well-crafted prompts:**

- Improve accuracy and consistency
- Reduce hallucinations
- Make AI-generated code easier to validate
- Save time during reviews and rework

## What You'll Master

- **Fundamentals** - Core principles and practical techniques
- **Advanced Methods** - Three Experts, Multiple Iterations reasoning
- **Shot Techniques** - Zero-shot, one-shot, and few-shot prompting
- **Real Examples** - Templates you can use immediately

## Core Principles

1. **Be specific** - Clear action, expected output, constraints
2. **Provide context** - File names, project structure, dependencies
3. **Break it down** - One focused task per prompt
4. **Iterate** - Refine prompts based on results
5. **Validate** - Always review and test AI output

Think of each prompt like a task you'd hand to a junior developer: detailed but focused, with clear expectations.


---


# Basics of Prompt Engineering

Prompt engineering is the practice of writing clear, structured instructions to guide AI coding agents like GitHub Copilot Agent or Cursor. Just like you'd explain a task to a junior developer, your job is to describe what you want, where to do it, and how to do it — in a way the AI can understand and act on.

During our internal experiment, we learned that prompt quality was one of the most critical success factors. Good prompts led to clean, scalable code. Vague or overly broad prompts caused hallucinations, bugs, and wasted time

## Why It Matters

A prompt is the main way you feed task-level context to the AI. Since the model can't guess what you're thinking, it relies entirely on what you say — and how you say it.

Well-crafted prompts:

- Improve accuracy and consistency
- Reduce hallucinations
- Make AI-generated code easier to validate and maintain
- Save time during reviews and rework

## Core Tips on prompting

- Start prompts with a clear action, expected output, and any important constraints.
- When possible specify the exact file, service, or component where the change should happen.
- Break large features into small, independent prompts whenever possible.
- Use "step-by-step" or "think like an expert" instructions to guide deeper reasoning.
- Attach code snippets, file names, terminal outputs, or #codebase context whenever possible.
- Treat each prompt like a task you would hand off to a junior developer: detailed but focused with clear expectations of the outcome.
- If the AI gives a bad output, refine the original prompt instead of fixing the wrong output manually.
- Validate every result manually — never trust AI output without review and testing.
- Prefer describing the "why" behind a feature when possible — it improves AI’s architectural decisions.
- Remember that vague prompts waste more time than spending a few extra seconds writing a better one.

## Prompting Fundamentals (With Practical Guidance)

Make sure to read the below pages before moving forward:

- [VSCode's Prompt engineering for Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting)
- [Github's Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)
- [Anthropic's Prompt Library](https://docs.anthropic.com/en/resources/prompt-library/library)
- [Craft Perfect AI Prompts](https://shumerprompt.com/)

## Examples

### Be clear and specific

Do:

```txt
Create a POST /users/login endpoint using NestJS. It should accept email and password, validate input, and return a JWT if credentials are correct. Use class-validator and JWT module.
```

Don’t:

```txt
Add login functionality.
```

### Define scope: one task at a time

Do:

```txt
Add email format validation to the user registration form in RegisterForm.tsx.
```

Don't (This is too broad — likely to produce incomplete or scattered results):

```txt
Finish all validations for the signup flow.
```

### Add context: Include file names, project structure, and relevant implementation details.

Do:

```txt
In auth.controller.ts, add a new endpoint that consumes authService.validateUser() and returns a JWT if valid.
Also, attach files or use the #codebase tag to help Copilot Agent or Cursor read project content.
```

### Describe expected behavior and constraints

Do:

```txt
Add unit tests for parseMedicalReport() in report.utils.ts. Cover edge cases like empty file, invalid format, and corrupted content.
```

Don't:

```txt
Write tests for report parser.
```

### Use a reasoning-first prompt format

#### Three Experts Method

```txt
Simulate three different experts answering the below questions. All experts will write down 1 step of their thinking and then share it with the group. Then all the experts will go on the next step, etc. If any expert realizes they are wrong at any point, then they leave. Stop once you have the final answer for each question.
```

#### Self-Refinement Loop

```txt
Try solving this <add context from IDE>. Then improve your answer in 3 iterations by critiquing and rewriting each version.
These methods improve architectural decisions and reduce low-quality responses.
```

#### Iterate and refine

It's normal to go through multiple prompt rounds. Use a feedback loop:

```txt
Prompt → Validate → Adjust prompt or fix code → Continue
```

> Never assume the first output is ready to merge.

## Common Pitfalls to Avoid

Too vague: Add error handling — What error? Where?

Too large: Build user profile page, backend API, tests, and styling — Break into smaller parts.

Assuming the AI knows your intent — it doesn’t. Be explicit.

Skipping validation — always review, test, and verify AI output.

## Interesting Open Source Prompts

https://shumerprompt.com/prompts/expert-conductor-reasoning-guide-prompt-2ff044e1-5e65-48b3-8004-5f51e10e4a94

https://shumerprompt.com/prompts/vibe-coding-documentation-prompt-de4b2917-b4e3-44bd-ba7c-90eb09b508cd

https://shumerprompt.com/prompts/super-prompt-generator-optimizer-prompt-22b2a360-9935-49d6-81db-684385866847

https://shumerprompt.com/prompts/o3-maximum-reasoning-prompt-71b5828e-3c09-4df3-a9b7-25ef399e8977

## References

- [Master the core principles of prompt engineering with GitHub Copilot](https://www.youtube.com/watch?v=hh1nOX14TyY)
- [Prompt engineering essentials: Getting better results from LLMs | Tutorial](https://www.youtube.com/watch?v=LAF-lACf2QY)
- [AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8)
- [Essential AI prompts for developers](https://www.youtube.com/watch?v=H3M95i4iS5c)

## Go Deeper

- [Three Experts Method](./PROMPT_THREE_EXPERTS_METHOD.md)
- [Zero-Shot, One-Shot, and Multi-Shot Prompts](./PROMPT_ZERO_ONE_N_SHOT_PROMPTS.md)
- [Multiple Iterations Reasoning Method](./PROMPT_MULTIPLE_ITERATIONS_REASONING.md)
- [See more examples here](./examples-prompts/)

## Keep Reading

[Workflows](./WORKFLOWS.md)


---


# Three Experts Method

The Three Experts prompt is a powerful reasoning pattern designed to help AI simulate deeper thinking and avoid shallow or generic responses. In agentic coding, it’s especially useful when you're working through complex architectural decisions, refactoring strategies, or debugging multi-layer issues.

This method turns the AI from a code generator into a panel of thought partners, each exploring the problem from a different angle — and converging on the most reasoned solution.

## What's the Method?

**Core Prompt Pattern:**

```txt
Simulate three different experts answering the question below.
Each expert will write down one step of their thinking and share it with the group.
Then all experts move to the next step.
If any expert realizes they're wrong at any point, they drop out.
Continue until there’s consensus on the final answer.
```

This creates a multi-step reasoning loop that encourages internal critique and deeper analysis.

| **Use Case**                              | **Why It Works**                                  |
| ----------------------------------------- | ------------------------------------------------- |
| Choosing between architectural strategies | Reveals tradeoffs in tech decisions               |
| Refactoring complex modules               | Surfaces alternative paths + risks                |
| Debugging non-obvious bugs                | Simulates root-cause analysis                     |
| Designing data models or APIs             | Balances structure, performance, and clarity      |
| Generating edge-case tests                | Experts act like QA engineers or systems thinkers |

## Example 1: Refactoring a Cross-Cutting Module

**Goal:** Decide how to refactor a shared NotificationService used across microservices.

Prompt:

```txt
Simulate three backend experts reviewing how to refactor the NotificationService, which is currently tightly coupled to both billing and auth services.
Each expert will write one step of reasoning at a time and discuss with the group.
If one is clearly wrong, they should drop out.
Keep going until they converge on a refactoring strategy that isolates the service and makes it reusable.
```

**Expected Outcome:**

- Tradeoffs discussed (e.g., pub/sub vs abstraction layer)
- Consensus reached through elimination of flawed approaches
- Final recommendation is reasoned, not guessed

## Example 2: Debugging a Non-Obvious UI State Bug

**Goal**: The UI shows stale data after login. Why?

Prompt:

```txt
Simulate three frontend engineers exploring why the dashboard shows stale user data after login.
Each one will reason step-by-step based on their own assumption:

Expert A suspects caching issues

Expert B suspects async state update problems

Expert C suspects token propagation failure
They’ll reason in steps and eliminate theories as they go.
Stop when they reach the most likely root cause.
```

**Expected Outcome:**

- Stepwise root-cause analysis
- Use of logs, network traces, or event timing
- Stronger hypothesis to guide debugging prompt

## Example 3: Designing a Robust Validation System

**Goal:** Choose between Zod, Yup, or class-validator for a multi-form web app.

Prompt:

```txt
Simulate three full-stack engineers debating which validation system to use for a multi-form onboarding flow with dynamic field types.
Each expert will write one reasoning step at a time.
Expert A prefers Zod, B prefers Yup, C prefers class-validator.
If any realize their approach won't scale or violates team standards, they should drop out.
Stop once consensus is reached.
```

**Expected Outcome:**

- Clarity on tradeoffs (TypeScript friendliness, async rules, nesting support)
- Selection based on real needs (team standards, backend integration)

## Summary: Why Use the Three Experts Pattern?

| **Benefit**                                       | **Why It Helps in Agentic Coding**              |
| ------------------------------------------------- | ----------------------------------------------- |
| Deepens reasoning                                 | Prevents superficial or default answers         |
| Simulates tradeoffs                               | Mirrors real-world team decision dynamics       |
| Reduces hallucination                             | Experts challenge each other's logic            |
| Enables exploration before code                   | Supports "reason first, code later" mindset     |
| Works well with Claude, GPT-4o, Cursor Agent Mode | High-context tools thrive on multi-step prompts |

## Bonus Variation

For complex decisions:

```txt
Simulate a system architect, a QA lead, and a product manager reasoning together.
Each shares their perspective, step-by-step, to align on a final implementation plan.
```

## References

- [Leveraging AI with the Three Experts Technique](https://www.loom.com/share/50de91feb2ca4abdbca0521d8049d81d)

## Keep Reading

[Multiple Iterations Reasoning Method](./PROMPT_MULTIPLE_ITERATIONS_REASONING.md)


---


# Multiple Iterations Reasoning Method

The Multiple Iterations Reasoning prompt is a structured approach designed to guide AI systems through progressive rounds of self-improvement. This method leverages iterative analysis and refinement to produce solutions that are more robust, optimized, and thoroughly considered.

In agentic coding, this technique is particularly valuable when dealing with complex problems that benefit from layered analysis, such as algorithm development, system architecture design, or code optimization where the first solution is rarely the best one.

## What's the Method?

**Core Prompt Pattern:**

```txt
I want you to solve the following problem/task: [DESCRIBE PROBLEM OR TASK HERE]

## Iterative Solution Process

### 1. Initial Solution
Provide a concise initial solution to the problem. Focus on core requirements and a working approach. Keep code examples minimal.

### 2. Analysis Rounds (3 iterations)
For each round:

#### a) Critical Analysis
- Strengths: What works well (2-3 key points)
- Weaknesses: Edge cases and limitations (2-3 key points)
- Potential optimizations (1-2 specific improvements)

#### b) Solution Refinement
- Implement key changes that address the most critical weaknesses
- Focus only on substantial improvements
- Note briefly what changed and why

### 3. Last Solution
Provide your optimized solution with:
- A brief summary of major improvements (2-3 sentences)
- Any remaining considerations
```

This creates a self-reflective loop that encourages the AI to critically evaluate and improve its own work multiple times.

| **Use Case**                     | **Why It Works**                                       |
| -------------------------------- | ------------------------------------------------------ |
| Algorithm optimization           | Forces consideration of edge cases and performance     |
| System design refinement         | Builds in layers of error handling and robustness      |
| Code quality improvement         | Progressively enhances readability and maintainability |
| Problem-solving with constraints | Tests solution against increasingly complex criteria   |
| Test coverage planning           | Expands from basic to comprehensive test scenarios     |

## Example 1: Optimizing a Search Algorithm

**Goal:** Develop an efficient algorithm for searching partially sorted data.

Prompt:

```txt
I want you to solve the following problem: Design an algorithm to find a target number in a partially sorted array (elements are sorted in ascending order, then rotated at some pivot).

## Iterative Solution Process

### 1. Initial Solution
Provide a concise initial solution to the problem. Focus on core requirements and a working approach. Keep code examples minimal.

### 2. Analysis Rounds (3 iterations)
For each round:

#### a) Critical Analysis
- Strengths: What works well (2-3 key points)
- Weaknesses: Edge cases and limitations (2-3 key points)
- Potential optimizations (1-2 specific improvements)

#### b) Solution Refinement
- Implement key changes that address the most critical weaknesses
- Focus only on substantial improvements
- Note briefly what changed and why

### 3. Last Solution
Provide your optimized solution with:
- A brief summary of major improvements (2-3 sentences)
- Any remaining considerations
```

**Expected Outcome:**

- Initial solution might use linear search O(n)
- First iteration might identify binary search potential
- Second iteration might handle the rotation complexity
- Final solution likely optimizes to O(log n) with detailed edge cases covered

## Example 2: Designing a Caching Strategy

**Goal:** Create a caching implementation for a data-intensive application.

Prompt:

```txt
I want you to solve the following problem: Design a caching strategy for a web application that handles thousands of product queries per minute with data that changes infrequently (once per day).

## Iterative Solution Process

### 1. Initial Solution
Provide a concise initial solution to the problem. Focus on core requirements and a working approach. Keep code examples minimal.

### 2. Analysis Rounds (3 iterations)
For each round:

#### a) Critical Analysis
- Strengths: What works well (2-3 key points)
- Weaknesses: Edge cases and limitations (2-3 key points)
- Potential optimizations (1-2 specific improvements)

#### b) Solution Refinement
- Implement key changes that address the most critical weaknesses
- Focus only on substantial improvements
- Note briefly what changed and why

### 3. Last Solution
Provide your optimized solution with:
- A brief summary of major improvements (2-3 sentences)
- Any remaining considerations
```

**Expected Outcome:**

- Initial solution might use a simple time-based cache
- Progressive iterations address invalidation strategies, memory concerns
- Later rounds might introduce Redis, cache layers, or warm-up procedures
- Final solution likely includes a comprehensive strategy with fallbacks

## Example 3: Building a Robust API Error Handling System

**Goal:** Design an error handling system for a microservice architecture.

Prompt:

```txt
I want you to solve the following problem: Design a standardized error handling system for a collection of microservices that needs to provide consistent error responses, logging, retries, and circuit breaking.

## Iterative Solution Process

### 1. Initial Solution
Provide a concise initial solution to the problem. Focus on core requirements and a working approach. Keep code examples minimal.

### 2. Analysis Rounds (3 iterations)
For each round:

#### a) Critical Analysis
- Strengths: What works well (2-3 key points)
- Weaknesses: Edge cases and limitations (2-3 key points)
- Potential optimizations (1-2 specific improvements)

#### b) Solution Refinement
- Implement key changes that address the most critical weaknesses
- Focus only on substantial improvements
- Note briefly what changed and why

### 3. Last Solution
Provide your optimized solution with:
- A brief summary of major improvements (2-3 sentences)
- Any remaining considerations
```

**Expected Outcome:**

- Initial solution might focus on basic error structure
- Middle iterations refine retry policies, circuit breaking logic
- Later iterations might add observability, error aggregation
- Final solution would be a layered approach with examples of implementation

## Summary: Why Use the Multiple Iterations Reasoning Pattern?

| **Benefit**                          | **Why It Helps in Agentic Coding**                 |
| ------------------------------------ | -------------------------------------------------- |
| Promotes depth over breadth          | Forces solutions beyond the obvious first approach |
| Documents the evolution of thinking  | Creates transparency in the solution development   |
| Identifies edge cases systematically | Reduces the "oh, I didn't think of that" factor    |
| Builds in justified refinement       | Each improvement has explicit reasoning            |
| Mimics real development processes    | Aligns with how engineers actually solve problems  |
| Works well with modern AI models     | Leverages LLM capabilities for self-critique       |

## Variations

For greater refinement in specific areas:

```txt
For iteration 2, focus specifically on performance optimization.
For iteration 3, focus exclusively on edge case handling.
```

For constrained prompting:

```txt
Limit each solution to under 50 lines of code, forcing increasingly elegant solutions.
```

## References

- [Multiple Iterations Reasoning Prompt Pattern](https://www.loom.com/share/10ecca1aa5a54eaf95669f2fe16cd56f?sid=1607557b-5d22-4d49-935e-933bdde55442)

## Keep Reading

[Zero-Shot, One-Shot, and Multi-Shot Prompts](./PROMPT_ZERO_ONE_N_SHOT_PROMPTS.md)


---


# Zero-Shot, One-Shot, and Multi-Shot Prompts

Prompting is the language of AI. In agentic coding, how you structure your prompts determines not just the quality of the code — but whether the model understands your intent at all.

This page breaks down three foundational prompting methods — Zero-Shot, One-Shot, and Multi-Shot — and demonstrates how to apply them strategically, using real-world engineering use cases with practical, reusable prompt examples.

## N-Shot Prompting

### Zero-Shot Prompting

- Tell the AI what to do without giving examples.
- Best when the task is well-known or model has strong prior knowledge.
- Risk of hallucination increases when task is ambiguous or implementation-sensitive.

### One-Shot Prompting

- Tell the AI what to do and give one example of how to do it.
- Best when you want consistency with an established pattern or want to reuse a known implementation format.

### Multi-Shot Prompting

- Give the AI multiple examples before asking it to continue the pattern.
- Best for generating multiple similar outputs (e.g., test cases, validators, endpoints) with consistent structure or formatting.

## Common use cases

| **Prompt Type** | **Ideal Use Case**                                                                                                   |
| --------------- | -------------------------------------------------------------------------------------------------------------------- |
| Zero-Shot       | Quick code snippets, refactors, doc generation, error analysis                                                       |
| One-Shot        | Repeating logic (e.g., endpoint structure, naming conventions, form components)                                      |
| Multi-Shot      | Bulk generation of tests, translation of logic across modules, repo-wide consistency (e.g., DTOs, service contracts) |

## Examples

### Writing a New API Endpoint with Specific Project Conventions

**Goal**: Create a new POST /users/invite endpoint using the same pattern as other endpoints in the project.

Zero-Shot Prompt

```txt
Write a NestJS controller method to handle POST /users/invite. It should accept email and name, call UserInviteService.inviteUser(), and return a success response or validation error.
```

Risk: Output may drift from project-specific naming, decorators, or DTO structure.

One-Shot Prompt

```txt
Here’s how we write our endpoints:

@Post('/users/register')
registerUser(@Body() body: RegisterUserDto) {
  return this.service.register(body);
}

Now create an endpoint for POST /users/invite that follows the same pattern, usingInviteUserDto and inviteUser().
```

Benefit: Ensures consistency in decorators, naming, and structure.

Multi-Shot Prompt

```txt
Here's how we write our endpoints:

@Post('/users/register')
registerUser(@Body() body: RegisterUserDto) {
  return this.service.register(body);
}

@Post('/users/reset-password')
resetPassword(@Body() body: ResetPasswordDto) {
  return this.service.resetPassword(body);
}

Now write a controller method for POST /users/invite.
```

Benefit: Enables the AI to model based on pattern, not just one instance. Useful for generating a series of aligned endpoints.

## Keep Reading

[Core Workflows](./core-workflows.md)


---


# 🛠️ Tools & Setup

Understanding the ecosystem of agentic coding tools and how to configure them for maximum effectiveness.

## AI Models & Context

- **Model Use Cases** - When to use different AI models
- **Model Context Providers (MCPs)** - Extending AI context and capabilities
- **Debugging MCPs** - Troubleshooting context providers

## Development Environment

- **IDE Setup** - Configuring Cursor, VS Code with Copilot
- **Context Management** - Maintaining project context across sessions
- **Quality Gates** - Automated validations and pre-commit hooks

## Best Practices

- **Privacy Considerations** - Handling sensitive data with AI
- **Team Guidelines** - Organization and project-specific standards
- **Debugging** - Systematic troubleshooting approaches

These tools and configurations form the foundation for effective agentic coding. Proper setup saves hours of debugging and ensures consistent, high-quality results across your team.


---


# Managing the Agent Context

Managing the agent context, especially by breaking features into smaller parts, is critical because of how LLMs work. Large Language Models can only “think” about a finite amount of information at once. When overloaded with too many files, specs, or vague requests, they lose track of important details — a common limitation known as the “lost in the middle” problem.

When you ask an LLM to build too much at once, it often misses dependencies, confuses structures, or generates inconsistent code. This increases bugs and rework. By breaking features into smaller, well-defined tasks, you give the LLM clear goals, reduce hallucinations, and create checkpoints for human validation — improving speed and quality.

A critical part of working with coding agents is feeding the right information, at the right time, in the right size. The engineer must fetch relevant files, surface meaningful snippets, and guide the model. The AI will only be as useful as the context you provide.

## Here are the main ways to provide effective context inside Visual Studio Code using GitHub Copilot Agent:

- **Feeding a well-described, action-oriented implementation plan:** Providing a clear step-by-step plan (like a specification or prompt plan) helps the AI understand the scope of the work and reason through implementation phases safely, one step at a time. This structured planning dramatically improves AI performance and reduces errors. (Source: [The Vibe Coding Workflow](https://www.linkedin.com/pulse/vibe-coding-workflow-michael-papadopoulos-n3wpf/))

- **Writing well-crafted prompts:** Prompts should be clear, specific, and focused. A good prompt clearly defines the task, expected input/output, and any constraints (like preferred frameworks or libraries). The quality of the prompt directly impacts the quality of the AI’s response. (Source: [Prompt engineering for Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting))

- **Using GitHub Copilot tools to provide additional context:** You can enrich your Copilot prompts by attaching files, folders, codebase search results, terminal outputs, problem reports, and even fetching public web content, ensuring the AI has all necessary information to generate better answers. (Source: [Copilot Chat Context](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context))

- **Integrating Modular Context Providers (MCPs):** MCPs allow Copilot to connect to external data sources and services dynamically during a session, extending the AI’s capabilities beyond just static files, enabling access to APIs, Figma, Jira, Github, and other live external systems. (Source: [Use MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers))

- **Adding visual attachments like mockup images:** Providing UI mockups, screenshots, or design references helps AI better understand the visual structure and user experience expected in frontend or product-related development tasks.

- **Defining project-level instructions for Copilot:** You can create instructions files to set custom project coding guidelines, preferred patterns, naming conventions, and rules. This ensures that Copilot follows consistent practices automatically across the project. (Source: [Customize Copilot Chat Responses](https://code.visualstudio.com/docs/copilot/copilot-customization))

- **Making sure your codebase is indexed:** When using GitHub Copilot’s code search and context features, ensuring your workspace is properly indexed allows Copilot to find relevant files more accurately and respond with better context-aware answers. (Source: [Copilot Tips and Tricks - Workspace Indexing](https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks#_workspace-indexing))

- **Use conversational memory strategically:** LLMs remember the flow of your session. Build on past exchanges instead of repeating everything from scratch. If a thread is working, continue it. If not, reset and start over to regain clarity.

- **Let the AI build small before scaling up:** Ask for simpler versions first. Let the model succeed in a small task, then build up complexity gradually. It improves performance and reduces overwhelm.

- **Reuse real code examples:** LLMs reason better from working examples than theory. Paste in past completions, existing code, or samples from similar features to anchor your prompt in reality.

- **Prefer tools that expose context:** Choose coding tools (like Cursor or Claude) that let you see the context window, not hide it. Visibility helps you debug, learn, and iterate faster.

- **Creating and Maintaing Project Documents:** The team can maintain as part of the codebase (such as instructions) or in external systems acessbible by MCPs (such as Confluence) documents that can feed the context with core information on the project. One example is a [UI/UX guidelines](./exmaples-documents/UI_UX_GUIDELINES.md) that aim to define patterns AI must follow to build user interfaces. Other examples can be a solution design handover document crafted by Modus Solution Design team, or a software architecture documentation.

## References

- [Introduction to the LLM Context Handling Problem](https://www.loom.com/share/29cc930d60c0438eb9174ae90a568051)

## Keep Reading

[Basics of Prompt Engineering](./PROMPT_ENGINEERING.md)


---


# Models Use Cases

When integrating AI agents into your development process, selecting the right foundation model is critical for productivity, quality of the output code, and cost-efficiency. Based on our internal experiment and industry observations, here’s how to evaluate and use the leading models:

## Claude 3.5 / 3.7 (Anthropic)

**Strengths:** Best for reasoning-heavy tasks like debugging, architecture decisions, system design, and breaking down complex prompts.
**Context Window:** ~128K tokens (Claude 3.7), great for multi-file reasoning and complex feature generation.
**When to avoid:** High-frequency interactive prompting (Claude is slightly slower) or when token costs are a concern.

### Ideal Use Cases Claude 3.5 / 3.7 (Anthropic)

- Writing comprehensive specs or planning files like spec.md, plan.md or todo.md.
- Refactoring legacy code with unclear logic but with relatively low amount of code.
- Debugging hard-to-identify issues with long history or dependencies.

## GPT-4o (OpenAI)

**Strengths:** Excellent for fast code generation, frontend scaffolding, and prototyping. Very fluent and interactive.
**Context Window:** 128K tokens.
**When to avoid:** Tasks that require deep logical steps across complex services — less precise in those scenarios compared to Claude.

### Ideal Use Cases for GPT-4o (OpenAI)

- Quick iteration of UI components.
- Writing test files, simple APIs, or scaffolding endpoints.
- Real-time coding during pair-programming sessions.

## Gemini 2.5 Pro (Google)

**Strengths:** Best model for full-repo understanding, DevOps, and infrastructure-as-code. Extremely powerful context window.

**Context Window:** Up to 1M tokens (2M with special setups).

**When to avoid:** Prompting conversationally on very small tasks — might be overkill in terms of latency and cost.

### Ideal Use Cases for Gemini 2.5 Pro (Google)

- Modifying infra using CDK/Terraform.
- Coordinating changes across microservices or large monorepos.
- CI/CD automation, API gateway routing, or handling config-heavy workflows.

## Comparison table

| **LLM**    | **Best at**                                         | **Avoid when**                          |
| ---------- | --------------------------------------------------- | --------------------------------------- |
| Claude 3.7 | System reasoning, specs, debugging                  | You need fast short feedback loops      |
| GPT 4o     | UI, scaffolding, fast prompting                     | You need deep logical accuracy          |
| Gemini 2.5 | Infra/codebase-wide operations and larger codebases | You're doing small or interactive tasks |

Each model offers a unique advantage depending on the nature of the task. For day-to-day work, a combination approach using GPT-4o for speed and Claude/Gemini for structure often yields the best outcome.

## Token Efficiency & Cost Awareness in AI Coding Workflows

As AI becomes part of our daily software development process, it’s essential to understand that the way we interact with AI models impacts both cost and performance. Even if you're using tools like GitHub Copilot, Cursor, or Claude on a fixed monthly license, there are still important limits tied to usage — especially around context window size and token quotas.

This section explains why developers must learn to work efficiently, and why engineering leaders and managers should actively support a cost-conscious mindset.

## Why This Matters

### For Developers

- **Better prompts cost less:** Specific, scoped prompts reduce token use and improve AI accuracy.
- **Avoid degraded performance:** Tools like Cursor and Copilot operate under token and context limits. Once usage exceeds those thresholds, performance drops (longer latency, weaker completions, missing context).
- **Prevent feature lockout:** Some tools may stop working temporarily when quota caps are exceeded — requiring additional credits or waiting until reset.

### For Managers

- **AFlat-rate is not unlimited:** Even with monthly pricing, most tools have soft or hard caps. Token abuse leads to throttling or degraded service across the team.
- **ATrack usage:** Understanding team-wide usage patterns can help plan licenses, detect misuse, and manage renewal tiers.
- **AToken efficiency = productivity efficiency:** Well-structured AI interactions save engineering time, avoid retries, and improve project timelines.

## Best Practices for Developers: Prompt Efficiently, Work Smart

- **Be Specific, Not Chatty:** Replace vague instructions with task-focused prompts. Don’t: `Can you help me fix this maybe?`. Instead do: `Refactor validateUser() to support optional phone number.`.
- **Use Attachments, Not Dumps:** Don’t paste full files into prompts. Use file references or context attachment features (#codebase, Cursor context menu).
- **One Task per Prompt:** Instead of asking for a test, refactor, and docs in one go — split into focused steps. Reduces retries and output bloat.
- **Limit Output Size:** Add constraints: `Return only the code, no explanation.`, `Limit to 20 lines.` Keeps the interaction sharp and reduces unnecessary token consumption, especially in tools where both input and output count toward your quota.
- **Avoid Recursive Prompt Chains Without Limits:** Prompts like `Refine this 10 times` may sound clever but can generate thousands of tokens. Use: `Improve this once. Stop after 2 iterations.`
- **Use Shorter Models for Simpler Tasks:** For documentation, variable naming, or test generation, models like GPT-3.5 or Claude 3.5 are cheaper and fast enough.
  Reserve GPT-4 or Claude 3.7 for architectural reasoning or multi-file refactoring.
- **Use Memory Banks and Instructions Files:** Store recurring context (architecture rules, naming patterns, stack details) in `.github/copilot-instructions.md`, `.cursor/rules`, or `CLAUDE.md`. This prevents repeating the same setup context in every prompt — a common source of wasted tokens.

| **Prompt Style**          | **Input Tokens** | **Output Tokens** | **Total** | **Result**               |
| ------------------------- | ---------------- | ----------------- | --------- | ------------------------ |
| Chatty, vague, multi-task | 700              | 1400              | 2100      | Low quality, AI misfires |
| Focused, scoped, clear    | 200              | 600               | 800       | High quality, no retries |

Even small improvements save thousands of tokens per day when repeated across engineers.

## What Managers Should Do

- Set token-awareness as a team expectation — just like we manage test coverage or code review discipline.
- Encourage shared context assets (instructions files, prompt plans, spec.md, etc.).
- Monitor usage if possible — via OpenAI dashboards, Claude usage logs, or billing APIs.
- Default to value-tier models where appropriate (e.g., staging/dev workflows).

By applying token-efficient practices, we keep our tools responsive, our budgets sustainable, and our workflows high-impact. This isn’t just about saving money — it’s about engineering with intention.

## References

- [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task)

## Keep Reading

[Privacy Considerations](./PRIVACY.md)


---


# MCP Use Cases

Model Context Providers (MCPs) extend the AI agent’s capabilities by automatically injecting context from external sources into your prompts. Instead of manually copying and pasting information, MCPs allow the AI to access critical data like Jira tickets, Confluence docs, Figma designs, and GitHub discussions in real time. This improves the accuracy, speed, and quality of AI-generated code and responses.

During our internal experiment, we validated several valuable MCP use cases that had a direct impact on productivity and output quality:

- Fetching feature request details directly from Jira tickets to understand acceptance criteria, edge cases, and business rules.
- Fetching architecture definitions, internal standards, reusable patterns, and product strategy notes from Confluence pages to guide implementations.
- Fetching UI mockups from Figma to generate frontend components aligned with the latest designs.
- Fetching GitHub pull request comments to incorporate peer feedback into the AI-driven coding flow.
- Fetching external API documentation to integrate third-party services faster and with fewer mistakes.
- Fetching live browser data like console errors to debug issues contextually during development.

By using MCPs, developers spend less time tab-switching between tools and more time staying focused on building and improving software.

## Available MCPs for Our Workflows

- Atlassian MCP for Jira and Confluence: [Atlassian Remote MCP](https://www.atlassian.com/platform/remote-mcp-server)

- GitHub MCP for Pull Requests and Comments: [GitHub - github/github-mcp-server: GitHub's official MCP Server](https://github.com/github/github-mcp-server)

- [Figma MCP Plugin (Talk to Figma)](https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin)

MCPs are a core enabler for efficient agentic coding at scale, helping the AI work with richer, more reliable information without needing constant manual intervention.

## Safety & Security Guidelines for Using MCPs

When integrating Model Context Providers (MCPs) into your agentic-coding workflow, security must be front-of-mind. Follow these guardrails to protect your codebase, data, and credentials:

| **Best-Practice**                                                  | **Why it matters**                                                                 | **What to do**                                                                                                                                                             |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prefer official MCPs                                               | Vendors maintain their own MCPs, patching bugs and security issues promptly.       | Use the MCP published by the API provider (e.g., GitHub, Atlassian, Figma). Avoid community forks unless absolutely necessary.                                             |
| Keep secrets out of MCPs                                           | Hard-coded credentials are a breach waiting to happen.                             | Store API keys or tokens in your secret-management layer (e.g., HashiCorp Vault, AWS Secrets Manager) and pass them via environment variables or a secrets-injection step. |
| Apply least-privilege keys                                         | Broad tokens increase blast radius if leaked.                                      | Generate scoped API keys that allow only the minimal actions the MCP needs (read-only if possible). Rotate them on a schedule.                                             |
| Use a trusted middleware when no official MCP exists               | Third-party automation hubs already isolate and encrypt credentials.               | Configure the middleware’s official connector and let it proxy requests, keeping your secrets out of an open-source repo.                                                  |
| Audit any unofficial open-source MCP                               | Community packages can contain malicious code, outdated deps, or hidden telemetry. | Fork the repo, review every line, run static analysis (e.g., Semgrep), and pin dependency versions before deploying.                                                       |
| Never trust closed-source, unofficial MCPs that demand credentials | You cannot inspect what you cannot see.                                            | If the provider won’t open the code, treat it as an immediate deal-breaker—no exceptions.                                                                                  |

In the next sections, we will explain how to configure and use each MCP step-by-step inside your coding workflows.

## References

- [Figma and Atlassian MCPs for Cursor](https://www.loom.com/share/2c651abeb3394c38a218f2860084da0d)
- [Introducing the GitHub MCP Server: AI interaction protocol | GitHub Checkout](https://www.youtube.com/watch?v=d3QpQO6Paeg)
- [The Only 3 Videos You Need to Get Started with MCP](https://www.youtube.com/watch?v=YRfOiB0Im64)

## Keep Reading

[Org Level Instructions](./ORG_INSTRUCTIONS.md)


---


# Debugging with an MCP

There are several Model Context Protocol (MCP) solutions for extracting runtime browser data for debugging and context-aware AI assistance. We evaluated a few current options and compared their abilities to capture console errors, network activity, and application state while ensuring security and privacy compliance. What follows is the preferred option, based on those evaluations.

## Puppeteer MCP

Comprehensive browser runtime data access

- More consistent JavaScript execution for complex scenarios
- Smaller dependency footprint
- Simpler API pattern
- Uses official reference implementation from the @modelcontextprotocol/servers repository

## Setup

Docs: [puppeteer mcp](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)

Installation: `npm install --save-dev @modelcontextprotocol/server-puppeteer`

This package comes from the official Model Context Protocol reference implementation

Configuration in `.vscode/mcp.json`:

```json
"puppeteer_mcp": {
  "command": "npx",
  "args": [
    "@modelcontextprotocol/server-puppeteer"
  ]
}
```

## Limitation and Challenge: Connecting to Existing Browser Sessions

A significant limitation is the inability to easily connect to an already running browser instance where an error occurred. Instead the AI assistant uses the MCP to navigate to the running app based on the running app's URL, which either reloads the browser window/tab or opens a new browser session.

This presents several challenges for real-world debugging:

- **Error Reproduction:** Developers must reproduce the error in a new browser session controlled by the MCP tool, which may be difficult for intermittent issues or those dependent on specific user actions or state.

- **Context Loss:** When an error occurs in a user's browser, valuable context (console history, network requests, application state) is lost if it cannot be extracted directly from that session.

- **Developer Experience:** The workflow becomes cumbersome as developers need to provide detailed instructions for reproducing the error in a separate MCP-controlled browser instance.

## Keep Reading

[Debugging Workflow](./WORKFLOW_DEBUG.md)


---


# Privacy Considerations for Agentic Coding

As we adopt AI coding agents in our daily workflow, it's critical that we stay vigilant about data privacy and security. Tools like Cursor, GitHub Copilot Agent, Claude, and others introduce new capabilities — but also new risks if misused.

This page outlines the non-negotiable privacy boundaries, best practices, and tooling recommendations that all developers must follow while using agentic coding techniques.

## What You Must Never Do

### ❌ Do not prompt with real user data

Never paste or reference real user emails, names, phone numbers, IDs, or any personally identifiable information (PII) into prompts.

This includes debugging issues, writing test cases, or requesting data transformations.

### ❌ Do not attach files containing sensitive data

Avoid storing at the codebase (even if git ignored), uploading or referencing exports with live data — such as CSVs, PDF reports, or logs with user identifiers.

These files may be stored temporarily or indexed by your IDE or tool.

### ❌ Do not connect AI tools to production databases

Never connect a agent to a live production database using a Model Context Provider (MCP).

Example: Do not create an MCP integration that fetches data directly from a production live PostgreSQL or DynamoDB instance. It is fine to connect to test data stores.

### ❌ Do not use AI tools that train on your data by default

Avoid uploading the codebase to any AI coding tool that may use inputs to improve their models unless explicitly allowed by legal and security teams.

## What You Should Do Instead

### ✅ Use mock data in all prompts and test cases.

Create safe, fake data sets or anonymized examples when showing the AI how your system behaves.

### ✅ Stick to tools with enterprise-safe defaults.

Preferred tools at Modus Create:

- Cursor – does not train models on your prompts or code.

- GitHub Copilot Agent (enterprise) – keeps data within GitHub and respects repo privacy boundaries.

- Claude (via secure workspace API) – when used through approved infrastructure, Claude does not retain prompt history.

### ✅ Use memory files or documentation, not live data, for context.

Store reusable information in safe .md files like spec.md, activeContext.md, and .copilot-instructions.md.

These are indexed but controllable, and never contain user data.

### ✅ Mask real data when debugging or generating logs.

Use placeholders: "user_123", "test@example.com", "TXN_0001"

Prompt: “This log contains simulated user activity. Based on this structure, can you help identify potential auth failure scenarios?”

### ✅ Connect MCPs to test/dev environment data stores.

## Real Risks If Ignored

- Privacy violations under GDPR, CCPA, HIPAA, or internal customer contracts.
- Credential leaks when full environment configs are prompted without redaction.
- Reputational damage if client data is exposed through AI usage logs or vendor breaches.
- Audit failure due to use of unvetted tools or unapproved data exposure in prompt flows.

Treat every prompt like a commit: if it contains sensitive data, it's already too late: Stay intentional, stay secure — agentic coding is powerful, but privacy comes first.

## Keep Reading

[Contributing](./CONTRIBUTING.md)


---


# Organization Level Instructions

GitHub Copilot now supports organization-level instructions, allowing administrators to define guidance that applies to all repositories and all users within a GitHub organization. This is a powerful tool to promote consistency, security, and governance across all AI-assisted development workflows.

This page explains how org-level instructions differ from project-level .copilot-instructions.md files and how to use each effectively.

## What Are Organization-Level Instructions?

Organization-level instructions are set in GitHub settings (via the Copilot tab) and are automatically injected into every Copilot Chat interaction for members of the organization — regardless of which repository they are working in.

This creates a baseline AI behavior model for all teams under the org umbrella.

## How It Differs from Project-Level Instructions

| **Feature**    | **Organization-Level**                | **Project-Level**                                             |
| -------------- | ------------------------------------- | ------------------------------------------------------------- |
| Scope          | All users & repos in the org          | Only applies to a specific repo                               |
| Who manages it | Org admins                            | Repo maintainers or developers                                |
| When it loads  | Always in context                     | Only when working in that repo                                |
| Purpose        | Company-wide guidance, policies, tone | Repo-specific architecture, stack, naming, etc.               |
| Format         | Text box in GitHub settings           | Markdown file in repo root: `.github/copilot-instructions.md` |

These two types of instructions are complementary: org-level defines global rules, project-level adds local specificity.

## Use Cases for Organization-Level Instructions

- **Security and Privacy Rules**

```txt
Never suggest using secrets or API keys directly in code.
Avoid using eval() or direct SQL string construction.
```

- **Documentation and Learning Resources**

```txt
When asked about frontend theming, refer to the Confluence Docs at <name>.
Link to internal API documentation for auth-related questions.
```

- **Consistency Across Teams**

```txt
Use PascalCase for class names and camelCase for functions.
Always wrap DB calls with the internal SafeQuery abstraction.
```

- **Style and Formatting Rules**

```txt
All logs must use LoggerService.debug() — never console.log().
Use ?? over || for nullish checks.
```

- **Process Guidelines**

```txt
For any deployment questions, remind the user to check the InfraRunbook first.
When unsure about security decisions, suggest reaching out in #ask-security.
```

## Best Practices for Writing Org-Level Instructions

- **Be clear and prescriptive:** Write them like onboarding rules — not suggestions.
- **Avoid repo-specific logic:** Don’t reference repo file paths or local variables.
- **Use structured categories:** Break into sections like "Security", "Logging", "Naming", etc.
- **Keep it short:** Aim for < 1,000 words to avoid hitting context compression limits.
- **Update periodically:** Sync changes with team-wide rollouts, language style updates, or new security policies.

## When to Use Project vs Org Instructions

| **Scenario**                                | **Use This**       |
| ------------------------------------------- | ------------------ |
| Defining architecture rules for a monorepo  | Project-level      |
| Standardizing logging across all projects   | Organization-level |
| Enforcing naming conventions per team       | Project-level      |
| Controlling AI suggestions for secret usage | Organization-level |
| Teaching a repo-specific design pattern     | Project-level      |

## How to Configure

- Go to your GitHub organization settings.
- Navigate to the Copilot tab.
- Click Custom Instructions.
- Enter your organization-wide instructions in the editor box.
- Save — they’re now live for all Copilot Chat interactions in the org.

Organization instructions are your first layer of LLM governance. They establish shared values and behaviors that AI should reflect — turning Copilot into an extension of your engineering culture.

## References

- [Organization custom instructions now available](https://github.blog/changelog/2025-04-17-organization-custom-instructions-now-available/)

## Keep Reading

[Project Level Instructions](./PRJ_INSTRUCTIONS.md)


---


# Project Level Instructions

One of the most effective ways to improve the quality of AI-generated code is by configuring project-level instructions that guide the behavior of GitHub Copilot and other coding agents. These instructions act like a persistent memory layer — they’re automatically injected into the LLM’s context, helping it follow your project's specific conventions and patterns without needing to be re-explained in every prompt. Copilot instructions can be used for keeping the behavior of the agent as you desire for your workflow. It both keeps how it works in terms of actions is going to execute and its also enforces the code quality.

## Why This Matters

During the experiment, we found that codifying quality expectations and design patterns up front made the AI much more likely to generate correct, review-ready code. It also reduced the need for prompt repetition, improved consistency between developers, and accelerated onboarding.

This concept is directly aligned with Cursor’s .cursor/rules, which was a key enabler in our experiment. The good news is: GitHub Copilot now supports this too through custom instructions.

## What to Include in Project Instructions

Create a file named .github/copilot-instructions.md in the root of your repo. In this Markdown file, document anything you want the AI to consider "non-negotiable" about how your team works, such as:

- Architecture decisions (e.g., This project uses a layered architecture with separate domain and infrastructure folders.)
- Naming conventions and file structure guidelines
- Security patterns (e.g., All user input must be sanitized before DB insertion.)
- Code quality expectations (e.g., Use ?? instead of || for nullish checks.)
- Testing rules (e.g., Every service must include unit tests using Jest and describe.each for parameterized coverage.)
- What to avoid (e.g., Never use any as a type.)

> These instructions are automatically loaded by Copilot Chat when you're prompting in the project, without needing to be referenced in the chat.

## How to Write a Good Project Instructions File

The .github/copilot-instructions.md (or .cursor/rules) file helps AI generate code that aligns with your team’s standards. Think of it as writing onboarding notes for a junior dev who will follow your rules exactly — but won’t ask questions.

Follow these guidelines:

### Be clear and directive

- Use instruction-style language.
  ✅ `Use Axios for all HTTP requests`
  ❌ `We usually prefer Axios.`

### Be specific

- Avoid vague advice.
  ✅ `Put all utility functions in src/utils using camelCase.`
  ❌ `Keep things organized.`

### Prioritize what the AI needs

Focus on structure, naming, preferred libraries, testing, and patterns. Skip in-depth business context it won’t help generation and should be shared as part of the implementation planning and execution.

### Use headers to group rules

Organize content with topics like:

- Project Structure
- Naming Conventions
- Error Handling
- Testing
- Things to Avoid

**Keep it short:** Stick to 1–2 pages. If it’s too long, it may be partially ignored due to context limits.

**Maintain it like code:** Update as project patterns evolve — especially before onboarding or major feature work.

## Resources and Examples

- You can find many rule examples at cursor.directory
- Cursor’s `.cursor/rules` and GitHub’s `.github/copilot-instructions.md` follow the same format — Markdown — and can be reused across tools with little to no adjustment.

- [Clean Code Rules Prompt](https://shumerprompt.com/prompts/clean-code-rules-prompt-554351c6-3bcb-4c20-9c77-f831b4aa6b0a)
- [Code Quality Guidelines Prompt](https://shumerprompt.com/prompts/-code-quality-guidelines-prompt-661c6a3f-cb69-46e6-b75c-97f7bfbb514b)
- [React Rules Prompt](https://shumerprompt.com/prompts/react-rules-prompt-76302cd0-5448-4056-a90e-4057388a9149)
- [Python Best Practices Prompt](https://shumerprompt.com/prompts/python-best-practices-prompt-ac25d837-ff42-4b89-92b1-5a7bbb558047)

```markdown
# COPILOT INSTRUCTIONS OPERATIONAL GUIDELINES

## PRIME DIRECTIVE

Avoid working on more than one file at a time.
Multiple simultaneous edits to a file will cause corruption.
Be chatting and teach about what you are doing while coding.

## LARGE FILE & COMPLEX CHANGE PROTOCOL

### MANDATORY PLANNING PHASE

When working with large files (>300 lines) or complex changes:

1. ALWAYS start by creating a detailed plan BEFORE making any edits
2. Your plan MUST include:

- All functions/sections that need modification
- The order in which changes should be applied
- Dependencies between changes
- Estimated number of separate edits required

3. Format your plan as:

## PROPOSED EDIT PLAN

Working with: [filename]
Total planned edits: [number]

### MAKING EDITS

- Focus on one conceptual change at a time
- Show clear "before" and "after" snippets when proposing changes
- Include concise explanations of what changed and why
- Always check if the edit maintains the project's coding style

### Edit sequence:

1. [First specific change] - Purpose: [why]
2. [Second specific change] - Purpose: [why]
3. Do you approve this plan? I'll proceed with Edit [number] after your confirmation.
4. WAIT for explicit user confirmation before making ANY edits when user ok edit [number]

### EXECUTION PHASE:

- After each individual edit, clearly indicate progress:
  "✅ Completed edit [#] of [total]. Ready for next edit?"
- If you discover additional needed changes during editing:
- STOP and update the plan
- Get approval before continuing

### REFACTORING GUIDANCE:

When refactoring large files:

- Break work into logical, independently functional chunks
- Ensure each intermediate state maintains functionality
- Consider temporary duplication as a valid interim step
- Always indicate the refactoring pattern being applied

### RATE LIMIT AVOIDANCE:

- For very large files, suggest splitting changes across multiple sessions
- Prioritize changes that are logically complete units
- Always provide clear stopping points

## General Requirements:

Use modern technologies as described below for all code suggestions. Prioritize clean, maintainable code with appropriate comments.
```

## Keep Reading

[Examples](./examples.md)


---


# 💡 Examples & Templates

Real-world examples and templates you can use immediately. These practical resources demonstrate how to apply agentic coding principles in your daily development workflow.

## What You'll Find

### Prompt Templates

Ready-to-use prompts for common development tasks:

- Implementation planning and architecture design
- Frontend debugging and UI optimization
- React + Vite project bootstrapping
- Code refactoring strategies
- Test case generation
- User story decomposition

### Automation Scripts

Production-ready scripts and tools:

- Pre-commit hooks with quality gates
- Automated code validation pipelines
- Git workflow automation

### Documentation Examples

Best practices for documenting agentic workflows:

- UI/UX guidelines for design consistency
- Team onboarding documentation
- Project-specific coding standards

## How to Use These Examples

1. **Copy and adapt** - These templates are starting points, not rigid rules
2. **Customize for your context** - Adjust language, tools, and patterns to match your stack
3. **Share improvements** - Help the community by contributing your refinements
4. **Combine patterns** - Mix and match different approaches for complex scenarios

Each example includes:

- **Context** - When and why to use this approach
- **Template** - Ready-to-copy prompt or script
- **Variations** - How to adapt for different situations
- **Results** - What to expect from the output

Start with the examples that match your current challenges, then explore related patterns as you build confidence with agentic coding workflows.

## Keep Reading

Share your own experiences and help grow our knowledge base: [Team Experiences](./TEAM_EXPERIENCES.md)


---


# Contributing

This handbook is a living document. It reflects what we’ve learned so far about coding with agents — but it’s not finished, and it never will be. We expect it to grow, evolve, and adapt as our team experiments, learns, and discovers better ways to collaborate with AI.

## Why Contributions Matter

- **The handbook evolves with you:** Every week, people across teams are learning new tricks, testing new workflows, and improving results. When you find something that works, document it here.
- **AI changes fast:** New models, features, and tools are launching constantly. What works today might be outdated in six months. Help us keep this handbook current.
- **Your experiments help everyone:** If you test a new prompting pattern, context feeding strategy, or way of organizing specs — document it. Share the knowledge.
- **Enterprise-scale Agentic Coding is still evolving:** We’re all figuring this out together. If you discover better ways to scale across squads or workflows, bring it here.

## Common Contribution Practices

To ensure consistency and collaboration, please follow these best practices:

- **Start small:** You don’t need to write a whole page. A short note, list of learnings, or useful prompt is enough to get started.
- **Use examples:** Real examples (with prompts, outputs, or before/after code) help others replicate what worked.
- **Keep the tone consistent:** Practical, direct, and focused on helping other engineers.
- **Avoid tool-specific bias unless needed:** Focus on transferable practices unless documenting something tool-specific (like Cursor, Copilot, Claude).
- **Group related updates:** If you're updating a section, make sure it's coherent as a whole — not a collection of unrelated edits.
- **Keep it structured:** Use headers, bullets, and short paragraphs to keep the content scannable and reusable.
- **Flag outdated content:** If you’re not sure how to replace old info, comment or tag it as "needs update".
- **Ask for peer review:** Major changes should be reviewed by at least one other engineer before publishing.

## How to Get Started

- Use inline comments in Confluence to suggest changes if you're not ready to write.
- For new ideas or patterns, create a new section or subpage under the most relevant area.
- Add your name or initials next to contributions when appropriate — this helps others follow up with questions.
- Let’s build this handbook the same way we build great products: collaboratively, iteratively, and with care.

## Keep Reading

[Team Experiences](./TEAM_EXPERIENCES.md)


---

