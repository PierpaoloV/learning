# Notes — Group Anagrams

## My Approach
I started by thinking that I should iterate through the list of strings and for each string, I should check if it is an anagram of any of the other strings in the list.
To do this, I would need to create a list of lists, where each inner list would contain the anagrams of a particular string. So for each string, I would create a new list and add it to the list of lists.
Then, I would iterate through the list of strings and for each string, I would check if it is an anagram of any of the other strings in the list. If it is, I would add it to the list of lists.
This way, I would be able to group the anagrams together.


## Complexity
- Time: O(?)
- Space: O(?)

## What I learned
Didn't know that to check if two strings are anagrams, I can sort the characters of the strings and check if the sorted strings are equal. It's a simple yet effective way to check for anagrams.

