class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's Triangle with a given number of rows.
        Each row starts and ends with 1.
        The numbers in between are made by adding two numbers above it.
        """

        # Base cases (the simplest answers we already know)
        if numRows == 0:   # If no rows requested, return empty triangle
            return []
        if numRows == 1:   # If only 1 row requested, return [[1]]
            return [[1]]
        
        # print(triangle)
        # Step 1: Get the triangle built so far (everything except the new row)
        triangle = self.generate(numRows - 1)
        print(f"Triangle after {numRows-1} rows: {triangle}")

        # Step 2: Get the last row (to build the next one from it)
        previous_row = triangle[-1]
        print(f"Previous row ({numRows-1}): {previous_row}")

        # Step 3: Start the new row with a 1
        current_row = [1]

        # Step 4: Fill in the middle numbers
        # Each middle number = sum of two numbers directly above it
        for i in range(1, numRows - 1):
            left_number = previous_row[i - 1]
            right_number = previous_row[i]
            new_number = left_number + right_number
            current_row.append(new_number)
            print(f"Added {left_number}+{right_number}={new_number} at position {i}")

        # Step 5: End the row with a 1
        current_row.append(1)
        print(f"Completed new row {numRows}: {current_row}")

        # Step 6: Add the new row to the triangle
        triangle.append(current_row)
        print(f"Triangle after {numRows} rows: {triangle}\n")

        return triangle
        