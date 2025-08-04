Peacecraft Game Plan

Game Concept

Peacecraft is a web-based interactive RPG designed to teach players how to diffuse hostile situations and resolve conflicts peacefully. The game follows a progression system similar to Mortal Kombat, where players must successfully resolve conflicts without failure to advance. It is a player vs. AI game, with AI-powered NPCs responding dynamically using generative AI from Ollama.

Game Structure & Rules

1. Gameplay Overview

The player engages in one-on-one conflict scenarios with AI-driven NPCs.

The goal is to de-escalate and resolve the conflict peacefully.

Players win by finding a mutually acceptable resolution.

Players lose if they fail to de-escalate or if the conflict worsens.

No predefined responses—players type their own responses, and AI interprets them dynamically.

2. Conflict Progression System

Players must successfully resolve each conflict to progress.

If a player fails, they must restart from the beginning or a checkpoint.

The game progresses from simple personal conflicts to high-stakes negotiations:

Level 1: Personal Conflicts (e.g., someone cuts in line, someone bumps into you).

Level 2: Workplace & Business Disputes (e.g., unfair treatment at work, customer complaints).

Level 3: Community & Government Conflicts (e.g., protests, political negotiations).

Level 4: War & Peace Negotiations (e.g., peace treaties, international diplomacy).

3. AI Opponent System

NPCs have different personalities and conflict styles, such as:

The Aggressor (Quick to anger)

The Manipulator (Tries to twist words)

The Emotional (Responds more to tone than logic)

The Skeptic (Doesn’t trust easily)

The Stubborn (Resistant to compromise)

AI tracks trust levels, tone, and logic to determine outcomes.

Conflicts will be AI-generated, but we will develop the prompts to properly define the game and scenarios.

4. Game Mechanics

Real-Time AI Dialogue: Players type responses, and NPCs reply in real time.

Trust & Reputation System: NPCs react based on the player's approach.

Scoring System: Players are graded on:

NPC Trust Level

Resolution Strength

Use of Empathy vs. Logic

Time Taken

Fail Conditions:

NPC refuses to negotiate further.

Conflict escalates beyond resolution.

Minimum Viable Product (MVP)

Core Features for MVP

Basic Conflict Resolution System

One simple scenario (e.g., someone cuts in line).

Player types their own responses.

AI interprets responses and reacts dynamically.

Simple win/loss condition: Player wins if conflict de-escalates, loses if it escalates.

AI-Driven NPC (Single Personality)

One AI opponent personality (e.g., The Aggressor).

AI tracks trust level and adjusts responses accordingly.

Basic tone analysis (e.g., detects aggression, neutrality, or empathy).

Simple Frontend (React)

Text-based chat UI where players interact with the NPC.

Input field for player responses.

Dialogue box displaying AI responses.

Basic progress tracking (e.g., trust bar, status updates).

Backend (FastAPI + AI Integration)

FastAPI backend to handle game logic.

Ollama AI integration for NPC responses.

Basic database (MongoDB/PostgreSQL) to track game state.

Basic Game Flow

Start game → Engage in conflict → AI reacts → Player responds → Win/Loss condition.

Next Steps

1. Finalize Initial Conflict Scenarios

Define the first simple conflict scenario:

Scenario Example: A person cuts in line at a store. How does the player handle it?

Define:

NPC personality type (e.g., Aggressor)

Possible player approaches (calm reasoning, confrontation, passive acceptance)

AI response framework (how NPC reacts based on trust level)

2. Develop AI Prompts for Generating Conflicts

Create structured prompts for AI to generate realistic conflict scenarios.

Example AI Prompt:
"Generate a conflict scenario where a player encounters an aggressive individual who cuts in line. The NPC should start hostile, and their responses should adapt based on the player's tone and word choice. The NPC should be able to escalate or de-escalate based on trust level."

3. Start Backend Development (FastAPI & AI Integration)

Set up API endpoints for:

Receiving player input.

Generating AI-driven NPC responses.

Tracking trust level and progression.

Connect Ollama AI for real-time responses.

4. Design the UI Wireframe

The React frontend will need:

A chat-style interface (similar to AI chatbots).

A trust bar to show NPC reactions.

A minimalist and clean UI.

This plan ensures a smooth development process for Peacecraft’s MVP. Let me know if you want any refinements before we move forward! 🚀

