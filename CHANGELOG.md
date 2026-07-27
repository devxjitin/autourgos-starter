# Changelog

## [1.0.0] - 2026-07-27

First release.

- Added: `create_starter_agent()` — builds a ready-to-use `ReactAgent`
  wired to `OpenAIChatModel` (autourgos-openaichat) and
  `ConversationBufferMemory` (autourgos-buffer-memory) in one call.
- Added: re-exports of `ReactAgent`, `tool`, `OpenAIChatModel`, and
  `ConversationBufferMemory` so beginners don't need to know which
  sub-package each class comes from.
- Depends on `autourgos-react-agent>=1.6.0`, `autourgos-openaichat>=1.0.2`,
  `autourgos-buffer-memory>=2.0.1` as real pip dependencies (no vendored
  or copied code).
