package main

// SnakeStartSize the initial size of the snake
var SnakeStartSize = 3

// Snake the main character in the game Snake
type Snake struct {
	body Queue
	grow bool
}

// Head returns the point where the head of the snake is
func (s *Snake) Head() Point {
	return s.body.head.value.(Point)
}

// Move this snake some direction
func (s *Snake) Move(dir Point) bool {
	s.body.AddFront(s.Head().Add(dir))
	if !s.grow {
		s.body.RemoveBack()
	}
	head := s.Head()
	s.grow = head == TheFood.position
	if s.grow {
		TheFood.NewFood()
	}

	if head.x < 0 || head.x > BoardSizeX-1 || head.y < 0 || head.y > BoardSizeY-1 {
		return false
	}

	iter := s.Iterable()
	<-iter
	for v := range iter {
		if v == head {
			return false
		}
	}

	return true
}

// Iterable allows you to iterate through the points of the snake
func (s *Snake) Iterable() chan Point {
	ch := make(chan Point)
	go func() {
		for v := range s.body.Iterator() {
			ch <- v.(Point)
		}
		close(ch)
	}()
	return ch
}

// Init initializes this snake
func (s *Snake) Init() {
	var q Queue
	q.AddFront(Point{BoardSizeX/2 - SnakeStartSize, BoardSizeY/2 - SnakeStartSize})
	s.body = q
	for i := 0; i < SnakeStartSize; i++ {
		s.grow = true
		s.Move(UP)
	}
}
