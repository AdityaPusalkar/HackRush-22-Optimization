# HackRush-22-Optimization
HackRush'22 Optimization Challenge Submission.

##Submission 1##
The code in the first submission "finalsubmission1.py" implements the following algorithm:
The bombs are added to a list as a quadruple of (Bomb-Radius, X-Coordinate, Y-Coordinate, Bomb-ID).

Then we sort the list in descending order according to the radius of the bombs.

After that we create clusters, here clusters are all those bombs which are in the radius of one another and can reach (explode) if any one of the bomb explodes.

The implementation considers bidirectional edges instead of unidirectional. In the end we have a graph connecting the bombs.

Then we calculate the area of explosion of each bomb cluster. The total area is calculated by having a traversal through cluster in the graph.

We also find the extreme coordinates (bounding coordinates) of each cluster. This is used to efficiently place the jammers in the reactangle formed by the coordinates.
Link to the arrangement can be found below. 

https://stackoverflow.com/questions/7716460/fully-cover-a-rectangle-with-minimum-amount-of-fixed-radius-circles
As an edge case if the algorithm places more jammers than the number of bombs then we simply place jammers on the bombs and disable nearby bombs until all bombs are defused. (greedy algorithm - will be mentioned in the next submission)

After this is done we have defused all the bombs. However, it is possible that some jammers are not worth it and we can remove them at the expense of a bomb explosion.
So we use the following function:
def notworthit(numjam, area, currjam):
    return (200 * numjam * currjam - 100 * currjam ** 2 > 0.7 * area)
Here currjam is the number of jammers in the cluster, numjam is the total number of jammers used so far, and area is the explosion area of the cluster.

We a return value for each cluster and if the function returns true, we consider the jammers to not be worth it, and remove the jammers from the cluster.
After this optimization, we get our final set of jammers.

This implementation gave a very good score for the first test case, but an average result for the second test case.

The code in the second submission "finalsubmission2.py" implements the following algorithm:
The bombs are added to a list as a quadruple of (Bomb-Radius, X-Coordinate, Y-Coordinate, Bomb-ID).

Then we sort the list in descending order according to the radius of the bombs.

Note: the following step (in * ) was not implemented in the submission but was intended to be done.

*We add a directed edge from one bomb to another if the first bomb's explosion area contains the second bomb.
We then calculate the area of explosion if a certain bomb was exploded by traversing through the tree starting at the said bomb.*

We now traverse through the list of bombs in descending order and greedily defuse each bomb. Once a bomb is defused (by placing a jammer on the bomb) we defuse all other bombs in its radius and remove them from the list.

After this is done we have defused all the bombs. However, it is possible that some jammers are not worth it and we can remove them at the expense of a bomb explosion.
So we use the following function:
def notworthit(numjam, radius):
    return (200 * numjam - 100 > 0.7 * 3.14 * radius ** 2)
Here numjam is the total number of jammers used so far, and radius is the radius of explosion area of a single bomb.

Note: In the algorithm, this step only considers removing bombs which have no outgoing edges are return true for the above function (not worth it). It was intended to do it for each bomb using the algorithm stated above in italics.

After this optimization, we get our final set of jammers.

This implementation gave a very good score for the first test case (although slightly less than the first submission), and an equally good result for the second test case.
