# Code Templates

This repo contains code templates that I have developed to complete various data tasks at SoCalGas. 

# Swipe File 
* Shutting down [Jupyter Notebook Kernels](https://github.com/jupyter/notebook/issues/2832)

# Notes
### k-NN Algorithm

1. Determine the number for `k`. This should be an odd number in order to avoid any ties when voting at the end 
2. Find distance from new point to all of the points in the dataset and add to an `np.array`.
3. Sort the `a = np.array()` in ascending order using `b = np.sort(a, axis=None)`
4. Pull out the first `k` elements from the sorted listed such that these are the `k` elements with the smallest distance using `c =b[k]` or `np.take()`.
5. For each of these `k` elements, determine the majority and assign that class to the new point using `d = np.argmax(np.bincount(c))`. The class of `d` is the classifiction of the new point. 