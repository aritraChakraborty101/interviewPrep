# There's an algorithms tournament taking place in which teams of programmers
# compete against each other to solve algorithmic problems as fast as possible.
# Teams compete in a round robin, where each team faces off against all other
# teams. Only two teams compete against each other at a time, and for each
# competition, one team is designated the home team, while the other team is
# the away team. In each competition there's always one winner and one loser;
# there are no ties. A team receives 3 points if it wins and 0 points if it
# loses. The winner of the tournament is the team that receives the most amount
# of points.
#

#


def tournamentWinner(competitions, results):
    result = {}

    for i in range(len(competitions)):
        temp = competitions[i]
        first_team = temp[0]
        second_team = temp[1]

        winner = results[i]

        if winner == 1:
            if first_team not in result:
                result[first_team] = 3
            else:
                result[first_team] += 3

        else:
            if second_team not in result:
                result[second_team] = 3
            else:
                result[second_team] += 3
    return max(result, key=result.get)






test = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

result = [0, 0, 1]

print(tournamentWinner(test, result))



