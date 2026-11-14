
type Trie struct {
	children map[byte]*Trie
	prefix   string
	isLeaf   bool
}

func Constructor() Trie {
	return Trie{
		children: make(map[byte]*Trie),
	}
}

func (t *Trie) Insert(word string) {
	node := t
	i := 0

	for i < len(word) {
		key := word[i]

		child, exists := node.children[key]

		if !exists {
			newNode := Constructor()
			newNode.prefix = word[i:]
			newNode.isLeaf = true

			node.children[key] = &newNode
			return
		}

		edge := child.prefix
		matchLen := commonPrefixLength(word[i:], edge)

		// Fully matched the existing edge -> descend
		if matchLen == len(edge) {
			node = child
			i += matchLen
			continue
		}

		// Partial match -> must split the edge
		split := &Trie{
			children: make(map[byte]*Trie),
			prefix:   edge[:matchLen],
			isLeaf:   false,
		}

		oldRemaining := edge[matchLen:]
		oldChild := &Trie{
			children: child.children,
			prefix:   oldRemaining,
			isLeaf:   child.isLeaf,
		}

		split.children[oldRemaining[0]] = oldChild

		newRemaining := word[i+matchLen:]
		if len(newRemaining) == 0 {
			split.isLeaf = true
		} else {
			newLeaf := &Trie{
				children: make(map[byte]*Trie),
				prefix:   newRemaining,
				isLeaf:   true,
			}
			split.children[newRemaining[0]] = newLeaf
		}

		node.children[key] = split
		return

	}

	node.isLeaf = true
}

func (t *Trie) Search(word string) bool {
	node := t
	i := 0

	for i < len(word) {
		key := word[i]

		child, exists := node.children[key]
		if !exists {
			return false
		}
		node = child

		matchLen := commonPrefixLength(word[i:], node.prefix)
		if matchLen != len(node.prefix) {
			return false
		}

		i += matchLen

		if i == len(word) {
			return node.isLeaf
		}

	}
	return false
}

func (t *Trie) StartsWith(prefix string) bool {
	node := t
	i := 0

	for i < len(prefix) {
		key := prefix[i]

		child, exists := node.children[key]
		if !exists {
			return false
		}

		node = child

		matchLen := commonPrefixLength(prefix[i:], node.prefix)
		if matchLen == 0 {
			return false
		}

		i += matchLen

		if matchLen < len(node.prefix) {
			return i == len(prefix)
		}
	}
	return true
}

func commonPrefixLength(a, b string) int {
	l := 0

	for l < len(a) && l < len(b) && a[l] == b[l] {
		l++
	}

	return l
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */