# mod_bs
A Modified Binary Search

## Description
Here is a log array, and each element is a timestamp.
The log array has limited fixed capacity.
If log exceed the limition, the new timestamp will be stored from the beginning of the log array, and we say this array be `overwritten`.

## Example
* A log array which length is 5
  * Array A didn't be overwritten
  * Array B has been overwritten.

| Array A             | Array B         |
| ------------------- | :--------------:|
| ts1                 | ts7             |
| ts3                 | ts9             |
| ts4                 | ts12            | 
| ts5                 | ts5             |
| ts6                 | ts6             |

## Definition
* We call Array A is `In-order`
* We call the whole Array B is `Out-of-Order`, but
  * First 3 elements of Array B (ts7 ~ ts12) is still `In-order`
  * Latest 2 elements of Array B (ts5 ~ ts6) is still `In-order`
  * Between ts12 and ts5 of Array B is an `overwritten point`.

## Question
Give a timestamp, detect whether this timestamp exist in the file.

## Solution 1
`find_val(arr, val)`
This function will find the oldest line,
Separate the array to two section,
Use the normal Binary Search for the section which contain the input value
Time complexity is [Find the oldest line] + [A Binary Search] = log(n) + log(n) ~= still log(n)

## Solution 2 
`modified_binary_search(arr, val)`

(TODO: Below descriptions need refine)
This function follow the origin process of Binary Search.
* A whole array may or may contain an `overwritten point`.
* Binary Search will separate an array to two sub-arrays.
* If one sub-array is `In-order` and its scope include the value we try to find, search this sub-array in the next loop of Binary Search, no matter whether an `overwritten point` is existent.
* At most one `overwritten point` is existent at any array.
  * a.k.a. At most one `Out-of-order` sub-array exist.
  * If the target timestamp is not in the other `In-order` sub-array, and **maybe** in the `Out-of-Order` sub-array, then search this sub-array in the next loop of Binary Search. 
