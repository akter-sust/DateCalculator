# DateCalculator

# Problem Description
You have joined a science project where a series of experiments are run for which you
need to calculate the number of full days elapsed in between two events.

The first and the last day are considered partial days and never counted. Following this
logic, the distance between two related events on 03/08/2018 and 04/08/2018 is 0,
since there are no fully elapsed days contained in between those, and 01/01/2000 to
03/01/2000 should return 1.

The solution needs to cater for all valid dates between 01/01/1901 and 31/12/2999.

# Test cases
1) 02/06/1983 - 22/06/1983 = 19 days
2) 04/07/1984 - 25/12/1984 = 173 days
3) 03/01/1989 - 03/08/1983 = 1979 days
(Please note these dates are formatted DD/MM/YYYY)
