import time
import datetime
import os.path

def start_up():
  welcome = """
  \n=======================================================
  \n               Welcome to bullet v1.0.0
  \n=======================================================
  """
  print (welcome)
  input ("press enter to begin\n\n>>")

  current_date = datetime.datetime.now()

  print ("\n\nToday is " + current_date.strftime("%m %d %y"))
  correct = input("is this correct? [Y/N]  ")

  journals = 'journals'

  if correct == "Y":
    print ("Great, creating today's jornal...\n\n")
    try: os.mkdir(journals)
    except Exception: pass
  else:
    print ("uhhhhhhh......")
    print ("\n\nclosing...\n\n")
    quit()

  journal_file = open( os.path.join(journals, current_date.strftime("%m%d%y") + '.txt'), 'a+')

  return journal_file

def format_time(m,s):
  if(s == 60):
    seconds = '00'
    m += 1
  elif(s < 10):
    seconds = '0' + str(s)
  else:
    seconds = str(s)
  if(m < 10):
    minutes = '0' + str(m)
  else:
    minutes = str(m)
  return minutes + ':' + seconds

def timer(minutes):
  m = minutes - 1
  while(m >= 0):
    s = 60
    while(s):
      print(format_time(m,s), end='\r')
      time.sleep(1)
      s -= 1
    m -= 1
  print('00:00')

def breathe(minutes):
  print('\n\ntime for a break...')
  timer(minutes)

def run_check():
  again = input('\n\nPress enter to continue, or type \'quit\' to stop: ')
  if again == "quit":
    return False
  else:
    return True

def bullet(minutes, journal):
  this_time = time.strftime("%H:%M")
  this_bullet = {}
  goal = input("\nWhat is your goal?  ")
  this_bullet.update({"goal" : goal})
  timer(minutes)
  complete = input("\nDid you accomplish your goal? [Y/N]  ")
  if complete == "Y":
    this_bullet.update({"complete": True})
  else:
    this_bullet.update({"complete": False})

  journal.append({ this_time : this_bullet })
  return journal

def reflect(journal):
  print('\n\nReflect on the past couple of hours.')
  print('\nHere\'s a recap:')
  print(journal)
  reflection = input('\nreflection: ')
  journal.append({'reflection' : reflection})
  return journal

def format_journal(journal):
  formatted = ''
  for entry in journal:
    line = ''
    for key in entry:
      line += '//// ' + key + ': '
      if key == 'reflection':
        line += entry[key] + '\n\n'
      else:
        line += entry[key]['goal'] + '\n//// '
        if entry[key]['complete'] == True:
          line += 'Goal accomplished!'
        elif entry[key]['complete'] == False:
          line += 'Didn\'t quite make it.'
      line += '\n\n'
    formatted += line
  return formatted

def main_loop():
  journal_file = start_up()
  journal = []
  run = True
  count = 0
  while run:
    if count < 4:
      count += 1
      journal = bullet(0, journal)
      break_time = 0

    if count == 4: 
      count = 0
      journal = reflect(journal)
      break_time = 0

    breathe(break_time)
    run = run_check()

  print('\nGood work today,\nSee ya later!')
  print('\n\nclosing...\n\n')

  print(format_journal(journal))
  journal_file.write(format_journal(journal))

main_loop()