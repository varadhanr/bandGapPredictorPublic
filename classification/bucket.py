bucket_list={0.5:1,1:2,1.5:3,2:4,2.5:5,3:6,3.5:7,4:8,4.5:9,5:10,5.5:11,6:12,6.5:13,7:14,7.5:15,8:16,8.5:17,9:18,9.5:19,10:20}
bucket_list_new=sorted(bucket_list.iteritems(),key=lambda (x,y):float(x))
new_bucket=[]
#pass 'a' as a list from the calling function!!
def create_bucket(a):
	new_bucket=[]
	for i in a:
		for j in bucket_list_new:
			if(j[0]>=i):
				new_bucket.append(j[1])
				break
	return new_bucket
			
