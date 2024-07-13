class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


asteroids = [5, 10, -5]
print(Solution().asteroidCollision(asteroids))
