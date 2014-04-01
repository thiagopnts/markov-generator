import random


class TweetBot:
  def __init__(self, file, n=3):
    self.n = n
    self.table = {}
    self.words = map(lambda s: s.lower(), open(file).read().split())
    self.create_table()

  def sequence(self):
    for i in range(len(self.words) - self.n - 1):
      yield tuple(self.words[i : i + self.n])

  def create_table(self):
    for s in self.sequence():
      key = s[:self.n - 1]
      next_word = s[-1]
      if key in self.table:
        self.table[key].append(next_word)
      else:
        self.table[key] = [next_word]

  def generate_tweet(self):
    seed = random.randint(0, len(self.words) - 3)
    tweet = self.words[seed : seed + self.n]
    while len(' '.join(tweet)) < 130:
      n_last = tweet[-(self.n - 1):]
      next_word = random.choice(self.table[tuple(n_last)])
      tweet.append(next_word)

    return ' '.join(tweet)


bot = TweetBot('tweets.txt', 3)
print bot.generate_tweet()

