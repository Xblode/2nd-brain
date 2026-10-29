import fs from "node:fs";
import path from "node:path";

/**
 * Valide la forme d'un projet qui a reçu le pack web-starter + socle Second Brain.
 * N'est pas une preuve que Cursor a chargé les skills.
 */
const root = process.cwd();
const errors = [];

const required = [
  "AGENTS.md",
  "brain/STATE.md",
  ".clickup/mapping.yaml",
  ".cursor/skills/cadrer/SKILL.md",
  ".cursor/skills/build/SKILL.md",
  ".cursor/skills/clickup/SKILL.md",
  "docs/00-discovery/PROJECT_BRIEF.md",
  "docs/03-architecture/STACK_PROFILES.md",
  "docs/90-templates/FIRST_PROMPT.md",
];

// Explicitly NOT required: docs/00-discovery/PROJECT_STATE.md (état maître = brain/STATE.md)

const exists = (relative) => fs.existsSync(path.join(root, relative));

for (const relative of required) {
  if (!exists(relative)) errors.push(`missing ${relative}`);
}

if (exists("docs/00-discovery/PROJECT_STATE.md")) {
  errors.push(
    "unexpected docs/00-discovery/PROJECT_STATE.md — use brain/STATE.md as sole state master",
  );
}

if (exists("docs/06-delivery/CLICKUP_CONVENTION.md")) {
  errors.push(
    "unexpected CLICKUP_CONVENTION.md — use brain-main/skills/clickup/modules/convention.md",
  );
}

if (errors.length) {
  console.error("validate-kit failed:");
  for (const e of errors) console.error(`- ${e}`);
  process.exit(1);
}

console.log("validate-kit: ok");
