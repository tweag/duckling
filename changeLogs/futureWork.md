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
