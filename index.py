import pytube
print("download video")
url = input("enter your url : ")
pytube.YouTube(url).streams.get_highest_resolution().download("document")