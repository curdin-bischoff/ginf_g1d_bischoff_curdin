import random as rd

bankautomat = rd.randrange (100, 2001)
anzahl_1000er = bankautomat // 1000
rest_1000er = bankautomat % 1000
anzahl_200er = rest_1000er // 200
rest_200er =  rest_1000er % 200
anzahl_100er = rest_200er // 100
rest_100er = rest_200er % 100
anzahl_50er = rest_100er // 50
rest_50er = rest_100er % 50
anzahl_20er = rest_50er // 20
rest_20er = rest_50er % 20
anzahl_10er = rest_20er // 10
rest_10er = rest_20er % 10
print(f"RANDOM-Bankautomat")
print(f"Es werden CHF {bankautomat} abgehoben")
print(f"1000er Noten:{anzahl_1000er}")
print(f"200er Noten:{anzahl_200er}")
print(f"100er Noten:{anzahl_100er}")
print(f"50er Noten:{anzahl_50er}")
print(f"20er Noten:{anzahl_20er}")
print(f"10er Noten:{anzahl_10er}")
print(f"Münzen:{rest_10er}")
