package main

import (
	"image/color"

	"github.com/faiface/pixel"
	"github.com/faiface/pixel/imdraw"
	"github.com/faiface/pixel/pixelgl"
	"golang.org/x/image/colornames"
)

// T the everything interface
type T interface{}

// Iterable returns a channel that can be used in a for each loop
type Iterable interface {
	Iterator() chan T
}

// BoardSizeX the size of the game board
const BoardSizeX = 60

// BoardSizeY the size of the game board
const BoardSizeY = 60

// UP constant direction
var UP = Point{0, 1}

// DOWN constant direction
var DOWN = Point{0, -1}

// LEFT constant direction
var LEFT = Point{-1, 0}

// RIGHT constant direction
var RIGHT = Point{1, 0}

// Point an x y point on the board
type Point struct {
	x, y int
}

// Add this point and the other point then returns a new point
func (p1 Point) Add(p2 Point) Point {
	return Point{
		x: p1.x + p2.x,
		y: p1.y + p2.y,
	}
}

// TheSnake that will be playing the game
var TheSnake Snake

// TheFood that the snake will eat
var TheFood Food

// BoardInit sets up the board to begin
func BoardInit() {
	TheFood.Init()
	TheSnake.Init()
}

// DrawBoard draws everything on the game board
func DrawBoard(win *pixelgl.Window) {
	DrawPoint(win, TheFood.position, colornames.Darkgreen)
	for v := range TheSnake.Iterable() {
		DrawPoint(win, v, colornames.Crimson)
	}
}

// DrawPoint draws a rectangle at a point
func DrawPoint(win *pixelgl.Window, p Point, c color.RGBA) {
	imd := imdraw.New(nil)
	imd.Color = c
	x := float64(p.x) * 10
	y := float64(p.y) * 10
	imd.Push(pixel.V(x, y))
	imd.Push(pixel.V(x+10, y+10))
	imd.Rectangle(0)
	imd.Draw(win)
}
