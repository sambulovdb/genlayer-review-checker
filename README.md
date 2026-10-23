# ReviewChecker — GenLayer Intelligent Contract

A minimal Intelligent Contract for [GenLayer](https://genlayer.com) that classifies the sentiment of a product review as **positive**, **negative** or **neutral** using LLMs, with the result agreed on by validator consensus (Optimistic Democracy).

## How it works

- `check_review(review: str)` — write method. Each validator runs the review through its own LLM via `gl.nondet.exec_prompt`, normalises the answer to one label, and the validators must reach the same label through `gl.eq_principle.strict_eq`. The agreed result is stored on-chain.
- `get_last_review()` — view method, returns the last checked review.
- `get_last_verdict()` — view method, returns the last verdict.

Normalising the LLM output to a fixed set of labels before comparison is what makes strict equality work: different models may phrase their answers differently, but they converge on the same single word.

## Tested on GenLayer Studio

- GenVM v0.2.16
- Deploy: FINALIZED
- `check_review("Great phone, battery lasts two days!")` → FINALIZED, `get_last_verdict()` returns `"positive"`

## Run it yourself

1. Open [GenLayer Studio](https://studio.genlayer.com).
2. Create a new contract and paste `review_checker.py`. If your Studio runs a different GenVM version, copy the two header lines from the built-in `storage.py` template.
3. Run and Debug → Deploy (no constructor arguments).
4. Call `check_review` with any review, then read `get_last_verdict`.

## Possible extensions

- Store a history of reviews in a `DynArray` instead of only the last one.
- Use `gl.eq_principle.prompt_comparative` to accept a short explanation alongside the label.
- Fetch reviews from a web page with `gl.nondet.web.render` instead of passing them in directly.
