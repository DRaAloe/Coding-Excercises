distance_mi = 0
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1 and not is_raining:
    print(True)

elif distance_mi <= 1 and is_raining:
    print(False)

elif distance_mi <= 6 and has_bike and not is_raining:
    print(True)

elif distance_mi <= 6:
    print(False)