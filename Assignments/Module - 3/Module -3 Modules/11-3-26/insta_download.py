import instaloader

L = instaloader.Instaloader()
username = input("Enter Instagram username: ")
L.download_profile(username,profile_pic_only = True)