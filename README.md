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




