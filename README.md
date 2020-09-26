# Election_Analsis #

Election Analysis by using Python programming language


### Project Background ###
The purpose of this phython secript is analysising the election data with the following tasks to complete the election audit of a recent local congressional election in Colorado.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

The other task is analysing the voter turnout for each county with following tasks,
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

### SOFTWARE/TOOLS/LIBRARIES ###
Python 3.7.6, Visual Studio Code, 1.49.2

Data Source: election_results.csv

## Result ##

The analysis of the candidate vote show that:

1. There were 369,711 votes cast in the election.
2. The candidates were: + Charles Casper Stockham, + Diana DeGette, + Raymon Anthony Doane
3. The total numbers of vote each candidate received were:
   + Charles Casper Stockham has recieved 85213 votes. 
   + Diana DeGette has recieved 272892 votes. 
   + Raymon Anthony Doane has recieved 11606 votes.
4. The percentages were:
   + 23.0% of the vote for Charles Casper Stockham.
   + 73.8% of the vote for Diana DeGette.
   + 3.1% of the vote for Raymon Anthony.
5. The winner of the election was: Diana DeGette received 73.8% of the vote and (272,892) number of votes.

The results of python script for election analysis are following,
  
![](/Image_of_Candidate_analysis.PNG)


The analysis of the the voter turnout for each county shows that:

1. There were 369,711 votes cast in the election.
2. The county involed for elction were: Jefferson, Denver, and Arapahoe in Colorado.
3. The voter turnout for each county were:
   + The Jefferson county has 38,855 votes. 
   + The Denver county has 306,055 votes. 
   + The Arapahoe county has 24,801 votes.
4. The vote turnout were:
   + 10.5% for the Jefferson county.
   + 82.8% for the Denver county.
   + 6.7% % for the Arapahoe county.
5. The largest county turnout was: Denver has turnout of 82.8% with (306,055) number of votes.

The resuls of python script for the voter turnout for each county are following,
  
![](/Image_of_County_and_Candidate_Analysis.PNG)

## Conclusion
In 2018, only *ENPH* and *RUN* two stocks had positive yearly Return as well as large Total Daily Volume. Both of them was outperformance than others green stocks.



In 2017, all of stocks had positive Return except *TERP* (-7.2%). "DQ" made best yearly return with 199.4% but with lowest total Daily Volume (35,796,200) in 2017.




## Program Logical Flow

1. Request users input which year they would like to analyze stock performance.
```
yearValue = InputBox("What year would you like to run the analysis on?") 
```
    
2. Create and activate an analysis worksheet to keep all information retrieved.
3. Declare 1 array for ticker and 3 outputs arrays for saving data, as well as a variable named tickerIndex.
```
    Dim tickers(12) As String
    Dim volume(12) As String
    Dim startingPrices(12) As String
    Dim endingPrices(12) As String
    
    Dim tickerIndex As Integer
```

4. Create a main loop **(A)** to assigned tickerIndex from 0 to 11. Initialize index as zero before loops.
```
    tickerIndex = 0
    For tickerIndex = 0 to 11
        if meet some criteria then
            tickerIndex = tickerIndex + 1
    Next tickerIndex
```
5. Make a **(B)** loop go through all stocks data.
```
    Worksheets(yearValue).Activate
    For J = 2 To RowCount
        If Cells(J, 1).Value <> Cells(J - 1, 1).Value Then
            tickers(tickerIndex) = Cells(J, 1).Value
            startingPrices(tickerIndex) = Cells(J, 6).Value
        End If
        
        If Cells(J + 1, 1).Value <> Cells(J, 1).Value Then
            endingPrices(tickerIndex) = Cells(J, 6).Value
            *tickerIndex = tickerIndex + 1*
            End If
    Next J    
```
6. Make a nested loop **(C)** to get incremental Daily volumes for each stock, then put into Volume(tickerIndex).
```
        For x = 2 To RowCount
            If Cells(x, 1).Value = tickers(tickerIndex) Then
                TotalVolume = TotalVolume + Cells(x, 8).Value
            End If
        Next x
     volume(tickerIndex) = TotalVolume
```
7.  Create new loop **(D)** for putting outcomes into analysis Worksheet which created on step 2
```

    Worksheets("Challenge_All Stocks Anlysis").Activate
    For i = 0 To 11      
      Cells(i + 4, 1).Value = tickers(i)
      Cells(i + 4, 3).Value = endingPrices(i) / startingPrices(i) - 1
      Cells(4 + i, 2).Value = volume(i)
    Next i
```
8. Decor Font Formatting and conditional color Formatting to analysis Worksheets
