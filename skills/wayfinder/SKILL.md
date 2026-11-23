---
name: wayfinder
description: Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. Use when a loose idea is too big for one session and wrapped in fog.
---

# Wayfinder

A loose idea has arrived, too big for one agent session, and wrapped in fog: the way from here to the **destination** isn't visible yet.

## Overview

Wayfinding is about finding that way, not charging at the destination. This skill charts the way as a **shared map** on the repo's issue tracker, then works its **decision tickets** (questions whose resolution is a decision, not slices of a build to execute) one at a time until the route is clear.

## When to Use

When a loose idea is too big for one agent session and wrapped in fog. Use when planning large work that needs a shared map of decision tickets.

## Process

### Plan, don't do

Wayfinder is **planning** by default: each ticket resolves a decision, and the map is done when the way is clear, with nothing left to decide before someone goes and does the thing.

### Refer by name

Every map and ticket is an issue, so it has a **name**: its title. In everything the human reads, refer to it by that name, never by a bare id, number, or slug.

### The Map

The map is a single issue on this repo's issue tracker, labelled `wayfinder:map`, the canonical artifact.

### Tickets

Each ticket is a **child issue** of the map; the tracker's issue id is its identity. Its body is the question.

### Fog of war

The map is _deliberately_ incomplete: don't chart what you can't yet see.

### Out of scope

Fog only ever gathers _toward_ the destination.

### Invocation

Two modes. Either way, **never resolve more than one ticket per session**, with the exception of research tickets.

## Rationalizations

| Excuse | Reality |
|---|---|
| Charging at the destination | Wayfinding is about finding the way, not charging |
| Charting everything upfront | The map is deliberately incomplete; leave fog in place |
| Resolving more than one ticket per session | Decisions must be resolved one at a time |

## Red Flags

- Charting everything up front instead of leaving fog
- Resolving more than one ticket per session
- A grilling ticket where the agent answers its own questions
- Restating decisions on the map instead of linking
- Bare ids instead of named links
- Charging at the destination instead of finding the way

## Verification

- [ ] Route to destination is clear with no open tickets
- [ ] All frontier tickets are unblocked and claimed
- [ ] Map shows complete decisions-so-far with no unresolved fog