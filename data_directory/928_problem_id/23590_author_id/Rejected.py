import random
import sys

def valid(st) :
  return len(set(x for x in st)) == 4

def comp(guess, secret) :
  b, c = 0, 0
  for i in range(4) : 
    if secret[i] == guess[i] : 
      b += 1
    elif secret[i] in guess :
      c += 1
  return (b, c)

def check(guess, secret, bulls, cows) :
  b, c = comp(guess, secret)
  return bulls == b and cows == c

def filtered(candidates, history) :
  ret = []
  for c in candidates :
    good = True
    for query, res in history :
      if not check(c, query, res[0], res[1]) :
        good = False
    if good :
      ret.append(c)
  return ret

def next_guess(candidates, step) :
  if step < 2 :
    return candidates[random.randint(0, len(candidates)-1)]
    # Can get an accuracy of 99% if go random each step
  best = 5040
  if len(candidates) == 1 :
    return candidates[0]
  now = candidates[0]
  for g in candidates :
    poss = [ [0] * 5 for x in range(5)]
    for s in candidates :
      b, c = comp(g, s)
      poss[b][c] += 1
    penalty = max( max(arr) for arr in poss )
    if penalty < best :
      best = penalty
      now = g
  return now

def generate_all_initial() :
  ret = list(filter(valid, map( lambda x : "%04d" % x, range(9999))))
  return ret

everyone = generate_all_initial()
def test(true_secret) :
  global everyone
  choices, history = everyone[:], []
  for step in range(6) :
    take_guess = next_guess(choices, step)
    if not valid(take_guess) :
      print("Crashed", true_secret)
      break
    result = comp(take_guess, true_secret)
    history.append((take_guess,result))
    choices = filtered(choices, history)
  if len(choices) != 1 :
    print("Failed", true_secret)
    print(len(choices),history)
    return False
  else :
    print("Pass", true_secret)
    return True

def run() :
  global everyone
  choices, history = everyone[:], []
  for step in range(7) :
    take_guess = next_guess(choices, step)
    print(take_guess)
    sys.stdout.flush()
    b, c = map(int, input().split())
    history.append((take_guess,(b,c)))
    choices = filtered(choices, history)

#### Main ####
#true_secret = start[random.randint(0,5039)]
"""
count = 0
for true_secret in everyone :
  if not test(true_secret) :
    count += 1
print(count, count / 5040.0)
"""

run()