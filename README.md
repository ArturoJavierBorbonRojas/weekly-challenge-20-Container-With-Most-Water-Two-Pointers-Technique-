# weekly-challenge-20-Container-With-Most-Water-Two-Pointers-Technique-

Milestone reached: Week 20! 🎉 For this challenge, I went back to the roots of algorithmic logic and optimization by solving the classic "Container With Most Water" problem.
The problem asks us to find two lines (walls) from an array of heights that, together with the x-axis, form a container that holds the absolute maximum amount of water.

## How it works (Two Pointers Technique)
A beginner's approach would use nested loops to calculate the area of every single pair of walls, resulting in a very slow $O(n^2)$ time complexity. 

Instead, I implemented the **Two Pointers Technique**:
1. Place one pointer at the very beginning (`left`) and one at the very end (`right`) of the array.
2. Calculate the area formed by these two walls: $Area = width \times \min(height[left], height[right])$.
3. Update the maximum area recorded so far.
4. **The core logic:** Since the height of the water is bottlenecked by the shorter wall, moving the taller wall inwards cannot possibly increase the area. Therefore, we always move the pointer that points to the shorter wall, hoping to find a taller one.
5. Repeat until the pointers meet.

##  Complexity Analysis
* **Time Complexity:** $O(n)$ - The algorithm only passes through the array exactly once, making it incredibly fast and scalable.
* **Space Complexity:** $O(1)$ - It only uses a few integer variables to keep track of indices and areas, requiring constant memory.

##  Dependencies
* Python 3.14 (Pure standard library)
