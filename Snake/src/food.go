package main

import (
	"math/rand"
	"time"
)

// Food something snakes love to eat
type Food struct {
	position Point
}

// NewFood creates some food at a random position
func (f *Food) NewFood() {
	f.position.x = rand.Int() % BoardSizeX
	f.position.y = rand.Int() % BoardSizeY
}

// Init initializes this food
func (f *Food) Init() {
	rand.Seed(time.Now().Unix())
	f.NewFood()
}
