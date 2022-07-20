class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        M = len(students)
        N = len(students[0])
        
        assignedMentor = [ False for _ in range(M) ]
        
        allScores = []
        self.__process(0, M, N, M, students, mentors, assignedMentor, 0, allScores)
        # print(allScores)
        
        return max(allScores)
        
    
    def __process(self, currentStudent, totalStudents, N, M, students, mentors, assignedMentor, compScore, allScores):
        
        if currentStudent >= totalStudents:
            allScores.append(compScore)
            return
        
        for mentor in range(M):
            if assignedMentor[mentor]:
                continue
            tempCompScore = self.__calcCompatibilityScore(students[currentStudent], mentors[mentor], N)
            assignedMentor[mentor] = True
            self.__process(currentStudent+1, totalStudents, N, M, students, mentors, assignedMentor, compScore + tempCompScore, allScores )
            assignedMentor[mentor] = False
        return
    
    def __calcCompatibilityScore(self, nums1, nums2, n):
        
        compScore = 0
        
        i = 0
        while i < n:
            if nums1[i] == nums2[i]:
                compScore += 1
            i += 1
            
        return compScore
        