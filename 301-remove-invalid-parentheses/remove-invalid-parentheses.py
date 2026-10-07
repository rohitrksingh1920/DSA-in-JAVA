class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}
        visited = {s}
        result = []
        found = False

        while queue:
            for string in queue:
                if isValid(string):
                    result.append(string)
                    found = True

            if found:
                return result

            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.add(new_string)

            queue = next_level

        return result