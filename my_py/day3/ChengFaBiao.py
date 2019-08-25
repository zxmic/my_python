#print('\n'.join([i +'*'+ j +'='+ i*j for j in range(1,i)])for i in range(10))

#[print(''.join([str(j)+"*"+str(i)+"="+str(i*j)+"\t" for j in range(1,i+1)])) for i in range(1,10)]
[print('\t'.join([str(i)+'*'+str(j)+'='+str(i*j)for i in range(1,j+1)]))for j in range(1,10)]

[print('\t'.join([str(2)+'*'+str(p)+'='+str(2*p)for p in range(2,6)]))]