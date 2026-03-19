# transactions = [100,2500,-10,500,8000,300,-5,1200]
#
# for trans in transactions:
#     if trans < 0:
#         print("Error: Negative value")
#         continue
#     elif trans > 5000:
#         print("FRAUD ALERT")
#         break
#     else:
#         print(f"Transaction processed {trans}")

#The cicling Trip Analyzer



# def analyze_trips(distances):
#     total_km = 0
#
#     for d in distances:
#         if d == "error" or d < 0:
#             continue
#
#         total_km += d
#         if d >= 100:
#             print(f"Limit {d} reached")
#             break
#
#     return total_km
#
# distances = [12,45,"error", 100, -5, 30, 15]
# result = analyze_trips(distances)
# print(f"Total Km: {result}")


#The social media Earning Tracker

# def calculate_earnings(video_views):
#     total_money = 0
#
#     for video in video_views:
#         if video == "error" or video < 0:
#             continue
#
#         current_earnings = (video/1000) * 2
#         total_money += current_earnings
#
#         if video > 10000:
#             print(f"Viral video detected {video} stopping analysis")
#             break
#
#     return total_money
#
# my_stats = [500,1200, "error", 4500, -100, 1200, 300, 800]
# result = calculate_earnings(my_stats)
# print(result)


#The e-bike battery simulator

# battery = 100
# while True:
#     a1 = input("(Ride Rest Check) What u wanna do?:").lower()
#     if a1.lower() == "ride":
#         battery -= 5
#
#     if a1 == 'check':
#         print(f"Current battery level. {battery}")
#
#     elif a1 == "rest":
#         battery += 2
#         if battery > 100:
#             battery = 100
#         print("Resting, batery charging")
#
#     if battery <= 0:
#         print("Battery empty")
#         break


# def e_bike():
#     battery = 100
#     print("Ride, Rest, Check")
#     while True:
#         action = input("What do u wanna do?: ").lower()
#         if action == "ride":
#             battery -= 5
#             print("You are riding...")
#
#         elif action == "rest":
#             battery += 2
#             if battery > 100:
#                 battery = 100
#             print("You are resting...")
#
#         elif action == "check":
#             print(f"Your battery level is {battery}")
#             continue
#
#         elif action == "exit":
#             print("Turning off...")
#             break
#
#         if battery <= 0:
#             print("Battery empty")
#             break
# e_bike()