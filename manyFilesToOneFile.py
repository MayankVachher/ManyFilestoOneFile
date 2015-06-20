import os

def manyToOne():
  # Set the directory you want to start from
  srcDir = './datacollection'
  # Set the directory and file name you want to store to
  dstDir = 'megaJava.java'
  
  mega = open(dstDir,"a+")
  for dirName, subdirList, fileList in os.walk(srcDir):
      for fname in fileList:
          sample = open(os.path.join(dirName, fname), "r")
          for line in sample:
          	mega.write(line)
          sample.close()
  mega.close()

if __name__ == '__main__':
  manyToOne()
