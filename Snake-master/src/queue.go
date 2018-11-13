package main

// Node represents an index of a linked list
type Node struct {
	parent *Node
	child  *Node
	value  T
}

// Queue a queue with a linked list implementation
type Queue struct {
	head *Node
	tail *Node
}

// AddFront added an element to the front of this queue
func (q *Queue) AddFront(value T) {
	n := &Node{
		parent: nil,
		child:  q.head,
		value:  value,
	}

	if q.head == nil {
		q.head = n
		q.tail = n
	} else {
		q.head.parent = n
		q.head = n
	}
}

// RemoveBack removes the last element of this queue
func (q *Queue) RemoveBack() T {
	value := q.tail.value
	if q.tail == q.head {
		q.head = nil
		q.tail = nil
	} else {
		q.tail = q.tail.parent
		q.tail.child = nil
	}
	return value
}

// Iterator returns a channel that can be iterated over
func (q *Queue) Iterator() chan T {
	ch := make(chan T)
	go func() {
		node := q.head
		for node != nil {
			ch <- node.value
			node = node.child
		}
		close(ch)
	}()
	return ch
}
