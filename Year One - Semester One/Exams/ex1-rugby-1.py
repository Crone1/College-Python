#! usr/bin/env python

tries_home = input()
conversions_home = input()
penalties_home = input()

tries_away = input()
conversions_away = input()
penalties_away = input()

score_home = (tries_home * 5) + (conversions_home * 2) + (penalties_home * 3)
score_away = (tries_away * 5) + (conversions_away * 2) + (penalties_away * 3)

if score_home == score_away:
   print 'draw'
elif score_home > score_away:
   print 'home win'
elif score_home < score_away:
   print 'away win'
