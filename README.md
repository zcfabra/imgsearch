# imgsearch
So how does image search work?


### Method
- Get some high dimensional embedding for an image w/ an nn --> do a nearest neighbours to find similar image embeddings
- Would like to do this over a potentially huge set of images
- **Goal:** Find all pairs of datapoints (xi, xj) that are w/in some distance threshold d(xi, xj) <= s (oh, and we want this done in O(N))

#### Locality Sensitive Hashing
- In general: map data into different buckets using several different hash fns
    - Consider only pairs of datapoints that share a bucket for at least one of the hashings
- With a correct design, only a very small fraction of pairs will ever be examined
    - HOWEVER, there will be false negatives: pairs of similar items that do not get considered
- In general:
    1. Shingling: Convert item into vector representation
    2. Min-hashing: Convert large items to short signatures (while preserving similarity)
    3. Locality sensitive hashing: Focus on pairs of signatures likely to be from similar items
- Shingling
    - Convert an item into a set (ex. if a document is your item, convert to a set of k-gram shingles)
    - Hash the shingles
    - If an item is represented as a set of shingles, its similarity to other documents can naturally be measured via Jaccard sim
    - Create a boolean matrix w/ rows = shingles, columns = items/documents/sets
        - Ones where the shingle is in the set
        - Column similarity is now the Jaccard similarity of the corresponding sets
- Min-hashing
    - Convert sets into short integer vectors that represent sets, and reflect their similarity
    - Want h(C) hash of each column C such that sim(C1, C2) has same similarity as sim(h(C1), h(C2))
        - Specifically, want h(C1) = h(C2) with high probability when sim(C1, C2) is high, and vice versa
    - Permute rows of boolean matrix using some permutation pi --> define a minhash fn for this permutation where h(C) = number of first element in column C w/ value 1 --> Apply several randomly chosen permutations pi to all columns to create a signature for each column --> result is a signature matrix: columns = sets and rows = minhash values for each permutation pi
    - Summarizing, we want P[h(C1) = h(C2)] = sim(C1,C2)
        - We know that the probability that in a random permutation that any element in the set is 1 / |N| where n is number of elements
        - So, for C1, the probability is 1/|N|, for C2 the probability is also 1 / |N|
            - Thus, the joint probability is 1 / |N| * 1 / |N| / Total number of shingles in both sets --> this is an intersection over union which is exactly the Jaccard similarity

    - Similarity for signatures: the fraction of the hash functions in which there is agreement
        - The inter columnar similarity in the signature matrices will correspond (though not match) the simiarity between columns of the input matrix
        - The more hash functions you add (i.e. the more random permutations you do), the closer the similarities between the signatures and the inputs will be 

- Locality Sensitive Hashing
    -  Goal is to find documents w/ similarity above some threshold s
        - Method: use a hash fn that tells us whether some pair x1 x2 is a candidate pair: candidate pairs are those whose similarity should be evaluated
        - A pair of columns x1 x2 are candidate pairs if their rows agree fraction s of the time 
        -  Apply yet another set of hash functions to signature matrix --> split signature matrix into b bands where each band contains r rows --> hash a band into a table with k buckets (k as large as possible) --> candidate pairs are those that hash to the same bucket for at least 1 band (i.e. have exactly same rows in a band)
        - Tune b and r to catch most similar pairs, but few non-similar pairs: this balances a tradeoff between false positives and negatives

- Generalizing LSH (cosine distances, euclidean distances):
    - Cosine Distance:  
        - Instead of minhashing, use random hyperplanes:
            - Take a random vector v, take its normal as a hyperplane
             - +1 if vectors are on same side of the hyperplane, -1 otherwise
    - Euclidean Distance:
        - Hash functions correspond to lines
        - Partition line into buckets of size a
        - Hash each point to the bucket containing its projection onto the line
        - An element of the signature is a bucket id for that given projection line
        - Inutition: points that are close hash in the same bucket, distant ones do not
        -  





