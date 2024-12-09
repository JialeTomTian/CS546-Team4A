# Credits: Partly taken from RepoQA (https://github.com/evalplus/repoqa/blob/main/repoqa/provider/vllm.py)
from typing import List

from transformers import AutoTokenizer  # type: ignore
from vllm import LLM, SamplingParams

from request import construct_message_list, hacky_assistant_stop_seq
from request.base import BaseProvider


class VllmProvider(BaseProvider):
    def __init__(
        self,
        model,
        tensor_parallel_size,
        max_model_len=None,
        trust_remote_code=False,
        attn_implementation=None,
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model, trust_remote_code=trust_remote_code
        )
        self.llm = LLM(
            model=model,
            tensor_parallel_size=tensor_parallel_size,
            max_model_len=max_model_len,
            trust_remote_code=trust_remote_code,
            attn_implementation=attn_implementation,
        )
        self.stop_seq = []
        if self.tokenizer.chat_template:
            self.stop_seq.append(hacky_assistant_stop_seq(self.tokenizer))

    def generate_reply(
        self, question, n=1, max_tokens=1024, temperature=0.0, system_msg=None
    ) -> List[str]:
        assert temperature != 0 or n == 1, "n must be 1 when temperature is 0"

        prompt = self.tokenizer.apply_chat_template(
            construct_message_list(question, system_msg),
            tokenize=False,
            add_generation_prompt=True,
        )
        vllm_outputs = self.llm.generate(
            [prompt],
            SamplingParams(
                temperature=temperature,
                max_tokens=max_tokens,
                stop=self.stop_seq,
            ),
            use_tqdm=False,
        )

        gen_strs = [x.outputs[0].text for x in vllm_outputs]
        return gen_strs
