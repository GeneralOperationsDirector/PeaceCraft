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

MVP Development Phases

Phase 1: Backend Setup

✅ Set up FastAPI backend.✅ Connect Ollama AI to generate NPC responses.✅ Implement basic AI conflict logic (simple scenario + personality).

Phase 2: Frontend Prototype

✅ Create simple chat UI (React).✅ Implement player input system.✅ Display AI responses in a conversation format.

Phase 3: AI Refinement

✅ Tune AI responses for basic tone detection.✅ Improve NPC personality logic.✅ Implement win/loss mechanics based on trust level.

Phase 4: Testing & Iteration

✅ Test AI-generated interactions.✅ Fix bugs & improve NPC logic.✅ Optimize player feedback system (e.g., show progress indicators).

Phase 5: MVP Deployment

✅ Deploy MVP to a test server.✅ Collect user feedback.✅ Plan for expanding scenarios & personalities.

Development Plan

Phase 1: Planning & Documentation

Define core game mechanics.

Outline AI behavior and response logic.

Draft UI wireframes.

Develop AI conflict-generation prompts.

Phase 2: Backend Development (Python, FastAPI)

Set up FastAPI backend.

Integrate Ollama AI for NPC interactions.

Implement conflict scenarios database (MongoDB/PostgreSQL).

Develop progression system to track player wins/losses.

Phase 3: Frontend Development (React)

Create chat-based UI for player-NPC interactions.

Implement dialogue display and response input.

Add progress tracking UI.

Phase 4: AI Optimization & Game Logic

Train NPC responses for different conflict styles.

Implement memory tracking for NPCs to recall past interactions.

Balance AI difficulty progression.

Fine-tune AI-generated conflicts with improved prompts.

Phase 5: Testing & Iteration

User testing for realistic AI responses.

Bug fixing and AI fine-tuning.

Implement fail-safe measures to prevent dead-end conflicts.

Phase 6: Deployment & Expansion

Deploy web app to production server.

Gather player feedback for improvements.

Expand with new scenarios, multiplayer mode, or voice interaction.

Next Steps

Finalize the initial conflict scenarios.

Develop AI prompts for generating realistic and structured conflicts.

Start backend development with FastAPI and AI integration.

Design the UI wireframe for the chat interface.

This plan ensures that Peacecraft is engaging, educational, and scalable while maintaining a streamlined development process. Let me know if you want to modify or add anything!
