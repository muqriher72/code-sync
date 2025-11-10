class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        # O(n) time and O(1) space
        
        # variable to track robot direction
        k = 0

        # variable to track distance travelled per direction
        dist = [0, 0, 0, 0] # n, w, s, e

        for instruction in instructions:
            if instruction == 'L':
                k = (k + 1) % 4
            elif instruction == 'R':
                k = (k + 3) % 4
            else:
                dist[k] += 1
        
        is_at_origin = (dist[0] == dist[2] and dist[1] == dist[3])

        is_not_facing_north = k != 0

        return is_at_origin or is_not_facing_north