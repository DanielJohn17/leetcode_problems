type Trie struct {
	children map[byte]*Trie
	isLeaf   bool
}

func Constructor() Trie {
	return Trie{
		children: make(map[byte]*Trie),
	}
}

func (t *Trie) Insert(word string) {
	curr := t
	for i := 0; i < len(word); i++ {
		c := word[i]

		if curr.children[c] == nil {
			newNode := Constructor()

			curr.children[c] = &newNode
		}
		curr = curr.children[c]
	}
	curr.isLeaf = true
}

func (t *Trie) Search(word string) bool {
	curr := t

	for i := 0; i < len(word); i++ {
		c := word[i]

		if curr.children[c] == nil {
			return false
		}
		curr = curr.children[c]
	}
	return curr.isLeaf
}

func (t *Trie) StartsWith(prefix string) bool {
	curr := t

	for i := 0; i < len(prefix); i++ {
		c := prefix[i]

		if curr.children[c] == nil {
			return false
		}
		curr = curr.children[c]
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */