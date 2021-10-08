# Kakuro
A study/exploration of the Kakuro number game

Intro/Context: Back in high school I discovered Sudoku Puzzles and quickly became enthralled with the logic and deduction needed to solve these puzzles. My mom later bought me "The Book of Kakuro" as another puzzle that was similar, but not the same.

For reference: https://en.wikipedia.org/wiki/Kakuro

Because both of these games revolve around logic, deduction, and math, I became curious about the underlying math of these games, and sought to explore the numeric properties of how these puzzles are arranged and how one could automate the deduction process.

Captured here will be my thought process while exploring this puzzle type. I've already begun exploring some avenues of tool development and solving techniques, but will begin capturing notes here for posterity.

05 OCT 2021:
My typical strategy for solving Kakuro puzzles is to first scan for numbers that have only one combination of digits. For example, a sum of 6 with 3 numbers can only be achieved by the set {1,2,3} and from there I need to figure out the order of these numbers. The easiest of these numbers to identify are those that sum up sequential numbers, but there are additional sums that have singular sets of numbers that I'm not the quickest at identifying. Thinking about the possible combinations that yield the desired sum and then eliminating sets as more information is revealed has generally worked, but I'm not sure what's the best way to code this.

I've built a script to generate all possible combinations of the numbers 1-9 to create desired sums, but I'm dissatisfied that my approach relies on guess and check. I had to use itertools to create a selection map of numbers and simply drop all sets that didn't result in my desired sum. This is easy to implement for only 9 numbers, but it certainly wouldn't scale.

07 OCT 2021:
Added include/exclude arguments to combinations function. Thinking of ways to chain calls to this to set up some system of equations to solve. I noticed a common tactic I've been using to determine numbers is to compare the remaining sum once a number has been placed. For example, for sums of 11-17 in 2 numbers, both numbers must be greater than (sum-10) otherwise I'll get an impossible set. Using this information will need to be able to reason out positional conditions though, and the current function does not do this.
