#!/usr/bin/env python3
"""Offline validation of an Codie GEO project profile."""
import sys
from pathlib import Path
try:
    import yaml
except ImportError:
    print("PyYAML is required: python -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REQUIRED = ["project_id", "project_name", "audience.who", "objectives.primary_goal", "content.channels", "content.languages", "storage.mode"]
VALID_STORAGE = {"local", "google_drive", "notion_or_other", "chat_only"}
VALID_ORG = {"existing", "date", "week_day", "flat"}

def get_path(data, path):
    for part in path.split("."):
        if not isinstance(data, dict) or part not in data:
            return None
        data = data[part]
    return data

def validate(path):
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return ["Profile must be a YAML mapping"]
    problems = [f"Missing required field: {p}" for p in REQUIRED if not get_path(data, p)]
    if get_path(data, "storage.mode") not in VALID_STORAGE:
        problems.append("storage.mode must be one of " + ", ".join(sorted(VALID_STORAGE)))
    if get_path(data, "storage.organization") not in VALID_ORG:
        problems.append("storage.organization must be one of " + ", ".join(sorted(VALID_ORG)))
    if get_path(data, "publishing.auto_publish") is True and get_path(data, "approval.content_to_publish") is True:
        problems.append("Auto-publish conflicts with mandatory content-to-publish approval")
    if get_path(data, "storage.mode") == "google_drive" and not get_path(data, "storage.root"):
        problems.append("Google Drive mode needs an authorized storage.root folder URL/ID")
    return problems

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_project.py path/to/project.yaml", file=sys.stderr)
        sys.exit(2)
    try:
        issues = validate(sys.argv[1])
    except (OSError, yaml.YAMLError) as exc:
        print(f"Cannot read YAML: {exc}", file=sys.stderr)
        sys.exit(2)
    if issues:
        print("INVALID PROFILE:\n- " + "\n- ".join(issues))
        sys.exit(1)
    print("VALID PROFILE")
