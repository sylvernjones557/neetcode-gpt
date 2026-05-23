class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
         # Starting position on the hill
        x = init

        # Move downhill repeatedly
        for _ in range(iterations):

            # Current slope
            gradient = 2 * x

            # Gradient descent update
            x = x - learning_rate * gradient

        # Final optimized value
        return round(x, 5)

