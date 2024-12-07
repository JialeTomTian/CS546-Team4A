# Credits: Partly taken from RepoQA (https://github.com/evalplus/repoqa/blob/main/repoqa/provider/base.py)
from abc import ABC, abstractmethod
from typing import List


class BaseProvider(ABC):
    @abstractmethod
    def generate_reply(
        self, question, n=1, max_tokens=1024, temperature=0.0, system_msg=None
    ) -> List[str]:
        ...
