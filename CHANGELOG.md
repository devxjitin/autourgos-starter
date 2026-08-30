# Changelog

## [1.0.3] - 2026-08-30

- BREAKING: dependency migrated from `autourgos-react-agent>=1.7.1` to
  `autourgos-agent>=2.0.2`. `autourgos-react-agent`'s PyPI releases are now
  fully yanked and none satisfy `>=1.7.1` anyway, so this package was
  completely uninstallable from PyPI until this release — `pip install
  autourgos-starter` failed with "No matching distribution found for
  autourgos-react-agent>=1.7.1" for anyone trying it.
- The primary re-export is now `Agent` (was `ReactAgent`), matching the
  current package name, and `create_starter_agent()` returns an `Agent`
  instance. `ReactAgent` is kept as a deprecated alias for `Agent` so
  existing imports don't break.

## [1.0.2] - 2026-08-30

- Maintenance: bumped dependency floors to `autourgos-react-agent>=1.7.1` and `autourgos-openaichat>=2.3.1`, which pick up native tool-calling mode and the `invoke_with_tools`/`ainvoke_with_tools` per-call override fix. No code changes needed here — this package's own tests (8/8) pass unchanged against the bumped versions.

## [1.0.1] - 2026-08-30

- Fixed: `create_starter_agent()` called `OpenAIChatModel(..., system_instruction=system_prompt)`, but that constructor param was renamed to `system_prompt` back in `autourgos-openaichat` 2.0.0 — this call was never updated, so any install resolving a current `autourgos-openaichat` raised `TypeError: OpenAIChatModel.__init__() got an unexpected keyword argument 'system_instruction'`. Only worked by accident while the dependency floor (`>=1.0.2`) still allowed pip to resolve a pre-rename version.
- Bumped dependency floors to `autourgos-react-agent>=1.6.3` and `autourgos-openaichat>=2.3.0` (both fix a `TypeError` in `on_before_iteration`-style per-call overrides — see their changelogs) — this is also what surfaced the `system_instruction` bug above, since it forces a post-rename `autourgos-openaichat`.

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
