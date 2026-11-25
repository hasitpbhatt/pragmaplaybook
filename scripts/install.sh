#!/usr/bin/env bash
# Install pragmaplaybook skills globally for common AI tools.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS="$REPO_DIR/skills"
ROUTER="$REPO_DIR/AGENTS.md"

link() { # link <target> <linkpath>
  mkdir -p "$(dirname "$2")"
  ln -sfn "$1" "$2"
  echo "linked $2 -> $1"
}

link "$SKILLS" "$HOME/.agents/skills"
link "$SKILLS" "$HOME/.claude/skills"
link "$ROUTER" "$HOME/.claude/CLAUDE.md"
link "$SKILLS" "$HOME/.copilot/skills"
mkdir -p "$HOME/.config/opencode"
link "$SKILLS" "$HOME/.config/opencode/skills"
link "$ROUTER" "$HOME/.config/opencode/AGENTS.md"

echo "Done. Skills from $REPO_DIR are now available globally."
