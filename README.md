# mod_bs
A Modified Binary Search

## Problem
Here is a log file, and each line is a timestamp.
The log file has limited fixed lines.
If log exceed the limition lines, the latest log will be overwrited from the beginning of the log file

Question: Give a timestamp, detect whether this timestamp exist in the file.

## Method 1
`find_val(arr, val)`
This function will find the oldest line,
Separate the array to two section,
Use the normal Binary Search for the section which contain the input value
Time complexity is [Find the oldest line] + [A Binary Search] = log(n) + log(n) ~= still log(n)

## Method 2
`modified_binary_search(arr, val)`
This function follow the origin process of Binary Search
But do some additional check:
* TBD...
