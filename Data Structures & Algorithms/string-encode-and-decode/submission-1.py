from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            # Ищем разделитель после длины
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            ans.append(s[start:end])
            i = end

        return ans