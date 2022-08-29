import torch

_device = "cuda" if torch.cuda.is_available() else "cpu"

def get_answer_prompt(claim):
    return f"The claim is:\n{claim}\n\nThe claim makes sense:\n"


def get_cause_prompt(claim, claim_is_true):
    return f"The claim is:\n{claim}\n\nThe claim makes sense:\n{claim_is_true}\n\nBecause:\n"


def generate_single_token(model, tokenizer, prompt):
    model.eval()
    with torch.no_grad():
        tokens = tokenizer.encode(prompt, return_tensors="pt")
        output = _inference(model, tokenizer, tokens.to(_device), length=1)
        decoded = tokenizer.decode(output[0], skip_special_tokens=True)
        
    return decoded[len(prompt)]


def generate_answer(model, tokenizer, prompt, length=5):
    model.eval()
    with torch.no_grad():
        tokens = tokenizer.encode(prompt, return_tensors="pt")
        text = prompt
        start = len(prompt)
        while "." not in text[start:]:
            output = _inference(model, tokenizer, tokens.to(_device), length)
            decoded = tokenizer.decode(output[0], skip_special_tokens=True)
            text += decoded[len(text):]
            tokens = output

    end = text.find(".", start)
    return text[start:end].split(":")[-1].strip()


def _inference(model, tokenizer, tokens, length):
    return model.generate(
        tokens.to(_device),
        max_length=tokens.shape[1] + length,
        pad_token_id=tokenizer.eos_token_id,
    )
