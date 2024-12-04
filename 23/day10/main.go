package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"sync"
	"syscall"
	"time"
)

var wg sync.WaitGroup

type File struct {
	name    string
	content []byte
}

func fileWriter(files <-chan File, ctx context.Context, errChan chan<- error) {
	defer wg.Done()

	for {
		select {
		case <-ctx.Done():
			fmt.Println("Context cancelled")
			// wg.Wait() // I want to wait the end of the file creation to avoid corrupted file.
		case file := <-files:
			fmt.Printf("%+v\n", file)
			// err := os.WriteFile(file.name, file.content, 0644)
			// if err != nil {
			// 	errChan <- err
			// 	return
			// }
			errChan <- nil
			fmt.Println("File", file.name, "created successfully")
			time.Sleep(6 * time.Second)
		}
	}
}

func main() {
	now := time.Now()
	os.Mkdir("files", 0755)
	errChan := make(chan error, 10)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGTERM, syscall.SIGINT)

	go func() {
		s := <-sig
		fmt.Printf("Received signal: %s\n", s.String())
		cancel()
	}()

	files := make(chan File)
	wg.Add(1)

	go fileWriter(files, ctx, errChan)

	for i := 1; i <= 10; i++ {
		filename := fmt.Sprintf("files/file%d.txt", i)
		content := []byte(fmt.Sprintf("This is content for file %d", i))
		time.Sleep(1 * time.Second)
		files <- File{filename, content}
	}

	wg.Wait()

	close(errChan)

	for err := range errChan {
		if err != nil {
			fmt.Println("Error:", err)
		}
	}

	fmt.Println("Time taken:", time.Since(now))
}
