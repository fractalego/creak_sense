import torch

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from creak_sense.utils import generate_answer, get_answer_prompt, generate_single_token, get_cause_prompt

_device = "cuda" if torch.cuda.is_available() else "cpu"


class CreakSense:
    def __init__(self, model_name: str):
        self._model = GPT2LMHeadModel.from_pretrained(model_name)
        self._model.to(_device)
        self._tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    def make_sense(self, claim: str) -> bool:
        prompt = get_answer_prompt(claim)
        if generate_single_token(self._model, self._tokenizer, prompt) == "Y":
            return True

        return False

    def get_reason(self, claim, claim_is_true=True):
        prompt = get_cause_prompt(claim, "Yes" if claim_is_true else "No")
        return generate_answer(self._model, self._tokenizer, prompt)
