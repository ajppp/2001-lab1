import sys
from datetime import datetime
from Bio import SeqIO
from Bio import Seq

def preprocessNeedle(needle, N, processedNeedle):
    leftCursor = 0
    rightCursor = 1

    while rightCursor < N:
        if needle[leftCursor] == needle[rightCursor]:
            leftCursor += 1
            processedNeedle[rightCursor] = leftCursor
            rightCursor += 1
        else:
            if leftCursor == 0:
                processedNeedle[rightCursor] = 0
                rightCursor += 1
            else:
                leftCursor = processedNeedle[leftCursor - 1]

def KMPSearch(needle, haystack):
    H = len(haystack)
    N = len(needle)
    cursorN = 0
    cursorH = 0

    processedNeedle = [0]*N
    preprocessNeedle(needle, N, processedNeedle)

    while cursorH < H:
        if needle[cursorN] == haystack[cursorH]:
            cursorH += 1
            cursorN += 1
        if cursorN == N:
            print(f'Pattern found at index: {cursorH - cursorN}')
            cursorN = processedNeedle[cursorN - 1]
        elif cursorH < H and needle[cursorN] != haystack[cursorH]:
            if cursorN == 0:
                cursorH += 1
            else:
                cursorN = processedNeedle[cursorN - 1]

# call if u wan to test on ur own needle and haystack
# def main():
    # haystack = sys.argv[1]
    # needle = sys.argv[2]
 #   needle = sys.argv[1]
 #   haystack = next(SeqIO.parse(sys.argv[2], "fasta")).seq
    # print(f'haystack: {haystack}\nneedle: {needle}')

 #   start = datetime.now()
 ##   KMPSearch(needle, haystack)
 #   end = datetime.now()
 #   duration = end - start
 #   print(duration.total_seconds())

# uncomment if u wanna call ur own needle haystack
# main()
