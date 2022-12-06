import pytube

url = input("Please paste your video link : ")
path = ("D://15 Development//15 Data Analyst//15 Smplcty//New Folder")

pytube.YouTube(url).streams.get_highest_resolution().download(path)
