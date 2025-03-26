MARKETING_FILE = '2024/Fall 2024/CSIA450 - Cyber Security Capstone/Week 8/HARVI/marketing.txt'
TECHNOLOGY_FILE = '2024/Fall 2024/CSIA450 - Cyber Security Capstone/Week 8/HARVI/technology.txt'
PILOT_SCORES = [[40, 68], [62, 61], [74, 64], [22, 76], [64, 90], [65, 75], [49, 66], [49, 60], [49, 63]]

def CreateList(file):
  # Empty list for storing score values
  scores = []
  # Open the file and read the scores to the list
  with open(file, 'r') as f:
    for line in f:
      sLine = line.split()
      scores.append(sLine)
  # Reformat all scores from str to int
  for score in scores:
    score[0] = int(score[0])
    score[1] = int(score[1])
  # Return the finished list
  return scores

def AverageScores(scores):
  # Keep track of the score sums for now
  beforeAvg = 0
  afterAvg = 0
  # Adding up the scores
  for score in scores:
    beforeAvg += score[0]
    afterAvg += score[1]
  # Finding the average before and after training
  beforeAvg = beforeAvg / len(scores)
  afterAvg = afterAvg / len(scores)
  # Return the averages
  return beforeAvg, afterAvg

def main():
  # Description of output
  print('Average HARVI Score by Department')
  print('(Lower is better)')

  # Pilot scores
  pilotBefore, pilotAfter = AverageScores(PILOT_SCORES)
  print('\nPilot Scores')
  print('Before:', f'{pilotBefore:.2f}')
  print('After:', f'{pilotAfter:.2f}')

  # Determine if training was successful
  if pilotBefore > pilotAfter:
    print('Successful training')
  else:
    print('Ineffective training')

  # Marketing department scores
  marketBefore, marketAfter = AverageScores(CreateList(MARKETING_FILE))
  print('\nMarketing Department')
  print('Before:', f'{marketBefore:.2f}')
  print('After:', f'{marketAfter:.2f}')

  # Determine if training was successful
  if marketBefore > marketAfter:
    print('Successful training')
  else:
    print('Ineffective training')

  # Technology department scores
  techBefore, techAfter = AverageScores(CreateList(TECHNOLOGY_FILE))
  print('\nTechnology Department')
  print('Before:', f'{techBefore:.2f}')
  print('After:', f'{techAfter:.2f}')
  
  # Determine if training was successful
  if techBefore > techAfter:
    print('Successful training')
  else:
    print('Ineffective training')

main()