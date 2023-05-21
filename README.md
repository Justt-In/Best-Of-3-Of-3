# Best-Of-3-Of-3
A mini project of mine to create what I believe to be the fairest game of chance to help anyone decide between 2 options.
'Heads' for Yes and 'Tails' for No

## How It Woks:
1. A random number is generated from 1-100, afterwards modulus of 2 is applied resulting in either 0 or 1(odd or even).
2. This repeats to complete a best of 3, meaning either heads or tails appears twice (Heads|Heads, Tails|Heads|Heads, etc...). This is marked as 1 'Best of 3' Round. 
3. This repeats till either 2 rounds go to 'Yes' or two rounds goes to 'No', completing the 'Best Of 3 Of 3'. Issuing a winner of either a Yes or No.
4. Next, another set of coinflips initializes to compete for consecutive 0's or 1's.

As follows:
  - 0,0 -> Restart step 4
  - 0,1 -> Restart from step 1 (remove all progress)
  - 1,0 -> Restart step 4
  - 1,1 -> Result of 'Best of 3 of 3' (Steps 1 - 3) is valid and is the decided option. 

## File Types:
1. BO3 is the detailed version that shows most of the outputs 
2. SimpleBO3 shows a simplified version without much outputs

___Run script in python ready console or your preferred IDE___
