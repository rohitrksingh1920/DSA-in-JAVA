class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            result = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    part, i = parse(i + 1)
                else:
                    part = {expression[i]}
                    i += 1

                newResult = set()

                # Concatenation
                for a in result:
                    for b in part:
                        newResult.add(a + b)

                result = newResult

                # Union
                if i < len(expression) and expression[i] == ',':
                    part, i = parse(i + 1)
                    result |= part
                    return result, i

            return result, i + 1

        return sorted(parse(0)[0])