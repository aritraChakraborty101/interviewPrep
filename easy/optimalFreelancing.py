#optimal freelancing

# you recently started freelancing development and have been offered variety
# of job opportunities. each job has a deadline, meaning there  is no
# value in completing a job after its deadline. you're given a list of jobs
# where each job has a deadline and profit.

# what is the maximum profit can be achived in 7 days period if you can only
# work on one job at a time.

jobs = [
    {
      "deadline": 1,
      "payment": 7
    },
    {
      "deadline": 2,
      "payment": 2
    },
    {
      "deadline": 2,
      "payment": 4
    },
    {
      'deadline': 6,
      'payment': 5
    }
  ]

#return a single integer representing the maximum profit you can make in 7 days
# if you can only work on one job at a time
#write a dynamic programming solution


def optimalFreelancing(jobs):
    week = 7
    profit = 0
    jobs.sort(key = lambda job: job["payment"], reverse = True)
    timeline = [False] * week
    for job in jobs:
        maxTime = min(job["deadline"], week)
        for time in reversed(range(maxTime)):
            if timeline[time] == False:
                timeline[time] = True
                profit += job["payment"]
                break
    return profit

