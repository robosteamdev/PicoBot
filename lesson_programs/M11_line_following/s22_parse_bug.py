# How the robot reads the last setting of the request
request_str = "GET /?action=update&speed=35&search=0.5 HTTP/1.1"

# old version: the text after "search=" up to the next "&"
old = request_str.split("search=")[1].split("&")[0]
print("old: [" + old + "]")

# corrected version: also cut at the first space
new = request_str.split("search=")[1].split("&")[0].split(" ")[0]
print("new: [" + new + "]")
print("as a number:", float(new))
