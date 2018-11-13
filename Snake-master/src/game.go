package main

import (
	"fmt"
	_ "image/png"
	"time"

	"github.com/faiface/pixel"
	"github.com/faiface/pixel/pixelgl"
	"github.com/faiface/pixel/text"
	"golang.org/x/image/colornames"
	"golang.org/x/image/font/basicfont"
)

const winSizeX = 600
const winSizeY = 600

func run() {
	cfg := pixelgl.WindowConfig{
		Title:  "Snake",
		Bounds: pixel.R(0, 0, winSizeX, winSizeY),
		VSync:  true,
	}
	win, err := pixelgl.NewWindow(cfg)
	if err != nil {
		panic(err)
	}

	atlas := text.NewAtlas(basicfont.Face7x13, text.ASCII)
	txt := text.New(pixel.V(150, 300), atlas)

	txt.Color = colornames.Black
	txt.WriteString("Game Over!")

	last := time.Now()
	dt := 0.0
	dir := UP
	dead := false
	BoardInit()
	for !win.Closed() {
		if !dead {
			dt += time.Since(last).Seconds()
			last = time.Now()

			if win.JustPressed(pixelgl.KeyW) {
				dir = UP
			} else if win.JustPressed(pixelgl.KeyA) {
				dir = LEFT
			} else if win.JustPressed(pixelgl.KeyS) {
				dir = DOWN
			} else if win.JustPressed(pixelgl.KeyD) {
				dir = RIGHT
			}

			if dt >= .1 {
				dt -= .1
				if !TheSnake.Move(dir) {
					dead = true
				}
				win.Clear(colornames.Aqua)
				DrawBoard(win)
			}
		} else {
			win.Clear(colornames.Aqua)
			fmt.Printf("Dead %v\n", TheSnake.Head())
			txt.Draw(win, pixel.IM.Scaled(txt.Orig, 4))
		}

		win.Update()
	}
}

func main() {
	pixelgl.Run(run)
}
