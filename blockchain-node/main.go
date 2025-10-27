package main

import (
	"flag"
	"fmt"
	"os"
)

const LOCALIP = "127.0.0.1"
const DEF_PORT = "8000"

func main() {
	fmt.Println("STARTING UP THE NODE")

	server_ip := flag.String("ip", LOCALIP, "bootstrap node ip")
	server_port := flag.String("p", DEF_PORT, "bootstrap node port")
	server_password := flag.String("pass", "", "connection password") //We can enhance the security features , now this can use for it
	flag.Parse()

	if *server_password == "" {
		fmt.Printf("\033[31mError: Enter the server password\033[0m\n")
		os.Exit(1)
	}
	// Look at server , is it authenticat this node

	fmt.Println(*server_ip, *server_port)
}
