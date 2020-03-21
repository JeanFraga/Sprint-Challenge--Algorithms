#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

    I justify this answer because there is one loop, meaning the runtime complexcity is just (n). I remove (a) because it is a constant.


b) O(n^2)

    I justify this answer because, after removing the 4 constants(O(1)) we are left with O(n*M) = O(n^2)

c) O(n)

    I justify this answer because of recursion. It behaves a lot like a loop, more memory intensive of course, but like a loop nonetheless. The bigger 'bunnies' the more times this loop will run. But it will behave like a constant.

## Exercise II

This algorithm requires me to keep track of n(the number of stories this building has) and f(the theoretical number of floors the eggs can survive).
We know that if the egg cracks on floor (f) we have to go down one floor(f-1). In order to minimize the number of eggs dropped + borken we will also want to keep track of this value internally, but possibly not relevant as a return value. I would begin by creating a while loop that continues until the test reaches (n) floors; from the first floor up to (n) floor, to minimize the amount of eggs broken. Inside the while loop I would make a for loop that will drop the egg(theoretically) and check if the egg broke. If it did not break the loop would continue adding floors (f+=1) one floor at a time until the egg breaks once. When the egg breaks, (break) out of the loop and set the (counter = n) to break out of the while loop, with an (if) statement. Then return (f-1).

The runtime complexcity for this algorithm is: O(n)
I justify this answer because the first while loop is just counting up (counter+=1) until (n) floors. Meaning that the complexcity will increase in a constant (n) manner. One floor at a time. My answer would change if the exercise asked us to test an egg breaking 3 times before returning (f-1) as a scientific experiment haha. But it did not.