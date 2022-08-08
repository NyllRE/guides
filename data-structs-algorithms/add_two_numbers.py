#Definition for singly-linked list.
import math

class Solution:
   def addTwoNumbers(l1, l2):
      newlist = []
      addnextround = False

      longer = len(l1) if len(l1)>=len(l2) else len(l2)

      if len(l1) != len(l2):
         firstIsLarger = True if len(l1) > len(l2) else False

         for missing in range( math.floor( math.fabs(len(l1) - len(l2)) ) ):
            print(missing)
            if firstIsLarger:
               l2.append(0)
            else:
               l1.append(0)

      for iter in range(longer):
         toadd = l1[iter] + l2[iter]
         toadd += 1 if addnextround else 0
         if toadd >= 10:
            toadd -= 10
            addnextround = True
         else:
            addnextround = False

         newlist.append( toadd )
      
      if addnextround:
         newlist.append(1)
      return newlist

   


result = Solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])
print(result)