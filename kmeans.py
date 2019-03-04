
import sys

class kmeans:
    def __init__(self,inp,k):
        self.inp=inp
        self.k=k
        #self.controller(inp,k)
        
    def newMean(self,clusters,k):
        mean=[]
        mean2=[]
        sum1=0
        print("k here is ",k)
        for i in range(k):
            for lk in range(len(clusters[i][0])):
                sum1=0
                for j in range(len(clusters[i])):
                    sum1+=clusters[i][j][lk]
                mean1=sum1/len(clusters[i])
                mean.append(mean1)
                
            print("mean here is",mean)
            mean2.append(mean)
            mean=[]
            
        return mean2
                    
                    
                    
                    
            
            
        
    
    def distance(self,a,b):
        sum1=0
        for i in range(len(a)):
            sum1+=(a[i]-b[i])**2
        return sum1
    
    
    def checkDistance(self,inp1,centroid):
        cluster=[[] for i in range(len(centroid))]
        keep=0
        for i in range(len(inp1)):
            minDistance=sys.maxsize
            for j in range(len(centroid)):
                dist=self.distance(inp1[i],centroid[j])
                if(dist<minDistance):
                    keep=j
                    minDistance=dist
            cluster[keep].append(inp1[i])
        return cluster
    
    def controller(self,inp,k):
        centroid=[]
        flag=0
        # selecting k random numbers
        import random
        count=0
        inp1=inp
        n=len(inp1)
        while(count<k):
            bk=inp1[random.randint(0,n-1)]
            if(len(centroid)==0):
                centroid.append(bk)
                count+=1
            else: 
                for lj in range(len(centroid)):
                    flag=0
                    if((bk == centroid[lj])):
                        flag=1
                        break
                if(flag==0):
                    centroid.append(bk)
                    count+=1
        #centroid=[16,22]
        print("centroid len",centroid)
        print("\n\n")
        
        #inp=[15, 15, 16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
        clusters=self.checkDistance(inp1,centroid)
        print("\n clusters are \n")
        print(clusters)
        print("\n\n")
        # find mean of clusters and assign this to centroid
        mean_clusters=self.newMean(clusters,k)
        print("prev centroid",centroid)
        print("mean entroid",mean_clusters)
        
        prev_centroid=centroid
        for i in range(k):
            while(not(set(prev_centroid[i]) <= set(mean_clusters[i]))):
                print("yup")
                
                clusters=self.checkDistance(inp1,mean_clusters)
                prev_centroid=mean_clusters
                mean_clusters=self.newMean(clusters,k)
                print("prev centroid",prev_centroid)
                print("mean entroid",mean_clusters)
            
        return clusters,mean_clusters



    
    
        
        
            






    