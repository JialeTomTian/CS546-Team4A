import os
import signal
import time
from typing import List

import openai
from openai import Client
from openai.types.chat import ChatCompletion
from transformers import AutoTokenizer

from request import construct_message_list, hacky_assistant_stop_seq
from request.base import BaseProvider


def make_request(
    client: openai.Client,
    message: str,
    model: str,
    max_tokens: int = 512,
    temperature: float = 1,
    n: int = 1,
    system_msg="You are a helpful assistant good at coding.",
    **kwargs,
) -> ChatCompletion:
    return client.chat.completions.create(
        model=model,
        messages=construct_message_list(message),
        max_tokens=max_tokens,
        temperature=temperature,
        n=n,
        **kwargs,
    )


def handler(signum, frame):
    # swallow signum and frame
    raise Exception("end of time")


def make_auto_request(*args, **kwargs) -> ChatCompletion:
    ret = None
    while ret is None:
        try:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(100)
            ret = make_request(*args, **kwargs)
            signal.alarm(0)
        except openai.RateLimitError:
            print("Rate limit exceeded. Waiting...")
            signal.alarm(0)
            time.sleep(10)
        except openai.APIConnectionError:
            print("API connection error. Waiting...")
            signal.alarm(0)
            time.sleep(5)
        except openai.APIError as e:
            print(e)
            signal.alarm(0)
        except Exception as e:
            print("Unknown error. Waiting...")
            print(e)
            signal.alarm(0)
            time.sleep(1)
    return ret


class OpenAIProvider(BaseProvider):
    def __init__(self, model, base_url: str = None):
        self.model = model
        self.client = Client(
            api_key=os.getenv("OPENAI_API_KEY", "none"), base_url=base_url
        )
        self.stop_seq = []
        try:
            tokenizer = AutoTokenizer.from_pretrained(model)
            if tokenizer.chat_template:
                self.stop_seq.append(hacky_assistant_stop_seq(tokenizer))
            print("Using stop sequence: ", self.stop_seq)
        except:
            print("Failed to automatically fetch stop tokens from HuggingFace.")

    def generate_reply(
        self, question, n=1, max_tokens=1024, temperature=0.0, system_msg=None
    ) -> List[str]:
        assert temperature != 0 or n == 1, "n must be 1 when temperature is 0"
        replies = make_auto_request(
            self.client,
            message=question,
            model=self.model,
            temperature=temperature,
            n=n,
            max_tokens=max_tokens,
            system_msg=system_msg,
            stop=self.stop_seq,
        )

        return [reply.message.content for reply in replies.choices]
