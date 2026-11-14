type Trie struct {
	children [26]*Trie
	isLeaf   bool
}

func Constructor() Trie {
	return Trie{
		isLeaf: false,
	}
}

func (this *Trie) Insert(word string) {
	curr := this

	for _, c := range word {
		if curr.children[c-'a'] == nil {
			newNode := Constructor()

			curr.children[c-'a'] = &newNode
		}
		curr = curr.children[c-'a']
	}
	curr.isLeaf = true
}

func (this *Trie) Search(word string) bool {
	curr := this

	for _, c := range word {
		if curr.children[c-'a'] == nil {
			return false
		}
		curr = curr.children[c-'a']
	}
	return curr.isLeaf
}

func (this *Trie) StartsWith(prefix string) bool {
	curr := this

	for _, c := range prefix {
		if curr.children[c-'a'] == nil {
			return false
		}
		curr = curr.children[c-'a']
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