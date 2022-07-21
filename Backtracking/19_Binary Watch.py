class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        if turnedOn >= 9:
            return []
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        
        indexMapperHrs = {
            8: 0,
            4: 1,
            2: 2,
            1: 3        
        }
        indexMapperMin = {
            32: 0,
            16: 1,
            8: 2,
            4: 3,
            2: 4,
            1: 5        
        }
        
        visitedHrs = [False, False, False, False]
        visitedMins = [False, False, False, False, False, False]
        
        allPossTime = []
        
        self.__getAllPossibleTime(0, 0, turnedOn, hours, minutes, visitedHrs, visitedMins, allPossTime, indexMapperHrs, indexMapperMin)
        
        return allPossTime
    
    def __getAllPossibleTime(self, currentHrs, currentMin, turnedOn, hours, minutes, visitedHrs, visitedMins, allPossTime, indexMapperHrs, indexMapperMin):
        
        if currentHrs >= 12 or currentMin >= 60:
            return
        
        if turnedOn <= 0:
            if currentMin < 10:
                if str(currentHrs) + ":0" + str(currentMin) not in allPossTime:
                    allPossTime.append( str(currentHrs) + ":0" + str(currentMin) )
            else:
                if str(currentHrs) + ":" + str(currentMin) not in allPossTime:
                    allPossTime.append( str(currentHrs) + ":" + str(currentMin) )
            #print(f'{currentHrs, currentMin}')
            return

        
        # include minutes
        for minute in minutes:
            if visitedMins[ indexMapperMin[minute] ]:
                continue
            visitedMins[ indexMapperMin[minute] ] = True
            self.__getAllPossibleTime(currentHrs, currentMin + minute, turnedOn-1, hours, minutes, visitedHrs, visitedMins, allPossTime, indexMapperHrs, indexMapperMin)
            visitedMins[ indexMapperMin[minute] ] = False
        
        # include hours
        for hour in hours:
            if visitedHrs[ indexMapperHrs[hour] ]:
                continue
            visitedHrs[ indexMapperHrs[hour] ] = True
            self.__getAllPossibleTime(currentHrs + hour, currentMin, turnedOn-1, hours, minutes, visitedHrs, visitedMins, allPossTime, indexMapperHrs, indexMapperMin)
            visitedHrs[ indexMapperHrs[hour] ] = False
            
        return
        
        