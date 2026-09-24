type Node struct {
	key   int
	value int
	next  *Node
	prev  *Node
}

type LRUCache struct {
	capacity int
	len      int
	store    map[int]*Node
	head     *Node
	tail     *Node
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		len:      0,
		store:    make(map[int]*Node, capacity),
	}
}

func (this *LRUCache) moveToFront(node *Node) {

	if this.head.key != node.key {
		if node.prev != nil {
			if node.next == nil {
				this.tail = node.prev
			} else {
				node.next.prev = node.prev
			}
			node.prev.next = node.next
		}

		this.head.prev = node
		node.next = this.head
		this.head = node
	}

}

func (this *LRUCache) Get(key int) int {
	node, exists := this.store[key]
	if !exists {
		return -1
	}

	this.moveToFront(node)

	return node.value
}

func (this *LRUCache) Put(key int, value int) {

	if node, exists := this.store[key]; exists {
		node.value = value

		this.moveToFront(node)

		return
	}

	node := &Node{key: key, value: value}

	if this.head == nil || this.tail == nil {
		this.head = node
		this.tail = node
		this.len++
		this.store[key] = node

		return
	}

	if this.len >= this.capacity {
		if this.tail.prev != nil {
			this.tail.prev.next = nil
		}

		delete(this.store, this.tail.key)

		this.tail = this.tail.prev

		this.len--
	}

	this.moveToFront(node)

	this.store[key] = node

	this.len++

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */