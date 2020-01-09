# https://app.codesignal.com/challenge/deMCqfKThepek7YMH

def lrc2subRip(lrcLyrics, songLength):
    returnedFormat = []
    
    currStamp = []
    nextStamp = []
    
    for i in range(len(lrcLyrics)):
        if i == 0:
            currStamp = [timeConvert(lrcLyrics[i][1:9]), lrcLyrics[i][11:]]
        else:
            currStamp = nextStamp
            
        if i < len(lrcLyrics) - 1:
            nextStamp = [timeConvert(lrcLyrics[i+1][1:9]), lrcLyrics[i+1][11:]]
        else:
            nextStamp = [songLength + ",000"]
        
        returnedFormat.append(str(i + 1))        
        returnedFormat.append(currStamp[0] + " --> " + nextStamp[0])        
        returnedFormat.append(currStamp[1])
        if i < len(lrcLyrics) - 1:
            returnedFormat.append("")
        

    
    return returnedFormat

def timeConvert(lrcTime):
    timeStamp = [int(lrcTime[:2]), int(lrcTime[3:5]), lrcTime[-2:]]
    SS = timeStamp[1] % 60
    SS = str(SS)
    if len(SS) == 1:
        SS = "0" + SS
        
    MM = (timeStamp[0] + timeStamp[1] // 60) % 60
    MM = str(MM)
    if len(MM) == 1:
        MM = "0" + MM
        
    HH = (timeStamp[0] + timeStamp[1] // 60) // 60
    return "0" + str(HH) + ":" + MM + ":" + SS + "," + lrcTime[-2:] + "0"