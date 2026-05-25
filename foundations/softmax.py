import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # Step 1: Numerical stability trick
        z = z - np.max(z)
        
        # Step 2: Compute exponentials
        exp_z = np.exp(z)
        
        # Step 3: Normalize into probabilities
        softmax_output = exp_z / np.sum(exp_z)
        
        # Step 4: Round to 4 decimal places
        return np.round(softmax_output, 4)
