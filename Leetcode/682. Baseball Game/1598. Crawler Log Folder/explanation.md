**Algorithm Idea**

For every "return home" operation we see, 
go back one level if we are not in the main
home. Otherwise, if the current element is not 
"./", we have seen an operation to extend the log. 
Update the cur variable correspondingly based 
on the seen elements. 

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 69 ms, faster than 25.41% of Python3 online submissions for Crawler Log Folder.
Memory Usage: 14.4 MB, less than 80.76% of Python3 online submissions for Crawler Log Folder.
