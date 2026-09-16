# -*- coding: utf-8 -*-
"""Public-tree hygiene for agents-knowledge-base (Johnny Decimal template)."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv"}
FORBIDDEN = (
    "G:\\",
    "G:/",
    "C:\\Hermes",
    "C:/Hermes",
    "C:\\Users\\alexm",
    "d1c207fb-9854-441f-8c16-c0be2ef6faff",
    "0aac62bb-906d-43c4-830a-04136cd73ae0",
    "626af52f-5bbf-4146-a6dc-653f3318aa49",
    "thesamohod4ik@",
)
# Short UUID prefixes from private design chats (full IDs also listed above).
FORBIDDEN_PREFIXES = (
    "d1c207fb",
    "0aac62bb",
    "626af52f",
)
TEXT_SUFFIXES = {
    ".md",
    ".mdc",
    ".py",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".gitignore",
}
REQUIRED_SKILLS = (
    "projects-data-verification",
    "vault-router",
    "session-distill",
    "save-research",
)


def iter_text_files():
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.name == "test_docs_hygiene.py":
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            "LICENSE",
            "AGENTS.md",
        }:
            if path.suffix.lower() == "" and path.name in {"LICENSE"}:
                pass
            elif path.suffix.lower() not in TEXT_SUFFIXES:
                continue
        yield path


class HygieneTests(unittest.TestCase):
    def test_no_host_paths_or_private_chat_ids(self):
        hits = []
        for path in iter_text_files():
            text = path.read_text(encoding="utf-8", errors="replace")
            for token in FORBIDDEN:
                if token in text:
                    hits.append("%s: %s" % (path.relative_to(ROOT), token))
            for prefix in FORBIDDEN_PREFIXES:
                if prefix in text:
                    hits.append("%s: %s" % (path.relative_to(ROOT), prefix))
        self.assertEqual(hits, [])

    def test_readme_is_bilingual(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## English", text)
        self.assertIn("## Русский", text)
        self.assertIn("docs/obsidian.md", text)
        self.assertIn("<VAULT>", text)
        self.assertIn("<SKILLS_ROOT>", text)
        self.assertIn("<GIT_REMOTE>", text)

    def test_banned_product_words_absent(self):
        hits = []
        # Adjacent literals concatenate at runtime; source avoids contiguous banned spellings.
        needles = ("R" "AG", "Tele" "gram", "tele" "gram")
        for path in iter_text_files():
            if path.name == "test_docs_hygiene.py":
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for token in needles:
                if token in text:
                    hits.append("%s: %s" % (path.relative_to(ROOT), token))
        self.assertEqual(hits, [])

    def test_required_public_docs_and_skills(self):
        required = [
            "README.md",
            "LICENSE",
            "SECURITY.md",
            "CONTRIBUTING.md",
            "AGENTS.md",
            "docs/obsidian.md",
            "docs/problem-and-approach.md",
            "docs/architecture.md",
            "docs/killer-features.md",
            "docs/cursor-integration.md",
            "docs/repository-audit.md",
            "vault-skeleton/README.md",
            "vault-skeleton/00_profile/README.md",
            "vault-skeleton/10_projects/example_library/README.md",
            "vault-skeleton/10_projects/example_service/README.md",
            "vault-skeleton/.cursor/rules/obsidian-vault-maintenance-protocol.mdc",
            "vault-skeleton/.cursor/rules/obsidian-vault-markdown-standards.mdc",
        ]
        missing = [p for p in required if not (ROOT / p).is_file()]
        self.assertEqual(missing, [])
        for name in REQUIRED_SKILLS:
            skill = ROOT / "skills" / name / "SKILL.md"
            self.assertTrue(skill.is_file(), msg="missing %s" % skill)

    def test_skills_ship_briefs_only(self):
        skills_root = ROOT / "skills"
        script_dirs = list(skills_root.rglob("scripts"))
        self.assertEqual(
            [str(p.relative_to(ROOT)) for p in script_dirs if p.is_dir()],
            [],
        )
        for name in REQUIRED_SKILLS:
            text = (skills_root / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Не используй", text)
            self.assertIn("Успех", text)
            # Must not present doctor as a required first step.
            self.assertNotRegex(
                text,
                r"(?mi)^##\s*Doctor\s*$",
                msg="%s still has ## Doctor section" % name,
            )

    def test_johnny_decimal_map_present(self):
        skeleton = ROOT / "vault-skeleton"
        for decade in (
            "00_profile",
            "10_projects",
            "20_infra",
            "30_db",
            "40_patterns",
            "50_runbooks",
            "60_skills",
            "70_researches",
            "90_archive",
        ):
            self.assertTrue((skeleton / decade).is_dir(), msg=decade)
        self.assertFalse((skeleton / "80_unused").exists())
        self.assertFalse((skeleton / "00-System").exists())


if __name__ == "__main__":
    unittest.main()
