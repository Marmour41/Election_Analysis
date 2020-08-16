# Stock Price Analysis

## Overview of Project

### Purpose
The purpose of this analysis was to create an efficient code to run over a list of casted votes for a congressional election and output the results.

## Election Audit Results
- The total number of votes casted in this election was 369,711.
- There were three counties that voted in this congressional election; **Jefferson**, **Denver**, and **Arapahoe**. Jefferson county had 38,855 votes casted, which equals *10.5%* of the total votes casted. Denver county had 306,055 votes casted, which equals *82.8%* of the total votes casted. The last county, Arapahoe, had 24,801 votes casted, which equals *6.7%* of the total votes casted.
- Denver county had the largest number of votes casted.
- There were three candidates that ran in this elections; **Charles** **Stockham**, **Diana** **DeGette**, and **Raymon** **Doane**. Charles Stockham received 85,213 votes, which was *23.0%* of the total votes. Diana Degette received 272,892 votes, which was *73.8%* of the total vote. Finally, Raymon Doane received 11,606 votes, which was *3.1%* of the total votes.
- The winner of the election was **Diana Degette**. She received 272,892 votes which was 73.8% of the total votes. The full election results can be found here [Election results](Module_3_Challenge/Resources/Election_Results.png).


## Summary

### Proposal
I recommend to the election commission to use this code for other elections as well. Using this code, the election commission would be able to easily analyze other elections. A few modifications would need to be made, specifically, getting the candidate and county names for each row. The code that I have developed gets the candidate name using `candidate_name = row[2]`. Depending on the .csv file for other elections, you might need to change the row to make sure this gets the candidate name. Similarly, I used `county_name = row[1]` to get the county name. This will need to change if another election has a different file format. 
