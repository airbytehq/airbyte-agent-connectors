# md2gdoc - Claude Code Skill

Convert markdown files into styled Google Docs using your own Google Doc template.

## What this skill does

- Auto-generates a template skeleton from a Google Doc URL
- Maps markdown sections into template placeholders
- Converts via pandoc and post-processes styling with python-docx
- Uploads the final `.docx` and converts it to a native Google Doc

## Install

### Via plugin marketplace

In Claude Code, run:
```
/plugin marketplace add airbytehq/airbyte-agent-connectors
```
Then install:
```
/plugin install airbyte-agent-connectors@md2gdoc
```

### Manual

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/airbytehq/airbyte-agent-connectors.git /tmp/airbyte-skills
cp -r /tmp/airbyte-skills/skills/md2gdoc .claude/skills/
rm -rf /tmp/airbyte-skills
```

## Requirements

- Python 3.13+
- `pandoc`
- Google OAuth credentials for Drive API access
- Python dependencies from `requirements.txt`

See [SKILL.md](SKILL.md) for full setup and workflow details.
