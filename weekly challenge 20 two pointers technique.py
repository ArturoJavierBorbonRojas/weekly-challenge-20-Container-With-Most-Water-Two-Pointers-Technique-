# Week 20: Container With Most Water (Two Pointers Technique)
# Author: Ing. Arturo Javier Borbon Rojas

def max_area(heights):
    print(f"Analyzing wall heights: {heights}")
    print("-" * 60)
    
    # Initialize our two pointers
    left = 0
    right = len(heights) - 1
    
    max_water = 0
    best_left = 0
    best_right = 0
    step = 1

    # The loop continues as long as the pointers haven't crossed
    while left < right:
        # Calculate the dimensions of our current container
        width = right - left
        
        # The water level is bottlenecked by the shorter wall
        current_height = min(heights[left], heights[right])
        current_area = width * current_height
        
        print(f"Step {step:02d} | Pointers at index [{left}] and [{right}] | Heights: ({heights[left]}, {heights[right]}) | Area: {current_area}")
        
        # Update our record if we found a bigger container
        if current_area > max_water:
            max_water = current_area
            best_left = left
            best_right = right
            print(f" New Max Area found: {max_water}!")
            
        # Optimization logic: 
        # To find a potentially larger area, we MUST move the pointer of the shorter wall
        # because the shorter wall limits the height of the container.
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
            
        step += 1

    print("-" * 60)
    print(f"Maximum Water Contained: {max_water} units")
    print(f"Optimal Container formed by walls at index {best_left} and {best_right}")
    print(f"Dimensions: Width = {best_right - best_left}, Height = {min(heights[best_left], heights[best_right])}")
    
    return max_water

# Test the algorithm with a classic dataset
walls = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area(walls)