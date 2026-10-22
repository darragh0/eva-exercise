# Architectural Decision Records

## ADR-001: Split into modules (one per responsibility)

- **Problem:** All responsibilities reside in a single 62-line module that shares global variables; nothing can be
  changed or tested in isolation.
- **Alternatives:** Keep a single file with functions; use classes per concern (e.g. `EvaReader`, `Plotter`).
- **Decision:** Seven modules (`models`, `loader`, `preparation`, `analysis`, `cli`, `charts`, `__main__`) in an `eva/`
  package that communicate through `RawEva`/`EvaRecord` and return values.
- **Rationale:** Each module maps to one separation-of-concerns responsibility; functions avoid stateless classes; no
  unnecessary dependencies, such as Pydantic.
- **Consequences:** Calculations are testable; new features touch fewer modules; more files for a small app.

## ADR-002: Validate year ranges in a `YearRange` model type

- **Problem:** The country comparison must reject invalid year ranges without crashing.
- **Alternatives:** Validate in `cli` only; validate in `__main__`; enforce it in the `YearRange` type itself.
- **Decision:** `YearRange` raises `ValueError` if the start year is after the end year, and `cli` catches it and
  re-prompts.
- **Rationale:** The rule lives in one place, and analysis can never receive an invalid range.
- **Consequences:** The invalid-input test only needs `YearRange`, at the cost of a new dependency from `cli` to
  `models`.
