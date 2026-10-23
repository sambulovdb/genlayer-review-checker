# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class ReviewChecker(gl.Contract):
    last_review: str
    last_verdict: str

    def __init__(self):
        self.last_review = ""
        self.last_verdict = "none"

    @gl.public.write
    def check_review(self, review: str) -> None:
        prompt = (
            "Classify the sentiment of this product review. "
            "Answer with exactly one lowercase word: "
            "positive, negative or neutral.\n\n"
            "Review: " + review
        )

        def judge() -> str:
            answer = gl.nondet.exec_prompt(prompt).strip().lower()
            if "positive" in answer:
                return "positive"
            if "negative" in answer:
                return "negative"
            return "neutral"

        self.last_verdict = gl.eq_principle.strict_eq(judge)
        self.last_review = review

    @gl.public.view
    def get_last_review(self) -> str:
        return self.last_review

    @gl.public.view
    def get_last_verdict(self) -> str:
        return self.last_verdict
