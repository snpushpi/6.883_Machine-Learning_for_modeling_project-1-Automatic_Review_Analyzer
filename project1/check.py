tweets = set()
for line in open('stopwords.txt').readlines():
    tweets.add(line.strip())
print(tweets)