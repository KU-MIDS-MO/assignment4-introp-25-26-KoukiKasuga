import numpy as np

def mask_and_classify_scores(arr):
    """
    write your solution here;
    follow the instructions in the README.
    """

    if type(arr) == np.ndarray and arr.ndim == 2 and arr.shape[0] == arr.shape[1] and arr.shape[0] >= 4:
      #Part A:
        cleaned = arr.copy()
        min_number = 0
        max_number = 100
        cleaned[cleaned < min_number] = min_number
        cleaned[cleaned > max_number] = max_number

        #cleaned = np.clip(arr, 0, 100)

      #Part B:
        levels = cleaned.copy()
        low_threshold = 40
        high_threshold = 70
        levels[levels < low_threshold] = 0
        levels[(levels >=low_threshold) & (levels < high_threshold)] = 1
        levels[levels >= high_threshold] = 2
        """
        conditions = [
            cleaned < 40,                       #0: low
            (cleaned >= 40) & (cleaned < 70),   #1: medium
            cleaned >= 70                       #2: high
        ]                                     
        levels_values = [0, 1, 2]
        levels = np.select(conditions, levels_values)
        """

      #Part C:
        n_rows = cleaned.shape[0]

        row_pass_counts = np.zeros(n_rows, dtype=int)
        pass_threshold = 50

        for i in range(n_rows):
            row = cleaned[i, :]
            count = 0

            for score in row:
                if score >= pass_threshold:
                    count += 1
            row_pass_counts[i] = count
        
        return cleaned, levels, row_pass_counts
        
    else:
        return None
      
    pass