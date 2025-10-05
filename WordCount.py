#WordCount.py
#Name:Kaitlyn Oswald
#Date:10/5/25
#Assignment:Lab 7

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    print(words)
    for w in words: 
      wordCount = wordCount + 1
      for l in w:
          letterCount = letterCount + 1

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)
  
if __name__ == '__main__':
  main()
