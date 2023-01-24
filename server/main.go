package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"

	"github.com/gofiber/fiber/v2"
)

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {

	db, err := sql.Open("sqlite3", "temp.sqlite")
	checkErr(err)
	stmt, err := db.Exec("SELECT * FROM test")
	checkErr(err)
	fmt.Print(stmt)
	app := fiber.New()

	app.Post("/addnew", func(c *fiber.Ctx) error {
		err := c.JSON(c.Body())
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(c.Body())
		return c.Send(c.Body())

	})
	log.Fatal(app.Listen(":5000"))
}
