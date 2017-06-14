1) Fix normalization of hours in "between <time-of-day> and <time-of-day> (interval)" rule.

Two subproblems
a) Remark : For "from" :Rather difficult to judge the correct interpretation for '10' -> Tell the user explicitly to add pm/am at all times?
b) "to" : needs to be changed to 23 hours

intersect by "on" (between 10 and 11 pm on Monday)
-- between <time-of-day> and <time-of-day> (interval) (between 10 and 11 pm)
-- -- regex (between)
-- -- time-of-day (latent) (10)
-- -- -- integer (numeric) (10)
-- -- -- -- regex (10)
-- -- regex (and)
-- -- <time-of-day> am|pm (11 pm)
-- -- -- time-of-day (latent) (11)
-- -- -- -- integer (numeric) (11)
-- -- -- -- -- regex (11)
-- -- -- regex (pm)
-- regex (on)
-- Monday (Monday)
-- -- regex (Monday)
[Entity {dim = "time", body = "between 10 and 11 pm on Monday", value = "{\"values\":[{\"to\":{\"value\":\"2013-02-19T00:00:00.000-02:00\",\"grain\":\"hour\"},\"from\":{\"value\":\"2013-02-18T10:00:00.000-02:00\",\"grain\":\"hour\"},\"type\":\"interval\"},{\"to\":{\"value\":\"2013-02-19T00:00:00.000-02:00\",\"grain\":\"hour\"},\"from\":{\"value\":\"2013-02-18T22:00:00.000-02:00\",\"grain\":\"hour\"},\"type\":\"interval\"},{\"to\":{\"value\":\"2013-02-26T00:00:00.000-02:00\",\"grain\":\"hour\"},\"from\":{\"value\":\"2013-02-25T10:00:00.000-02:00\",\"grain\":\"hour\"},\"type\":\"interval\"}],\"to\":{\"value\":\"2013-02-19T00:00:00.000-02:00\",\"grain\":\"hour\"},\"from\":{\"value\":\"2013-02-18T10:00:00.000-02:00\",\"grain\":\"hour\"},\"type\":\"interval\"}", start = 0, end = 30}]

2) general rule: no absorption of preposition unless they change semantics + repeatedInterval type
  e.g. 'June' (Time) -> 'in June' (Time)  will remain disactivated
  however '2 hours' (Duration) -> 'in two hours' (Time) should be reactivated. It has been disabled so as not to interfere with 'in 15-minute intervals' for Milestone 1. This should be solved by making a distinction between durations and repeatedIntervals. For example, per + '2 hours' (Duration) should become (repeatedInterval), just like ('every 2 hours'), or even '15-minute' (Duration) + 'interval(s)'. By adding a separate type we can guide the rules more precisely.
  For normalization of repeatedTypes, use same format as duration?

3) More Haskell-like integration of the test suite.
currently, diff on the output of lines that are posted through curl. Rationale is that the tests in the Test directory are organized per Type and I'm more interested in checking which Types are recognized over others (as well as repeated performance on the same test set.) Where should I place the ecoTest set in the Duckling Test directories?
