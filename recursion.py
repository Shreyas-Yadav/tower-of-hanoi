NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []
print(A, B, C, '\n')



"""
This module solves the Tower of Hanoi problem using recursion.
Attributes:
    NUMBER_OF_DISKS (int): The number of disks in the Tower of Hanoi problem.
    A (list): The source rod containing the disks initially.
    B (list): The auxiliary rod used during the process.
    C (list): The target rod where disks need to be moved.
Functions:
    move(n, source, auxiliary, target):
        Recursively moves disks from the source rod to the target rod using the auxiliary rod.
        Args:
            n (int): The number of disks to move.
            source (list): The rod from which disks are moved.
            auxiliary (list): The rod used as an auxiliary during the process.
            target (list): The rod to which disks are moved.
"""
def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    print(A, B, C, '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B


if __name__ == '__main__':
    move(NUMBER_OF_DISKS, A, B, C)

