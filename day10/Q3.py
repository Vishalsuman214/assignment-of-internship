import numpy as np

arr=np.array([[1,np.nan,3],[4,5,6],[7,np.nan,9]])
print(arr)
col=np.nanmean(arr,axis=0)
inds=np.where(np.isnan(arr))
arr[inds]=np.take(col,inds[1])
print("\nUpdated array:")
print(arr)